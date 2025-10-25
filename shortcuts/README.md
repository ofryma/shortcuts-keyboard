# Shortcuts Folder

This folder contains all your application shortcuts. Each shortcut has its own subfolder.

## Structure

Each shortcut folder should contain:
- **config.json** (required) - Configuration with id, label, and appName
- **logo.svg** (optional) - SVG logo file

## Example

```
shortcuts/
├── notion/
│   ├── config.json
│   └── logo.svg
└── safari/
    ├── config.json
    └── logo.svg
```

## Adding New Shortcuts

**Easiest way:**
```bash
python add_shortcut_v2.py
```

**Manual way:**
1. Create a new folder with your shortcut ID (e.g., `myapp`)
2. Add `config.json` with id, label, and appName
3. (Optional) Add `logo.svg` with your icon

See `../FOLDER_STRUCTURE.md` for detailed documentation.

## No Logo?

If you don't include a `logo.svg`, the UI will automatically display a beautiful circular avatar with the first letter of your shortcut's label!

Example: "Chrome" → Shows "C" in a gradient circle

