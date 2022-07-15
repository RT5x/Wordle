from words import wordstr
import random

wordlist = wordstr.split()

word1 = random.choice(wordlist)
word2 = list(word1)

i = 1
while i <= 6:
  g = str(input("guess word" + "[" + str(i) + "]: "))
  gl = list(g)
  j = 0

  if g in wordlist:
    print(" ")
  else:
    print("Not in word list")

  
  if len(gl) != 5:
    print("Word must be 5 letters")

  while j <= 4:
    guesslist = ["", "", "", "", ""]
    if gl[j] == word2[j]:
      guesslist[j] = gl[j]
      print("Correct letter guess: " + str(guesslist))
      j += 1

    else:
      j+=1

  if gl == word2:
    print("Correct guess!")
    break  

  i += 1
print("The correct word was " + word1)
