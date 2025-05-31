try:
    user = input("The absloute file path: ") 
    file = open(user, "r")
    word = input("The word: ")
    print(f"The word {word} has appeared",file.read().split().count(word),"times")
except:
    print("Error! no files exist in this path.")    