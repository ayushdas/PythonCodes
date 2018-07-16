### Code to get the most frequently used words in a text document
### Concepts Used:
### 1. Dictionary 2. Tuple 3. File Reading
fileName = raw_input('Enter a file name: ')
if len(fileName) < 1:
    fileName = 'trial.txt'
try:
    fileHandle = open(fileName)
    print ('Searching file: '+fileName)
except:
    print('Cannot open file: '+fileName)
    quit()

print('File ready for reading...')

print ('Counting words...')

countOfWords = dict()
for line in fileHandle:
    line = line.strip()
    words = line.split(' ')
    for word in words:
        if word=='':
            continue
        countOfWords[word] = countOfWords.get(word,0) + 1

print ('Counting completed...')

print ('Computing the top 10 words in the document WITHOUT dynamic lists...')

wordList = list()
for key,value in countOfWords.items():
    newTup = (value,key)
    wordList.append(newTup)

wordList = sorted(wordList, reverse=True)

print ('The top 10 words in the document WITHOUT dynamic lists...')
for item in wordList[:10]:
    print(item)

print ('Computing the top 10 words in the document WITH dynamic lists...')

print(sorted([(v,k) for k,v in countOfWords.items()],reverse=True)[:10])

### Object Oriented programming in Python
### Creating classes, methods and using inheritance

class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, name):
        self.name = name
        print('I am constructed')  

    def party(self):
        self.x +=1
        print ('The value of x so far: ',self.x)

    def __del__ (self):
        print('I am destructed')

class DummyClass:
    def __init__(self):
        print ('I am contructed')

    def dummyFunction(self):
        print('This is a dummyFunction')

    def __del__(self):
        print ('I am destructed')                

class FootballFan(PartyAnimal,DummyClass):
    points = 0
    def touchdown(self):
        self.points = self.points+7
        self.party()   
        self.dummyFunction()     
        print(self.name,self.points)               

an = PartyAnimal('Ayush')
an.party()
an.party()
an.party()
an=42
print(an)

ab = FootballFan('Ayush')
ab.dummyFunction()
ab.touchdown()


