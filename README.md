# Emotion Detector

A Python coursework project that sends text to a hosted Watson NLP emotion-prediction endpoint and returns the raw response.

## Project context

Created as part of the **Python Project for AI & Application Development** course. This repository demonstrates a small API integration module; the current files do not include a Flask server, browser interface, or local machine-learning model.

## What the module does

- Accepts text through `emotion_detector(text_to_analyse)`.
- Sends an HTTP POST request using Python `requests`.
- Calls the Skills Network Watson NLP `EmotionPredict` endpoint with the configured English emotion model.
- Returns `response.text` directly to the caller.

## Tech stack

Python · requests · hosted Watson NLP endpoint

## Try the module

From the repository root, install the dependency:

```bash
python -m pip install requests
```

Then call the function:

```python
from EmotionDetection.emotion_detection import emotion_detector

print(emotion_detector("I am happy to learn something new."))
```

The example requires network access and an accessible Skills Network endpoint. Endpoint availability has not been verified for use outside the course environment.

## Current scope

The function returns the raw API response. It does not currently parse emotion scores, select a dominant emotion, validate input, set a request timeout, or handle unsuccessful HTTP responses. Those are possible next steps for extending this learning project.

---

[Explore my other projects](https://github.com/ghiffarr#readme)
