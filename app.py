from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return "<h1>ჩემი პროექტი მუშაობს</h1><p>ფიშინგ-სიმულატორის საწყისი ეტაპი</p>"

if __name__ == '__main__':
    app.run(debug = True)