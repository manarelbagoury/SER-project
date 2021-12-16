import speech_recognition as sr
import wave
from scipy.io.wavfile import write, read 
filename = sr.AudioFile("C:\\Users\\user\\Angry.wav")
r = sr.Recognizer()
with filename as source:
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.record(source)
    with open("Done.wav", "wb") as file:
        file.write(source.get_wav_data())

#import noisereduce as nr 
#load data 
#rate, data = read("C:\\Users\\user\\python\\uploads\\Angry.wav")
#(Frequency, array) = read("C:\\Users\\user\\python\\uploads\\Angry.wav") 
#data = data/1.0
# select section of data that is noise 
#noisy_part = data[0:15000] 
# perform noise reduction 
#reduced_noise = nr.reduce_noise(audio_clip=data,noise_clip=noisy_part, verbose=True)
#sample_rate = 44100
#write('denoised_speech.wav', Frequency, reduced_noise)
#from noiseReduction import noise_reduction
#noise_reduction("C:\\Users\\user\\python\\uploads\\Angry.wav")