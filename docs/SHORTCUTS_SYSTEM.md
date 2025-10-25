# Shortcuts Configuration System

## Overview

Your shortcuts panel now uses a **JSON-based configuration system** with **SVG icon support**! This makes it easy to add, modify, and manage shortcuts without editing HTML code.

## What Changed?

### Before
- ❌ Shortcuts hardcoded in HTML
- ❌ Only emoji icons
- ❌ Required HTML knowledge to add shortcuts
- ❌ No API for programmatic management

### After
- ✅ Shortcuts stored in `shortcuts.json`
- ✅ SVG icon support (scalable, theme-aware)
- ✅ Multiple ways to add shortcuts (script, API, manual)
- ✅ RESTful API for management
- ✅ Dynamic rendering from JSON
- ✅ Still supports emojis if you prefer

## Files Added

1. **`shortcuts.json`** - Configuration file storing all shortcuts
2. **`add_shortcut.py`** - Interactive helper script to add shortcuts
3. **`SVG_ICONS_GUIDE.md`** - Guide for finding and using SVG icons
4. **`SHORTCUTS_SYSTEM.md`** - This file

## How to Add Shortcuts

### 🎯 Method 1: Helper Script (Easiest)

```bash
python add_shortcut.py
```

This interactive script will:
1. Ask for shortcut details (ID, label, app name)
2. Let you choose icon type (emoji, custom SVG, or examples)
3. Save it to the JSON file
4. Validate that IDs are unique

### 🔧 Method 2: REST API

Add shortcuts while the server is running:

```bash
curl -X POST http://localhost:8000/api/shortcuts \
  -H "Content-Type: application/json" \
  -d '{
    "id": "chrome",
    "label": "Chrome",
    "appName": "Google Chrome",
    "icon": {
      "type": "svg",
      "data": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z\"/></svg>"
    }
  }'
```

### ✏️ Method 3: Edit JSON Directly

Open `shortcuts.json` and add entries:

```json
{
  "shortcuts": [
    {
      "id": "unique-id",
      "label": "Display Name",
      "appName": "Actual macOS App Name",
      "icon": {
        "type": "svg",
        "data": "<svg>...</svg>"
      }
    }
  ]
}
```

## API Endpoints

### Get All Shortcuts
```bash
GET /api/shortcuts
```

Returns:
```json
{
  "shortcuts": [
    {
      "id": "notion",
      "label": "Notion",
      "appName": "Notion",
      "icon": {
        "type": "svg",
        "data": "<svg>...</svg>"
      }
    }
  ]
}
```

### Add Shortcut
```bash
POST /api/shortcuts
```

Body:
```json
{
  "id": "string",
  "label": "string",
  "appName": "string",
  "icon": {
    "type": "svg|emoji",
    "data": "string"
  }
}
```

### Delete Shortcut
```bash
DELETE /api/shortcuts/{shortcut_id}
```

## JSON Structure

```json
{
  "shortcuts": [
    {
      "id": "unique-identifier",      // Unique ID (no spaces)
      "label": "Display Name",         // Shown on button
      "appName": "macOS App Name",     // Exact name to open
      "icon": {
        "type": "svg",                 // "svg" or "emoji"
        "data": "<svg>...</svg>"       // SVG code or emoji
      }
    }
  ]
}
```

### Field Descriptions

- **id**: Unique identifier (lowercase, no spaces, e.g., "vscode")
- **label**: Display name shown on the button
- **appName**: Exact macOS application name (case-sensitive)
- **icon.type**: Either "svg" or "emoji"
- **icon.data**: 
  - For SVG: Complete SVG XML code
  - For emoji: Single emoji character

## Icon Support

### SVG Icons (Recommended)
- ✅ Scalable to any size
- ✅ Automatically colored based on theme
- ✅ Professional look
- ✅ Consistent with modern UI

**Where to find SVG icons:**
- [Material Icons](https://fonts.google.com/icons)
- [Heroicons](https://heroicons.com)
- [Feather Icons](https://feathericons.com)
- [Bootstrap Icons](https://icons.getbootstrap.com)

See `SVG_ICONS_GUIDE.md` for detailed instructions.

### Emoji Icons (Still Supported)
```json
{
  "icon": {
    "type": "emoji",
    "data": "🎨"
  }
}
```

## Features

### ✨ Dynamic Loading
Shortcuts are loaded from the JSON file when you open the page. No need to edit HTML!

### 🎨 Theme-Aware Icons
SVG icons automatically adapt to your light/dark theme preference.

### 🔄 Hot Reload Ready
Just edit the JSON file and refresh your browser to see changes.

### 🛡️ Validation
- Duplicate ID detection
- JSON schema validation via Pydantic models
- Error messages for invalid data

### 📝 Management Tools
- Interactive CLI script
- RESTful API
- Direct file editing

## Examples

### Example 1: Adding Visual Studio Code with SVG

```json
{
  "id": "vscode",
  "label": "VS Code",
  "appName": "Visual Studio Code",
  "icon": {
    "type": "svg",
    "data": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z\"/></svg>"
  }
}
```

### Example 2: Adding Finder with Emoji

```json
{
  "id": "finder",
  "label": "Finder",
  "appName": "Finder",
  "icon": {
    "type": "emoji",
    "data": "📁"
  }
}
```

## Tips

1. **Use the helper script** - It's the easiest way and includes validation
2. **Consistent IDs** - Use lowercase, no spaces (e.g., "my-app")
3. **SVG over emoji** - SVG icons look more professional and scale better
4. **Test app names** - Make sure the app name matches exactly (case-sensitive)
5. **Backup your config** - Keep a copy of `shortcuts.json`

## Troubleshooting

**Shortcuts don't appear?**
- Check the browser console for errors
- Verify JSON syntax is valid
- Make sure the server is running

**Icon doesn't show?**
- Check SVG syntax (must start with `<svg` and end with `</svg>`)
- Try using an emoji as fallback
- Verify icon.type is "svg" or "emoji"

**App doesn't open?**
- Verify the appName matches exactly
- Check server logs for error messages
- Test with `/api/open-app` endpoint directly

## Next Steps

1. **Customize your shortcuts**: Run `python add_shortcut.py`
2. **Find SVG icons**: Check `SVG_ICONS_GUIDE.md`
3. **Explore the API**: Try the REST endpoints
4. **Share your setup**: The JSON file is easy to share with others!

---

**Need help?** Check the README.md or the API documentation at `http://localhost:8000/docs` (FastAPI auto-generated docs)

