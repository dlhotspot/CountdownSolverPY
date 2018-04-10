import random
import time
import sys
from operator import *
from random import sample, randint
from sys import argv
from itertools import combinations
import _pickle as pickle
import winsound
n=len
wordFile = open('output.txt', 'r')
matches = []
ti=30
hgs=[]
from tkinter import *
def matchWord(word1, word2):
    isMatch = True
    #The idea here is to compare each letter of the word with another
    #If the letter is a match, need to ignore that same letter so it won't be counted twice
    for letter in word1:
        #Found you can conveniently check if an item is in a list in python using 'in'
        #Found out here: http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/ifstatements.html
        if letter in word2:
            word2.remove(letter)
        elif len(word2) == 0:
            isMatch = True
        else:
            isMatch = False

    return isMatch
def solveLetters(anagram):
    #Longest word in file is best word
    longestWord = ""
    for word in wordFile:
        #Remove newline characters, messes with output
        word = word.rstrip()
        #Find all matches and add them to my matches list
        if matchWord(anagram, list(word)) == True:
            #Add word
            matches.append(word)
            if len(longestWord) < len(word):
                #Set longest word when new one is found.
                longestWord = word
    return longestWord
def solveNumbers(N,T):
  # M is a map: (bitmask of used input numbers -> (expression value -> expression text))                  
  M=[{} for i in range(1<<len(N))]

  # initialize M with single-number expressions                                                           
  for i in range(len(N)):
    M[1<<i][1.0*N[i]] = "%d" % N[i]

  # allowed operators                                                                                     
  ops = (("+",lambda x,y:x+y),("-",lambda x,y:x-y),("*",lambda x,y:x*y),("/",lambda x,y:x/y))

  # enumerate all expressions                                                                             
  n=0
  while 1:

    # test to see if we're done (last iteration didn't change anything)                                   
    c=0
    for x in M: c +=len(x)
    if c==n: break
    n=c

    # loop over all values we have so far, indexed by bitmask of used input numbers                       
    for i in range(len(M)):
      for j in range(len(M)):
        if i & j: continue    # skip if both expressions used the same input number                       
        for (x,s) in M[i].items():
          for (y,t) in M[j].items():
            if y: # avoid /0 (and +0,-0,*0 while we're at it)                                             
              for (o,f) in ops:
                M[i|j][f(x,y)]="(%s%s%s)"%(s,o,t)

  # pick best expression                                                                                  
  L=[]
  for t in M:
    for(x,e) in t.items():
      L+=[(abs(x-T),e)]
  L.sort();return L[0][1]      
def numbers():
    l=0
    s=0
    picked=[]
    while (l + s) != 6:
        l=0
        s=0       
        l=int(input("How many large numbers?"))
        s=int(input("How many small numbers?"))
        if (l + s) != 6:
            print("Not equal to six.\nTry again.")
    large=[25 , 50 , 75 , 100]
    small=[1 , 1 , 2 , 2 , 3 , 3 , 4 , 4 , 5 , 5 , 6 , 6 , 7 , 7 , 8 , 8 , 9 , 9 , 10 , 10]
    picked=[]
    for i in range(0,l): # big
        randomint=random.randint(1,4)
        a=large[randomint-1] #throwaway var 
        picked.append(a)
    for i in range(0,s): # small
        randomint=random.randint(1,20)
        a=small[randomint-1] #throwaway var
        picked.append(a)
    goal=random.randint(100,999)
    print(goal)
    print(picked[0],picked[1],picked[2],picked[3],picked[4],picked[5])
    return picked,goal

def letters():
    c=0
    v=0
    while (c + v) != 9:      
        c=int(input("How many consonants?"))
        v=int(input("How many vowels?"))
        if (c + v) != 9:
            print("Not equal to nine.\nTry again.")
    consonant=["B","B", "C","C", "D","D","D","D", "F","F", "G","G","G", "H","H", "J","J", "K", "L","L","L","L", "M","M", "N","N","N","N","N","N", "P","P", "Q", "R","R","R","R","R","R", "S","S","S","S", "T","T","T","T","T","T", "V","V", "W","W", "X", "Y","Y", "Z"]
    vowel=["A","A","A","A","A","A","A","A","A","E","E","E","E","E","E","E","E","E","E","E","I","I","I","I","I","I","I","I","I","O","O","O","O","O","O","O","O","U","U","U","U"]
    picked=[]
    for i in range(0,c): # CONSONANTS
        randomint=random.randint(1,57)
        a=consonant[randomint-1] #throwaway var 
        picked.append(a)
    for i in range(0,v): # VOWELS
        randomint=random.randint(1,41)
        a=vowel[randomint-1] #throwaway var
        picked.append(a)
    print(picked[0],picked[1],picked[2],picked[3],picked[4],picked[5],picked[6],picked[7],picked[8])
    b="".join(picked)
    return b

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\n')
        time.sleep(1)
        t -= 1
    print('Times up!')
window=Tk()
while 1==1:
    print("What do you want to do?")
    print("(1) Number Round")
    print("(2) Letters Round")
##    print("(3) Letter Solver")
##    print("(4) Number Solver")
    print("(0) Exit")
    z=int(input(">>>"))
    if z == 1:
        w,x=numbers()
        input("")
        countdown(ti)
        print(solveNumbers(w,x))
    elif z == 2:
        y=letters()
        input("")
        countdown(ti)
        bestWord = solveLetters(y.strip(" ").lower())
        print("Words from anagram: ")
        for match in matches:
          print(match)
        print("The best match is: ", bestWord)
    
##    elif error
##    elif z == 4:
##      for i in range(1,9):
##        lettersjfj=input("Enter letter",i,":")
##        hgs.append(lettersjfj)
##      asdwsadwa="".join(lettersjfj)
##      bestWord = solveLetters(asdwsadwa.strip(" ").lower())
##    elif z == 3:
##      for i in range(1,6):
##        numbersjfjas=input("Enter number",i,":")
##        ius.append(numberersjfjas)
##      goalasda=int(input("Enter the goal Number:"))
##      print(solveNumbers(ius,goalasda))
    else:
        sys.exit()
