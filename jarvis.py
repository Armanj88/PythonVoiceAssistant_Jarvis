import wmi
from rich.traceback import install
from rich.console import Console
from jarvisUi import Ui_Jarvis
from pywikihow import search_wikihow
from JarvisModule import *
from selenium import webdriver
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from pydub import AudioSegment
from pydub.silence import split_on_silence
from phonenumbers import geocoder, carrier
from string import ascii_lowercase
from selenium import webdriver
from selenium.webdriver.common.by import By
import speech_recognition as sr
from googletrans import Translator  # pip install googletrans==3.1.0a0
from tkinter import *
from tkcalendar import *
import pyttsx3
import JarvisModule
import win32com.client as win32
import json
import datetime
import pickle
import os
import phonenumbers
import random
import sys
import psutil
import requests
import cv2
import wikipedia
import socket
import webbrowser
import pywhatkit
import smtplib
import pyjokes
import soundcard as sc
import soundfile as sf
import pyautogui
import time
import PyPDF2
import winsound
import speedtest
import subprocess
import re
from plyer import notification
import rotatescreen

os.system("cls")

# rich configurations.
install()
console = Console(record=True)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 177)

with open("name.txt", "r") as f:
    full_name = f.read()
    name = full_name.split(" ")[0]
    lastname = full_name.split(" ")[1]

password_original = f"play soccer with {name}"

if os.path.exists("alarms.pkl"):
    if os.path.getsize("alarms.pkl") > 0:
        with open("alarms.pkl", "rb") as f:
            alarms = pickle.load(f)
    else:
        with open("alarms.pkl", "wb") as f:
            pickle.dump([], f)
            alarms = []
else:
    with open("alarms.pkl", "wb") as f:
        pickle.dump([], f)
        alarms = []

_password_protect = False
if os.path.exists("protect.secret"):
    with open("protect.secret", "rb") as f:
        _password_protect = pickle.load(f)


# cloudconvert_api_key = """eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYzFkNmE0OTdjMTRhOWViMzViMzAzYWNkMWFiYjA4NzQ3MDg2MjA4ODJmNzg3ZWFhYmI2NTliM2JiZmM4M2MyZGU1M2IzMGQ2OWRlMjZjZTciLCJpYXQiOjE2NTg5NDM3MDAuMjM4MTQzLCJuYmYiOjE2NTg5NDM3MDAuMjM4MTQ0LCJleHAiOjQ4MTQ2MTczMDAuMjM0NTc0LCJzdWIiOiI1MjQ2OTE3MCIsInNjb3BlcyI6WyJ1c2VyLnJlYWQiLCJ1c2VyLndyaXRlIiwidGFzay53cml0ZSIsInRhc2sucmVhZCIsIndlYmhvb2sud3JpdGUiLCJ3ZWJob29rLnJlYWQiLCJwcmVzZXQucmVhZCIsInByZXNldC53cml0ZSJdfQ.AT62jjGugY2NIrjanYHKcOSYFQa29zJPGtuv7PoAocrIcs6MSAxPVilsX6qlPTMOnpMY8te6iCnoOVx17jD2MX5UXrB4RAK4tPaJ4os-dQEALU980jOhBAOmdaTJwj4hw0BeY_HlsBbESs9FCEjwd3AQ2LQYTwrMpLNuBgpScAkDO09-O4sfn961UeyMiqZQpYsfSQ76R1wceAw-mKiWXK5R2n2rgVb0LFc-tWlDvpwCvTNnLZvqkQYu_WhGHPMvZFjW0TJkhF0kdBS53pXEtKmolov10-DDwJN8McCkEhnOnNirgoEhH8SoYBUUZzGvsrjzBmw90rJfd_zEudXbH3BAaW3keXMav3VbtcziSYpmr82W9ndoGCSmG_wvDIPf6X9BsNRP8TTdJpUL8ulZJipsnMPOwWEgaPRE0_cMtfElli8zZyNZKvBC3DcolFLt9CgTNVPSSUR-kWRU_IaJkDLdBer_GBegKyHVoLNB6DRJm_BXQg0wNlRt9_dfwGYi82yw9f70ff2WpnErBsAKgBTW1zdSBkh0pwfmZyN3Rc3hWda0PJqJXAa8SLZk-7trYkH7GkOPm5FGUT5n0neX1X0t8y5guYYS0PWkXv9JvPTUoB7xmQToESckQuV4YMlX3RTR4jJwEt7bATvJE_fP0tQ8DuLhHXdL8KTyIGyAYP4"""
# cloudconvert.configure(api_key=cloudconvert_api_key, sandbox=False)


# print(voices)


# Check whatsapp messages
def check_whatsapp():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://web.whatsapp.com/")
    speak("Sir, You have to scan the QR code to login to your whatsapp account.")
    time.sleep(25)
    ready = "no"
    while ready == "no":
        speak("Sir, Are you ready?")
        ready = startExecution.take_command()
        if ready == "yes":
            break
        else:
            continue
    unread_chats = driver.find_elements(By.XPATH,
        '/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/span[1]/div/span')
    unread_chats_count = len(unread_chats)
    if unread_chats_count > 0:
        speak(f"Sir, You have {unread_chats_count} unread messages on whatsapp")
    else:
        speak(f"Sir, You don't have any unread messages on whatsapp")


