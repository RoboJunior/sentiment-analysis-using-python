from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
import pyaudio
import pyttsx3


recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print('Clearing background noise')
    recognizer.adjust_for_ambient_noise(source)
    print('Waiting for your message')
    recordedaudio = recognizer.listen(source)
    print('Done recording')
try:
    print('Printing the message')
    text = recognizer.recognize_google(recordedaudio, language='en-US')
    print('Your message :{}'.format(text))
except Exception as e:
    print(e)

sentence = str(text)
analyzer = SentimentIntensityAnalyzer()
for i in sentence:
    v = analyzer.polarity_scores(sentence)
if v['compound'] >= 0.05:
    print('Happy')
elif v['compound'] <= -0.05:
    print('Sad')
else:
    print('Netural')
     
