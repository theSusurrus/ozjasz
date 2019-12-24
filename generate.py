from phrases import *
import random
import sys
import pyttsx3

def get_phrase(phrase_list):
        num_phrases = len(phrase_list)
        return phrase_list[random.randint(0,num_phrases-1)]

def protocol_1_percent(phrase, speed):
    print("")
    print(phrase)

    engine = pyttsx3.init('espeak')

    engine.setProperty('voice', 'polish')
    engine.setProperty('rate', speed)
    engine.say(phrase)
    engine.runAndWait()
    engine.stop()

phrase = ""

phrase = phrase + get_phrase(list1) + " "
phrase = phrase + get_phrase(list2) + " "
phrase = phrase + get_phrase(list3) + " "
phrase = phrase + get_phrase(list4) + ", "
phrase = phrase + get_phrase(list5) + " "
phrase = phrase + get_phrase(list6) + "."

#protocol_1_percent("Aktywowano protokół jeden procent...", 150)
protocol_1_percent(phrase, 150)
    