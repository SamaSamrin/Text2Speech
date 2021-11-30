# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 20:18:44 2021

@author: SamaSamrin
"""

# =============================================================================
# GTTS = Google Text to Speech, 
# Python library to interface with Google Translate's text to speech API
# requires Internet connection
# =============================================================================

import gtts
from playsound import playsound
#pass text to gTTS object 

# make request to google to get synthesis
english = gtts.gTTS("Hello world") #retrieved the actual audio speech from the API

# save the audio file
english.save("hello.mp3")
# play the audio file
playsound("hello.mp3")

# =============================================================================
# spanish = gtts.gTTS("Hola Mundo", lang="es")
# spanish.save("hola.mp3")
# playsound("hola.mp3")
# =============================================================================

