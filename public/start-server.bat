@echo off
chcp 65001 >nul
title ALLS STORE - PWA Server
echo.
echo ========================================
echo    🛍️ ALLS STORE - PWA Local Server
echo ========================================
echo.
echo Démarrage du serveur...
echo.

python start-server.py

if errorlevel 1 (
    echo.
    echo ❌ Erreur: Python n'est pas installé ou n'est pas dans le PATH
    echo.
    echo Veuillez installer Python depuis https://python.org
    echo.
    pause
)
