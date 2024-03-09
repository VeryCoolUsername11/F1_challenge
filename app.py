from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Function to perform keyword recognition
def keyword_recognition(text):
    # Define a dictionary of keywords along with their corresponding regular expressions
    keywords = {
        'graining': r'\bgraining\b',  # Regular expression to match the keyword "graining"
        'blistering': r'\bblistering\b',  # Regular expression to match the keyword "blistering"
        'degradation': r'\bdegradation\b',  # Regular expression to match the keyword "degradation"
        'pit_stop': r'\bpit\s+stop\b',  # Regular expression to match the keyword "pit stop"
        'box': r'\bbox\b',  # Regular expression to match the keyword "box"
        'oversteer': r'\boversteer\b',  # Regular expression to match the keyword "oversteer"
        'loss_of_power': r'\bloss\s+of\s+power\b',  # Regular expression to match the keyword "loss of power"
        'traffic': r'\btraffic\b',  # Regular expression to match the keyword "traffic"
        'overtake': r'\bovertake\b',  # Regular expression to match the keyword "overtake"
        'defend': r'\bdefend\b',  # Regular expression to match the keyword "defend"
    }

    # List to store detected keywords
    results = []
    
    # Iterate through the keywords and their regular expressions
    for key, pattern in keywords.items():
        # Search for the keyword in the text using the corresponding regular expression
        match = re.search(pattern, text, re.IGNORECASE)
        # If the keyword is found, add it to the results list
        if match:
            results.append(key)

    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    # Handle form submission
    if request.method == 'POST':
        # Get the race information from the submitted form
        race_info = request.form['race_info']
        # Perform keyword recognition on the race information
        detected_keywords = keyword_recognition(race_info)
        # Render the HTML template with the race information and detected keywords
        return render_template('index.html', race_info=race_info, detected_keywords=detected_keywords)
    # Render the HTML template for initial page load
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)