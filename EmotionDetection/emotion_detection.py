import requests


def emotion_detector(text_to_analyse):
    """Detect emotions in the provided text using Watson NLP."""

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    return response.text
