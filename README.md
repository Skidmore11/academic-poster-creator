# Academic Poster Creator

Turn your research papers into beautiful academic posters with AI! Just upload a PDF and watch the magic happen.

## What This Does

Ever spent hours trying to fit your research into a poster template? This app does that for you. Upload your research paper (PDF), and it uses AI to pull out the important stuff and put it into a professional poster format.

## Features

- **AI Magic**: Uses ChatGPT or Claude to read your paper and extract the good stuff
- **Multiple Templates**: Choose from different poster styles
- **Add Your Figures**: Upload up to 4 images with descriptions
- **Smart Sizing**: Automatically adjusts text size so everything fits nicely
- **Easy to Use**: Just upload and download - no design skills needed

## What You Need

- Python 3.8 or newer
- An OpenAI API key (or Anthropic if you prefer Claude)
- That's it!

## Quick Start

### 1. Get the Code
```bash
git clone https://github.com/Skidmore11/academic-poster-creator.git
cd academic-poster-creator
```

### 2. Set It Up
```bash
python setup.py
```
This will create a virtual environment and install everything you need.

### 3. Add Your API Key
Edit the `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=your_key_here
```

### 4. Run It
```bash
python app.py
```
Open your browser to `http://localhost:5000`

## Getting an API Key

### OpenAI (Recommended)
1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign up (it's free)
3. Go to "API Keys" 
4. Click "Create new secret key"
5. Copy the key (starts with `sk-`)

### Anthropic (Alternative)
1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up
3. Go to "API Keys"
4. Create a new key
5. Copy it (starts with `sk-ant-`)

## How It Works

1. **Upload**: You upload a research paper PDF
2. **AI Reads**: The AI reads through your paper and extracts:
   - Title and authors
   - Introduction and background
   - Methods and results
   - Conclusions and references
3. **Template**: It puts everything into a professional poster template
4. **Download**: You get a PowerPoint file ready to print


## Support

Having trouble?
1. Check the troubleshooting section above
2. Look at existing GitHub issues
3. Create a new issue with details about what went wrong

## Why I Built This

I got tired of spending hours manually copying text from papers into poster templates. This automates the boring part so you can focus on the research!
