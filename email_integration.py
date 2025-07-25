# Email Integration for PosterPro Landing Page
# Add these imports to your app.py file

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Add these environment variables to your .env file:
# GMAIL_EMAIL=your-gmail@gmail.com
# GMAIL_APP_PASSWORD=your_gmail_app_password
# ADMIN_EMAIL=your-personal-email@gmail.com

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

# Add this route to your app.py file
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

# Updated JavaScript for landing_page.html
"""
// Replace the current form submission with this:
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
""" 