# Enigma class
class Enigma:
    def __init__(self, steckerbrett=None, settings_file=None, alpha=None, beta=None, gama=None):
        """ The initial setting of enigma before the encryption """
        # Creating a list of all alphabet letters
        if steckerbrett is None:
            steckerbrett = {" ": " "}
        self.alphabet = list(ascii_lowercase)

        '''
            Steckerbrett is a system of sockets that connects pairs of letters that are interchanged between them,
            without going throw all the rotors of enigma
        '''
        self.steckerbrett = steckerbrett
        if settings_file is not None:
            ''' If the setting sites is got then we load the setting from it as a json format '''
            try:
                # I verify if there is a such file with setting that we got
                self.settings = json.load(open(settings_file, 'r'))[0]
            except IOError:
                # The first enigma error - There is no such a settings file
                print("Enigma Error 1: There is no such setting file")
            finally:
                # steckerbratt -> a dictionary with pairs of interchangeable pairs of letters
                self.steckerbrett = self.settings['steckerbrett']
                # Setting the states of rotors
                self.alpha = self.settings['alpha']
                self.beta = self.settings['beta']
                self.gama = self.settings['gama']
        elif alpha is not None and beta is not None and gama is not None and steckerbrett is not None:
            ''' Setting the rotors and the steckerbrett manually '''
            if type(steckerbrett) is not dict:
                self.steckerbrett = {" ": " "}
            self.alpha = alpha
            self.beta = beta
            self.gama = gama
        else:
            # Setting all rotors to base states and steckerbrett to have only space case
            if type(steckerbrett) is not dict:
                self.steckerbrett = {" ": " "}
            rotors = [self.alpha, self.beta, self.gama]
            for rotor in rotors:
                if rotor is None or type(rotor) is not int or type(rotor) is not float:
                    rotor = 0
                else:
                    rotor = rotor % 26
            self.alpha = rotors[0]
            self.beta = rotors[1]
            self.gama = rotors[2]
        # Making the steckerbrett interchangeable and removing these pairs from the alphabet
        for letter in list(self.steckerbrett.keys()):
            if letter in self.alphabet:
                self.alphabet.remove(letter)
                self.alphabet.remove(self.steckerbrett[letter])
                self.steckerbrett.update({self.steckerbrett[letter]: letter})
        # Setting the reflector
        self.reflector = [letter for letter in reversed(self.alphabet)]

    def permutate(self, rotor):
        """ This function is permutatting the alphabet depending on the rotors settings """
        new_alphabet = ''.join(self.alphabet)
        new_alphabet = list(new_alphabet)
        for _iter in range(rotor):
            new_alphabet.insert(0, new_alphabet[-1])
            new_alphabet.pop(-1)
        # print(self.alphabet)
        # print(new_alphabet)
        return new_alphabet

    def inverse_permutation(self, rotor):
        """ This function is permutatting the alphabet depending on the rotors settings on the back way """
        new_alphabet = ''.join(self.alphabet)
        new_alphabet = list(new_alphabet)
        for _iter in range(rotor):
            new_alphabet.append(new_alphabet[0])
            new_alphabet.pop(0)
        # print(self.alphabet)
        # print(new_alphabet)
        return new_alphabet

    def encrypt_text(self, text):
        """ This function encrypts a string """
        encrypted_text = []
        # Text preprocessing
        text = text.lower()
        text.split()
        # Encryption of every letter
        for letter in text:
            # Checking if the letter is in steckerbrett
            if letter in self.steckerbrett:
                # If it is, the we encrypt it as it's pair
                encrypted_text.append(self.steckerbrett[letter])
                # Turning the rotors
                self.alpha += 1
                if self.alpha % len(self.alphabet) == 0:
                    self.beta += 1
                    self.alpha = 0
                if self.beta % len(self.alphabet) == 0 and self.alpha % len(self.alphabet) != 0 and self.beta >= len(
                        self.alphabet) - 1:
                    self.gama += 1
                    self.beta = 1
            else:
                # Encrypting throw rotors
                # Letter is encrypted by first rotor
                temp_letter = self.permutate(self.alpha)[self.alphabet.index(letter)]
                # print("alpha - {}".format(temp_letter))
                # Letter is encrypted by second rotor
                temp_letter = self.permutate(self.beta)[self.alphabet.index(temp_letter)]
                # print("beta - {}".format(temp_letter))
                # Letter is encrypted by third rotor
                temp_letter = self.permutate(self.gama)[self.alphabet.index(temp_letter)]
                # print("gama - {}".format(temp_letter))
                # Reflector is returning the inverse of that letter
                # print(temp_letter)
                temp_letter = self.reflector[self.alphabet.index(temp_letter)]
                # print("reflector - > {}".format(temp_letter))
                # Back way
                # Letter is encrypted by third rotor
                temp_letter = self.inverse_permutation(self.gama)[self.alphabet.index(temp_letter)]
                # print("gama - {}".format(temp_letter))
                # Letter is encrypted by second rotor
                temp_letter = self.inverse_permutation(self.beta)[self.alphabet.index(temp_letter)]
                # print("beta - {}".format(temp_letter))
                # Letter is encrypted by first rotor
                temp_letter = self.inverse_permutation(self.alpha)[self.alphabet.index(temp_letter)]
                # print("alpha - {}".format(temp_letter))
                encrypted_text.append(temp_letter)
                # print(temp_letter)
                # turning the rotors
                self.alpha += 1
                if self.alpha % len(self.alphabet) == 0:
                    self.beta += 1
                    self.alpha = 0
                if self.beta % len(self.alphabet) == 0 and self.alpha % len(self.alphabet) != 0 and self.beta >= len(
                        self.alphabet) - 1:
                    self.gama += 1
                    self.beta = 1
                # print('alpha - {}'.format(self.alpha))
        return ''.join(encrypted_text)

    def encrypt_txt(self, original_path, encrypted_path=None):
        """ This function allows to encrypt an entire .txt file """
        global _file
        try:
            # I verify if there is a such file to encrypt
            _file = open(original_path, 'r')
        except IOError:
            # The second enigma error - There is no such file to encrypt
            print("Enigma Error 2: There is no such file to encrypt")
            return None
        finally:
            # If the is such a file the, we run this section
            # We check if the user putted an output file
            if encrypted_path is None:
                # If not then we create one with just adding 'encrypted_' before the name of the original file
                encrypted_path = "encrypted_" + original_path
            # Creating of an encrypted file
            encrypted_file = open(encrypted_path, 'w')
            # Encrypting and writing every line to the encrypted file
            for line in _file:
                encrypted_file.write(self.encrypt_text(line.rstrip()) + '\n')
            # Closing the file
            _file.close()
            encrypted_file.close()


# Get Location by phone number
def get_number_info(number):
    if number[0] != "+":
        number = "+" + number
    try:
        ch_number = phonenumbers.parse(number, "CH")
        country = geocoder.description_for_number(ch_number, "en")
        service_number = phonenumbers.parse(number, "RO")
        isp = carrier.name_for_number(service_number, "en")

        return country, isp
    except Exception:
        console.print_exception()
        return "", ""


# Get the Wi-Fi passwords
def get_wifi_passwords():
    command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()
    profile_names = (re.findall("All User Profile" + " " * 5 + ": (.*)\r", command_output))
    wifi_list = []
    if len(profile_names) != 0:
        for profile_name in profile_names:
            wifi_profile = {}
            profile_info = subprocess.run(["netsh", "wlan", "show", "profile", profile_name],
                                          capture_output=True).stdout.decode()
            if re.search('Security key' + " " * 11 + ": Absent", profile_info):
                continue
            else:
                wifi_profile['ssid'] = name
                profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"],
                                                   capture_output=True).stdout.decode()
                password = re.search("Key Content " + " " * 12 + ": (.*)\r", profile_info_pass)
                if password is None:
                    wifi_profile['password'] = None
                else:
                    wifi_profile['password'] = password[1]
                wifi_list.append(wifi_profile)
    return wifi_list


# Recognize text from audio
def recognize_text(_path, length, lang="en-US"):
    r = sr.Recognizer()
    if length == "short":
        with sr.AudioFile(_path) as source:
            audio = r.record(source)
            try:
                text = r.recognize_google(audio, language=lang)
                return text
            except Exception:
                console.print_exception()
                speak("Sorry sir, I couldn't understand that!")
            return None
    elif length == "long":
        def get_large_audio_transcription(_path):
            sound = AudioSegment.from_file(_path)
            chunks = split_on_silence(
                sound,
                min_silence_len=500,
                silence_thresh=sound.dBFS - 14,
                keep_silence=500,
            )
            folder_name = "audio-chunks"
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
            whole_text = ""
            for i, audio_chunk in enumerate(chunks, start=1):
                chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
                audio_chunk.export(chunk_filename, format="wav")
                with sr.AudioFile(chunk_filename) as _source:
                    audio_listened = r.record(_source)
                    try:
                        _text = r.recognize_google(audio_listened, language=lang)
                    except sr.UnknownValueError as e:
                        print("Error:", str(e))
                    else:
                        _text = f"{_text.capitalize()}. "
                        print(chunk_filename, ":", _text)
                        whole_text += _text
            with open("transcription.txt", "w") as file:
                file.write(whole_text)
            return whole_text

        get_large_audio_transcription(_path)


# Summarize the file
def file_summarize(path):
    r = requests.post(
        "https://api.deepai.org/api/summarization",
        files={
            'text': open(path, 'rb'),
        },
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    ).json()
    summarize = r['output']
    return summarize


# Summarize the text
def text_summarize(text):
    r = requests.post(
        "https://api.deepai.org/api/summarization",
        data={
            'text': text,
        },
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    ).json()
    summarize = r['output']
    return summarize


