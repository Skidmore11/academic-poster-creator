# Email Integration Setup Guide

## Overview
This guide will help you integrate email notifications into your PosterPro landing page. When someone completes the form, you'll receive an email notification with their details.

## Step 1: Add Email Imports to app.py

Add these imports to the top of your `app.py` file (after the existing imports):

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
```

## Step 2: Add Email Functions to app.py

Add these functions to your `app.py` file (you can add them after the existing functions, before the routes):

```python
def send_signup_notification(name, email):
    """Send email notification when someone signs up."""
    try:
        # Get email settings from environment
        sender_email = os.getenv('GMAIL_EMAIL')
        sender_password = os.getenv('GMAIL_APP_PASSWORD')
        admin_email = os.getenv('ADMIN_EMAIL')
        
        if not all([sender_email, sender_password, admin_email]):
            return False, "Email configuration missing"
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = admin_email
        msg['Subject'] = f"🎉 New PosterPro Signup: {name}"
        
        # Email body
        body = f"""
🎉 New PosterPro Signup!

Name: {name}
Email: {email}
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
IP Address: {request.remote_addr}
User Agent: {request.headers.get('User-Agent', 'Unknown')}

This person has joined your PosterPro waitlist!

---
Sent automatically from your PosterPro landing page.
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email using Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        
        return True, "Notification sent successfully"
        
    except Exception as e:
        return False, f"Email error: {str(e)}"
```

## Step 3: Add API Route to app.py

Add this route to your `app.py` file (you can add it with the other routes):

```python
@app.route('/api/subscribe', methods=['POST'])
def subscribe():
    """Handle email subscription from landing page."""
    try:
        data = request.get_json()
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        
        # Validation
        if not name or not email:
            return jsonify({'success': False, 'message': 'Name and email are required'}), 400
        
        # Send notification to admin
        email_success, email_message = send_signup_notification(name, email)
        
        if email_success:
            return jsonify({
                'success': True, 
                'message': 'Thank you! We\'ll notify you when we launch.'
            })
        else:
            # Still return success to user, but log the email error
            print(f"Email notification failed: {email_message}")
            return jsonify({
                'success': True, 
                'message': 'Thank you! We\'ll notify you when we launch.'
            })
            
    except Exception as e:
        return jsonify({'success': False, 'message': 'Server error occurred'}), 500
```

## Step 4: Update .env File

Add these lines to your `.env` file:

```env
# Email Notification Settings
GMAIL_EMAIL=your-gmail@gmail.com
GMAIL_APP_PASSWORD=your_gmail_app_password
ADMIN_EMAIL=your-personal-email@gmail.com
```

## Step 5: Get Gmail App Password

1. Go to your Google Account settings: https://myaccount.google.com/
2. Go to "Security" → "2-Step Verification" (enable if not already)
3. Go to "Security" → "App passwords"
4. Select "Mail" and "Other (Custom name)"
5. Name it "PosterPro Landing Page"
6. Copy the generated 16-character password
7. Use this password as your `GMAIL_APP_PASSWORD`

## Step 6: Update Landing Page JavaScript

Replace the form submission code in `landing_page.html` with this updated version:

```javascript
// Email form handling
document.getElementById('emailForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const name = e.target.querySelector('input[type="text"]').value;
    const email = e.target.querySelector('input[type="email"]').value;
    
    // Hide any existing messages
    document.getElementById('successMessage').style.display = 'none';
    document.getElementById('errorMessage').style.display = 'none';
    
    // Simple validation
    if (!name || !email) {
        showError('Please fill in all fields');
        return;
    }
    
    if (!isValidEmail(email)) {
        showError('Please enter a valid email address');
        return;
    }
    
    // Show loading state
    const submitBtn = e.target.querySelector('.submit-btn');
    const originalText = submitBtn.innerHTML;
    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Subscribing...';
    submitBtn.disabled = true;
    
    // Send to server
    fetch('/api/subscribe', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, email })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showSuccess(data.message);
            e.target.reset();
        } else {
            showError(data.message);
        }
    })
    .catch(error => {
        showError('Network error. Please try again.');
    })
    .finally(() => {
        // Reset button
        submitBtn.innerHTML = originalText;
        submitBtn.disabled = false;
    });
});
```

## Step 7: Test the Integration

1. Start your Flask server: `python app.py`
2. Go to your landing page: `http://localhost:5000/landing_page.html`
3. Fill out the form and submit
4. Check your email for the notification

## What You'll Receive

When someone signs up, you'll get an email like this:

```
Subject: 🎉 New PosterPro Signup: John Smith

🎉 New PosterPro Signup!

Name: John Smith
Email: john.smith@university.edu
Date: 2025-01-27 15:30:45
IP Address: 192.168.1.100
User Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36

This person has joined your PosterPro waitlist!

---
Sent automatically from your PosterPro landing page.
```

## Troubleshooting

### "Email configuration missing"
- Make sure all three environment variables are set in your `.env` file
- Check that the variable names match exactly

### "Authentication failed"
- Make sure you're using an App Password, not your regular Gmail password
- Verify that 2-Step Verification is enabled on your Google account

### "Network error"
- Check that your Flask server is running
- Verify the `/api/subscribe` route is accessible

## Security Notes

- Never commit your `.env` file to version control
- The Gmail App Password is more secure than using your regular password
- IP addresses and user agents are logged for your reference

## Next Steps

Once this is working, you could also:
1. Add email validation on the server side
2. Store signups in a database
3. Send welcome emails to subscribers
4. Add email marketing integration

Let me know if you need help with any of these steps! 🚀 