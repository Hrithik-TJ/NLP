from gtts import gTTS
import os
text = input ("Enter some text:")
language = 'kn'
speech = gTTS (text=text, lang=language, slow=False)
speech.save ("namaskara.mp3")
os.system("start namaskara.mp3")
