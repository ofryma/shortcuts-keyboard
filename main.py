import subprocess
import socket
import json
from pathlib import Path
from typing import Dict, Any
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Shortcuts Panel")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Path to shortcuts folder
SHORTCUTS_DIR = Path(__file__).parent / "shortcuts"


class ShortcutRequest(BaseModel):
    app_name: str


class IconData(BaseModel):
    type: str  # "svg" or "emoji"
    data: str  # SVG string or emoji character


class ShortcutConfig(BaseModel):
    id: str
    label: str
    appName: str


class CreateShortcutRequest(BaseModel):
    id: str
    label: str
    appName: str
    logo_svg: str = None  # Optional SVG content


@app.get("/")
async def read_root():
    """Serve the main HTML page"""
    return FileResponse("static/index.html")


@app.post("/api/open-app")
async def open_app(request: ShortcutRequest):
    """
    Open an application on macOS
    
    Args:
        request: ShortcutRequest with app_name field
        
    Returns:
        Success message or error
    """
    try:
        app_name = request.app_name
        logger.info(f"Attempting to open application: {app_name}")
        
        # Use macOS 'open' command to launch applications
        # -a flag specifies the application name
        result = subprocess.run(
            ["open", "-a", app_name],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode != 0:
            error_msg = result.stderr or "Failed to open application"
            logger.error(f"Error opening {app_name}: {error_msg}")
            raise HTTPException(status_code=400, detail=f"Failed to open {app_name}: {error_msg}")
        
        logger.info(f"Successfully opened {app_name}")
        return {"status": "success", "message": f"Opened {app_name}"}
    
    except subprocess.TimeoutExpired:
        logger.error(f"Timeout opening {app_name}")
        raise HTTPException(status_code=408, detail="Request timed out")
    except Exception as e:
        logger.error(f"Unexpected error opening {app_name}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


def get_local_ip():
    """
    Get the local IP address of this machine
    
    Returns:
        str: Local IP address or None if not found
    """
    try:
        # Create a socket connection to get the local IP
        # We don't actually connect, just use it to determine the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        logger.error(f"Error getting local IP: {e}")
        return None


@app.get("/api/ip")
async def get_ip():
    """Get the local IP address of this machine"""
    ip = get_local_ip()
    if ip:
        return {
            "ip": ip,
            "url": f"http://{ip}:8765"
        }
    else:
        raise HTTPException(status_code=500, detail="Could not determine local IP address")


def scan_shortcuts() -> list:
    """
    Scan the shortcuts directory and load all shortcut configurations
    
    Returns:
        List of shortcut dictionaries with id, label, appName, and hasLogo
    """
    try:
        if not SHORTCUTS_DIR.exists():
            logger.warning(f"Shortcuts directory not found at {SHORTCUTS_DIR}")
            SHORTCUTS_DIR.mkdir(parents=True, exist_ok=True)
            return []
        
        shortcuts = []
        
        # Iterate through each subdirectory in shortcuts folder
        for shortcut_dir in SHORTCUTS_DIR.iterdir():
            if not shortcut_dir.is_dir():
                continue
            
            config_file = shortcut_dir / "config.json"
            logo_file = shortcut_dir / "logo.svg"
            
            if not config_file.exists():
                logger.warning(f"No config.json found in {shortcut_dir.name}, skipping")
                continue
            
            try:
                with open(config_file, "r") as f:
                    config = json.load(f)
                
                # Add hasLogo flag
                config["hasLogo"] = logo_file.exists()
                shortcuts.append(config)
                
            except Exception as e:
                logger.error(f"Error reading config from {shortcut_dir.name}: {e}")
                continue
        
        logger.info(f"Successfully loaded {len(shortcuts)} shortcuts")
        return shortcuts
        
    except Exception as e:
        logger.error(f"Error scanning shortcuts directory: {e}")
        raise HTTPException(status_code=500, detail=f"Error reading shortcuts: {str(e)}")


@app.get("/api/shortcuts")
async def get_shortcuts():
    """
    Get all configured shortcuts
    
    Returns:
        List of shortcut configurations
    """
    shortcuts = scan_shortcuts()
    return {"shortcuts": shortcuts}


@app.post("/api/shortcuts")
async def create_shortcut(shortcut: CreateShortcutRequest):
    """
    Create a new shortcut with its own folder
    
    Args:
        shortcut: Shortcut configuration including id, label, appName, and optional logo_svg
        
    Returns:
        Success message with the created shortcut
    """
    try:
        # Check if shortcut with this ID already exists
        existing_shortcuts = scan_shortcuts()
        existing_ids = [s.get("id") for s in existing_shortcuts]
        if shortcut.id in existing_ids:
            raise HTTPException(
                status_code=400, 
                detail=f"Shortcut with ID '{shortcut.id}' already exists"
            )
        
        # Create shortcut directory
        shortcut_dir = SHORTCUTS_DIR / shortcut.id
        shortcut_dir.mkdir(parents=True, exist_ok=True)
        
        # Create config.json
        config = {
            "id": shortcut.id,
            "label": shortcut.label,
            "appName": shortcut.appName
        }
        
        config_file = shortcut_dir / "config.json"
        with open(config_file, "w") as f:
            json.dump(config, f, indent=2)
        
        # Create logo.svg if provided
        has_logo = False
        if shortcut.logo_svg:
            logo_file = shortcut_dir / "logo.svg"
            with open(logo_file, "w") as f:
                f.write(shortcut.logo_svg)
            has_logo = True
        
        logger.info(f"Created new shortcut: {shortcut.label} ({shortcut.id})")
        return {
            "status": "success",
            "message": f"Shortcut '{shortcut.label}' created successfully",
            "shortcut": {
                **config,
                "hasLogo": has_logo
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating shortcut: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/shortcuts/{shortcut_id}/logo.svg")
async def get_shortcut_logo(shortcut_id: str):
    """
    Get the logo.svg file for a specific shortcut
    
    Args:
        shortcut_id: The ID of the shortcut
        
    Returns:
        SVG file or 404 if not found
    """
    try:
        logo_file = SHORTCUTS_DIR / shortcut_id / "logo.svg"
        
        if not logo_file.exists():
            raise HTTPException(
                status_code=404,
                detail=f"Logo not found for shortcut '{shortcut_id}'"
            )
        
        return FileResponse(
            logo_file,
            media_type="image/svg+xml",
            headers={"Cache-Control": "public, max-age=3600"}
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error serving logo for {shortcut_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/api/shortcuts/{shortcut_id}")
async def delete_shortcut(shortcut_id: str):
    """
    Delete a shortcut by ID (removes the entire folder)
    
    Args:
        shortcut_id: The ID of the shortcut to delete
        
    Returns:
        Success message
    """
    try:
        import shutil
        
        shortcut_dir = SHORTCUTS_DIR / shortcut_id
        
        if not shortcut_dir.exists():
            raise HTTPException(
                status_code=404,
                detail=f"Shortcut with ID '{shortcut_id}' not found"
            )
        
        # Remove the entire shortcut directory
        shutil.rmtree(shortcut_dir)
        
        logger.info(f"Deleted shortcut: {shortcut_id}")
        return {
            "status": "success",
            "message": f"Shortcut '{shortcut_id}' deleted successfully"
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting shortcut: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    
    # Get and display local IP address
    local_ip = get_local_ip()
    if local_ip:
        logger.info("=" * 60)
        logger.info("🚀 Shortcuts Panel Server Starting")
        logger.info("=" * 60)
        logger.info(f"📱 Access from your phone: http://{local_ip}:8765")
        logger.info("💻 Access from this Mac: http://localhost:8765")
        logger.info("=" * 60)
    
    uvicorn.run("main:app", host="0.0.0.0", port=8765, reload=True)

