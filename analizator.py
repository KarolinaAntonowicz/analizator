import requests
import os
menu = ['1. Choose input file', '2. Count the number of letters in the downloaded file',
        '3. Count the number of words in the file',
        '4. Count the number of punctuation marks in the file.', '5. Count the number of sentences in the file',
        '6. Generate a letter usage report (A-Z)', '7. Save the statistics from points 2-5 to a statystyki.txt file',
        '8. Exit the program']
isWorking = True
status_code = 200
text = list()

def download():
    print("download file from internet?")  
    action = (input())
    if action == "Y":
        global status_code
        print("add the source")
        url = input()
        #url = 'https://s3.zylowski.net/public/input/6.txt'
        r = requests.get(url)
        if r.status_code != 200:
            print ("error")
            status_code = 0
            return 0
        filename = url.split('/')[-1]
        # writing file
        with open(filename, 'wb') as f:
            f.write(r.content)
        # open file
        file = open(filename, 'r')
        text = list(file)
        # text = file.read()
        file.close()
        return text
    if action == "N":
         print("add name file")
         filename = input()
         if(not os.path.exists(filename)) or (not os.path.exists(filename)):
            filename = input("Whhoops! Your file does not exist")
            return 0
         file = open(filename, 'r')
         text = list(file)
         text = file.read()
         
         return text
        


def countLetters(text, printing):
    global status_code
    if status_code == 0:
        print('error')
        return 0
    x = [None] * 26
    vowel = [None] * 5
    consonant = [None] * 21
    #vowel is
    #AEIOU
    #consonant is
    #BCDFGHJKLMNPQRSTVWXYZ

    for i, letter in enumerate('AEIOU'):
        for line in text:
            # print(line.count(letter))
            vowel[i] = line.count(letter)
            vowel[i] += line.count(letter.lower())

    for i, letter in enumerate('BCDFGHJKLMNPQRSTVWXYZ'):
        for line in text:
            # print(line.count(letter))
            consonant[i] = line.count(letter)
            consonant[i] += line.count(letter.lower())

    for i, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        for line in text:
            # print(line.count(letter))
            x[i] = line.count(letter)
            x[i] += line.count(letter.lower())
        if printing == True:
            print(letter, ': ', x[i])
    # print(x)
    return [sum(vowel), sum(consonant)]

def countWords(text):
    global status_code
    if status_code == 0:
        print('error')
        return 0
    countingWords = []
    for line in text:
        wordslist = line.split()
        for i in range(len(wordslist)-1):
            if len(wordslist[i]) > 1:
                countingWords.append(wordslist[i])
    words = len(countingWords)
    return words

def countPunctations(text):
    global status_code
    if status_code == 0:
        print('error')
        return 0
    full_stops = 0
    #commas = 0
    #semicolon = 0
    #exclamation_mark = 0
    question_mark = 0
    #dash = 0
    #colon = 0
    #ellipsis = 0
    for line in text:
        full_stops = full_stops + len(line.split('.'))
        #commas = commas + len(line.split(','))
        #semicolon = semicolon + len(line.split(';'))
        #exclamation_mark = exclamation_mark + len(line.split('!'))
        question_mark = question_mark + len(line.split('?'))
        #dash = dash + len(line.split('-'))
        #colon = colon + len(line.split(':'))
        #ellipsis = ellipsis + len(line.split('...'))
    return full_stops+question_mark

def countSentences(text):
    global status_code
    if status_code == 0:
        print('error')
        return 0
    full_stops = 0
    exclamation_mark = 0
    question_mark = 0
    ellipsis = 0
    for line in text:
        full_stops = full_stops + len(line.split('.'))
        ellipsis = ellipsis + len(line.split('...'))
        exclamation_mark = exclamation_mark + len(line.split('!'))
        question_mark = question_mark + len(line.split('?'))
    return full_stops+exclamation_mark+question_mark+ellipsis

#TODO
while (isWorking):
    for element in menu:
        print(element)
    action = int(input())
    if action == 1:
        download()
    elif action == 2:
        pass
    elif action == 3:
        print('Total words:   ', countWords(text))
    elif action == 4:
        print('Total punctations:   ', countPunctations(text))
    elif action == 5:
        print('Total sentences:    ', countSentences(text))
    elif action == 6:
        countLetters(text, True)
    elif action == 7:
        plik = open('statystyki.txt', 'w')
        plik.write("2: %s\n3: %s \n4: %s \n5: %s" % (countLetters(text, False), countWords(text), countPunctations(text), countSentences(text)))
        plik.close()
    elif action == 8:
        if(os.path.exists("statystyki.txt")):
            os.remove("statystyki.txt")
        if(os.path.exists("6.txt")):
            os.remove("6.txt")
        isWorking = False
