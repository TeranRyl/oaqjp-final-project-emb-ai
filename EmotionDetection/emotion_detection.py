import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, headers=header, json=input, timeout=2.5)
    if response.status_code == 500 or response.status_code == 400:
        return {
        "anger": None, "disgust": None, "fear": None,
        "joy": None, "sadness": None, "dominant_emotion": None
        }
    formatted_response = json.loads(response.text)
    emotions_score = formatted_response["emotionPredictions"][0]["emotion"]
    emotion_key = "anger"
    dominant_emotion  = {emotion_key: emotions_score[emotion_key]}
    for emotion in emotions_score:
        if emotions_score[emotion] > dominant_emotion[emotion_key]:
            dominant_emotion = {emotion: emotions_score[emotion]}
            emotion_key = emotion
    output_format = {
        "anger": emotions_score["anger"],
        "disgust": emotions_score["disgust"],
        "fear": emotions_score["fear"],
        "joy": emotions_score["joy"],
        "sadness": emotions_score["sadness"],
        "dominant_emotion": emotion_key
    }
    return output_format
