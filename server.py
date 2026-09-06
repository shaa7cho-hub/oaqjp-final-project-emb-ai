"""
This module sets up a Flask web server for executing emotion detection analysis
on user-provided text inputs via an AI backend service.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Instantiate the Flask application
app = Flask(__name__)

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Retrieves text from the web request parameters, analyzes it using
    the emotion detector package, and returns a formatted result string.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return formatted_response

@app.route("/")
def render_index_page():
    """
    Serves the main application landing page interface using the HTML template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
