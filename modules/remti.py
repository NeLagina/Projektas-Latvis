from . import nospam
from . import tts
from . import numertoworld
import random

def remetts(message,zin,name,money):
    amount = numertoworld.numertoworld(message[money])
    username = message[name]
    tts_Text = username + " Paukojo " + amount
    print(tts_Text)
    tts.text_to_speech(tts_Text)
    if nospam.is_spam(message[zin]) == "False":
        tts_Text = "Žinute " + str(message[zin])
        print(tts_Text)
    else:
        tts_Text = random.choice(nospam.NOspaming)
        print(tts_Text)   
    tts.text_to_speech(tts_Text)