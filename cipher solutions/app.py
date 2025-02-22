from flask import Flask, render_template, request, redirect, flash
import smtplib

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone = request.form['phone']
        email = request.form['email']
        message = request.form['message']
        
        sender_email = "srp0093@gmail.com"
        sender_password = "mxdt pxmq ysqc uhmh"
        recipient_email = "cipherconsults@gmail.com"
        
        email_message = f"Subject: New Contact Form Submission\n\nFirst Name: {first_name}\nLast Name: {last_name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}"
        
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, recipient_email, email_message)
            flash("Message sent successfully!", "success")
        except Exception as e:
            flash("Error sending message. Please try again.", "danger")
            print(e)
        
        return redirect('/contact')
    
    return render_template('contact.html')

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy.html')

if __name__ == "__main__":
    app.run(debug=True)
