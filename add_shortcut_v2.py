#!/usr/bin/env python3
"""
Helper script to easily add new shortcuts to the shortcuts folder structure.
Usage: python add_shortcut_v2.py
"""

import json
from pathlib import Path


def get_svg_icon_examples():
    """Return some example SVG icons that can be used"""
    return {
        "document": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6zm4 18H6V4h7v5h5v11z"/></svg>',
        "browser": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>',
        "music": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/></svg>',
        "chat": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2z"/></svg>',
        "code": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z"/></svg>',
        "mail": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>',
        "calendar": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11z"/></svg>',
        "folder": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M10 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2h-8l-2-2z"/></svg>',
        "terminal": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.11 0-2 .89-2 2v12c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V6c0-1.11-.89-2-2-2zm0 14H4V8h16v10zm-2-1h-6v-2h6v2zM7.5 17l-1.41-1.41L8.67 13l-2.58-2.59L7.5 9l4 4-4 4z"/></svg>',
        "camera": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 15c1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3 1.34 3 3 3z"/><path d="M9 2L7.17 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2h-3.17L15 2H9zm3 15c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5z"/></svg>',
    }


def add_shortcut():
    """Interactive function to add a new shortcut"""
    shortcuts_dir = Path(__file__).parent / "shortcuts"
    shortcuts_dir.mkdir(exist_ok=True)
    
    print("=" * 60)
    print("Add New Shortcut")
    print("=" * 60)
    print()
    
    # Get shortcut details
    shortcut_id = input("Enter shortcut ID (lowercase, no spaces, e.g., 'vscode'): ").strip()
    
    # Check if shortcut folder already exists
    shortcut_folder = shortcuts_dir / shortcut_id
    if shortcut_folder.exists():
        print(f"\n❌ Error: Shortcut folder '{shortcut_id}' already exists!")
        return
    
    label = input("Enter display label (e.g., 'Visual Studio Code'): ").strip()
    app_name = input("Enter macOS app name (e.g., 'Visual Studio Code'): ").strip()
    
    # Icon selection
    print("\nIcon Options:")
    print("1. Skip logo (use default avatar with first letter)")
    print("2. Use custom SVG")
    print("3. Choose from example SVGs")
    
    icon_choice = input("\nSelect option (1-3): ").strip()
    
    logo_svg = None
    
    if icon_choice == "1":
        print(f"\n✅ Will use default avatar with letter '{label[0].upper()}'")
    elif icon_choice == "2":
        print("\nPaste your SVG code (should start with '<svg' and end with '</svg>'):")
        logo_svg = input().strip()
    elif icon_choice == "3":
        examples = get_svg_icon_examples()
        print("\nAvailable examples:")
        for i, (name, _) in enumerate(examples.items(), 1):
            print(f"{i}. {name}")
        
        example_choice = input("\nSelect example (1-10): ").strip()
        example_names = list(examples.keys())
        if example_choice.isdigit() and 1 <= int(example_choice) <= len(example_names):
            selected_example = example_names[int(example_choice) - 1]
            logo_svg = examples[selected_example]
        else:
            print("Invalid choice, using default document icon")
            logo_svg = examples["document"]
    else:
        print("Invalid choice, will use default avatar")
    
    # Create shortcut folder
    shortcut_folder.mkdir(parents=True, exist_ok=True)
    
    # Create config.json
    config = {
        "id": shortcut_id,
        "label": label,
        "appName": app_name
    }
    
    config_file = shortcut_folder / "config.json"
    with open(config_file, "w") as f:
        json.dump(config, f, indent=2)
    
    # Create logo.svg if provided
    if logo_svg:
        logo_file = shortcut_folder / "logo.svg"
        with open(logo_file, "w") as f:
            f.write(logo_svg)
        print(f"\n✅ Created logo.svg")
    
    print("\n" + "=" * 60)
    print(f"✅ Successfully created '{label}' shortcut!")
    print(f"📁 Location: shortcuts/{shortcut_id}/")
    print("=" * 60)
    print("\nRefresh your browser to see the new shortcut.")


def list_shortcuts():
    """List all existing shortcuts"""
    shortcuts_dir = Path(__file__).parent / "shortcuts"
    
    if not shortcuts_dir.exists():
        print("No shortcuts folder found!")
        return
    
    shortcuts = []
    for shortcut_folder in shortcuts_dir.iterdir():
        if not shortcut_folder.is_dir():
            continue
        
        config_file = shortcut_folder / "config.json"
        if not config_file.exists():
            continue
        
        try:
            with open(config_file, "r") as f:
                config = json.load(f)
            
            logo_file = shortcut_folder / "logo.svg"
            config["hasLogo"] = logo_file.exists()
            shortcuts.append(config)
        except Exception as e:
            print(f"Error reading {shortcut_folder.name}: {e}")
    
    if not shortcuts:
        print("No shortcuts configured yet.")
        return
    
    print("\n" + "=" * 60)
    print(f"Configured Shortcuts ({len(shortcuts)} total)")
    print("=" * 60)
    
    for shortcut in shortcuts:
        print(f"\nID: {shortcut['id']}")
        print(f"Label: {shortcut['label']}")
        print(f"App: {shortcut['appName']}")
        logo_status = "✓ Has logo.svg" if shortcut['hasLogo'] else "✗ No logo (using default avatar)"
        print(f"Logo: {logo_status}")
        print("-" * 40)


if __name__ == "__main__":
    print("\n🚀 Shortcuts Panel - Shortcut Manager (v2)\n")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a new shortcut")
        print("2. List existing shortcuts")
        print("3. Exit")
        
        choice = input("\nSelect option (1-3): ").strip()
        
        if choice == "1":
            add_shortcut()
        elif choice == "2":
            list_shortcuts()
        elif choice == "3":
            print("\nGoodbye! 👋")
            break
        else:
            print("\nInvalid choice, please try again.")

