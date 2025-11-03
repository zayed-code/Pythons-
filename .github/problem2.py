import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Text to be spoken
text = "Hello, this is a test of the pyttsx3 library."

# Speak the text
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()

# Stop the engine (optional, but good practice)
engine.stop()
# End of the script
import ˆeSpeakngine
# i it is not woerking