def isAnagram(list1, list2):
    if len(list1)!= len(list2):
        print("not an anagram!")
        return 0
    checker = []
    for i in range(len(list1)):
        checker.append(False)
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                checker[i]=True
                list2[i]==0
    #print(checker)
    for i in range(len(checker)):
        if checker[i]==False:
            print("NOT an anagram!")
            return 0
    print("anagram!")



while True:
    #check if two given words are anagrams
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")

    #slice words into separate letters by loading into a list
    list1 = list(word1)
    list2 = list(word2)

    isAnagram(list1, list2)

    
    
    


