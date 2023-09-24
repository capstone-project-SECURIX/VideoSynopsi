# VideoSynopsi
VideoSynopsi is a NLP subject mini project for Fr CRCE - BE Sem - 7

## Team
```
    - Hitest Sharma (Back-END :  Video to Text Conversion)
    - Aditya Vyas   (Back-END :  Research & LLM for summarization)
    - Atharva Pawar (Front-END:  Flask Api & Web-App)
```

This project is designed for text summarization of YouTube videos. It leverages the capabilities of the SpeechRecognition, moviepy, pydub, and pytube libraries for efficient text analysis and processing. The summarization algorithm employed in this project effectively extracts key sentences from the input text, resulting in a concise and informative summary of the video's content.


## Installation
    Project Folder : https://github.com/capstone-project-SECURIX/VideoSynopsi_.git

1. Clone the repository:

   ```bash
   git clone https://github.com/capstone-project-SECURIX/VideoSynopsi_.git
   cd VideoSynopsi_

2. Install Dependencies: 
    ```bash
    pip install -r requirements.txt

    #OR 

    # pip install cmd 
    pip install SpeechRecognition moviepy pydub pytube

## Usage
Video to Text Summarization:

The VideoSynopsi_ takes an youtube video link (URL) as input and returns a summary of that Video.

## VideoSynopsi_ (Video to Text) API

This API allows you to extract text data from a video using a provided API key and URL. It's designed to provide video-to-text summarization capabilities.

## API Endpoint

- **Endpoint:** `/apiVideo2Text`
- **Method:** GET

## Request Parameters

- `api_key` (string, required): An API key for authentication. Use `api123` for testing purposes.
- `url` (string, required): The URL of the video you want to process.

## Usage:
    1. Run the Flask app:
        python app.py

    2. Send a GET request to http://127.0.0.1:5000/apiVideo2Text?api_key=api123&url=https://www.youtube.com/watch?v=ankpGxGh8cA 

    3. The API will return the summarized text and other relevant information.

## Google Colab

`https://colab.research.google.com/drive/1_aTfavawuo8sE8waewwT-18BvTmel-Dc#scrollTo=SIB_bYdhF_qK`

## Example Request:

- GET /apiVideo2Text?api_key=api123&url=https://www.youtube.com/watch?v=ankpGxGh8cA


## Response

- If the API key is valid and the URL is accessible, the API will respond with a JSON object containing the following information:
  - `title` (string): The title of the video.
  - `url` (string): The URL of the video that was processed.
  - `author` (string): The author of the video.
  - `views` (integer): The view count of the video.
  - `length` (integer): The length of the video in seconds.
  - `raw_text` (string): A Raw text extracted from the video content.
  - `summarized_text` (string): A summarized text extracted from the raw_text.

## Example Response:
```json
{
    "title": "Unit 1- Lesson 7 - How To Pronounce the S in Plural Nouns - Pronunciation - Beginners Level",
    "url": "https://www.youtube.com/watch?v=ankpGxGh8cA",
    "author": "TEFLship",
    "views": 334,
    "length": 72,
    "Raw_text": "hello this time we got pronunciation yes let's pronounce these words together we got three sounds to pronounce the letter S at the end of the plural nouns now let's listen to them and repeat the words tape script 1.14 pronunciation books students cause computers hamburgers Cambridge televisions bags phones some images houses buses wait for more units more lessons for the beginners English level and more levels coming soon thank you ",
    "summarized_text": "14 pronunciation books students cause computers hamburgers Cambridge televisions bags phones some images houses buses wait for more units more lessons for the beginners English level an an English for adults level 1 and 2. 1. Pronunciation books: 1. The sound of the letter S at the end of the plural nouns now let's listen to them and repeat the words. 2. The sounds of the letters A, E, and F at the beginning of the nouns.\nMore levels coming soon thank you. d more levels comingSoon.    d more level coming soon. Thank you for your support and support.  D more levels  coming soon thanks for support. d  more levelsComing soon.  More levels coming Soon.",
}

```

## Status Codes:

- `200 OK`: The request was successful, and the API has responded with the expected data.
- `401 Unauthorized`: The provided API key is invalid or missing. You need a valid API key for access.
- `500 Internal Server Error`: An error occurred during processing. This could be due to various reasons, such as video download failures or other unexpected errors.

## Responses Time

- for `72 Second` long video it took `2 mins`. 


## Contributing
Contributions are welcome! If you have suggestions, improvements, or bug fixes, please create an issue or a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.