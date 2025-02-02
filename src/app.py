from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)

# Define a dictionary for symptom checking
symptom_dict = {
    "fever": "You might have a viral or bacterial infection. Drink fluids and rest. If fever persists for more than 3 days, consult a doctor.",
    "cold": "You might have a common cold. Rest, drink warm fluids, and take over-the-counter medication if needed.",
    "cough": "It could be due to a viral infection, allergies, or irritation. If it lasts more than 2 weeks, see a doctor.",
    "chest pain": "Chest pain can be serious. If it's severe or accompanied by breathlessness, seek medical help immediately!",
    "headache": "This could be due to stress, dehydration, or migraines. If it is severe or persistent, see a doctor.",
    "difficulty breathing": "This could indicate asthma, pneumonia, or even a heart issue. Seek emergency medical care!",
    "sore throat": "It may be due to an infection. Drink warm liquids and use throat lozenges. If it worsens, consult a doctor.",
    "stomach pain": "Could be due to indigestion, food poisoning, or other conditions. Monitor your symptoms and see a doctor if needed."
}

# Function to check symptoms
def check_symptom(symptom):
    symptom = symptom.lower()
    if symptom in symptom_dict:
        return symptom_dict[symptom]
    else:
        return "I'm not sure about this symptom. Please consult a medical professional."

# Flask Routes
@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/get', methods=['POST'])
def get_response():
    user_message = request.form.get('msg')  # Get user input
    response = check_symptom(user_message)  # Check the symptom
    return response  # Return chatbot response

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)