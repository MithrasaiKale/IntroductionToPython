intro = str(input("Introduce Yourself-") )

CharacterCount=0
WordCount=1
for i in intro:
    CharacterCount += 1
    #This is exactly the same thing as CharacterCount=CharacterCount+1. just shorter
    if(i==" "):
        WordCount += 1

#print(CharacterCount, WordCount)
print("Character Count : " + str( CharacterCount))
print("Word Count : "+str(WordCount))