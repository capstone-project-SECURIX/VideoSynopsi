from flask import Flask, render_template, request, redirect, send_file
from pytube import YouTube
import os
import re

import speech_recognition as sr
import moviepy.editor as mp
from pydub import AudioSegment

import requests

import matplotlib.pyplot as plt
from wordcloud import WordCloud



app = Flask(__name__)

# Function to clean and sanitize a filename
def clean_filename(filename):
    # Remove invalid characters by using a regular expression
    return re.sub(r'[\/:*?"<>|]', '', filename)

def video_2_text(filename):
    # clip = mp.VideoFileClip(r"Obama_1.mp4")

    clip = mp.VideoFileClip(r"static/downloads/sampleVideo.mp4")
    clip.audio.write_audiofile(r"static/vid_2_Audio_converted/converted.wav")

    # Split the audio file into smaller chunks to avoid memory issues
    audio_file = AudioSegment.from_file(r"static/vid_2_Audio_converted/converted.wav", format="wav")
    chunk_size = 10 * 1000  # 10 seconds
    chunks = []
    for i in range(0, len(audio_file), chunk_size):
        chunks.append(audio_file[i:i + chunk_size])

    # Initialize variables for result text and summarized text
    result_text = ""

    # Create a Recognizer instance and transcribe each chunk
    r = sr.Recognizer()
    for chunk in chunks:
        try:
            with sr.AudioFile(chunk.export(format="wav")) as audio:
                audio_data = r.record(audio)
                text = r.recognize_google(audio_data)
                result_text += text + " "
        except sr.UnknownValueError:
            # Handle the case when no speech is recognized in the chunk
            print("No speech detected in a chunk.")
            continue
    # print(result_text)


    # # Write the data to the file
    # file_path = 'static/videotext.txt'
    # with open(file_path, 'w') as file:
    #     file.write(result_text)
    # print(f"Data saved to {file_path}")

    return result_text

@app.route("/v2text")
def video_2text():
    filename = "sampleVideo.mp4"
    output = video_2_text(filename)
    summarize = largetext_2_summarize(output)
    video_info = {"largeText": output,
                "summarize": summarize,
                  }
    # print("v2text: ", output)
    # print("\n\nsummarize: ", summarize)


    data_forFile = f"Raw Text : {output} \n\n\n Summarize Text : {summarize}"
    # Write the data to the file
    file_path = 'static/videotext.txt'
    with open(file_path, 'w') as file:
        file.write(data_forFile)
    # print(f"Data saved to {file_path}")

    return render_template("index.html", video_info=video_info)

@app.route("/dummy")
def dummy():
    largeText = "are you an introvert or a shy person do you not know what to say and you feel awkward in social gatherings or after the first introduction you just completely words or in a conversation your always thinking of what next to say so you are always distracted as well I get it I understand that a lot of US I want to that when I was growing up and it's unfortunate that school and college never pays attention in teaching how to become an effective communicator because if you effective communicator if you are a confident communicator a whole host of opportunities open in front of you you can know how to make friends you can know how to you can know how to get growth you can grow in life create opportunities for yourself get respected in the world for who you are all of this is possible if you know how to become a good communicator and that's why I created this course for you to teach you everything that I know about communication and what is the ultimate guide to effective communication in this course I basically give you three key elements of communication I teach you how to become an effective speaker of what your native language is I also didn't teach you how to become an effective writer in today's world writing documents creating presentations has become such an important part of our growth that you cannot not know how to write well on the number 3 but as the most important communication is not just about how will you speak it's not just about how will you right it's a lot more about how well do you listen and if you do not know how to listen to the one opposite you will never be an effective communicator so when you combine these three things of speaking writing and listening you get the ultimate guide to active communication skill if you buy the 749 premium plan you also get a bonus exclusive content module on cold emailing Industries my life and have certain will create a lot of opportunities for you as well so what we have with three and a half hours only three and a half hours to become an effective communicator we have a bonus content on cold emailing we have PDF notes to revise everything with exercises to own your skills and whatever you learnt and then you have live class where you can clarify questions with me as part of a large group all of this with lifetime access and with all future upgrades for this course absolutely free 749 but I don't make it even more exciting for you if you do not like the course in the first two weeks of doing it making it the most risk free and ultimate investment towards an effective"

    summarize = "Are you an introvert or a shy person do you not know what to say and you feel awkward in social gatherings or after the first introduction you just completely words or in a conversation your always thinking of what next to say so you are always distracted as well. I understand that a lot of US I want to that when I was growing up and it's unfortunate that school and college never pays atte. \"If you are a confident communicator a whole host of opportunities open in front of you" "All of this is possible if you know how to make friends" "You can grow in life create opportunities for yourself" "Get respected in the world for who you are" "I created this course for you to teach you everything that I know about communication and what is the ultimate guide to effective communication in this course I basically give you three key elements of communication" "I teach you how to become an effective speaker of what your native language is\" In today's world writing documents creating presentations has become such an important part of our growth that you cannot not know how to write well on the number 3. As the most important communication is not just about how will you speak but about how well do you listen. If you do not knowHow to listen to the one opposite you will never be able to understand the other. If you buy the 749 premium plan you also get a bonus exclusive content module on cold emailing. \"I have certain will create a lot of opportunities for you as well so what we have with three and a half hours only three and two hours. be an effective communicator\" Learn how to cold email for two and a half hours. Live class where you can clarify questions with me as part of a large group. Free lifetime access and with all future upgrades for this course absolutely free 749 but I don't make it 749 but I don't make it. The course is designed to be a risk-free and ultimate investment towards an effective career. Even more exciting for you if you do not like the course in the first two weeks of doing it making it the most risk free and ultimate investment in your career."


    generate_word_cloud(summarize)

    video_info = {

        "title": "IOT intro by Atharva Pawar",
        "author": "Atharva Pawar",
        "length": "2321",
        "views": "10120282",

        "largeText": largeText,
        "summarize": summarize,

    }
    return render_template("index.html", video_info=video_info)



