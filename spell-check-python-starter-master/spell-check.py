# Spell Check Starter

import re
import time

def loadWordsFromFile(fileName):
    # Read file into an array of words
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    return re.findall(r"[\w']+", textData)

# Load data files into global variables
dictionary = loadWordsFromFile("data-files/dictionary.txt")
aliceWordsCh1 = loadWordsFromFile("data-files/AliceInWonderLandCh1.txt")
aliceWordsFull = loadWordsFromFile("data-files/AliceInWonderLand.txt")

def linearSearch(anArray, item):
    for i in range(len(anArray)):
        if anArray[i] == item:
            return i
   
    return -1

def binarySearch(anArray, item):
    LI = 0
    UI = len(anArray)-1
    while LI <= UI:
        MI = (LI + UI) // 2
 
        if (anArray[MI] < item):
           LI = MI + 1
        elif (anArray[MI] > item):
           UI = MI - 1
        else:
           return MI
  
    return -1

# Main Menu
loop = True
while loop:
    # Print Main Menu
    print("Main Menu")
    print("1: Linary Search Alice In Dictionary")
    print("2: Binary Search Alice In Dictionary")    
    print("3: Binary Search Alice In Wonderland Ch. 1")
    print("4: Linear Search Alice In Wonderland Ch. 1")
    print("5: Binary Search Alice In Wonderland Full")
    print("6: Linear Search Alice In Wonderland Full")
    print("7: Exit")
    selection = input("Enter menu selection (1-7): ")

    # Process selection
    if (selection == "1"):

        cool = input("Word: ")
        index = linearSearch(dictionary, cool)
        if (index == -1):
            print ("No such word man")
        else:
            print (cool + " is a word man at ", + index)
    elif (selection == "2"):
        cool = input("Word: ")
        index = binarySearch(dictionary, cool)
        if (index == -1):
            print ("No such word man")
        else:
            print (cool + " is a word man at ", + index)
    elif (selection == "3"):
        start_time = time.time()
        for word in aliceWordsCh1:
            index = binarySearch(dictionary, word.lower())
            if (index == -1):
                print (word, "was not found.")           
        end_time = time.time()
        print("Time: ", (end_time - start_time))
    elif (selection == "4"):
        start_time = time.time()
        for word in aliceWordsCh1:
            index = linearSearch(dictionary, word.lower())
            if (index == -1):
                print (word, "was not found.")           
        end_time = time.time()
        print("Time: ", (end_time - start_time))
    elif (selection == "5"):
        start_time = time.time()
        for word in aliceWordsFull:
            index = binarySearch(dictionary, word.lower())
            if (index == -1):
                print (word, "was not found.")           
        end_time = time.time()
        print("Time: ", (end_time - start_time))
    elif (selection == "6"):
        start_time = time.time()
        for word in aliceWordsFull:
            index = linearSearch(dictionary, word.lower())
            if (index == -1):
                print (word, "was not found.")           
        end_time = time.time()
        print("Time: ", (end_time - start_time))
    elif (selection == "7"):
        loop = False
# end while loop
print("Goodbye")


