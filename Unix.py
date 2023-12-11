import os
import speech_recognition as sr

r = sr.Recognizer()
input_folder = "F:/Unix_Lia/Calls"
output_folder = "F:/Unix_Lia/TranscribedCalls"

while True:
    for file in os.listdir(input_folder):
        if file.endswith(".wav"):

            audio_file = sr.AudioFile(os.path.join(input_folder, file))

            with audio_file as source:
                audio = r.record(source)
                text = r.recognize_google(audio)

            with open(os.path.join(output_folder, file.replace(".wav",".txt")), "w") as f:
                f.write(text)