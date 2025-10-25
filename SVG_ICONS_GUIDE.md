# SVG Icons Guide

This guide helps you add SVG icons to your shortcuts.

## Quick Start

The easiest way to add shortcuts with SVG icons is using the helper script:

```bash
python add_shortcut.py
```

## Finding SVG Icons

### 1. Material Design Icons (Recommended)
- **Website**: https://fonts.google.com/icons
- **Free to use**: Yes
- **How to use**:
  1. Search for an icon
  2. Click on it
  3. Click "Download SVG"
  4. Open the SVG file and copy the content

### 2. Heroicons
- **Website**: https://heroicons.com
- **Free to use**: Yes
- **How to use**: Click on any icon and copy the SVG code

### 3. Feather Icons
- **Website**: https://feathericons.com
- **Free to use**: Yes
- **How to use**: Click on any icon to copy the SVG code

### 4. Bootstrap Icons
- **Website**: https://icons.getbootstrap.com
- **Free to use**: Yes
- **How to use**: Click on an icon and copy the SVG code

## SVG Format

Your SVG should look like this:

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
  <path d="M..."/>
</svg>
```

**Important**: Make sure your SVG uses `fill="currentColor"` so it matches your theme!

## Example Icons

Here are some ready-to-use SVG icons for common applications:

### Visual Studio Code
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z"/></svg>
```

### Terminal
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.11 0-2 .89-2 2v12c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V6c0-1.11-.89-2-2-2zm0 14H4V8h16v10zm-2-1h-6v-2h6v2zM7.5 17l-1.41-1.41L8.67 13l-2.58-2.59L7.5 9l4 4-4 4z"/></svg>
```

### Mail
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
```

### Calendar
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11z"/></svg>
```

### Camera
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 15c1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3 1.34 3 3 3z"/><path d="M9 2L7.17 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2h-3.17L15 2H9zm3 15c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5z"/></svg>
```

### Folder
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M10 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2h-8l-2-2z"/></svg>
```

## Tips

1. **Size**: SVGs are automatically sized to 48x48px by the CSS, so any viewBox works
2. **Color**: The app automatically colors icons based on your theme (light/dark mode)
3. **Simplicity**: Simpler icons look better at small sizes
4. **Testing**: After adding, refresh your browser to see the new icon

## Customizing SVG Icons

You can customize the icon size in the CSS by editing `static/index.html`:

```css
.shortcut-icon svg {
    width: 48px;   /* Change this */
    height: 48px;  /* Change this */
    color: var(--accent-primary);
}
```

## Troubleshooting

**Icon doesn't appear?**
- Make sure the SVG code is complete (starts with `<svg` and ends with `</svg>`)
- Check that the SVG uses `fill="currentColor"` or `fill` attribute
- Verify the JSON is valid (no missing quotes or commas)

**Icon looks wrong?**
- Some SVGs need specific viewBox values
- Try getting the icon from a different source
- Use emoji as a fallback: `{"type": "emoji", "data": "🎨"}`

**Icon is too small/large?**
- Adjust the CSS values in `static/index.html`
- The default is 48x48px

