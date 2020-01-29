import requests
import json

#name = input("name")

def cutString(sentence, len):

    if '.' not in sentence: 
        sentence += '.'

    arrays = sentence.split(".")
    print(arrays)
    newString = ""

    for x in range(0, len):
        if arrays[x] != '':
            newString += arrays[x] + "."
    return newString

# print(cutString("Hello i fucking love you", 2))

def findDefinition(name):
    URL = "http://api.urbandictionary.com/v0/define?term=" + name
    data = requests.get(url=URL)
    information = data.json()
    #print(information)
    return cutString(information["list"][0]["definition"], 2)

#print(findDefinition(name))