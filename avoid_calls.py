import pyttsx3
engine = pyttsx3.init()

#Excuses that you want the bot to say for you not picking up the phone.
voice = ["switched off","busy", "Out of network"]
print("Excuses: \n" + "1. " + voice[0] + "\n" + "2. " + voice[1]+ "\n" + "3. " + voice[2])

excuse = input("Select which excuse you want bot to say: ")
if excuse == "1":
    speech = voice[0]
if excuse == "2":
    speech = voice[1]
if excuse == "3":
    speech = voice[2]
say = "The number you are trying to call is currently " + speech + " Please try again later "

#Bot saves you by saying the excuse
engine.say(say)
engine.runAndWait()
