def CountWordFromFile() :
    fileName = input("Enter the file name : ")
    file = open(fileName,"r")
    numberOfWords = 0

    for f in file :
        words = f.split()
        numberOfWords = numberOfWords+len(words)
        print ("Number Of Words are : ")
        print (numberOfWords)

CountWordFromFile()