# text to speech
def speak(text, *args):
    engine.say(text)
    print(text, *args)
    engine.runAndWait()


# set alarm
def alarm(time_alarm):
    hour = time_alarm['hour']
    minute = time_alarm['minute']
    t = time_alarm['alarm_time']
    alarm_time = f"{hour}:{minute} {t}"
    print(f"Done, alarm is set for {alarm_time}")

    while True:
        try:
            if datetime.datetime.now().strftime("%p").lower() == t.lower() and \
                    int(hour) == int(datetime.datetime.now().strftime("%I")) and \
                    int(minute) == int(datetime.datetime.now().strftime("%M")):
                print("Alarm is running")
                winsound.Beep(1000, 1000)
                t.sleep(3)
            else:
                continue
        except KeyboardInterrupt:
            speak("Alarm is stopped")
            break


# Send email
def send_email(from_, to, subject, body):
    olApp = win32.Dispatch("outlook.application")
    olNS = olApp.GetNamespace("MAPI")
    mailItem = olApp.CreateItem(0)
    mailItem.Subject = subject
    mailItem.BodyFormat = 1
    mailItem.Body = body
    mailItem.To = to
    mailItem._oleobj_.Invoke(*(64209, 0, 8, 0, olNS.Accounts.Item(from_)))

    mailItem.Display()
    mailItem.Save()
    mailItem.Send()


