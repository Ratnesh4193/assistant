if True:
    from tkinter import *
    import speech_recognition as sr
    from time import ctime
    import webbrowser,time
    import playsound
    import os
    import random,pyttsx3,pyautogui
    from gtts import gTTS
    import bs4 as bs
    import urllib.request
    
#******************************************************************************************************************************
if True:
    root=Tk()
    #root.geometry("400x125+225+50")
    root.geometry("340x100+225+50")
    root.title("Assistant")
    #root.iconbitmap("C:/Users/SWAPNESH TIWARI/Desktop/website/sentdex/music_player.ico")
    root.resizable(False,False)
    root.config(bg="black")
#******************************************************************************************************************************
class person:
    name = ''
    def setName(self, name):
        self.name = name
class asis:
    name = ''
    def setName(self, name):
        self.name = name
'''def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()'''
def there_exists(terms):
    global voice_data,asis_obj,person_obj,text_to_speak,speaking_text
    for term in terms:
        if term in voice_data:
            return True
def record_audio(ask=""):
    global voice_data,terms,asis_obj,person_obj,text_to_speak,speaking_text
    with sr.Microphone() as source:
        if ask:
            engine_speak(ask)
        audio = r.listen(source,5,5) 
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down') 
        engine_speak(f">> {voice_data.lower()}") 
        return voice_data.lower()
def respond(voice_data):
    global terms,asis_obj,person_obj,text_to_speak,speaking_text
    #  greeting
    if there_exists(['hey','hi','hello']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)
    #  name
    elif there_exists(["your name should be"]):
        asis_name = voice_data.split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + asis_name)
        asis_obj.setName(asis_name)
    elif there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            engine_speak("My name is Alexa")
        else:
            engine_speak("my name is Alexis. what's your name?")
    elif there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name) # remember name in person object
    #  greeting
    elif there_exists(["how are you","how are you doing"]):
        engine_speak(f"I'm very well, thanks for asking {person_obj.name}")
    #  time
    elif there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        engine_speak(time)
    #  search google
    elif there_exists(["search for","search","find for me"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url ='https://www.google.com/search?source=hp&ei=mzSKXrigErWL4-EPpe6NyA4&q='+search_term+"&oq=coro&gs_lcp=CgZwc3ktYWIQAxgCMgUIABCDATIFCAAQgwEyAggAMgUIABCDATIFCAAQgwEyBQgAEIMBMgIIADIFCAAQgwEyAggAMgIIADoOCAAQ6gIQtAIQmgEQ5QJKFQgXEhEwZzI1NGcyNzhnMjI1ZzIyNUoNCBgSCTBnMWcxZzFnMVC5QFjbQ2C2WGgDcAB4AIABsQKIAekIkgEHMC4yLjIuMZgBAKABAaoBB2d3cy13aXqwAQY&sclient=psy-ab"
        webbrowser.get().open(url)
        engine_speak(f'Here is what I found for {search_term} on google')
    # : search youtube
    elif there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        engine_speak(f'Here is what I found for {search_term} on youtube')
    # weather
    elif there_exists(["weather"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q="+search_term+"&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on google")
    # game 
    elif there_exists(["game"]):
        voice_data = record_audio("choose among rock,paper or scissor")
        moves=["rock", "paper", "scissor"]
        cmove=random.choice(moves)
        pmove=voice_data
        

        engine_speak("I chose " + cmove)
        engine_speak("You chose " + pmove)
        #engine_speak("hi")
        if pmove==cmove:
            engine_speak("the match is draw")
        elif pmove== "rock" and cmove== "scissor":
            engine_speak("Player wins")
        elif pmove== "rock" and cmove== "paper":
            engine_speak("Computer wins")
        elif pmove== "paper" and cmove== "rock":
            engine_speak("Player wins")
        elif pmove== "paper" and cmove== "scissor":
            engine_speak("Computer wins")
        elif pmove== "scissor" and cmove== "paper":
            engine_speak("Player wins")
        elif pmove== "scissor" and cmove== "rock":
            engine_speak("Computer wins")
    # toss a coin
    elif there_exists(["toss","flip","coin"]):
        moves=["head", "tails"]   
        cmove=random.choice(moves)
        engine_speak("The computer chose " + cmove)
    # calc
    elif there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")
    # screenshot
    elif there_exists(["capture","my screen","screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('B:/cam_rkt/media/images/capture.png')     
    # to search wikipedia for definition
    elif there_exists(["definition of"]):
        definition=voice_data.split("definition of")[-1][1:]
        #definition=record_audio("what do you need the definition of")
        url=urllib.request.urlopen('https://en.wikipedia.org/wiki/'+definition)
        soup=bs.BeautifulSoup(url,'lxml')
        definitions=[]
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        print(definitions)
        if definitions:
            if definitions[1]:
                engine_speak ('Here is what i found '+definitions[1])
            elif definitions[2]:
                engine_speak('here is what i found '+definitions[2])
            else:
                engine_speak('im sorry i could not find that definition, please try a web search')
                
        else:
                engine_speak("im sorry i could not find the definition for "+definition)
    # exit
    elif there_exists(["exit", "quit", "goodbye"]):
        engine_speak("going offline")
        exit()    
def engine_speak(audio_string):
    global speaking_text
    tts=gTTS(text=audio_string,lang='en')
    r=random.randint(1,10000000)
    audio_file='audio-'+str(r)+".mp3"
    tts.save(audio_file)
    audio_string=asis_obj.name + ":", audio_string[:40]
    speaking_text.set(audio_string)
    playsound.playsound(audio_file)
    os.remove(audio_file)
def run():
    #engine = pyttsx3.init()
    voice_data=record_audio("Recording")
    speaking_text.set("Done")
    a="Q:", voice_data
    speaking_text.set(a)
    respond(voice_data)
def run_text():
    global voice_data
    voice_data=text_to_speak.get()
    speaking_text.set("Done")
    a="Q:", voice_data
    speaking_text.set(a)
    respond(voice_data)
#******************************************************************************************************************************
if True:
    global voice_data,terms,asis_obj,person_obj,text_to_speak,speaking_text
    text_to_speak=StringVar()
    text_to_speak.set("")
    speaking_text=StringVar()
    speaking_text.set("Hello User")
#******************************************************************************************************************************
if True:
    
    #***************************************************************************************************************************************    
    TrackEntry=Entry(root,font=('chiller',15,'italic bold'),width=20,textvar=text_to_speak)
    TrackEntry.grid(row=0,column=0,padx=5,pady=5)
    #********************************************************************************************************************************************
    search_button = Button(bg="red",text="Enter", padx=5, pady=0,font=('chiller',15,'italic bold'),activebackground="purple",command=run_text)
    search_button.grid(row=0,column=1,padx=5,pady=5)
    #***************************************************************************************************************************************  
    photo=PhotoImage(file="C:/Users/SWAPNESH TIWARI/Desktop/New folder/download1.png")
    photo=photo.subsample(3,3)
    audio_button = Button(bg="red",image=photo, padx=5, pady=0,font=('chiller',15,'italic bold'),activebackground="purple",command=run)
    audio_button.grid(row=0,column=2,padx=5,pady=5)
    #***************************************************************************************************************************************  
    speaking_text_label=Label(root,textvar=speaking_text,fg="red",background="black",font=('chiller',15,'italic bold'))
    speaking_text_label.grid(row=1,column=0,padx=5,pady=5,columnspan=3)
    #********************************************************************************************************************************************
#******************************************************************************************************************************
r=sr.Recognizer()
person_obj = person()
asis_obj = asis()
asis_obj.name = 'kiki'
root.mainloop()
