# Shortcuts Folder Structure

## Overview

Your shortcuts panel now uses a **folder-based structure** where each shortcut has its own directory containing a configuration file and an optional logo.

## Structure

```
shortcuts-panel/
├── shortcuts/
│   ├── notion/
│   │   ├── config.json
│   │   └── logo.svg
│   ├── safari/
│   │   ├── config.json
│   │   └── logo.svg
│   ├── spotify/
│   │   ├── config.json
│   │   └── logo.svg
│   └── myapp/
│       ├── config.json
│       └── logo.svg (optional)
```

## Files

### `config.json` (Required)

Each shortcut must have a `config.json` file with the following structure:

```json
{
  "id": "notion",
  "label": "Notion",
  "appName": "Notion"
}
```

**Fields:**
- `id` - Unique identifier (must match folder name)
- `label` - Display name shown on the button
- `appName` - Exact macOS application name

### `logo.svg` (Optional)

An SVG file that serves as the icon for the button. If not provided, the UI will display a default avatar with the first letter of the label.

**Requirements:**
- Must be valid SVG format
- Recommended: Use `fill="currentColor"` for theme compatibility
- Recommended size: 24x24 viewBox

## Adding New Shortcuts

### Method 1: Helper Script (Recommended)

```bash
python add_shortcut.py
```

This interactive script will:
1. Create the shortcut folder
2. Create config.json
3. Optionally create logo.svg (or use default avatar)

### Method 2: Manual Creation

1. Create a new folder in `shortcuts/` with your shortcut ID:
   ```bash
   mkdir shortcuts/myapp
   ```

2. Create `config.json`:
   ```json
   {
     "id": "myapp",
     "label": "My App",
     "appName": "My Application"
   }
   ```

3. (Optional) Add `logo.svg`:
   ```bash
   # Copy your SVG file
   cp ~/Downloads/myapp.svg shortcuts/myapp/logo.svg
   ```

### Method 3: API

```bash
curl -X POST http://localhost:8000/api/shortcuts \
  -H "Content-Type: application/json" \
  -d '{
    "id": "myapp",
    "label": "My App",
    "appName": "My Application",
    "logo_svg": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"...\"/></svg>"
  }'
```

## Default Avatar

If a shortcut doesn't have a `logo.svg` file, the UI automatically displays a beautiful default avatar:
- **Circular design** with gradient background
- **First letter** of the label in uppercase
- **Theme-aware** colors matching your light/dark mode

Example: "Visual Studio Code" → Shows "V" in a circular gradient avatar

## Advantages of This Structure

✅ **Organized** - Each shortcut is self-contained in its own folder  
✅ **Flexible** - Easy to add/remove shortcuts by copying folders  
✅ **Version Control** - Git-friendly structure  
✅ **Portable** - Share shortcuts by sharing folders  
✅ **Scalable** - Add more files per shortcut in the future (e.g., metadata)  
✅ **Default Fallback** - No logo required, automatic avatar generation  

## Finding SVG Logos

### Option 1: Download from Icon Sites
- [Material Icons](https://fonts.google.com/icons)
- [Heroicons](https://heroicons.com)
- [Feather Icons](https://feathericons.com)
- [Bootstrap Icons](https://icons.getbootstrap.com)

### Option 2: Extract from Applications
Some apps include SVG icons in their packages:
```bash
# macOS app bundle structure
/Applications/MyApp.app/Contents/Resources/
```

### Option 3: Use Helper Script Examples
The `add_shortcut.py` script includes 10 pre-made SVG icons you can use.

## Managing Shortcuts

### View All Shortcuts
```bash
python add_shortcut.py
# Select option 2
```

### Delete a Shortcut
```bash
# Via API
curl -X DELETE http://localhost:8000/api/shortcuts/myapp

# Or manually
rm -rf shortcuts/myapp
```

### Update a Shortcut
Simply edit the files in the shortcut's folder:
```bash
# Edit configuration
nano shortcuts/myapp/config.json

# Replace logo
cp ~/new-logo.svg shortcuts/myapp/logo.svg
```

Refresh your browser to see the changes!

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
      "hasLogo": true
    }
  ]
}
```

### Get Shortcut Logo
```bash
GET /api/shortcuts/{id}/logo.svg
```

Returns the SVG file or 404 if not found.

### Create Shortcut
```bash
POST /api/shortcuts
```

Body:
```json
{
  "id": "string",
  "label": "string",
  "appName": "string",
  "logo_svg": "string (optional)"
}
```

### Delete Shortcut
```bash
DELETE /api/shortcuts/{id}
```

## Migration from Old Structure

If you were using the old `shortcuts.json` file, your existing shortcuts have already been migrated to the new folder structure with SVG logos preserved.

Old structure:
```
shortcuts.json (single file with all shortcuts)
```

New structure:
```
shortcuts/
├── notion/
│   ├── config.json
│   └── logo.svg
├── safari/
│   ├── config.json
│   └── logo.svg
...
```

## Tips

1. **Keep IDs simple** - Use lowercase letters and hyphens (e.g., "vs-code")
2. **Use descriptive labels** - The label is what users see
3. **Test app names** - Make sure the app name is exact (case-sensitive)
4. **Optimize SVGs** - Remove unnecessary attributes for smaller file sizes
5. **No logo? No problem!** - The default avatar looks great

## Troubleshooting

**Shortcut doesn't appear?**
- Check that `config.json` exists and is valid JSON
- Ensure the folder name matches the `id` in config.json
- Refresh your browser

**Logo doesn't display?**
- Verify `logo.svg` exists in the shortcut folder
- Check SVG syntax (must be valid XML)
- Look at browser console for errors
- The default avatar will show if logo fails to load

**App doesn't open?**
- Verify `appName` matches the exact application name
- Check server logs for error messages

---

**Need help?** Run `python add_shortcut.py` for an interactive guide!

