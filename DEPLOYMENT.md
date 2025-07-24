# Deployment Guide

This guide will walk you through deploying your Academic Poster Creator to various hosting platforms.

## 🚀 Quick Deploy Options

### Option 1: Railway (Easiest - Recommended)

**Time to deploy: ~5 minutes**

1. **Sign up**: Go to [railway.app](https://railway.app) and create an account
2. **Connect GitHub**: Click "New Project" → "Deploy from GitHub repo"
3. **Select Repository**: Choose your academic-poster-creator repository
4. **Auto-deploy**: Railway will automatically detect it's a Python app
5. **Set Environment Variables**: In the Railway dashboard:
   - Go to your project → Variables tab
   - Add `OPENAI_API_KEY` with your OpenAI key
   - Add `ANTHROPIC_API_KEY` with your Anthropic key (optional)
6. **Access**: Your app will be live at a Railway URL (e.g., `https://your-app.railway.app`)

**Pros**: Free tier available, automatic HTTPS, easy setup
**Cons**: Limited free tier resources

### Option 2: Render (Great Free Tier)

**Time to deploy: ~10 minutes**

1. **Sign up**: Go to [render.com](https://render.com) and create an account
2. **New Web Service**: Click "New" → "Web Service"
3. **Connect GitHub**: Link your repository
4. **Configure**:
   - **Name**: `academic-poster-creator`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Plan**: Free (or paid for more resources)
5. **Environment Variables**: Add:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `ANTHROPIC_API_KEY`: Your Anthropic API key (optional)
6. **Deploy**: Click "Create Web Service"
7. **Access**: Your app will be live at `https://your-app.onrender.com`

**Pros**: Generous free tier, automatic HTTPS, easy scaling
**Cons**: Free tier has cold starts

### Option 3: Heroku (Classic Choice)

**Time to deploy: ~15 minutes**

1. **Sign up**: Go to [heroku.com](https://heroku.com) and create an account
2. **Install Heroku CLI**: Download from [devcenter.heroku.com](https://devcenter.heroku.com/articles/heroku-cli)
3. **Login**: Open terminal/command prompt and run:
   ```bash
   heroku login
   ```
4. **Create App**: In your project directory:
   ```bash
   heroku create your-app-name
   ```
5. **Set Environment Variables**:
   ```bash
   heroku config:set OPENAI_API_KEY=your_openai_key_here
   heroku config:set ANTHROPIC_API_KEY=your_anthropic_key_here
   ```
6. **Deploy**:
   ```bash
   git add .
   git commit -m "Initial deployment"
   git push heroku main
   ```
7. **Open**: `heroku open`

**Pros**: Reliable, good documentation, many integrations
**Cons**: No free tier anymore, requires credit card

## 🔧 Pre-Deployment Checklist

Before deploying, make sure you have:

- [ ] ✅ Created a GitHub repository
- [ ] ✅ Pushed your code to GitHub
- [ ] ✅ Created a `.env` file locally (for testing)
- [ ] ✅ Tested the app locally with `python app.py`
- [ ] ✅ Obtained API keys (OpenAI or Anthropic)
- [ ] ✅ Created the files we just made:
  - `requirements.txt`
  - `.gitignore`
  - `README.md`
  - `Procfile` (for Heroku)
  - `runtime.txt`

## 📝 Step-by-Step GitHub Setup

If you haven't set up GitHub yet:

1. **Create GitHub Account**: Go to [github.com](https://github.com) and sign up
2. **Create Repository**: Click "New repository"
   - Name: `academic-poster-creator`
   - Description: `AI-powered academic poster generator`
   - Make it Public (for free hosting)
   - Don't initialize with README (we already have one)
3. **Push Your Code**: In your project directory:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/academic-poster-creator.git
   git push -u origin main
   ```

## 🔑 Getting API Keys

### OpenAI API Key
1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign up or log in
3. Go to "API Keys" section
4. Click "Create new secret key"
5. Copy the key (starts with `sk-`)

### Anthropic API Key
1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up or log in
3. Go to "API Keys" section
4. Click "Create Key"
5. Copy the key (starts with `sk-ant-`)

## 🌐 Custom Domain (Optional)

After deploying, you can add a custom domain:

### Railway
1. Go to your project dashboard
2. Click "Settings" tab
3. Under "Domains", click "Generate Domain"
4. Or add your own domain

### Render
1. Go to your service dashboard
2. Click "Settings" tab
3. Under "Custom Domains", add your domain
4. Update your DNS records as instructed

### Heroku
1. Go to your app dashboard
2. Click "Settings" tab
3. Under "Domains", add your domain
4. Update your DNS records

## 🔍 Post-Deployment Testing

After deployment, test these features:

1. **Homepage**: Loads correctly
2. **File Upload**: Can upload a PDF
3. **AI Processing**: Generates poster content
4. **Template Selection**: Can choose templates
5. **Download**: Can download the generated PowerPoint
6. **Figure Upload**: Can upload images (if supported)

## 🐛 Common Deployment Issues

### "Build Failed"
- Check that `requirements.txt` exists and has correct dependencies
- Ensure Python version in `runtime.txt` is supported
- Check build logs for specific errors

### "Application Error"
- Check environment variables are set correctly
- Verify API keys are valid
- Check application logs for errors

### "Module Not Found"
- Ensure all dependencies are in `requirements.txt`
- Check that the build completed successfully

### "Port Issues"
- Most platforms automatically handle port configuration
- If using Heroku, make sure you're using their port: `os.environ.get('PORT', 5000)`

## 💰 Cost Considerations

### Free Tiers
- **Railway**: $5/month after free tier (500 hours)
- **Render**: Free tier available (sleeps after inactivity)
- **Heroku**: No free tier (starts at $7/month)

### Paid Options
- **Railway**: Pay-as-you-use
- **Render**: $7/month for always-on service
- **Heroku**: $7/month basic dyno
- **DigitalOcean**: $5/month droplet

## 🔒 Security Best Practices

1. **Never commit API keys** to GitHub
2. **Use environment variables** for all secrets
3. **Enable HTTPS** (automatic on most platforms)
4. **Set up monitoring** for your deployed app
5. **Regular updates** of dependencies

## 📞 Getting Help

If you encounter issues:

1. **Check the logs** in your hosting platform's dashboard
2. **Test locally** first to isolate issues
3. **Search GitHub issues** for similar problems
4. **Check platform documentation** for specific requirements
5. **Ask in community forums** or create a GitHub issue

## 🎉 Success!

Once deployed, your Academic Poster Creator will be live on the internet! Share the URL with others and start creating amazing academic posters.

Remember to:
- Monitor your API usage and costs
- Keep your dependencies updated
- Backup your template library
- Test new features before deploying 