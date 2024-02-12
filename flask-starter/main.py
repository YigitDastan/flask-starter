from flask import Flask, render_template

app = Flask(__name__)

#routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin_panel():
    return render_template('admin_panel.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

#start
if __name__ == '__main__':
    app.run(debug=True)