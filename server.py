"""
Flask server for emotion detection.
Provides an endpoint /emotionDetector that accepts a text parameter.
Handles blank input error with appropriate user message.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page (index.html provided in templates folder)."""
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    """
    Handle GET request with 'textToAnalyze' query parameter.
    Returns formatted string with emotion scores or error message for blank input.
    """
    text = request.args.get('textToAnalyze')
    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is 'anger':"
        f"{result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']},"
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}."
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
