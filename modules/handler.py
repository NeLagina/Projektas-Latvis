from . import tts
from . import remti
import time
import json
from queue import Queue
import os
import threading
donation_events = []

# Lock for accessing the donation_events array
donation_events_lock = threading.Lock()

# Function to add a donation event to the JSON array
def add_donation_to_json(event_data):
    with donation_events_lock:
        donation_events.append(event_data)

# Function to process donation events
def process_donation_events():
    while True:
        with donation_events_lock:
            if donation_events:
                event_data = donation_events.pop(0)  # Get the first event in the list
                speech_file = "tts.mp3"
                while os.path.isfile(speech_file):
                    time.sleep(1)  # Wait until the file is not in use
                alert(event_data)
            else:
                time.sleep(1)  # Wait if no events are available

# Function to process a single donation event


# Start a thread for processing donation events
donation_thread = threading.Thread(target=process_donation_events)
donation_thread.daemon = False
donation_thread.start()    

def don(eventData):
    global donation_thread
    print("HANDLERIS GAVO TAVO INFORMACIJA")
    if donation_thread is not None and donation_thread.is_alive():
        print("The queue processing thread is already running.")
        add_donation_to_json(eventData)
    else:
        print("The queue processing thread is not running. Starting it now.")
        donation_thread = threading.Thread(target=process_donation_events)
        donation_thread.daemon = False
        donation_thread.start()
        add_donation_to_json(eventData)
        
        # Wait for the queue processing thread to start before returning
        while not donation_thread.is_alive():
            time.sleep(0.1)
def alert(eventData):
    print("GAUTAS DONATIONAS ar kaskas tai lauk 10 sekundžiu")
    time.sleep(0)
    if eventData['type'] == "donation": 
        message = eventData['message'][0]
        remti.remetts(message,'message','from','amount')
    if eventData['type'] == "superchat":
        message = eventData['message'][0]
        remti.remetts(message,'comment','name','displayString')
    if eventData['type'] == "subscription":
        message = eventData['message'][0]
        typeSUB = eventData['for']
        name = message['name']
        if typeSUB == "youtube_account":
            tts.text_to_speech(name + ' Prisijunge prie kiaušiu gretos ')
            print(name + ' Prisijunge prie kiaušiu gretos ')
        if typeSUB == "twitch_account":
            tts.text_to_speech(name + ' Pasubino kanala ')
            print(name + ' Pasubino kanala ')
    if eventData['type'] == "follow":
        message = eventData['message'][0]
        typeSUB = eventData['for']
        name = message['name']
        if typeSUB == "youtube_account":
            tts.text_to_speech(name + ' Pasubino Kanala ')
            print(name + ' Pasubino Kanala ')
        if typeSUB == "twitch_account":
            tts.text_to_speech(name + ' Pafolowino Kanala ')
            print(name + ' Pafolowino Kanala ')






