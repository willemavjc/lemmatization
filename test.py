string = """
Ceci est un texte d'exemple.
Le but est de remplacer des verbes conjugués par leur forme infinitive.
Mais également de simplifier les chaînes de caractères accentués.
"""

print(string)

import unicodedata
def strip_accents(string):
   return ''.join(c for c in unicodedata.normalize('NFD', string) if unicodedata.category(c) != 'Mn')

string=strip_accents(string)

print(string)

import json
import re

data = {}
dic_ = {}

with open("/data/fr_FR.json", "r") as read_file:
    data = json.load(read_file)

for v in data["words"]:
    for verb in v["verbs"]:
        for suffix in v["suffixes"]:
            dic_.update( {re.sub("^(.*)"+v["infinitive"], "\\1"+suffix, verb) : verb} )
# aidées => replace accent => (aid)(ees) => \2 in suffixes ? => infinitive => (aid)(er) => \1\2 in verbs ? => OK
# aidées => in list ? "aidées;aider" => replace # list generated from json?

for word in re.findall("\w+", string):
    if word in dic_.keys():
        print(dic_[word])
    else:
        print(word)
