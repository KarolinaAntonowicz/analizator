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

#TODO
while (isWorking):
    for element in menu:
        print(element)
    action = int(input())
    if action == 1:
        text = download()
