def word_count(str):  #function definition
    counts = dict()   #define dictionary
    words = str.split()  #split the sentence to word

    for word in sorted(words): #iterate each word from the sorted list
        if word in counts: #check if each word is already present in dictionary
            counts[word] += 1  #increment the count by 1
        else:
            counts[word] = 1    #if not present the assign the value as 1

    return counts    #sends the count value to calling function
name=input("Enter the sentence: ")  #take input from user
print( word_count(name))  #prints the count value
