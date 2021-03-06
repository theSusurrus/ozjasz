from phrases import *
import random
import sys
import pyttsx3

def get_phrase(phrase_list):
        num_phrases = len(phrase_list)
        return phrase_list[random.randint(0,num_phrases-1)]

def construct_sentence():
    sentence = get_phrase(list1) + " " \
             + get_phrase(list2) + " " \
             + get_phrase(list3) + " " \
             + get_phrase(list4) + ", "\
             + get_phrase(list5) + " " \
             + get_phrase(list6) + "."
    return sentence

def protocol_1_percent(phrase, speed, speak=True):
    print(phrase)

    if(speak):
        engine = pyttsx3.init('espeak')
        engine.setProperty('voice', 'polish')
        engine.setProperty('rate', speed)
        engine.say(phrase)
        engine.runAndWait()
        engine.stop()

if __name__ == "__main__":
    protocol_1_percent(phrase="Aktywowano protokół jeden procent...", speed=150, speak=False)
    with open("korwinizmy.txt", "wb") as f:
        for i in range(1000):
            phrase=construct_sentence()
            f.write((phrase + '\r\n').encode('utf8'))
            protocol_1_percent(phrase=phrase, speed=150, speak=False)
    