def isAnagram(list1, list2):
    #first check if the words are the same length
    #if not, kick it out!
    if len(list1)!= len(list2):
        print("not an anagram!")
        return 0
    #create a new list named "checker" to hold if each letter has one and only one match,
    #fill with a "False" value (assume it doesn't have a match)
    checker = []
    for i in range(len(list1)):
        checker.append(False)
        
    #walk through the first list, see if the letter being looked at has a match in second list
    #if it does, change the slot in the "checker" to true
    #and change the matching letter in the second list to a "0" to avoid counting it twice
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                checker[i]=True
                list2[i]==0
    #go through the "checker" list to see if it has any False values
    #if any remain, print out that it's NOT an anagram
    for i in range(len(checker)):
        if checker[i]==False:
            print("NOT an anagram!")
            return 0
    print("anagram!")



while True:
    #get two words from the user
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")

    #slice words into separate letters by loading into a list
    list1 = list(word1)
    list2 = list(word2)

    isAnagram(list1, list2)

    
    
    



    
    
    


