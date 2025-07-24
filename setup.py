#!/usr/bin/env python3
"""
Setup script for Academic Poster Creator
This script helps you set up the project for local development.
"""

import os
import sys
import subprocess
import shutil

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python version {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def create_env_file():
    """Create .env file if it doesn't exist."""
    env_file = ".env"
    if os.path.exists(env_file):
        print("✅ .env file already exists")
        return True
    
    print("📝 Creating .env file...")
    env_content = """# Academic Poster Creator Environment Variables
# Add your API keys here (at least one is required)

# OpenAI API Key (get from https://platform.openai.com/api-keys)
OPENAI_API_KEY=your_openai_api_key_here

# Anthropic API Key (get from https://console.anthropic.com)
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Flask Secret Key (optional - will be auto-generated if not set)
FLASK_SECRET_KEY=your_secret_key_here

# Debug mode (set to True for development, False for production)
FLASK_DEBUG=True
"""
    
    try:
        with open(env_file, 'w') as f:
            f.write(env_content)
        print("✅ .env file created successfully")
        print("⚠️  Remember to add your actual API keys to the .env file!")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False

def create_directories():
    """Create necessary directories."""
    directories = ['uploads', 'template_library/available', 'template_library/coming_soon', 'template_library/premium']
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"📁 Created directory: {directory}")
        else:
            print(f"✅ Directory exists: {directory}")

def main():
    """Main setup function."""
    print("🚀 Academic Poster Creator Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Create .env file
    create_env_file()
    
    # Check if virtual environment exists
    venv_dir = "venv"
    if not os.path.exists(venv_dir):
        print("🐍 Creating virtual environment...")
        if not run_command("python -m venv venv", "Creating virtual environment"):
            sys.exit(1)
    else:
        print("✅ Virtual environment already exists")
    
    # Activate virtual environment and install dependencies
    print("\n📦 Installing dependencies...")
    
    # Determine the correct activation command
    if os.name == 'nt':  # Windows
        activate_cmd = "venv\\Scripts\\activate"
        pip_cmd = "venv\\Scripts\\pip"
    else:  # Unix/Linux/Mac
        activate_cmd = "source venv/bin/activate"
        pip_cmd = "venv/bin/pip"
    
    # Install requirements
    if not run_command(f"{pip_cmd} install -r requirements.txt", "Installing Python dependencies"):
        print("❌ Failed to install dependencies")
        print("💡 Try running: pip install -r requirements.txt manually")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Edit the .env file and add your API keys")
    print("2. Activate the virtual environment:")
    if os.name == 'nt':
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    print("3. Run the application:")
    print("   python app.py")
    print("4. Open your browser to: http://localhost:5000")
    
    print("\n🌐 To deploy to the internet:")
    print("1. Create a GitHub repository")
    print("2. Push your code to GitHub")
    print("3. Follow the instructions in DEPLOYMENT.md")
    
    print("\n📚 For more information, see README.md and DEPLOYMENT.md")

if __name__ == "__main__":
    main() 