# Academic Poster Creator Startup Script
Write-Host "🚀 Starting Academic Poster Creator Setup..." -ForegroundColor Green

# Set Python path
$pythonPath = "$env:USERPROFILE\AppData\Local\Programs\Python\Python311\python.exe"

# Check if Python exists
if (-not (Test-Path $pythonPath)) {
    Write-Host "❌ Python not found at: $pythonPath" -ForegroundColor Red
    Write-Host "Please install Python 3.11 or update the path in this script" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "✅ Python found at: $pythonPath" -ForegroundColor Green

# Install/upgrade pip
Write-Host "📦 Upgrading pip..." -ForegroundColor Cyan
& $pythonPath -m pip install --upgrade pip

# Install requirements
Write-Host "📦 Installing dependencies..." -ForegroundColor Cyan
& $pythonPath -m pip install -r requirements.txt

# Check if Flask is installed
Write-Host "🔍 Checking Flask installation..." -ForegroundColor Cyan
try {
    & $pythonPath -c "import flask; print('✅ Flask is installed')"
    Write-Host "✅ Flask installation verified" -ForegroundColor Green
} catch {
    Write-Host "❌ Flask installation failed" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Kill any existing Python processes
Write-Host "🧹 Cleaning up existing processes..." -ForegroundColor Yellow
Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force

# Start the server
Write-Host "🚀 Starting Flask server..." -ForegroundColor Green
Write-Host "📱 Open your browser and go to: http://localhost:5000" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""
& $pythonPath app.py 