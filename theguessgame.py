print("########################################\n#  Hi , I am Mr.G host of the game.    #\n#  So I welcome you to The Guess Game  #\n########################################\nThe game is like you guess the word i am thinking of , and you get infinite tries to guess with a percentage match of word every time you guess as a hint.\n\nIf you want to quit game at any point type '*close'. \nOk Lets Start !\n")
#words=['work', 'hard', 'sir', 'i', 'goona', 'tell', 'you', 'something', 'that', 'is', 'not', 'a', 'number', 'fort', 'happy', 'sad', 'kill', 'bill', 'cat', 'bat', 'name', 'fame', 'jam', 'coat', 'boat', 'bald', 'salt', 'car', 'train', 'airplane', 'aeroplane', 'rocket', 'laptop', 'jacket', 'pocket', 'screen', 'display', 'nut', 'cult', 'charger', 'file', 'rubber', 'bolt']
words=["bill","ball"]
total=len(words)
from secrets import randbelow
from difflib import SequenceMatcher

#string similarity percent calcultor Start
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
#string similarity percent calcultor END
i=0
ffrist=True
gamequit=False
while i<total:
    if gamequit:
        break
    if not ffrist:print("Lets play again\n")
    ffrist=False
    myword=words[randbelow(total)]
    mw=[]
    for letter in myword:mw.append(letter)
    x=len(myword)
    j=1
    y=""
    guess=""
    for j in range(0,x) :
        y=y+"*"
    print("Now my word is "+y)
    till=True
    trycount=0
    hint=""
    hc=0
    hintltr=""
    first=True
    success=False
    while till:
        if not first:print("Oops! it was not what i thought.\nLets give it another try.")
        first=False
        guess=input("Guess a word :")
        if guess=="*close":
            gamequit=True
            break
        if guess != myword:
            trycount+=1
            matchper=similar(guess,myword)
            print("Your guess percentage match to my word : "+str(matchper))
            if trycount>5 and trycount%3==0:
                bn=input("I think is hard for you.Do you want hint?(Y/N)")
                if bn=='y' or bn=='Y':
                    hintltr+=mw[hc]
                    w=0
                    hz=""
                    for w in range(0,x-len(hintltr)):
                        hz+="*"
                    hint=hintltr+hz
                    hc+=1
                    print("Here I a reveal letter of my word :"+hint)
                    if hint==myword:
                        print("\nIts all you have the full word in hint.\n\nSorry but you loose this time.\n")
                        success=False
                        break
        else:
            till=False
            success=True
            break
    if success:
        print("You guessed it correct\nTotal guesses:"+str(trycount)+"\n")
    i+=1
if not gamequit:print("Probably I am short on words now, you have tried all of my vocalury.\nSo for this time i think that is all i got.\nSee you again.\nTill then Bye.")
print("###################################################\n#Thanks for playing with me,hope to see you again.#\n###################################################")    
