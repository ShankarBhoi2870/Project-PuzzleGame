import random

def Shuffleword(wrd):
    pw=random.sample(wrd,k=len(wrd))
    return ' '.join(pw)

def PrintPuzzleQuestion(word,score):
    Problemword=Shuffleword(word)
    print("\n Arrange the letters to from a valid word:")
    print(Problemword)
    userword=input()
    print()
    if userword.upper()==word:
        print("Correct")
        score=score+1
    else:
        print("Wrong")
        score=score-1
    return score

def main():
    score=0
    words=["FATHER","BREAK","COUNTRY","GREEN","AEROPLANE"]
    words=random.sample(words,k=len(words))
    print(words)
    for word in words:
        score=PrintPuzzleQuestion(word,score)
    print("your score is",score)
    print()
main()