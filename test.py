def cutSentences(sentence, rangeVar): 
    arrays = sentence.split(".")
    newString = ""
    print(arrays)

    for x in range(0, rangeVar):
        newString += arrays[x] + "."

    return newString

print(cutSentences("Hey there. It's nice to see you. I really miss you.", 2))