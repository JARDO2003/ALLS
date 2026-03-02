#!/usr/bin/env python3
"""
Serveur local pour tester la PWA ALLS STORE
Usage: python start-server.py [port]
"""

import http.server
import socketserver
import os
import sys
import webbrowser
from pathlib import Path

# Configuration
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
DIRECTORY = Path(__file__).parent

class PWAHandler(http.server.SimpleHTTPRequestHandler):
    """Handler avec les bons headers pour les PWAs"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)
    
    def end_headers(self):
        # Headers nécessaires pour les Service Workers
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Service-Worker-Allowed', '/')
        
        # CORS pour permettre les requêtes Firebase
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        
        super().end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()
    
    def log_message(self, format, *args):
        # Log coloré
        print(f"\033[36m[SERVER]\033[0m {self.address_string()} - {format % args}")

def print_banner():
    """Affiche une bannière stylisée"""
    banner = f"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║           🛍️  ALLS STORE - PWA Local Server                  ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  📱 Application disponible sur:                              ║
║     http://localhost:{PORT}                                    ║
║                                                              ║
║  🌐 Sur votre réseau local:                                  ║
║     http://{get_local_ip()}:{PORT}                           ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  📋 Instructions d'installation:                             ║
║                                                              ║
║  • Chrome/Edge (Desktop):                                    ║
║    Cliquez sur l'icône 📲 dans la barre d'adresse           ║
║                                                              ║
║  • Chrome (Android):                                         ║
║    Menu → "Ajouter à l'écran d'accueil"                     ║
║                                                              ║
║  • Safari (iOS):                                             ║
║    Partager → "Sur l'écran d'accueil"                       ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

Appuyez sur Ctrl+C pour arrêter le serveur
    """
    print(banner)

def get_local_ip():
    """Récupère l'IP locale pour les tests sur mobile"""
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def main():
    print_banner()
    
    with socketserver.TCPServer(("", PORT), PWAHandler) as httpd:
        print(f"\033[32m✅ Serveur démarré avec succès!\033[0m\n")
        
        # Ouvrir automatiquement le navigateur
        try:
            webbrowser.open(f"http://localhost:{PORT}")
            print("\033[33m🌐 Ouverture automatique du navigateur...\033[0m\n")
        except:
            pass
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n\033[31m👋 Serveur arrêté. À bientôt!\033[0m\n")
            httpd.shutdown()

if __name__ == "__main__":
    main()