# Clock
def clock():
    my_clock = Tk()
    my_clock.title("Clock")
    my_clock.geometry("500x500")

    def time_update():
        string = time.strftime('%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000, time)

    lbl = Label(my_clock, font=('DS-Digital', 72, 'bold'), background='purple', foreground='white')

    lbl.pack(anchor='center', expand=True, fill=BOTH)
    time_update()

    my_clock.mainloop()


# for read pdf
def pdf_reader():
    speak("Please enter path of your pdf file.")
    path = input("Enter path: ").replace('"', "").replace("'", "").replace("/", "\\").strip()
    book = open(path, 'rb')
    reader = PyPDF2.PdfFileReader(book)
    pages = reader.numPages
    speak(f"Total numbers of pages in this pdf file is {pages}")
    speak("Sir please enter the page number I have to read from.")
    pg = int(input("Enter page number: "))
    for num in range(pg - 1, pages):
        page = reader.getPage(num)
        text = page.extractText()
        speak(text)


# For get number counters
def NumberCounters(num):
    num = int(num)
    _counters = []
    for i in range(1, num + 1):
        if num % i == 0:
            _counters.append(i)
    return _counters


# For check number is prime or not
def is_prime(num):
    prime = True
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
    else:
        prime = None
    return prime


# Get news
def news(category='technology', country='us', language='en'):
    _api_key = 'pub_973342609b08d4418932d411b9c8639d343b'
    base_url = f'https://newsdata.io/api/1/news?apikey={_api_key}&country={country}&language={language}&category={category}'
    response = requests.get(base_url).json()
    if response['status'] == 'success':
        _news = response['results']
        for i in _news:
            try:
                speak(f"News number {_news.index(i) + 1}. {i['title']}")
                speak(f"{i['description']}")
                i['url'] = i['url'].replace('http', 'https').replace("https://", "")
                speak(f"Url: {i['url']}")
            except KeyboardInterrupt:
                speak("News reading stopped sir.")
                break
    else:
        speak("Sorry sir, The response of news api is not success")


# Take persian
def take_persian(print_command=True):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if print_command:
            print("Listening...")
        audio = r.listen(source)
        try:
            if print_command:
                print("Recognizing...")
            q = r.recognize_google(audio, language='fa-IR')
            if print_command:
                print(f"User said: {q}\n")
        except Exception:
            # speak("I can't understand you sir")
            return "None"
        return q.lower()


# Translator
def Translate(text1, lang1, lang2):
    translate = Translator()
    result = translate.translate(text1, src=lang1, dest=lang2)
    translated = result.text
    # _summary_of = f"({result.src}) {result.origin} \n({result.dest}) {result.text}"
    _summary_of = (result.src, result.origin, result.dest, result.text)
    return translated, _summary_of


# for dictionary
def dictionary(word):
    global partOfSpeech, definition, example
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    response = requests.get(url).json()
    try:
        audio_phonetics = response[0]['phonetics'][0]['audio']
    except:
        audio_phonetics = None
    speak("Word:", word)
    speak("Audio phonetics:", audio_phonetics)
    try:
        speak("Meanings:")
        for i in response[0]['meaning']:
            partOfSpeech = i['partOfSpeech']
            definition = i['definitions'][0]['definition']
            example = i['definitions'][0]['example']
        speak(
            f"Part of speech: {partOfSpeech}\nDefinition: {definition}\nExample: {example}"
        )
    except:
        pass


# To split string by numbers
def split_string(text):
    global _items
    match = re.match(r"([a-z]+)([0-9]+)", str(text), re.I)
    if match:
        _items = match.groups()
    return _items


def game():
    speak("Lets play a game. ROCK PAPER SCISSORS")
    rounds = 0
    Me_score = 0
    Computer_score = 0
    while rounds < 5:
        choose = ('rock', 'paper', 'scissors')
        com_choose = random.choice(choose)
        speak("Choose your weapon:")
        speak("Rock, Paper, Scissors")
        me_choose = startExecution.take_command().lower()
        if me_choose == "rock":
            if com_choose == "rock":
                speak("Draw")
            elif com_choose == "paper":
                speak("Computer wins")
                Computer_score += 1
            elif com_choose == "scissors":
                speak("You win")
                Me_score += 1
        elif me_choose == "paper":
            if com_choose == "rock":
                speak("You win")
                Me_score += 1
            elif com_choose == "paper":
                speak("Draw")
            elif com_choose == "scissors":
                speak("Computer wins")
                Computer_score += 1
        elif me_choose == "scissors":
            if com_choose == "rock":
                speak("Computer wins")
                Computer_score += 1
            elif com_choose == "paper":
                speak("You win")
                Me_score += 1
            elif com_choose == "scissors":
                speak("Draw")
        else:
            speak("Please choose rock, paper or scissors")
            continue
        rounds += 1
    speak("Final score: You:", Me_score, "Computer:", Computer_score)
    if Me_score > Computer_score:
        speak("You won the game")
    elif Me_score < Computer_score:
        speak("Computer won the game")
    else:
        speak("Draw")


# To Generate Password
def generate_password(length):
    _password = ""
    for i in range(length):
        _password += random.choice(pass_chars)
    return _password


# Whatsapp automation
def whatsapp():
    pass


# To close jarvis
def close():
    exit(app.exec_())
    speak("Thanks for using me sir, Have a good day.")


# Set brightness
def set_brightness(brightness):
    brightness = int(brightness)
    if brightness > 100:
        brightness = 100
    if brightness < 0:
        brightness = 0
    c = wmi.WMI(namespace='wmi')
    methods = c.WmiMonitorBrightnessMethods()[0]
    methods.WmiSetBrightness(brightness, 0)


# To wish
def wish():
    hour = int(datetime.datetime.now().hour)
    _now = datetime.datetime.now()
    if 0 <= hour <= 12:
        speak(f"Good morning sir. it's {_now.strftime('%I:%M %p')}")
    elif 12 <= hour <= 18:
        speak(f"Good afternoon sir. it's {_now.strftime('%I:%M %p')}")
    else:
        speak(f"Good evening sir. it's {_now.strftime('%I:%M %p')}")
    speak("I am jarvis, how can I help you?")


# play music function
def music_youtube():
    speak("Sir, please tell me the name of music you want to play")
    _name = startExecution.take_command().lower()
    pywhatkit.playonyt(_name)
    

# take a photo
def take_photo():
    pyautogui.press("win")
    pyautogui.typewrite("camera")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(4)
    speak("SMILE")
    speak("3")
    time.sleep(1)
    speak("2")
    time.sleep(1)
    speak("1")
    time.sleep(1)
    pyautogui.press("enter")
    speak("I took a photo of you")


# Burglar alarm
def security_camera():
    def volume_max():
        for i in range(50):
            pyautogui.press("volumeup")

    def alert(sound="assets\\alert.wav"):
        samples, samplerate = sf.read(sound)
        default_speaker = sc.default_speaker()

        volume_max()
        default_speaker.play(samples, samplerate=samplerate)

    def lock():
        cmd = 'rundll32.exe user32.dll, LockWorkStation'
        subprocess.call(cmd)

    time.sleep(0.5)
    cam = cv2.VideoCapture(0)
    detection_count = 0

    while cam.isOpened():
        voice_password = startExecution.take_command().lower()
        if password_original in voice_password:
            speak(f"Password is correct. Welcome {name}. Burglar alarm is turning off")
            break
        _, frame1 = cam.read()
        _, frame2 = cam.read()
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
        for c in contours:
            if cv2.contourArea(c) < 5000:
                continue
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            detection_count += 1
            voice_password = startExecution.take_command().lower()
            if password_original in voice_password:
                speak(f"Password is correct. Welcome {name}. Security camera is turning off")
                break
            filename = "Detection_" + str(detection_count) + ".jpg"
            cv2.imwrite(filename, frame1)
            time.sleep(5)
            alert()
            lock()
            print("Found")
        cv2.waitKey(1)
        cv2.imshow('Security Cam', frame1)
    cam.release()


# Calendar
def calendar():
    cal = Tk()
    cal.title("Calendar")
    cal.iconbitmap('assets/calendar1.ico')
    _now = datetime.datetime.now()
    this_calendar = Calendar(cal, selectmode="day", year=_now.year, month=_now.month, day=_now.day)
    this_calendar.pack(fill=BOTH, expand=True)
    cal.mainloop()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
        self.query = ""
        self.permission = ""

    def run(self):
        # while True:
        # try:
        #     self.permission = self.take_command(True).lower()
        #     if 'wake up' in self.permission or 'jarvis' in self.permission or 'can you hear me' in self.permission or "hello" in self.permission or "hi" in self.permission or "hey" in self.permission:
        #         os.system("cls")
        #         self.TaskExecution()
        #     elif 'goodbye' in self.permission:
        #         quit()
        #         os.system("cls")
        #         break
        # except KeyboardInterrupt:
        #     continue
        self.TaskExecution()

    # Take command from user
    @staticmethod
    def take_command(print_command=True):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            if print_command:
                print("Listening...")
            audio = r.listen(source)
            try:
                if print_command:
                    print("Recognizing...")
                q = r.recognize_google(audio, language='en-IN')
                if print_command:
                    print(f"User said: {q}\n")
            except Exception:
                # speak("I can't understand you sir")
                return "None"
            return q.lower()

    # Exit jarvis
    def exit(self, **kwargs):
        speak("Thanks for using me sir, Have a good day.")
        self.close()

    # Task execution
    def TaskExecution(self):
        global content, name, password_original, alarms
        wish()
        while True:
            try:
                if len(alarms) > 0:
                    for a in alarms:
                        _now = datetime.datetime.now()
                        if _now.year == a['year']:
                            if _now.month == a['month']:
                                if _now.day == a['day']:
                                    if _now.hour == a['hour']:
                                        if _now.minute == a['minute']:
                                            for x in range(5):
                                                for y in range(2):
                                                    winsound.Beep(1000, 100)
                                                    time.sleep(0.1)
                                                time.sleep(1)
                                            notification.notify(
                                                title=a['title'],
                                                message=f"Alarm set for {a['hour']}:{a['minute']}",
                                                timeout=2,
                                            )
                                            time.sleep(7)
                self.query = self.take_command().lower()

                # logic building for tasks:
                if self.query != "jarvis":
                    self.query = self.query.replace("jarvis", "")

                if self.query == "jarvis":
                    speak("Yes sir?")
                elif "open camera" in self.query:
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, frame = cap.read()
                        cv2.imshow("Camera", frame)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                elif "play" in self.query and "game" in self.query:
                    game()
                elif "play" in self.query and "music" in self.query and "youtube" in self.query:
                    music_youtube()

                elif "play" in self.query and "music" in self.query:
                    songs = os.listdir("music/")
                    rd = random.randint(0, len(songs) - 1)
                    os.startfile(os.path.join("music\\", songs[rd]))
                elif "ip address" in self.query:
                    speak("Please wait while I get your ip address")
                    try:
                        ip = requests.get("https://api.ipify.org").text
                        local_ip = socket.gethostbyname(socket.gethostname())
                        speak(f"Your global IP address is {ip} and your local IP address is {local_ip}")
                    except Exception:
                        speak("Unable to get your IP address")
                elif "show" in self.query and "clock" in self.query:
                    speak("Here you are.")
                    clock()
                elif "check" in self.query and "prime" in self.query:
                    speak("Please tell me the number you want to check")
                    num = self.take_command().lower()
                    if num.isnumeric():
                        num = int(num)
                        if num > 1:
                            prime = is_prime(num)
                            if prime:
                                speak("Yes sir, number {} is prime".format(num))
                            elif not prime:
                                speak("No sir, number {} is not prime".format(num))
                        else:
                            speak("You have to enter a number greater than 1")
                    else:
                        speak("You have to enter a number")
                elif "counters" in self.query and "number" in self.query:
                    speak("Please tell me the number you want to count")
                    num = self.take_command().lower()
                    if num.isnumeric():
                        num = int(num)
                        if num > 1:
                            counters = NumberCounters(num)
                            count = len(counters)
                            speak(f"Counters of number {num} are")
                            for i in counters:
                                speak(i)
                            print()
                            speak(f"And there are {count} counters")
                        else:
                            speak("You have to enter a number greater than 1")
                    else:
                        speak("You have to enter a number")
                elif "wikipedia" in self.query:
                    speak("What should I search on wikipedia?")
                    search = self.take_command().lower()
                    result = wikipedia.summary(search, sentences=2)
                    speak("According to Wikipedia")
                    speak(result)
                    speak("That was your search result.")
                elif "open" in self.query and "calendar" in self.query and "search" not in self.query:
                    speak("Sir, Please wait while I open calendar")
                    Calendar()
                elif "open google" in self.query:
                    webbrowser.open("https://www.google.com")
                elif "close" in self.query and "tabs" in self.query:
                    for this_word in self.query.split():
                        if this_word.isnumeric() and this_word[-1] == self.query[self.query.find("tabs") - 2]:
                            count_tabs = int(this_word)
                            for tab in range(count_tabs):
                                pyautogui.hotkey('ctrl', 'w')
                            speak(count_tabs, "tabs closed")
                            break
                    else:
                        pyautogui.hotkey('ctrl', 'w')
                        speak("1 tab closed")
                elif "open" in self.query and "tab" in self.query:
                    pyautogui.hotkey("ctrl", "t")
                elif "press" in self.query and "enter" in self.query:
                    pyautogui.press("enter")
                elif "search" in self.query and "google" in self.query:
                    speak("sir, what should i search on google? ")
                    search = self.take_command().lower()
                    if search != "none":
                        pywhatkit.search(search)
                        speak("This is the result of your search")
                    else:
                        speak("Sir, Please try again.")
                elif "search" in self.query and "youtube" in self.query:
                    speak("Sir, what should i search on youtube? ")
                    search = self.take_command().lower()
                    if search != "none":
                        youtube_search = "https://www.youtube.com/results?search_query=" + search
                        webbrowser.open(youtube_search)
                        speak("This is the result of your search")
                elif "open website" in self.query:
                    speak("Sir, please enter the url of website")
                    url = input("Enter the url: ")
                    webbrowser.open(url)
                elif "summarize" in self.query and "text" in self.query:
                    speak("Please enter the text to summarize")
                    text = self.take_command().lower()
                    if text != "none":
                        speak("Please wait while I summarize your text")
                        summarize = text_summarize(text)
                        with open("summary.txt", "w") as f:
                            f.write(str(summarize))
                            f.close()
                        speak("I saved the summarized text in a file named summary.txt")
                        speak("Do you want to open file, open folder, open both or none of them?")
                        choice = self.take_command().lower()
                        if "none" in choice or "no" in choice or "cancel" in choice:
                            speak("I will not open any file or folder")
                        elif "both" in choice or ("file" in choice and "folder" in choice):
                            speak("I will open both file and folder")
                            os.startfile("summary.txt")
                            os.system("start " + os.getcwd())
                        elif "file" in choice:
                            speak("I will open file in notepad")
                            os.startfile("summary.txt")
                        elif "folder" in choice:
                            speak("I will open folder in file explorer")
                            os.system("start " + os.getcwd())
                        else:
                            speak("I will not open any file or folder")
                elif "open" in self.query and "system 32" in self.query:
                    os.system("start C:/Windows/System32")
                elif "open" in self.query and "control panel" in self.query:
                    os.system("start C:/Windows/System32/control.exe")
                elif "open" in self.query and "program files" in self.query:
                    os.system("start C:/Program Files")
                elif "summarize" in self.query and "file" in self.query:
                    speak("Please enter the path of the file to summarize")
                    path = self.take_command().lower()
                    if path != "none":
                        speak("Please wait while I summarize your text")
                        summarize = text_summarize(path)
                        with open("summary.txt", "w") as f:
                            f.write(str(summarize))
                            f.close()
                        speak("I saved the summarized text in a file named summary.txt")
                        speak("Do you want to open file, open folder, open both or none of them?")
                        choice = self.take_command().lower()
                        if "none" in choice or "no" in choice or "cancel" in choice:
                            speak("I will not open any file or folder")
                        elif "both" in choice or ("file" in choice and "folder" in choice):
                            speak("I will open both file and folder")
                            os.startfile("summary.txt")
                            os.system("start " + os.getcwd())
                        elif "file" in choice:
                            speak("I will open file in notepad")
                            os.startfile("summary.txt")
                        elif "folder" in choice:
                            speak("I will open folder in file explorer")
                            os.system("start " + os.getcwd())
                        else:
                            speak("I will not open any file or folder")
                elif "wifi" in self.query and "password" in self.query:
                    speak("Please wait while I get your wifi passwords")
                    try:
                        wifi_passwords = get_wifi_passwords()
                        speak("I have found your wifi passwords")
                        for x in range(len(wifi_passwords)):
                            speak(wifi_passwords[x])
                    except Exception:
                        speak("Unable to get your wifi passwords")
                elif "open" in self.query and self.query.replace("open", "").strip() in sites_list:
                    webbrowser.open(sites_list[self.query.replace("open", "").strip()])
                elif "enigma" in self.query or "encryptor" in self.query:
                    speak("Do you want to setup enigma settings? ")
                    choice = self.take_command().lower()
                    if "yes" in choice:
                        speak("Please tell me the alpha rotor value")
                        _alpha = self.take_command().lower()
                        if type(_alpha) == int:
                            _alpha = int(_alpha)
                        else:
                            speak("I can't understand your alpha rotor value")

                        speak("Please tell me the beta rotor value")
                        _beta = self.take_command().lower()
                        if type(_beta) == int:
                            _beta = int(_beta)
                        else:
                            speak("I can't understand your gama rotor value")

                        speak("Please tell me the gama rotor value")
                        _gama = self.take_command().lower()
                        if type(_gama) == int:
                            _gama = int(_gama)
                        else:
                            speak("I can't understand your alpha rotor value")
                    else:
                        _alpha, _beta, _gama = 5, 17, 24
                    with open("enigma.txt", "w") as f:
                        f.write(f"Alpha rotor: {_alpha}\nBeta rotor: {_beta}\nGama rotor: {_gama}")
                        f.close()
                    enigma = Enigma(_alpha, _beta, _gama)
                    speak("Please tell me the text to encrypt")
                    text = self.take_command().lower()
                    encrypted = enigma.encrypt_text(text)
                    speak("Encrypted text is " + encrypted)
                    speak(
                        "I saved this enigma settings in a file named enigma.txt. because you need them to decrypt the text")
                elif ("generate" in self.query or "generator" in self.query) and "password" in self.query:
                    speak("Sir, how many characters should I generate?")
                    length = self.take_command().lower()
                    if type(length) == int:
                        password = generate_password(int(length))
                    else:
                        password = generate_password(8)

                    speak("I have generated a password for you. I will not save it in a file or say it to you loudly")
                    print(password)
                    if type(length) is not int:
                        speak(
                            "I didn't generate password with length you said. Because I didn't understand your length. I have generated a password with default length 8")
                elif "change" in self.query and "my" in self.query and "name" in self.query:
                    speak("Really? Do you want to change your name in jarvis?")
                    choice = self.take_command().lower()
                    if "yes" in choice:
                        speak("Ok, first of all tell me the password")
                        password = self.take_command().lower()
                        if password == password_original:
                            speak("Ok. The password is correct. you can change your name now")
                            speak("Tell me your new name in jarvis")
                            name = self.take_command().lower()
                            with open("name.txt", "w") as file:
                                file.write(name)
                                file.close()
                            speak("Your name has been changed to " + name)
                        else:
                            speak("The password is incorrect. I can't change your name.")
                    else:
                        speak("Ok. I will not change your name")
                elif "change" in self.query and "my" in self.query and "password" in self.query:
                    speak("Ok. First of all tell me the old password")
                    old_password = self.take_command().lower()
                    if old_password == password_original:
                        speak("Ok. The password is correct. you can change your password now")
                        speak("Tell me your new password in jarvis")
                        new_password = self.take_command().lower()
                        speak("Tell me your new password again in jarvis")
                        new_password_again = self.take_command().lower()
                        if new_password == new_password_again:
                            password_original = new_password
                            with open("password.secret", "wb") as file:
                                pickle.dump(password_original, file)
                                file.close()
                            speak("Your password has been changed to " + new_password)
                        else:
                            speak("The passwords are not same. I can't change your password.")
                    else:
                        speak("The password is incorrect. I can't change your password.")
                elif (
                        "speech" in self.query and "recognition" in self.query and "audio" in self.query) or "transcribe" in self.query or "transcribed" in self.query or "transcription" in self.query:
                    speak("Sir, Please enter the path of your audio file. remember. the file must be in .wav format")
                    path = input("Enter path: ").replace("'", '"').replace("/", "\\").strip()
                    speak("Sir, Please tell me this audio file is in what language? ")
                    language = self.take_command().lower()
                    if "persian" in language or "farsi" in language or "fa" in language or "ir" in language or "iran" in language:
                        language = "fa-IR"
                    elif "english" in language or "en" in language or "us" in language or "usa" in language:
                        language = "en-US"
                    elif language == "none":
                        language = "en-US"

                    if "long" in self.query or (
                            "short" in self.query and "not" in self.query):
                        length = "long"
                    elif "short" in self.query or ("long" in self.query and "not" in self.query):
                        length = "short"
                    else:
                        speak("Sir, Please tell me your audio file is long or it is short?")
                        choice = self.take_command().lower()
                        if "cancel" in choice:
                            speak("Ok sir, I will not recognize your audio file")
                            continue
                        elif "long" in choice or ("short" in choice and "not" in choice):
                            length = "long"
                        else:
                            length = "short"
                    if path != "cancel":
                        recognize_text(path, length, language)
                elif "burglar alarm" in self.query or "security camera" in self.query:
                    speak("Security camera will start at 15 seconds later")
                    for i in range(1, 16):
                        print(i, "seconds to start burglar alarm")
                        time.sleep(1)
                    security_camera()
                    speak("Burglar alarm started.")
                elif "roll" in self.query and "dice" in self.query:
                    speak("Rolling the dice")
                    speak(f"The dice rolled {random.randint(1, 6)}")
                elif "type" in self.query:
                    speak("What do you want to type? ")
                    type_ = self.take_command().lower()
                    if type_ != "none":
                        pyautogui.typewrite(type_ + ". " if "." not in type_ else type_ + " ")
                elif "time" in self.query and "what" in self.query:
                    now = datetime.datetime.now()
                    speak(f"Sir, it's {now.strftime('%I:%M %p')}")
                elif "date" in self.query and "what" in self.query:
                    now = datetime.datetime.now()
                    speak(f"Sir, it's {now.strftime('%d %B %Y')}")
                elif "day" in self.query and "what" in self.query:
                    now = datetime.datetime.now()
                    speak(f"Sir, it's {now.strftime('%d %B %Y')}")
                elif "month" in self.query and "what" in self.query:
                    now = datetime.datetime.now()
                    speak(f"Sir, this month is {now.strftime('%B')}")
                elif "year" in self.query and "what" in self.query:
                    now = datetime.datetime.now()
                    speak(f"Sir, this year is {now.strftime('%Y')}")
                elif "alarm" in self.query:
                    speak("Sir, please tell me the title of this alarm")
                    title = self.take_command().lower()
                    if title != "none":
                        speak("Sir please tell me the hour to set alarm")
                        hour = self.take_command().lower()
                        if hour != "none":
                            speak("Sir, please tell me the minute to set alarm")
                            minute = self.take_command().lower()
                            if minute != "none":
                                speak("Sir, please tell me the day to set alarm")
                                day = self.take_command().lower()
                                if day != "none":
                                    speak("Sir, please tell me the month to set alarm")
                                    month = self.take_command().lower()
                                    if month != "none":
                                        speak("Sir, please tell me the year to set alarm")
                                        year = self.take_command().lower()
                                        if year != "none":
                                            this_alarm = {
                                                "day": day,
                                                "month": month,
                                                "year": year,
                                                "hour": hour,
                                                "minute": minute,
                                            }
                                            alarms.append(this_alarm)
                                            with open("alarms.pkl", "wb") as file:
                                                pickle.dump(alarms, file)
                                            speak(
                                                "Alarm set with title {} for {} of month {} of year {} and at hour {} and minute {}".format(
                                                    this_alarm['title'],
                                                    this_alarm['day'],
                                                    this_alarm['month'],
                                                    this_alarm['year'],
                                                    this_alarm['hour'],
                                                    this_alarm['minute']
                                                ))
                                            break
                                        else:
                                            speak("Sir, Something went wrong")
                                    else:
                                        speak("Sir, Something went wrong")
                                else:
                                    speak("Sir, Something went wrong")
                            else:
                                speak("Sir, Something went wrong")
                        else:
                            speak("Sir, Something went wrong")
                    else:
                        speak("Sir, Something went wrong")
                elif "rotate" in self.query and "screen" in self.query:
                    screen = rotatescreen.get_primary_display()
                    screen.rotate_to(90)
                elif "open" in self.query and "folder" in self.query:
                    for folder in os.listdir("C:\\"):
                        if folder.lower() in self.query and os.path.isdir(os.path.join("C:\\", folder)):
                            speak("Opening {} folder".format(folder))
                            os.startfile("C:\\{}".format(folder))
                            break
                elif "check" in self.query and "whatsapp" in self.query:
                    webbrowser.open("https://web.whatsapp.com/")
                elif "brightness" in self.query:
                    speak("Sir, please tell me the brightness level you want to set")
                    brightness = self.take_command().lower()
                    if brightness != "none" and brightness.isnumeric():
                        brightness = int(brightness)
                        if brightness > 100:
                            brightness = 100
                        elif brightness < 0:
                            brightness = 0
                        brightness = brightness / 100
                        set_brightness(brightness)
                    else:
                        speak("Something went wrong. Please try again")
                elif (
                        "send" in self.query and "message" in self.query and "whatsapp" in self.query) or "send whatsapp message" in self.query:
                    speak("sir, what should i send? ")
                    message = self.take_command().lower()
                    if message != "none":
                        speak("sir, Who should I send to? ")
                        who = self.take_command().lower()
                        if who != "none":
                            if who in contacts:
                                pywhatkit.sendwhatmsg(contacts[who], message, datetime.datetime.now().hour,
                                                      datetime.datetime.now().minute + 2)
                            else:
                                speak("Please enter phone number, sir")
                                phone = input("Enter phone number: ")
                                who = input("Enter name of this phone number: ")
                                contacts[who] = phone
                                pywhatkit.sendwhatmsg(phone, message, datetime.datetime.now().hour,
                                                      datetime.datetime.now().minute + 2)
                        else:
                            speak("Something went wrong! Please try again")
                    else:
                        speak("Something went wrong! Please try again")
                elif "dictionary" in self.query:
                    speak("Dictionary activated!")
                    speak("Tell me the word")
                    word = self.take_command()
                    dictionary(word)
                elif "can" in self.query and "remember" in self.query:
                    speak("Please wait while I try to remember")
                    if os.path.exists("remember.txt"):
                        with open("remember.txt", "r") as file:
                            old_remembers = file.readlines()
                            speak("I can remember these")
                            for remember in old_remembers:
                                speak(remember)
                            speak("That was what cdid i remember.")
                    else:
                        speak("Sorry sir, I can't remember anything.")
                elif "remember" in self.query:
                    speak("Sir, what should I remember? ")
                    remember = self.take_command()
                    if os.path.exists("remember.txt"):
                        with open("remember.txt", "r") as f:
                            old_remembers = f.readlines()
                            f.close()
                    else:
                        old_remembers = []
                    old_remembers.append(remember)
                    with open("remember.txt", "w") as f:
                        f.writelines(old_remembers)
                elif "calculate" in self.query or "calculation" in self.query or "calculator" in self.query:
                    speak("Sir, what should I calculate? ")
                    calculate = self.take_command().lower()
                    if calculate != "none":
                        # def got_operator_fn(op):
                        #     return {
                        #         "+": operator.add,
                        #         "-": operator.sub,
                        #         "×": operator.mul,
                        #         "/": operator.truediv,
                        #         "divided": operator.truediv,
                        #         "divide": operator.truediv,
                        #         "multiple": operator.mul,
                        #         "plus": operator.add,
                        #         "minus": operator.sub,
                        #         "multiplied": operator.mul,
                        #         "multiplied by": operator.mul,
                        #         "divided by": operator.truediv,
                        #         "*": operator.mul,
                        #         "x": operator.mul,
                        #         "multiples": operator.mul,
                        #     }[op]
                        #
                        # def eval_binary_expr(op1, operation, op2):
                        #     op1, op2 = int(op1), int(op2)
                        #     return got_operator_fn(operation)(op1, op2)

                        speak(f"Your result is")
                        speak(eval(str(calculate)))
                elif "weather" in self.query:
                    speak("Sir, which city should I display weather for?")
                    city = self.take_command().lower()
                    if city != "none":
                        city = city
                    else:
                        city = "Tehran"
                    _api_key_weather = 'f76449ed2e1f45b7826132233222407'
                    url = f'http://api.weatherapi.com/v1/current.json?key={_api_key_weather}&q={city}'
                    r = requests.get(url).json()
                    speak(
                        f"Sir, the temperature in {city} is {r['current']['temp_c']} degrees celsius and it is {r['current']['temp_f']} degrees fahrenheit. But feels like {r['current']['feelslike_c']} degrees celsius and it is {r['current']['feelslike_f']} degrees fahrenheit.")
                    speak(f"The weather in {city} is {r['current']['condition']['text']}.")
                    speak(f"The wind speed in {city} is {r['current']['wind_kph']} kilometers per hour.")
                    speak(
                        f"The wind direction in {city} is {r['current']['wind_dir']} and with {r['current']['wind_degree']} degrees.")
                elif "battery" in self.query or 'battery level' in self.query or 'power' in self.query:
                    battery = psutil.sensors_battery()
                    percentage = battery.percent
                    speak(f"Sir, the battery level is {percentage} percent")
                    if percentage >= 75:
                        speak("Sir, We have enough power to continue our work")
                    elif 40 <= percentage < 75:
                        speak("Sir, We should connect our system to charging point to charge our battery")
                    elif 15 <= percentage <= 30:
                        speak("Sir, We don't have enough power to work, please connect to charging")
                    elif percentage <= 15:
                        speak(
                            "Sir, we have very low power, please connect to charging the system will shutdown very soon")
                elif "internet speed" in self.query:
                    # st -> Speed test, dl -> Download, up -> upload
                    speak("Please wait while I check your internet speed")
                    try:
                        st = speedtest.Speedtest()
                        st.get_best_server()
                        dl = st.download()
                        up = st.upload()
                        ping = st.results.ping
                        dl_mb = round(dl / 1000000, 2)
                        up_mb = round(up / 1000000, 2)
                        ping_2 = round(ping, 2)
                        speak(f"Sir, the internet speed report:")
                        speak(f"Download speed: {dl_mb} MegaBytes per second")
                        speak(f"Upload speed: {up_mb} MegaBytes per second")
                        speak(f"Ping: {ping_2} Milliseconds")
                    except:
                        speak("Sir, There is no internet connection")
                elif "activate" in self.query and "how to do" in self.query:
                    speak("'How to do mode' is activated.")
                    while True:
                        speak("Please tell me what you want to know")
                        how = self.take_command().lower()
                        try:
                            if "exit" in how or "close" in how:
                                speak("Okay sir, how to do mode is closed")
                                break
                            else:
                                max_result = 1
                                how_to = search_wikihow(how, max_result)
                                assert len(how_to) == max_result
                                how_to[0].print()
                                speak(how_to[0].summary)
                                speak("Say 'continue' to continue using jarvis")
                                continue_ = ''
                                while continue_ != 'continue':
                                    continue_ = self.take_command().lower()
                                    if "continue" in continue_:
                                        speak("Ok sir")
                                        break
                        except Exception:
                            speak("Sorry sir, I am not able to find this")
                elif "translate" in self.query or "translator" in self.query:
                    speak("Sir, Translate from which language?")
                    from_lang = input("Enter language ( for example en, fa, de, ar, etc): ").lower()
                    speak("Sir, Translate to which language? ")
                    to_lang = input("Enter language ( for example en, fa, de, ar, etc): ").lower()
                    speak("sir, do you want to translate txt file or translate text you enter? tell me file or text")
                    choice = self.take_command().lower()
                    if "file" in choice:
                        speak("Enter file path")
                        file_path = input("Enter file path: ").replace("/", "\\").replace("'", '"')
                        try:
                            with open(file_path, "r") as f:
                                content = f.read().lower()
                        except:
                            speak("Something went wrong! try again later")
                    else:
                        speak("Please type your text")
                        content = input("Type your text: \n> ")
                    try:
                        speak("Translating started. please wait.")
                        translation, summary = Translate(content, from_lang, to_lang)
                        with open("translate.txt", "w") as f:
                            f.write(str(translation))
                        speak("Translating completed. I saved the translation in file named translate.txt")
                        speak("I converted text from {} to {}".format(summary[0], summary[2]))
                    except:
                        speak("Something went wrong. try again.")
                elif "where i am" in self.query or "where am i" in self.query or "where we are" in self.query or "where are we" in self.query or (
                        "where" in self.query and "we" in self.query) or (
                        "where" in self.query and "i" in "self.query"):
                    speak("wait sir, let me check")
                    try:
                        ip_addr = requests.get("https://api.ipify.org").text
                        print(ip_addr)
                        url = 'https://get.geojs.io/v1/ip/geo/' + ip_addr + '.json'
                        geo_requests = requests.get(url)
                        geo_data = geo_requests.json()
                        city = geo_data['city']
                        country = geo_data['country']
                        speak(f"I think we are in {city} of {country}")
                    except Exception:
                        speak("Sorry sir, I am not able to get your location")
                elif "location" in self.query and "google" in self.query and "map" in self.query:
                    webbrowser.open(sites_list['google maps'])
                elif "take" in self.query and ("screen shot" in self.query or "screenshot" in self.query):
                    speak("Please wait while I take your screenshot")
                    img = pyautogui.screenshot()
                    img.save("screenshot.png")
                    speak("Your screen shot has been saved in the main folder of jarvis")
                elif "read" in self.query and "pdf" in self.query:
                    pdf_reader()
                elif ("information" in self.query or "info" in self.query) and "phone" in self.query:
                    speak("Sir, Please enter the phone number")
                    phone_number = input("Enter the number: ")
                    country, isp = get_number_info(phone_number)
                    if country != "" and isp != "":
                        speak(f"Sir, The phone number {phone_number} is for country {country} and isp {isp}")
                    else:
                        speak(f"Sorry sir, I am not able to find the information for {phone_number}")
                elif "send" in self.query and "email" in self.query:
                    speak("Sir, tell me the body of the email")
                    content = self.take_command().lower()
                    content = "" if content == "none" else content
                    speak("Sir, please enter the target email address")
                    target_email = input("Enter the email address: ")
                    speak("Sir, please tell me the subject of email")
                    email_subject = self.take_command().lower()
                    email_subject = "" if email_subject == "none" else email_subject
                    speak("Sir, please enter your email address ")
                    my_email = input("Enter your email address: ")
                    speak("Send it? ")
                    choice = self.take_command().lower()
                    if "yes" in choice:
                        send_email(target_email, email_subject, content)
                        speak("Sir, I send that email.")
                    else:
                        speak("Ok sir, I didn't send that.")
                elif "repeat" in self.query:
                    speak("Sir, Please say what you want to repeat")
                    content = self.take_command().lower()
                    speak(content)
                elif "what" in self.query and "name" in self.query and "your" in self.query:
                    speak("Sir, My name is Jarvis")
                elif "what" in self.query and "name" in self.query and "my" in self.query:
                    speak(f"Sir, Your name is {name}")
                elif "what" in self.query and "can" in self.query and "you" in self.query and "do" in self.query:
                    speak("I can do many things sir")
                    try:
                        for ability in abilities:
                            speak("I can " + ability)
                    except KeyboardInterrupt:
                        pass
                elif "tell" in self.query and "joke" in self.query:
                    joke = pyjokes.get_joke()
                    speak(joke)
                elif "tell" in self.query and "news" in self.query:
                    for category in news_categories:
                        if category in self.query:
                            this_news_category = category
                            break
                    else:
                        this_news_category = "technology"
                    speak("Please wait. I am fetching news for you")
                    news(category=this_news_category)
                elif "hello" in self.query or "hey" in self.query or "hi" in self.query.split():
                    speak("Hello sir, May I help you with something? ")
                elif "how" in self.query and "are" in self.query and "you" in self.query:
                    speak("I am fine sir, what about you? ")
                elif "exit" in self.query or 'goodbye' in self.query or "bye" in self.query or (
                        'you need' in self.query and 'break' in self.query) or ("you" in self.query and "can" in self.query and "sleep" in self.query):
                    speak("Thanks for using me sir, Have a good day.")
                    # speak("Ok sir. You can call me any time.")
                    # speak("just say 'wake up jarvis'")
                    startExecution.quit()
                    # exit()
                    jarvis.exit()
                    # os._exit(0)
                    sys.exit(__status=True)
                elif 'good' in self.query or 'fine' in self.query:
                    speak("That's great to hear from you.")
                elif ('thank' in self.query and 'you' in self.query) or 'thanks' in self.query:
                    speak("It's my pleasure sir.")
                elif "ok" in self.query:
                    speak("Can I help more?")
                elif 'you' in self.query and 'there' in self.query:
                    speak("Yes sir, I am here.")
                elif "play" in self.query:
                    for music in os.listdir("music"):
                        if music.lower().replace(".mp3", "") in self.query:
                            music_name = music
                            music_path = os.path.join("music", music_name)
                            os.system("start " + music_path)
                            break
                elif "open" in self.query:
                    for site in sites_list:
                        if site in self.query:
                            if "school" in site:
                                time.sleep(0.5)
                                driver = webdriver.Chrome("chromedriver.exe")
                                driver.maximize_window()
                                driver.get(sites_list[site])
                                username_input = driver.find_element(By.XPATH, '//*[@id="username"]')
                                password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
                                username_input.send_keys("0251138003")
                                password_input.send_keys("Aa_123456")
                                submit_btn = driver.find_element(By.XPATH, '//*[@id="loginbtn"]')
                                submit_btn.click()
                                os.system("cls")
                            else:
                                webbrowser.open(sites_list[site])
                            break
                    else:
                        pyautogui.hotkey("win", "s")
                        time.sleep(1)
                        search = self.query.replace("jarvis", "").replace("open", "").replace("please", "").replace("thanks", "").replace("thank you", "")
                        pyautogui.typewrite(search)
                        time.sleep(1)
                        pyautogui.press("enter")
                elif "be" in self.query and "quiet" in self.query:
                    speak("Ok sir, I will be quiet.")
                    while True:
                        can_speak = self.take_command(print_command=False).lower()
                        if "speak" in self.query or "jarvis" in self.query or "wake up" in self.query:
                            speak("Hello sir, I'm back.")
                            break
                elif "volume" in self.query and "up" in self.query:
                    for i in range(4):
                        pyautogui.press("volumeup")
                elif "volume" in self.query and "down" in self.query:
                    for i in range(2):
                        pyautogui.press("volumedown")
                elif "volume" in self.query and "mute" in self.query:
                    pyautogui.press("volumemute")
                elif "switch the window" in self.query:
                    pyautogui.keyDown('alt')
                    pyautogui.press('tab')
                    time.sleep(0.7)
                    pyautogui.keyUp('alt')
                elif "shutdown the computer" in self.query:
                    speak("Shutting down sir")
                    os.system("shutdown /s /t 1")
                elif "restart the computer" in self.query:
                    speak("Restarting sir")
                    os.system("shutdown /r /t 1")
                elif "logout" in self.query:
                    speak("Logging out sir")
                    os.system("shutdown /l /t 1")
                elif "lock the computer" in self.query:
                    speak("Locking sir")
                    os.system("rundll32.exe user32.dll,LockWorkStation")
                elif "sleep the computer" in self.query:
                    speak("Sleeping sir")
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                elif "close" in self.query:
                    program = self.query.replace("close", "").replace("please", "").strip()
                    if program in programs:
                        os.system(f"taskkill /f /im {programs[program]}.exe")
                        speak(f"{program} is closed")
                    else:
                        speak("I can't find this program")
                elif self.query != "" and self.query != "none":
                    speak("I can't understand you sir")
            except KeyboardInterrupt:
                speak("Thanks for using me sir, Have a good day.")
                self.close()
            except:
                console.print_exception()
                speak("Something went wrong. Trying again...")
                os.system("pause")
                os.system("cls")
                continue


startExecution = MainThread()

try:
    with open("password.secret", "rb") as f:
        password_original = pickle.load(f)
except:
    password_original = f"play soccer with {name}"


def password_protect():
    for i in range(3):
        speak("Sir, Please tell me the password")
        password = startExecution.take_command()
        if password == password_original:
            speak("Sir, Password accepted")
            return True
        else:
            speak("Sir, Wrong password. Try again")
            continue
    else:
        speak("You can not use jarvis because of wrong password. Try again later.")
        return False


protect = True

if _password_protect:
    # Password protection
    protect = password_protect()


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Jarvis()
        self.ui.setupUi(self)
        startExecution.start()
        # self.ui.pushButton.clicked.connect(self.startTask)
        # self.ui.pushButton_2.clicked.connect(self.exit)

    def exit(self):
        # speak("Thanks for using me sir, Have a good day.")
        self.close()

    # def startTask(self):
    #     self.ui.movie = QtGui.QMovie("assets/iron man.gif")
    #     self.ui.label.setMovie(self.ui.movie)
    #     self.ui.movie.start()
    #     self.ui.movie = QtGui.QMovie("assets/Jarvis_Loading_Screen.gif")
    #     self.ui.label_2.setMovie(self.ui.movie)
    #     self.ui.movie.start()
    #     timer = QTimer(self)
    #     timer.timeout.connect(self.showTime)
    #     timer.start(1000)
    #     startExecution.start()
    #
    # def showTime(self):
    #     current_time = QTime.currentTime()
    #     now = QDate.currentDate()
    #     label_time = current_time.toString('hh:mm:ss')
    #     label_date = now.toString(Qt.ISODate)
    #     self.ui.textBrowser.setText(label_date)
    #     self.ui.textBrowser_2.setText(label_time)


if not protect:
    speak("You can not use jarvis")
    speak("Bye for now")
    startExecution.quit()
    # exit()
    os._exit(0)
    # sys.exit()

app = QApplication(sys.argv)
jarvis = Main()
# jarvis.ui.textBrowser_2.setStyleSheet(
#     'background: transparent; color: white; border: none; border-radius: 0px; font-size: 30px; font-style: bold; font-family: "Nirmala UI"')
# jarvis.ui.textBrowser.setStyleSheet(
#     'background: transparent; color: white; border: none; border-radius: 0px; font-size: 30px; font-style: bold; font-family: "Nirmala UI"')
jarvis.show()
close()
