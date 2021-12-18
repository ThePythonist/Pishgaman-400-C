def pangram(word):
    if len(set(word)) == len(word) :
        return True
    else :
        return False

print(pangram(input("Enter any word : ")))
