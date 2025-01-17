import speech_recognition as sr
import datetime
import wikipedia
import pyttsx3
import subprocess
import webbrowser
import random
import os
import smtplib

MASTER = "Shivaani"

#Text To Speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)

#here audio is a var which contains text
def speak(audio):  
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good morning Shivani mam, how may i help you?")
    elif hour>=12 and hour<18:
        speak("good afternoon shivani mam")
    else:
        speak("good evening Shivani mam")

#now convert audio to text
def takecom():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        speak('command')
        print("Listening....")
        audio = r.listen(source)
    try:
        print("Recognising...")
        text = r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:                #For Error handling
        speak("Your last command couldn't be heard")
        print("Network connection error")
        return "none"
    return text

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com')
    server.ehlo()
    server.starttls()
    server.login('shivaani2525@gmail.com','shivani123')
    server.sendmail("shivaniverma2120@gmail.com",to,"hello")
    server.close()

#for main function
if __name__ == "__main__":
    wish()
    while True:
        query = takecom().lower()

        #Wikipedia
        if "wikipedia" in query:
            speak("searching details....Wait")
            query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{MASTER} the time is {strTime}")
            print(f"{MASTER} the time is {strTime}")
        
        #Web Searches
        elif 'open youtube' in query or "open video online" in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")
        elif 'open github' in query or 'github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")
        elif 'open facebook' in query or 'facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")
        elif 'open instagram' in query or 'instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")
        elif 'open google' in query or 'google' in query:
            webbrowser.open("https://www.google.com")
            speak("opening google")
        elif 'join a video call' in query or 'join a meeting' in query or 'join a call' in query:
            webbrowser.open("https://zoom.us/join")
            speak("joining call")
        elif 'open yahoo' in query or 'yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")
        elif 'open snapdeal' in query or 'snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com")
            speak("opening snapdeal")
        elif 'open amazon' in query or 'shop online' in query or 'amazon' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")
        elif 'open flipkart' in query or 'flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")
        elif 'open ebay' in query or 'ebay' in query:
            webbrowser.open("https://www.ebay.com")
            speak("opening ebay")
               
        elif "youtube search" in query or 'search in youtube' in query:
            stMsgs = ['please tell what you want to search','sir please dictate your search']
            ans_q = random.choice(stMsgs)
            speak(ans_q)
            ans_take_from_user_youtube_search = takecom().lower()
            temp = ans_take_from_user_youtube_search.replace(' ','+')
            g_url="https://www.youtube.com/results?search_query="
            res_g = 'Showing results for' + ans_take_from_user_youtube_search + 'in youtube'
            print(res_g)
            speak(res_g)
            webbrowser.open(g_url+temp)

        #Gmail 
        elif "open gmail" in query or "gmail" in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail")

        elif "send an email" in query or "send a mail" in query or "send a gmail" in query:
            try:
                speak("whom am i supposed to send the email?")
                reciever = input("Please enter the recievers email address.\n")
                speak("what should i send")
                content = takecom().lower()
                to = reciever
                sendEmail(to,content)
                speak("email has been send successfully")
            except Exception as e:
                print(e)

        #Music and Video
        elif 'music from pc' in query or "music" in query:
            speak("ok i am playing music")
            music_dir = './music'
            musics = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,musics[0]))
        elif 'video from pc' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = './video'
            videos = os.listdir(music_dir)
            os.startfile(os.path.join(video_dir,videos[0]))

        #Chatbot and others
        elif 'good bye' in query or 'bye bye' in query or "goodbye" in query:
            speak("good bye")
            exit()
        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing! how are you?', 'I am fine! how are you?', 'Nice!', 'ALEXIS for her boss','I am nice and full of energy! how are you?','i am ready to serve you! how are you?','i am okay ! How are you?']
            ans_q = random.choice(stMsgs)
            speak(ans_q)
            ans_take_from_user_how_are_you = takecom()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okay' in ans_take_from_user_how_are_you:
                speak('okay..')
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you or 'mood off' in ans_take_from_user_how_are_you:
                speak('oh sorry... how may I relieve you ')
        elif 'made you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " For your information Shivani Created me ! I give Lot of Thanks to Her "
            print(ans_m)
            speak(ans_m)
        elif 'you are better than siri' in query or 'you are better than google assistant' in query or 'you are better than bixby' in query or 'you are better'in query or 'yuo are best' in query:
            stMsgs = ['thank you sir', 'always on your duty', 'ready to serve','i thank a lot to you','always for you','Always my slogan ALEXIS for her Boss.']
            ans_q = random.choice(stMsgs)
            speak(ans_q)
        elif "who are you" in query or "about you" in query or "your details" in query or "what are you" in query:
            about = "I am ALEXIS which means Artificial learning executable Xtra Integrated Software, an AI based computer program but I can help you lot like a your close friend ! I promise you ! Simple try me to give simple command ! like playing music or video from your directory. I also play video and song from web or online ! I can also entertain you. So I think that you Understood me ! Lets Start "
            print(about)
            speak(about)
        elif "hello" in query or "hello ALEXIS" in query or "hello assistant" in query:
            stMsgs = ['Hi there', 'Hello boss', 'Hello Shivani mam','How can I help you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)
        elif 'thank you' in query or 'thanks' in query or 'thank you jarvis' in query or 'i thank you'in query:
            stMsgs = ['Welcome Sir', 'Always on your duty', 'Anytime','No Need','always for you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)
        elif 'you drink' in query or 'you drink alchohol' in query or 'drink beer' in query:
            stMsgs = ['fluids are not required by virtual assistants', 'not a big fan ', 'no not at all and i request you to do the same','i am a bit health consious']
            ans_q = random.choice(stMsgs)
            speak(ans_q)
        elif 'you take tobacco' in query or 'you eat tobacco' in query or 'you take cigarette' in query or 'you smoke' in query or 'you take drugs' in query:
            stMsgs = ['not a big fan ', 'no not at all and i request you to do the same','i am a bit health consious']
            ans_q = random.choice(stMsgs)
            speak(ans_q)
        elif "do you eat" in query:
            stMsgs = ["eatables aren't required by softwares."]
            ans_q = random.choice(stMsgs)
            speak(ans_q)
            print(ans_q)
        elif "your name" in query or "sweet name" in query:
            na_me = "Thanks for Asking my name.  My self ! ALEXIS"
            print(na_me)
            speak(na_me)
        elif "you feeling" in query:
            print("Feeling very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you")
        elif "wait" in query:
            print("Waiting for your command...")
            speak("waiting for your command...")
            continue
        elif query == 'none':
            continue

        #Opening Apps
        elif "open notepad" in query or "make a note" in query or "note down" in query:
            stMsgs = ['What would you like me to note?', 'What would you like to note?']
            ans_q = random.choice(stMsgs)
            speak(ans_q)
            print(ans_q)
            ans_take_from_user_notepad_note = takecom().lower()
            speak("okay... made a note")
            print("okay... made a note")
            def note(text):
                date = datetime.datetime.now()
                file_name = str(date).replace(":","-") + "-note.txt"
                with open(file_name, "w") as f:
                    f.write(text)

                subprocess.Popen(["notepad.exe",file_name])
            note(ans_take_from_user_notepad_note)
 
        elif "open zoom" in query:
            zoomPath = "C:\\Users\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoomPath)
        elif "open command prompt" in query:
            speak("opening cmd")
            cmdPath = "C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(cmdPath)
        elif "open photoshop" in query:
            speak("photoshop will open shortly")
            photoshopPath = "C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\Photoshop.exe"
            os.startfile(photoshopPath)
        elif "open whatsapp" in query:
            speak ("opening whatsapp")
            whatsappPath = "https://web.whatsapp.com/"
            os.startfile(whatsappPath)
       
        
        #Exit
        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')
        elif 'exit' in query or 'abort' in query or 'got what i wanted' in query or 'stop'in query:
            stMsgs = ['nice meeting with you', 'I feeling very sweet after meeting with you but you are going!', 'contact me anytime for help','bye bye sir','boss will meet you next time']
            ans_q = random.choice(stMsgs)
            speak(ans_q)
            exit()
        
        #Else
        else:
            temp = query.replace(' ','+')
            g_url="https://www.google.com/search?q="
            res_g = 'i need to search the web!'
            print(res_g)
            speak(res_g)
            webbrowser.open(g_url+temp)
