@echo off
echo 🚀 Starting Academic Poster Creator Setup...

REM Set Python path
set PYTHON_PATH=%USERPROFILE%\AppData\Local\Programs\Python\Python311\python.exe

REM Check if Python exists
if not exist "%PYTHON_PATH%" (
    echo ❌ Python not found at: %PYTHON_PATH%
    echo Please install Python 3.11 or update the path in this script
    pause
    exit /b 1
)

echo ✅ Python found at: %PYTHON_PATH%

REM Install/upgrade pip
echo 📦 Upgrading pip...
"%PYTHON_PATH%" -m pip install --upgrade pip

REM Install requirements
echo 📦 Installing dependencies...
"%PYTHON_PATH%" -m pip install -r requirements.txt

REM Check if Flask is installed
echo 🔍 Checking Flask installation...
"%PYTHON_PATH%" -c "import flask; print('✅ Flask is installed')" 2>nul
if errorlevel 1 (
    echo ❌ Flask installation failed
    pause
    exit /b 1
)

REM Kill any existing Python processes
echo 🧹 Cleaning up existing processes...
taskkill /f /im python.exe 2>nul

REM Start the server
echo 🚀 Starting Flask server...
echo 📱 Open your browser and go to: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.
"%PYTHON_PATH%" app.py

pause 