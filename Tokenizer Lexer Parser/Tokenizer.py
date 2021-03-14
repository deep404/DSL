import re

def Tokenize (word):
    shapeName = ['Triangle', 'Circle']
    methodName = ['draw','setParameters','setVertices']
    specialCharacters = ['(', ')', '.']
    numericType = '(\d+(?:\.\d+)?)'
    # string = '\[".*?""\]'
    identifier = r'^[A-Za-z][A-Za-z0-9_]*$'

    if (word[0]=='"' and word[-1]=='"'):
        print("Token : {token_type:(string), value: (",word,")")
    elif (word in shapeName):
        print("Token : {token_type:(shapeName), value: (",word,")")
    elif(bool(re.search(identifier, word)) and word not in shapeName and word not in methodName):
        print("Token : {token_type:(identifier), value: (",word,")")
    elif (word in methodName):
        print("Token : {token_type:(methodName), value: (",word,")")
    elif (word in specialCharacters):
        print("Token : {token_type:(specialCharacter), value: (",word,")")
    elif (re.findall(numericType,word)):
        print("Token : {token_type:(numericType), value: (",word,")")

# program = 'Triangle myTriangle     \n '\
#           'myTriangle . setParameters     ( 123,1.45 , 2 , 3 )\n' \
#           'myTriangle.setVertices("A", "B", "C")     \n' \
#           'myTriangle.draw'

program = open("Program.txt", "r")

programlines = []
for line in program.readlines():
    programlines.append(line.strip())

for line in programlines:
    print(line)

for line in programlines:
    if '(' in line:
        argumentlist = line[line.index('('):line.index(')')+1]
        Tokenize('(')
        argumentlist = argumentlist[1:len(argumentlist)-1]
        line = line.replace(argumentlist, '')
        argumentlist = argumentlist.split(',')
        for string in argumentlist:
            string = string.strip()
            Tokenize(string)
        Tokenize(')')
    words = re.findall(r'[^\s]+', line)
    for word in words:
        Tokenize(word)


