import json
import re
import time
import unicodedata

data = {}
with open("/data/fr_FR.json", "r") as read_file:
    data = json.load(read_file)

def timer(arg):
    return round(time.monotonic()-arg, 9)

def strip_accents(string):
    return "".join(char for char in unicodedata.normalize("NFD", string) if unicodedata.category(char) != "Mn")

# reverse word into drow for a more effective lookup?

# pick a word like "aidées"
# checks if the end of the word is a known suffix (currently merged with next check)
# if so, proceed to the replacement to the infinitive form
# checks if the word exists
# if so, proceed to the replacement in string
def solution_1(string):
    timestamp = time.monotonic()
    for word in re.findall("\w+", string):
        for v in data["words"]:
            for suffix in v["suffixes"]:
                if re.sub("(\w+)"+suffix+"$", "\\1"+v["infinitive"], word) in v["verbs"]:
                    string = string.replace(word, re.sub("(\w+)"+suffix+"$", "\\1"+v["infinitive"], word), 1)
    print("Time: ", timer(timestamp))
    return string

# pick a word like "aidées"
# is it in dictionary? Note: Dictionary is mainly a list of tuples - sort of - like ("aidées", "aider") generated from json
# if found, word is replaced
def solution_2(string):
    timestamp = time.monotonic()
    dic_ = {}
    for v in data["words"]:
        for verb in v["verbs"]:
            for suffix in v["suffixes"]:
                dic_.update( {re.sub("^(.*)"+v["infinitive"], "\\1"+suffix, verb) : verb} )
    for word in re.findall("\w+", string):
        if word in dic_.keys():
            string = string.replace(word, dic_[word], 1)
    print("Time: ", timer(timestamp))
    return string

heredoc = """
Ceci est un texte d'exemple.
Le but est de remplacer des verbes conjugués par leur forme infinitive.
Mais également de simplifier les chaînes de caractères accentués.
"""

print("TEXTE ORIGINAL")
print("========================================")
print(heredoc)
print("")

print("TEXTE SANS ACCENT")
print("========================================")

heredoc = strip_accents(heredoc)

print(heredoc)
print("")

print("TEXTE AVEC VERBE SOUS FORME INFINITIVE")
print("Solution 1")
print("========================================")

s1 = solution_1(heredoc)

print(s1)
print("")

print("TEXTE AVEC VERBE SOUS FORME INFINITIVE")
print("Solution 2")
print("========================================")

s2 = solution_2(heredoc)

print(s2)
print("")
