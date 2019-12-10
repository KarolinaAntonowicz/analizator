import requests
menu = ['1. Download the file from the internet', '2. Count the number of letters in the downloaded file',
        '3. Count the number of words in the file',
        '4. Count the number of punctuation marks in the file.', '5. Count the number of sentences in the file',
        '6. Generate a letter usage report (A-Z)', '7. Save the statistics from points 2-5 to a statystyki.txt file',
        '8. Exit the program']
isWorking = True
status_code = 200
text = list()

def download():
    url = 'https://s3.zylowski.net/public/input/6.txt'
    r = requests.get(url)
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


text = download()

def countLetters(text, printing):
    global status_code
    if status_code == 0:
        print('error')
        return 0
    x = [None] * 26
    for i, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        for line in text:
            # print(line.count(letter))
            x[i] = line.count(letter)
            x[i] += line.count(letter.lower())
        if printing == True:
            print(letter, ': ', x[i])
    # print(x)
    return sum(x)

def countWords(text):
    for line in text:
        wordslist = line.split()
        words = len(wordslist)
    return words

def countPunctations(text):
    global status_code
    if status_code == 0:
        print('error')
        return 0
    full_stops = 0
    commas = 0
    semicolon = 0
    exclamation_mark = 0
    question_mark = 0
    dash = 0
    colon = 0
    ellipsis = 0
    for line in text:
        full_stops = full_stops + len(line.split('.'))
        commas = commas + len(line.split(','))
        semicolon = semicolon + len(line.split(';'))
        exclamation_mark = exclamation_mark + len(line.split('!'))
        question_mark = question_mark + len(line.split('?'))
        dash = dash + len(line.split('-'))
        colon = colon + len(line.split(':'))
        ellipsis = ellipsis + len(line.split('...'))
    return full_stops+commas+semicolon+exclamation_mark+question_mark+dash+colon+ellipsis

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
        text = download()
    elif action == 2:
        print('Total letters:   ', countLetters(text, False))
    elif action == 3:
        print('Total words:   ', countWords(text))
    elif action == 4:
        print('Total punctations:   ', countPunctations(text))
    elif action == 5:
        print('Total sentences:    ', countSentences(text))