def largetext_2_summarize(largeText):

    LARGE_ARTICLE = largeText

    # Your input text
    #data = """do you have to practice who you want to be you know you don't wake up one morning and you're suddenly who you think you wlay some some """

    # Split the input text into blocks of 400 characters each
    block_size = 400
    text_blocks = [LARGE_ARTICLE[i:i+block_size] for i in range(0, len(LARGE_ARTICLE), block_size)]
    print("text_blocks: ", len(text_blocks))

    # Initialize a list to store the summaries
    summaries = []

    # Generate summaries for each block and store them - (max_length=130)
    for block in text_blocks:
        # summary = summarizer(block, max_length=50, min_length=30, do_sample=False)
        try:
            summary = summarizeText(block)
            # print("\t\t\t\tsummary: ", summary)
            summaries.append(summary[0]["summary_text"])
        except:
            pass

    # Combine the individual summaries into a final summary
    final_summary = "\n".join(summaries)

    # Print the final summary
    # print(final_summary)
    return final_summary


def summarizeText(text):

    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": "Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    output = query({  "inputs": text,  })

    # print(output)
    return output


@app.route("/", methods=["GET", "POST"])
def index():
    video_info = None
    download_link = None

    if request.method == "POST":
        youtube_url = request.form["youtube_url"]
        try:
            yt = YouTube(youtube_url)

            # print("Download YT Video") 
            stream = yt.streams.get_highest_resolution()
            # filename = clean_filename(yt.title) + ".mp4"  # Clean the filename
            # stream.download(filename=os.path.join("downloads", "sampleVideo.mp4"))
            stream.download(filename="static/downloads/sampleVideo.mp4")
            download_link = "static/downloads/sampleVideo.mp4"
            # download_link = "/download/sampleVideo.mp4" + filename

            # convert video to text
            # print("convert video to text ") 
            largeText = video_2_text("sampleVideo.mp4")
            # print("largeText: ", largeText)

            # summarize the large text
            # print("summarize the large text") 
            summarize = largetext_2_summarize(largeText)
            # print("summarize: ", summarize)

            generate_word_cloud(summarize)


            video_info = {

                "title": yt.title,
                "author": yt.author,
                "length": yt.length,
                "views": yt.views,

                "largeText": largeText,
                "summarize": summarize,

            }


        except Exception as e:
            return "Error: " + str(e)

    return render_template("index.html", video_info=video_info, download_link=download_link)

@app.route("/download/<filename>")
def download(filename):
    # return send_file(os.path.join("downloads", filename), as_attachment=True)
    return send_file(filename, as_attachment=True)

def generate_word_cloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(8, 4))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig("static/wordcloud.png")  # Save the word cloud as an image





if __name__ == "__main__":
    app.run(debug=True)
