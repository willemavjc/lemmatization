import json
import re

data = {}

with open("fr_FR.json", "r") as read_file:
    data = json.load(read_file)

for v in data["words"]:
    for verb in v["verbs"]:
        print(verb)
        for suffix in v["suffixes"]:
            print(re.sub("^(.*)"+v["infinitive"], "\\1"+suffix, verb))
# aidées => replace accent => (aid)(ees) => \2 in suffixes ? => infinitive => (aid)(er) => \1\2 in verbs ? => OK
# aidées => in list ? "aidées;aider" => replace # list generated from json?
