#!/user/bin/env python

import subprocess

def speak(text, lang="en"):
	return subprocess.Popen(["espeak-ng", "-v", lang, text])

p= speak("I LOVE YOU")
