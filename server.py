''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotions and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    anger_score = result["anger"]
    disgust_score = result["disgust"]
    fear_score = result["fear"]
    joy_score = result["joy"]
    sadness_score = result["sadness"]
    dominant_emotion = result["dominant_emotion"]
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is 'anger': {anger_score}, \
    'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and \
    'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
