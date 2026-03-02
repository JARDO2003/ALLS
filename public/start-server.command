#!/bin/bash

# ALLS STORE - PWA Local Server (macOS/Linux)

cd "$(dirname "$0")"

echo ""
echo "========================================"
echo "    🛍️ ALLS STORE - PWA Local Server"
echo "========================================"
echo ""
echo "Démarrage du serveur..."
echo ""

python3 start-server.py || python start-server.py

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Erreur: Python n'est pas installé"
    echo ""
    echo "Veuillez installer Python:"
    echo "  - macOS: brew install python3"
    echo "  - Linux: sudo apt-get install python3"
    echo ""
    read -p "Appuyez sur Entrée pour continuer..."
fi
