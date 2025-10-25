# 🚀 Shortcuts Panel

A web-based shortcuts panel that allows you to control your macOS applications from your phone or tablet.

## Features

- 📱 Mobile-friendly interface
- 🎯 One-click application launching
- 🔄 Real-time feedback
- 🌐 Automatic IP address detection and display
- 📋 One-click URL copying for easy sharing
- 🌓 Automatic light/dark theme based on system preference
- 🎨 Clean, minimal Hero UI-inspired design
- 🐳 Docker support
- ⚡ Fast and lightweight

## Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (Python package manager)
- Docker (optional)

## Quick Start

### Option 1: Using uv (Recommended for Development)

1. **Install uv** (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. **Install dependencies**:
```bash
uv pip install -e .
```

3. **Run the application**:
```bash
python main.py
```

The server will automatically display your Mac's IP address in the console:
```
============================================================
🚀 Shortcuts Panel Server Starting
============================================================
📱 Access from your phone: http://192.168.1.100:8000
💻 Access from this Mac: http://localhost:8000
============================================================
```

4. **Access the panel**:
   - On your Mac: Open `http://localhost:8000`
   - On your phone: Open the URL shown in the console or displayed on the web interface
   - The web interface will automatically show your Mac's IP address with a convenient copy button!

### Option 2: Using Docker

1. **Build the Docker image**:
```bash
docker build -t shortcuts-panel .
```

2. **Run the container**:
```bash
docker run -p 8000:8000 shortcuts-panel
```

**Note**: Docker containers run in an isolated environment, so the `open` command won't be able to open applications on your host macOS. For this application to work properly, you should run it directly on your Mac using Option 1.

## Finding Your Mac's IP Address

The application automatically detects and displays your Mac's IP address in three ways:

1. **Console Output**: When you start the server, the IP is displayed in the terminal
2. **Web Interface**: The IP address is shown prominently at the top of the page
3. **Copy Button**: Click the "Copy URL" button to copy the full URL to your clipboard

If you need to find it manually:

### Method 1: System Settings
1. Open **System Settings**
2. Click **Network**
3. Select your active connection (Wi-Fi or Ethernet)
4. Your IP address will be shown (e.g., `192.168.1.100`)

### Method 2: Terminal
```bash
ifconfig | grep "inet " | grep -v 127.0.0.1
```

## Usage

1. Start the application on your Mac
2. Open the web interface on your phone's browser
3. Tap any shortcut button to open the corresponding application on your Mac

## Adding New Shortcuts

Shortcuts use a **folder-based structure** where each shortcut has its own directory with a config file and optional logo. If no logo is provided, a beautiful default avatar with the first letter is shown!

### 📁 Folder Structure

```
shortcuts/
├── notion/
│   ├── config.json
│   └── logo.svg (optional)
├── safari/
│   ├── config.json
│   └── logo.svg
└── myapp/
    ├── config.json
    └── logo.svg (optional)
```

### Method 1: Using the Helper Script (Recommended)

Run the interactive helper script:

```bash
python add_shortcut.py
```

This will guide you through:
1. Creating the shortcut folder
2. Setting up config.json
3. Optionally adding a logo.svg (or using the default avatar)

### Method 2: Manual Creation

Create a new folder and files:

```bash
# Create shortcut folder
mkdir shortcuts/myapp

# Create config.json
cat > shortcuts/myapp/config.json << 'EOF'
{
  "id": "myapp",
  "label": "My App",
  "appName": "My Application"
}
EOF

# (Optional) Add logo.svg
cp ~/Downloads/myapp.svg shortcuts/myapp/logo.svg
```

### Method 3: Via API

Add shortcuts programmatically using the REST API:

```bash
curl -X POST http://localhost:8000/api/shortcuts \
  -H "Content-Type: application/json" \
  -d '{
    "id": "vscode",
    "label": "VS Code",
    "appName": "Visual Studio Code",
    "logo_svg": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z\"/></svg>"
  }'
```

### Default Avatar Feature

If a shortcut doesn't have a `logo.svg` file:
- ✅ A beautiful circular avatar is automatically displayed
- ✅ Shows the first letter of the label
- ✅ Gradient background matching your theme
- ✅ No configuration needed!

Example: "Visual Studio Code" → Shows "V" in a gradient circle

See `FOLDER_STRUCTURE.md` for detailed documentation.

## API Endpoints

### Application Control
- `POST /api/open-app` - Opens an application on macOS
  ```json
  {
    "app_name": "Notion"
  }
  ```

### Shortcuts Management
- `GET /api/shortcuts` - Get all configured shortcuts
  ```json
  {
    "shortcuts": [
      {
        "id": "notion",
        "label": "Notion",
        "appName": "Notion",
        "hasLogo": true
      }
    ]
  }
  ```
- `GET /api/shortcuts/{id}/logo.svg` - Get the logo SVG file for a shortcut
- `POST /api/shortcuts` - Create a new shortcut
  ```json
  {
    "id": "vscode",
    "label": "VS Code",
    "appName": "Visual Studio Code",
    "logo_svg": "<svg>...</svg> (optional)"
  }
  ```
- `DELETE /api/shortcuts/{id}` - Delete a shortcut by ID (removes entire folder)

### System
- `GET /` - Serves the web interface
- `GET /api/ip` - Returns the local IP address and URL
  ```json
  {
    "ip": "192.168.1.100",
    "url": "http://192.168.1.100:8000"
  }
  ```
- `GET /api/health` - Health check endpoint

## Common Application Names

- Notion
- Safari
- Chrome
- Spotify
- Slack
- Visual Studio Code
- Finder
- Mail
- Calendar
- Notes

## Troubleshooting

### Application doesn't open
- Make sure the application name matches exactly (case-sensitive)
- Verify the application is installed on your Mac
- Check the server logs for error messages

### Cannot connect from phone
- Ensure your phone and Mac are on the same Wi-Fi network
- Check your Mac's firewall settings
- Verify you're using the correct IP address

### Port already in use
```bash
# Find and kill the process using port 8000
lsof -ti:8000 | xargs kill -9
```

## Security Note

This application is designed for local network use. Do not expose it to the public internet without proper authentication and security measures.

## License

MIT

