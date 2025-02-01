from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/get', methods=['POST'])  # Ensure this route exists
def get_response():
    user_message = request.form.get('msg')  # Get the message from the user
    response = f"I received your message: {user_message}"  # Basic response
    return response

if __name__ == '__main__':
    app.run(debug=True)
