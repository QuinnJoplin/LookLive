import random
name = ""

#Print's the intro messages
def PrintMenu():
  play = input("Would you like to play a game of Hangman? (Y/N)")
  while (1):
    if play == 'n' or play == 'N':
      return None
    if play == 'y' or play == 'Y':
      name = input("Tell, me... what is your name? (First Last)")
      return name
    play = input("I'm sorry, I didn't catch that. Please repeat your answer. Y or n?")

#Pick's a word from the list
def GenerateWord(words):
  word = random.choice(words)
  return word;

#Prints the Gallows and Hangman (if applicaple)
def PrintStage(body):
  print("|---\n|  |\n|  {0}\n| {1}{2}{3}\n|_{4}{5}\n|___|\n".format(body[0], body[1], body[2], body[3], body[4], body[5]))

#Checks User's guess for correctness
def GuessCheck(correctWord, guess):
  tmp = 0
  indeces = []
  for i in correctWord:
    if guess == i:
      indeces.append(tmp)
      print("Correct!")
    tmp += 1
  if len(indeces) == 0:
    print("Incorrect Guess!")
    indeces.append(-1)
    return indeces
  return indeces

#Adds incorrect guess to list
def AddToUsed(used, letter):
  used.append(letter)

#Draws the "HangMan"
def ChangeBody(strike, body):
  def one():
    body[0] = "O"
  def two():
    body[1] = "/"
  def three():
    body[2] = "|"
  def four():
    body[3] = "\\"
  def five():
    body[4] = "/"
  def six():
    body[5] = "\\"
  
  options = {1: one, 2: two, 3:three, 4:four, 5:five, 6: six}
  options[strike]()

def main():
  guessed = False
  words = {
  "coyote": "Dingo of the wild west", 
  "cowboy":"Rides a horse and wrangles cattle","dessert":"Hot, dry, and sandy",
  "road runner":"meep, meep", 
  "jackrabbit":'"What\'s up, Doc"', 
  "horse":"The car that drives itself",
  "duel":"Usually done in the middle of town at high noon", 
  "revolver":"Classic six-shooter", 
  "holster":"Stephen Colbert once called Trump one of these", 
  "lasso":"Use this to wrap up them heifers", "bounty":"Think Duane `Dog' Chapman and Boba Fett","tumble weed":"Rolls through the dessert", "cactus":"covered in prickly spines", "sombrero":"Spanish for hat", "poncho":"Rhymes with honcho", 
  "spurs":"Makes your horse go faster", 
  "boots":"I just got me a pair of new..."}
  name = PrintMenu().split()[0]

  while (True):
    strike = 0
    correctWord = random.choice(list(words.keys()))
    body = [" ", " ", " ", " ", "_", "_" ]
    currentWord = []
    used = []

    print("Well then, %s, let's begin..." % name)

    #Builds underscores for unknown letters
    for i in correctWord:
      if i != " ":
        currentWord.append(" _ ")
      else:
        currentWord.append("   ")

    
    #Game Loop
    while strike != 6 and guessed == False:
      PrintStage(body)
      print("Hint: ", words[correctWord])
      i = 0
      for x in currentWord:
        print(currentWord[i], end = "")
        i += 1
      
      #If the user has made at least one incorrect guess, the letters they've guessed incorrectly
      if strike != 0:
        print("Wrong Letters: ", end = "")
        i = 0
        for x in used:
          print(used[i], end = ", ")
          i += 1
        print("\n")

      #Takes In User Guess
      guess = input("Try to guess one of the letters")
      if len(guess) == 1 and guess >= 'a' and guess <= 'z': 

        #User's Guess checked
        index  = GuessCheck(correctWord, guess)
        
        tmp = False
        for i in used:
          if i == guess:
            tmp = True
        #Incorrect Guess
        if index[0] == -1 and tmp != True:
          strike += 1
          AddToUsed(used, guess)
          ChangeBody(strike, body)
        else:
          for x in index:
            currentWord[x] = " {0} ".format(guess)


        #Game Lost Check
        if strike == 6:
          PrintStage(body)
          print("Game Over, the word was {0}!".format(correctWord))
          tmp = input("Would you like to play again? (Y/N)")
          if tmp == 'Y' or tmp == 'y':
            break
          if tmp != 'Y' and tmp != 'y':
            return None

        #Game Won Check
        guessed = True
        for x in currentWord:
          if x == " _ ":
            guessed = False
        if guessed == True:
          print("Congrats, you win! The word was {0}".format(correctWord))
          tmp = input("Would you like to play again? (Y/N)")
          if tmp != 'Y' and tmp != 'y':
            return None
          if tmp == 'Y' or tmp == 'y':
            break
        print("\n\n\n\n")
      else:
        print("Please repeat your guess [a-z]")
  


    
  


main()
