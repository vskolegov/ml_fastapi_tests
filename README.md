[![Tests](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml)

# An example of ML Application with the pretrained model and test.

An example of English text tone detection with [Hugging Face](https://huggingface.co/) library.


Tests GitHub Actions

## API Methods

### GET /

- **Description:** Returns a welcome message.
- **Response:**
  - 200 OK
  - `{"message": "Hello World"}`

### POST /predict/

- **Description:** Predicts the sentiment of a given text.
- **Request:**
  - `{"text": "Your text here"}`
- **Response:**
  - 200 OK
  - `{"label": "POSITIVE/NEGATIVE", "score": 0.99}`

### POST /detailed_predict/

- **Description:** Predicts the sentiment of a given text with detailed information.
- **Request:**
  - `{"text": "Your text here"}`
- **Response:**
  - 200 OK
  - `{"label": "POSITIVE/NEGATIVE", "score": 0.99, "text": "Your text here"}`
