@echo off
REM Color codes for Windows
setlocal enabledelayedexpansion

echo.
echo =====================================================================
echo.
echo      AVIATOR PREDICTOR CONGO BET - DEMARRAGE OPTIMISE (WINDOWS)
echo.
echo =====================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Python n'est pas installe
    echo Telechargez depuis: https://www.python.org/downloads/
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [OK] Python %PYTHON_VERSION% detecte

REM Create virtual environment
if not exist "venv\" (
    echo [CREATION] Environnement virtuel...
    python -m venv venv
    echo [OK] Environnement virtuel cree
)

REM Activate virtual environment
echo [ACTIVATION] Environnement virtuel...
call venv\Scripts\activate.bat

REM Upgrade pip
echo [INSTALLATION] pip mise a jour...
python -m pip install --upgrade pip setuptools wheel >nul 2>&1
echo [OK] pip mis a jour

REM Install requirements
echo [INSTALLATION] Dependances...
pip install -r requirements.txt >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Installation des dependances echouee
    pause
    exit /b 1
)
echo [OK] Dependances installees

REM Create .env
if not exist ".env" (
    echo [CREATION] Fichier .env...
    copy .env.example .env >nul
    echo [OK] Fichier .env cree
)

REM Create directories
if not exist "data\" mkdir data
if not exist "models\" mkdir models
if not exist "logs\" mkdir logs
echo [OK] Repertoires crees

REM Clear database
if exist "data\aviator_games.db" (
    echo [NETTOYAGE] Base de donnees...
    del data\aviator_games.db
)

echo.
echo =====================================================================
echo                    CHOIX DU MODE DE DEMARRAGE
echo =====================================================================
echo.
echo 1 - MODE DEVELOPPEMENT (Flask - Port 5000)
echo 2 - MODE PRODUCTION (Gunicorn - Port 8000)
echo 3 - MODE DOCKER (Requiert Docker Desktop)
echo.
set /p choice="Entrez votre choix (1-3): "

if "%choice%"=="1" (
    echo.
    echo =====================================================================
    echo [DEMARRAGE] MODE DEVELOPPEMENT
    echo =====================================================================
    echo.
    echo [INFO] Application: http://localhost:5000
    echo [INFO] Dashboard: http://localhost:5000
    echo [INFO] API Health: http://localhost:5000/api/health
    echo.
    echo Appuyez sur CTRL+C pour arreter
    echo.
    
    set FLASK_ENV=development
    set FLASK_APP=app.py
    python app.py
    
) else if "%choice%"=="2" (
    echo.
    echo =====================================================================
    echo [DEMARRAGE] MODE PRODUCTION (Gunicorn)
    echo =====================================================================
    echo.
    echo [INFO] Application: http://localhost:8000
    echo [INFO] Dashboard: http://localhost:8000
    echo [INFO] API Health: http://localhost:8000/api/health
    echo.
    echo Appuyez sur CTRL+C pour arreter
    echo.
    
    gunicorn --workers=4 --bind=0.0.0.0:8000 --timeout=120 ^
             --access-logfile=logs/access.log ^
             --error-logfile=logs/error.log wsgi:app
    
) else if "%choice%"=="3" (
    echo.
    echo =====================================================================
    echo [DEMARRAGE] MODE DOCKER
    echo =====================================================================
    echo.
    echo [VERIFICATION] Docker Desktop...
    docker --version >nul 2>&1
    if errorlevel 1 (
        echo ERREUR: Docker n'est pas installe
        echo Telechargez depuis: https://www.docker.com/products/docker-desktop
        pause
        exit /b 1
    )
    
    echo [CONSTRUCTION] Image Docker...
    docker-compose build
    
    echo.
    echo [DEMARRAGE] Conteneur Docker...
    echo.
    echo [INFO] Application: http://localhost:8000
    echo [INFO] Dashboard: http://localhost:8000
    echo.
    
    docker-compose up
    
) else (
    echo ERREUR: Choix invalide
    pause
    exit /b 1
)

pause
