# Academic Poster Creator

An AI-powered web application that automatically generates professional academic posters from research manuscripts. Upload a PDF, and the app extracts key information using AI to create a beautifully formatted research poster.

## 🚀 Features

- **AI-Powered Content Extraction**: Uses OpenAI GPT-4 or Anthropic Claude to extract structured content from research papers
- **Multiple Template Support**: Choose from various professional poster templates
- **Figure Integration**: Upload up to 4 figures with descriptions
- **Dynamic Font Sizing**: Automatically adjusts font sizes based on content length
- **Modern Web Interface**: Beautiful, responsive design with drag-and-drop uploads
- **Template Library Management**: Upload and manage your own templates
- **Dual AI Provider Support**: Switch between OpenAI and Anthropic APIs

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **AI APIs**: OpenAI GPT-4, Anthropic Claude
- **PDF Processing**: PyMuPDF
- **Document Generation**: python-pptx
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Image Processing**: Pillow

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key OR Anthropic API key
- Git

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/academic-poster-creator.git
cd academic-poster-creator
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
# Required: At least one API key must be set
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Optional: Flask secret key (auto-generated if not set)
FLASK_SECRET_KEY=your_secret_key_here
```

### 5. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 🌐 Deployment Options

### Option 1: Railway (Recommended for Beginners)

1. **Create Railway Account**: Sign up at [railway.app](https://railway.app)
2. **Connect GitHub**: Link your GitHub repository
3. **Deploy**: Railway will automatically detect it's a Python app and deploy
4. **Set Environment Variables**: Add your API keys in Railway dashboard
5. **Access**: Your app will be live at a Railway URL

### Option 2: Render

1. **Create Render Account**: Sign up at [render.com](https://render.com)
2. **New Web Service**: Connect your GitHub repository
3. **Configure**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Environment**: Python 3
4. **Set Environment Variables**: Add your API keys
5. **Deploy**: Render will build and deploy your app

### Option 3: Heroku

1. **Create Heroku Account**: Sign up at [heroku.com](https://heroku.com)
2. **Install Heroku CLI**: Download and install from Heroku website
3. **Login**: `heroku login`
4. **Create App**: `heroku create your-app-name`
5. **Set Environment Variables**:
   ```bash
   heroku config:set OPENAI_API_KEY=your_key_here
   heroku config:set ANTHROPIC_API_KEY=your_key_here
   ```
6. **Deploy**: `git push heroku main`

### Option 4: DigitalOcean App Platform

1. **Create DigitalOcean Account**: Sign up at [digitalocean.com](https://digitalocean.com)
2. **Create App**: Connect your GitHub repository
3. **Configure**:
   - **Source**: GitHub repository
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Run Command**: `python app.py`
4. **Set Environment Variables**: Add your API keys
5. **Deploy**: DigitalOcean will build and deploy your app

## 🔧 Configuration

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | Yes* | Your OpenAI API key |
| `ANTHROPIC_API_KEY` | Yes* | Your Anthropic API key |
| `FLASK_SECRET_KEY` | No | Flask secret key (auto-generated if not set) |

*At least one API key must be set

### App Configuration

Edit the configuration section in `app.py`:

```python
# File Settings
UPLOAD_FOLDER = 'uploads'
MAX_CONTENT_LENGTH = 500 * 1024 * 1024  # 500MB max file size

# Cleanup Settings
AUTO_CLEANUP_UPLOADS = True
KEEP_FINAL_OUTPUT = True

# Testing Settings
USE_DUMMY_DATA = False
```

## 📁 Project Structure

```
academic-poster-creator/
├── app.py                 # Main Flask application
├── template_configs.py    # Template configuration and settings
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── .gitignore            # Git ignore rules
├── README.md             # This file
├── static/               # Static assets (CSS, JS, images)
├── templates/            # HTML templates
├── template_library/     # PowerPoint template library
│   ├── available/        # Available templates
│   ├── coming_soon/      # Coming soon templates
│   └── premium/          # Premium templates
└── uploads/              # Temporary upload storage
```

## 🎨 Customization

### Adding New Templates

1. Create your PowerPoint template with named shapes
2. Upload via the web interface or place in `template_library/available/`
3. Add configuration in `template_configs.py` if needed

### Modifying AI Prompts

Edit the prompt in the `call_ai_api()` function in `app.py` to customize how the AI extracts information.

### Styling Changes

Modify the CSS in `templates/index.html` to change the appearance.

## 🔒 Security Considerations

- **API Keys**: Never commit API keys to version control
- **File Uploads**: The app validates file types and sizes
- **Environment Variables**: Use `.env` file for local development
- **HTTPS**: Always use HTTPS in production

## 🐛 Troubleshooting

### Common Issues

1. **"API key not configured"**: Make sure your `.env` file has the correct API keys
2. **"Module not found"**: Run `pip install -r requirements.txt`
3. **"Port already in use"**: Change the port in `app.py` or kill the existing process
4. **Large file uploads fail**: Check the `MAX_CONTENT_LENGTH` setting

### Debug Mode

Set `USE_DUMMY_DATA = True` in `app.py` to test without API calls.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Search existing GitHub issues
3. Create a new issue with detailed information

## 🙏 Acknowledgments

- OpenAI for GPT-4 API
- Anthropic for Claude API
- The Flask community for the excellent web framework
- All contributors and users of this project 