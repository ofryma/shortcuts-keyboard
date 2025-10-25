#!/bin/bash

# Example: Add a shortcut via API
# Make sure the server is running first!

echo "Adding Visual Studio Code shortcut..."

curl -X POST http://localhost:8000/api/shortcuts \
  -H "Content-Type: application/json" \
  -d '{
    "id": "vscode",
    "label": "VS Code",
    "appName": "Visual Studio Code",
    "icon": {
      "type": "svg",
      "data": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z\"/></svg>"
    }
  }'

echo -e "\n\nAdding Chrome with emoji icon..."

curl -X POST http://localhost:8000/api/shortcuts \
  -H "Content-Type: application/json" \
  -d '{
    "id": "chrome",
    "label": "Chrome",
    "appName": "Google Chrome",
    "icon": {
      "type": "emoji",
      "data": "🌐"
    }
  }'

echo -e "\n\nGetting all shortcuts..."

curl http://localhost:8000/api/shortcuts

echo -e "\n\nDone! Refresh your browser to see the new shortcuts."

