from flask import Flask, render_template

app = Flask(__name__)  # Ensure Flask is correctly initialized

@app.route('/')
def index():
    return render_template('chat.html')  # Ensure chat.html exists inside "templates/"

if __name__ == '__main__':
    app.run(debug=True)