import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from gtts import gTTS
import pygame

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


