import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime
import openai
from config import apikey
import random



chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Chetana: {query}\n Mickey: "
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt= chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["text"])
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language = "en-in")
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError:
        return "Sorry, there was an error in reaching the speech recognition service."




if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Mickey A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],["google", "https://www.google.com"],["instagram", "https://www.instagram.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}...")
                webbrowser.open(site[1])

        # todo: Add a feature to play a specific song
        if "open music" in query:
            musicPath = r"C:\Users\Chetana\Downloads\Hymn.mp3"
            os.system(f"start {musicPath}")

        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"The time is {hour} and {min} minutes")

        elif "open spotify".lower() in query.lower():
            spotifyPath = r"C:\Users\Chetana\AppData\Local\Microsoft\WindowsApps\Spotify.exe"
            os.system(f"start {spotifyPath}")

        elif "open skype".lower() in query.lower():
            skypePath = r"C:\Users\Chetana\AppData\Local\Microsoft\WindowsApps\Skype.exe"
            os.system(f"start {skypePath}")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Mickey Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)



        #say(query)


