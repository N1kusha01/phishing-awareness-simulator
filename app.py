from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def home():
    #ხსნის intel.html 
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():
    #მონაცემები რასაც მომხმარებელი შეიყვანს
    email = request.form.get('email')
    password = request.form.get('password')

    print(f"მონაცემები მოვიდა! Email: {email}, Password: {password}")

    return "<h1>ეს არის საგანმანათლებლო სიმულაცია</h1><p>თქვენი მონაცემები არსად არ გაიგზავნება</p>"

if __name__ == '__main__':
    app.run(debug = True)