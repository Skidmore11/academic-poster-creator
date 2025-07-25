# 🚀 Quick Start Guide

## Daily Startup (Choose One Method)

### Method 1: PowerShell Script (Recommended)
```powershell
.\start_server.ps1
```

### Method 2: Batch File
```cmd
start_server.bat
```

### Method 3: Manual (if scripts don't work)
```powershell
# Kill any existing Python processes
taskkill /f /im python.exe

# Start the server
& "$env:USERPROFILE\AppData\Local\Programs\Python\Python311\python.exe" app.py
```

## What These Scripts Do

1. ✅ **Find Python** - Locates your Python installation
2. 📦 **Install Dependencies** - Automatically installs Flask and other requirements
3. 🧹 **Clean Up** - Kills any existing Python processes to avoid conflicts
4. 🚀 **Start Server** - Launches the Flask development server

## Access Your App

Once the server is running, open your browser and go to:
**http://localhost:5000**

## Troubleshooting

### If you see "Python was not found":
- The scripts automatically find Python in the user directory
- If you have Python installed elsewhere, edit the `PYTHON_PATH` in the scripts

### If you see "Flask not found":
- The scripts automatically install dependencies
- Just run the script again

### If you see multiple Python processes:
- The scripts automatically clean up existing processes
- Or manually run: `taskkill /f /im python.exe`

## Development Mode

The server runs in debug mode, so it will automatically reload when you make changes to the code! 🎉 