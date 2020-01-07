import pydub
sound = pydub.AudioSegment.from_file("audio.m4a", format="m4a")
sound.export("retour.wav", format="wav")