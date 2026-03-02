# 🛍️ ALLS STORE - PWA Installation Guide

Ce dossier contient votre Progressive Web App (PWA) ALLS STORE prête à être testée et installée localement.

## 📁 Contenu du dossier

```
alls-store-pwa/
├── index.html              # Page principale
├── manifest.json           # Configuration PWA
├── service-worker.js       # Service Worker pour offline
├── offline.html            # Page hors ligne
├── icons/                  # Icônes de l'application
│   ├── icon-72x72.png
│   ├── icon-96x96.png
│   ├── icon-128x128.png
│   ├── icon-144x144.png
│   ├── icon-152x152.png
│   ├── icon-192x192.png
│   ├── icon-384x384.png
│   └── icon-512x512.png
├── start-server.py         # Serveur Python
├── start-server.bat        # Lanceur Windows
├── start-server.command    # Lanceur macOS
└── README-PWA.md           # Ce fichier
```

## 🚀 Démarrage rapide

### Option 1 : Double-clic (Recommandé)

| Système | Action |
|---------|--------|
| **Windows** | Double-cliquez sur `start-server.bat` |
| **macOS** | Double-cliquez sur `start-server.command` |
| **Linux** | Ouvrez un terminal et exécutez `python3 start-server.py` |

### Option 2 : Ligne de commande

```bash
# Naviguer dans le dossier
cd chemin/vers/alls-store-pwa

# Démarrer le serveur
python start-server.py        # Windows
python3 start-server.py       # macOS/Linux

# Ou avec un port personnalisé
python start-server.py 3000
```

## 🌐 Accès à l'application

Une fois le serveur démarré :

- **Local** : http://localhost:8000
- **Réseau local** : http://VOTRE_IP:8000 (pour tester sur mobile)

## 📱 Installation de la PWA

### Sur Android (Chrome)

1. Ouvrez http://localhost:8000 dans Chrome
2. Un popup "Ajouter à l'écran d'accueil" devrait apparaître
3. Sinon, cliquez sur le bouton flottant "📲 Installer l'app"
4. Confirmez l'installation

### Sur iOS (Safari)

1. Ouvrez http://VOTRE_IP:8000 dans Safari
2. Appuyez sur le bouton **Partager** (carré avec flèche)
3. Faites défiler et sélectionnez **"Sur l'écran d'accueil"**
4. Confirmez avec **"Ajouter"**

### Sur Desktop (Chrome/Edge)

1. Ouvrez http://localhost:8000
2. Cliquez sur l'icône **📲** dans la barre d'adresse
3. Ou utilisez le bouton "Installer ALLS STORE"
4. L'app s'ouvrira dans sa propre fenêtre

## ⚠️ Important

**NE PAS** ouvrir directement `index.html` dans le navigateur !

Les Service Workers nécessitent un serveur HTTP pour fonctionner. Utilisez toujours le serveur fourni.

## 🔧 Fonctionnalités PWA

- ✅ **Installation** : Bouton d'installation visible
- ✅ **Hors ligne** : Fonctionne sans internet après la première visite
- ✅ **Icône** : Apparaît sur l'écran d'accueil
- ✅ **Splash screen** : Écran de démarrage personnalisé
- ✅ **Mode standalone** : Sans barre d'adresse du navigateur
- ✅ **Mises à jour** : Notification quand une nouvelle version est disponible

## 🛠️ Dépannage

### Le bouton d'installation n'apparaît pas

1. Vérifiez que vous utilisez Chrome/Edge (pas Firefox/Safari sur desktop)
2. Assurez-vous d'être en HTTPS ou localhost
3. Ouvrez les DevTools (F12) → Console pour voir les erreurs

### Le Service Worker ne s'enregistre pas

1. Rafraîchissez la page (F5)
2. Dans DevTools → Application → Service Workers
3. Cochez "Update on reload" pour le développement

### Tester sur mobile

1. Connectez votre téléphone au même WiFi
2. Trouvez votre IP locale : `ipconfig` (Windows) ou `ifconfig` (macOS/Linux)
3. Accédez à http://VOTRE_IP:8000 sur votre téléphone

## 📝 Notes

- Le serveur utilise le port 8000 par défaut
- Les fichiers sont servis avec les headers nécessaires pour les PWAs
- Le cache est désactivé pour faciliter le développement

---

**Bonne utilisation de votre PWA ALLS STORE !** 🎉
