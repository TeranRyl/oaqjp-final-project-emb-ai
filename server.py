from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    anger_score = result["anger"]
    disgust_score = result["disgust"]
    fear_score = result["fear"]
    joy_score = result["joy"]
    sadness_score = result["sadness"]
    dominant_emotion = result["dominant_emotion"]
    return f"For the given statement, the system response is 'anger': {anger_score}, \
    'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and \
    'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
