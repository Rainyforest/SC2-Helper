import pyttsx3
import re
from build import Build

global_engine = pyttsx3.init()
voices = global_engine.getProperty('voices')
global_engine.setProperty('voice', voices[3].id)
def display_announcers():
    voices = global_engine.getProperty('voices')
    for voice in voices:
        print("Voice: %s" % voice.name)
        print(" - ID: %s" % voice.id)
        print(" - Languages: %s" % voice.languages)
        print(" - Gender: %s" % voice.gender)
        print(" - Age: %s" % voice.age)
        print("\n")


def load_translation_dict():
    with open('glossary.txt', 'r', encoding='utf-8') as reader:
        pattern = re.compile(r'(?P<space>\s)') # 匹配空格的正则
        
        table = dict([("".join(match[0:-1]).strip(),match[-1]) for line in reader.readlines() if (match := re.split(pattern, line.strip()))])
        return table

def announce(str):
    global_engine.say(str)
    global_engine.runAndWait()

def announce_build(build):
    if isinstance(build,Build):
        announce("造一个"+build.name)
        # print(build.name +"\t====\t"+ str(build.time_in_seconds))
    else:
        pass
