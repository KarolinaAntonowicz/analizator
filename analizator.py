import requests
import os
menu = ['1. Choose input file', '2. Count the number of letters in the downloaded file',
        '3. Count the number of words in the file',
        '4. Count the number of punctuation marks in the file.', '5. Count the number of sentences in the file',
        '6. Generate a letter usage report (A-Z)', '7. Save the statistics from points 2-5 to a statystyki.txt file',
        '8. Exit the program']
isWorking = True
status_code = 0
text = list()

def download():
    global status_code
    global text
    print("Download file from internet?[Y/N]")
    action = (input())
    if action == "Y":
        print("Add the source")
        url = input()
        #url = 'https://s3.zylowski.net/public/input/6.txt'
        r = requests.get(url)
        if r.status_code != 200:
            print ("error")
            status_code = 0
            return 0
        else:
            status_code =200
        filename = url.split('/')[-1]
        # writing file
        with open(filename, 'wb') as f:
            f.write(r.content)
        # open file
        file = open(filename, 'r')
        text = list(file)
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
            vowel[i] = line.count(letter)
            vowel[i] += line.count(letter.lower())

    for i, letter in enumerate('BCDFGHJKLMNPQRSTVWXYZ'):
        for line in text:
            consonant[i] = line.count(letter)
            consonant[i] += line.count(letter.lower())

    for i, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        for line in text:
            x[i] = line.count(letter)
            x[i] += line.count(letter.lower())
        if printing == True:
            print(letter, ': ', x[i])
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
    question_mark = 0
    for line in text:
        full_stops = full_stops + len(line.split('.'))
        question_mark = question_mark + len(line.split('?'))
    return full_stops+question_mark

def countSentences(text):
    global status_code
    if status_code == 0:
        print('error')
        return 0
    full_stops = 0
    question_mark = 0
    for line in text:
        full_stops = full_stops + len(line.split('.'))
        question_mark = question_mark + len(line.split('?'))
    return full_stops+question_mark


while (isWorking):
    for element in menu:
        print(element)
    action = int(input())
    if action == 1:
        download()
    elif action == 2:
        letters = countLetters(text, False)
        print('Total vowels:', letters[0], 'Total consonants:', letters[1])
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
        plik.write("Vowels: %s\nConsonants: %s\nWords: %s \nPunctations: %s \nSentences: %s" % (letters[0], letters[1], countWords(text), countPunctations(text), countSentences(text)))
        plik.close()
    elif action == 8:
        if(os.path.exists("statystyki.txt")):
            os.remove("statystyki.txt")
        if(os.path.exists("6.txt")):
            os.remove("6.txt")
        isWorking = False
