# Migration to Folder-Based Structure (v2)

## What Changed?

Your shortcuts panel has been upgraded from a single JSON file to a folder-based structure!

### Before (v1)
```
shortcuts.json    # Single file with all shortcuts and inline SVG data
```

### After (v2)
```
shortcuts/
├── notion/
│   ├── config.json
│   └── logo.svg
├── safari/
│   ├── config.json
│   └── logo.svg
└── ...
```

## Why This Is Better

✅ **More Organized** - Each shortcut is self-contained  
✅ **Easier to Manage** - Add/remove shortcuts by copying folders  
✅ **Better Icons** - Separate SVG files instead of inline strings  
✅ **Default Avatars** - No logo? No problem! Auto-generated avatars  
✅ **Git Friendly** - Cleaner diffs and easier collaboration  
✅ **Extensible** - Add more files per shortcut in the future  

## Migration Status

✅ **Already Complete!** Your existing shortcuts have been migrated to the new structure:
- `shortcuts/notion/` - Notion with SVG logo
- `shortcuts/safari/` - Safari with SVG logo
- `shortcuts/spotify/` - Spotify with SVG logo
- `shortcuts/slack/` - Slack with SVG logo

## What You Need to Know

### 1. Use the New Helper Script

**Old:** `python add_shortcut.py`  
**New:** `python add_shortcut_v2.py`

The new script creates folders and files for you.

### 2. API Changes

**Old Structure:**
```json
{
  "id": "myapp",
  "label": "My App",
  "appName": "My Application",
  "icon": {
    "type": "svg",
    "data": "<svg>...</svg>"
  }
}
```

**New Structure:**
```json
{
  "id": "myapp",
  "label": "My App",
  "appName": "My Application",
  "hasLogo": true
}
```

The SVG is now a separate `logo.svg` file!

### 3. Default Avatars

If a shortcut doesn't have a `logo.svg`, the UI automatically shows a beautiful circular avatar with the first letter.

**Example:**
- "Visual Studio Code" → Shows "V" in a gradient circle
- "Chrome" → Shows "C" in a gradient circle

No configuration needed!

### 4. New API Endpoint

Get logos via:
```bash
GET /api/shortcuts/{id}/logo.svg
```

This returns the actual SVG file.

## Cleaning Up

The old `shortcuts.json` file is no longer used. You can safely delete it:

```bash
rm shortcuts.json
```

It's already been added to `.gitignore` to prevent accidentally committing it.

## Adding New Shortcuts

### Quick Start

```bash
python add_shortcut_v2.py
```

### Manual Creation

```bash
# 1. Create folder
mkdir shortcuts/myapp

# 2. Create config
cat > shortcuts/myapp/config.json << 'EOF'
{
  "id": "myapp",
  "label": "My App",
  "appName": "My Application"
}
EOF

# 3. (Optional) Add logo
cp ~/Downloads/logo.svg shortcuts/myapp/logo.svg
```

### Via API

```bash
curl -X POST http://localhost:8000/api/shortcuts \
  -H "Content-Type: application/json" \
  -d '{
    "id": "myapp",
    "label": "My App",
    "appName": "My Application",
    "logo_svg": "<svg>...</svg>"
  }'
```

## Documentation

New documentation files:
- **FOLDER_STRUCTURE.md** - Complete guide to the folder structure
- **README.md** - Updated with new methods
- **SVG_ICONS_GUIDE.md** - Still relevant for finding SVG logos

Old documentation (deprecated):
- **SHORTCUTS_SYSTEM.md** - Describes the old JSON-based system
- **add_shortcut.py** - Old helper script (use `add_shortcut_v2.py` instead)

## Troubleshooting

### Shortcuts don't appear?
1. Check that each shortcut has a `config.json`
2. Verify folder names match the IDs in config.json
3. Refresh your browser

### Logo doesn't show?
1. Check that `logo.svg` exists
2. Verify it's valid SVG
3. The default avatar will show as fallback

### Need help?
Run the helper script for an interactive guide:
```bash
python add_shortcut_v2.py
```

## Summary

🎉 **You're all set!** Your shortcuts have been migrated and the new system is ready to use.

**Quick commands:**
- Add shortcuts: `python add_shortcut_v2.py`
- View structure: `ls -R shortcuts/`
- Read docs: Open `FOLDER_STRUCTURE.md`

Enjoy the new folder-based structure! 🚀

