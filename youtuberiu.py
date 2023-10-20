import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import asyncio
import socketio
from gtts import gTTS
import pygame
import time
import re
import random

#
#TOKENAS WEBSOCKET
#https://streamlabs.com/dashboard#/settings/api-settings
# API TOKEN > SOCKET API
Token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbiI6IjMxMkM0NDAwMTk2RUU1NTY0MjE4RUFEODY1N0I3QzFGNDZENUU1MTFDNTk2MjlFQjlEMDI5NDhDRDI5ODFGQjI2QTgxM0QyMzE1RjBFNUUxMjRBM0M3MkI3RUI4QzdFRDQ4ODMxNjlGNDFGMkVGQzg4M0Y4RUY4RDBDNzQxQTZBMDEzQkMzMUZGRDFDNTQ5RkVERUFGNzhEREE1NzQ5QTkzREVCNUJDQTFGOTJBMEU5Nzk3QzQ1M0RCNkE4QTIxRkQ5NEE0NDYyOTI0RjZGRENBNjFCMjM5NjQ2NTE4MUY4QTg3QzlGQ0U2MTQxMjYxRUEzNzQ5ODA0RDAiLCJyZWFkX29ubHkiOnRydWUsInByZXZlbnRfbWFzdGVyIjp0cnVlLCJ5b3V0dWJlX2lkIjoiVUMyUmc1a2V3cFMwUlR6blE2MUMwQ2pRIn0.8X18HzCs91pD_uZWxI39HhEb3NqFbRwccqOX9gVD7MI"
#
NOspaming = [
    "Nu negalima tu lenktas",
    "Kiek kartu sakyti NESKAITYSIU TO TAVO spamo",
    "NU negrazu spaminti",
    "Nu jei leidi kalbeti tai gero vakaro čatas",
    "dabar negausi močiutes cepelinu už toky",
    "NU rimtai sugauk",
    "Katinas net geresne žinute butu parašes negul tu"
    ]

sio = socketio.AsyncClient()
def is_spam(message):
    # Define the regular expression pattern
    pattern = r'^\d{10}\s[A-Z]{8}\s[A-Z]{4}$'
    
    # Check if the message matches the pattern
    if re.match(pattern, message):
        return True  # It's spam
    else:
        return False  # It's not spam
def text_to_speech(text):
    speech_file = "tts.mp3"
    speech = gTTS(text=text, lang="lv", slow=True)
    speech.save(speech_file)
    pygame.mixer.init()

    pygame.mixer.music.load(speech_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove(speech_file)

def numertoworld(numerinput):
    units = ["", "Vienas", "Du", "Trys", "Keturi", "Penki", "Šeši", "Septyni", "Aštuoni", "Devyni"]
    tens = ["", "Dešimt", "Dvidešimt", "Trisdešimt", "Keturiasdešimt", "Penkiasdešimt", "Šešiasdešimt", "Septyniasdešimt", "Aštuoniasdešimt", "Devyniasdešimt"]
    hundreds = ["", "Šimtas", "Dviejų šimtų", "Trejų šimtų", "Keturių šimtų", "Penkių šimtų", "Šešių šimtų", "Septynių šimtų", "Aštuonių šimtų", "Devynių šimtų"]
    
    # Separate the integer and decimal parts
    

# Remove the Euro symbol
    
    number = str(numerinput).replace('€', '')
    parts = number.split('.')
    
    if len(parts) == 1: 
        integer_part = int(parts[0])
        decimal_part = 0
    elif len(parts) == 2: 
        integer_part = int(parts[0])
        decimal_part = int(parts[1])
    else:
        raise ValueError("Invalid number format")

 
    euras = "eurai" if integer_part % 10 in [1, 2, 3] else "eura" if integer_part % 10 == 4 else "euru"


    integer_text = ""
    decimal_text = ""
    if integer_part >= 5:
        if integer_part == 0:
            decimal_text = numertoworld(decimal_part) + " centų"
        elif integer_part < 10:
            integer_text = units[integer_part] + " " + euras
        elif integer_part < 100:
            integer_text = tens[integer_part // 10] + " " + units[integer_part % 10] + " " + euras
        else:
            integer_text = (
                hundreds[integer_part // 100]
                + " "
                + numertoworld(integer_part % 100)
                + " "
                + euras
            )
        
        if decimal_part > 0:
            decimal_text = numertoworld(decimal_part) + " centų"

        return f"{integer_text} ir {decimal_text}" if decimal_part > 0 else integer_text
def remetts(message,zin,name,money):
    amount = numertoworld(message[money])
    username = message[name]
    tts_Text = username + " Paukojo " + amount
    print(tts_Text)
    text_to_speech(tts_Text)
    if is_spam(message[zin]) is False:
        tts_Text = "Žinute " + str(message[zin])
        print(tts_Text)
    else:
        tts_Text = random.choice(NOspaming)
        print(tts_Text)   
    text_to_speech(tts_Text)

@sio.event
async def connect():
    print('Prijunkta Prie StreamLabs Serverio')
@sio.event
async def my_message(data):
    print('message received with ', data)
    #await sio.emit('my response', {'response': 'my response'})
@sio.event
async def disconnect():
    print('Atsijunget Nuo StreamLabs Serverio')



@sio.on('event')
async def handle_event(eventData):
    if eventData['type'] == "donation" or "superchat" or "subscription" or "follow":
        print("GAUTAS DONATIONAS ar kaskas tai lauk 10 sekundžiu")
        time.sleep(10)
        if eventData['type'] == "donation": 
            message = eventData['message'][0]
            remetts(message,'message','from','amount')
        if eventData['type'] == "superchat":
            message = eventData['message'][0]
            remetts(message,'comment','name','displayString')
        if eventData['type'] == "subscription":
            message = eventData['message'][0]
            typeSUB = eventData['for']
            name = message['name']
            if typeSUB == "youtube_account":
                text_to_speech(name + ' Prisijunge prie kiaušiu gretos ')
                print(name + ' Prisijunge prie kiaušiu gretos ')
            if typeSUB == "twitch_account":
                text_to_speech(name + ' Pasubino kanala ')
                print(name + ' Pasubino kanala ')
        if eventData['type'] == "follow":
            message = eventData['message'][0]
            typeSUB = eventData['for']
            name = message['name']
            if typeSUB == "youtube_account":
                text_to_speech(name + ' Pasubino Kanala ')
                print(name + ' Pasubino Kanala ')
            if typeSUB == "twitch_account":
                text_to_speech(name + ' Pafolowino Kanala ')
                print(name + ' Pafolowino Kanala ')
    else:
        print("GAUTA zinute")
        print(eventData)




async def main():
    text_to_speech("Sveiki visi , mane damagis buvo ikišes i rusy del jusu , delto dabar penki eurai kad skaityčiau jusu donationus")
    await sio.connect('https://sockets.streamlabs.com?token=' + Token)
    await sio.wait()
if __name__ == '__main__':
    asyncio.run(main())

