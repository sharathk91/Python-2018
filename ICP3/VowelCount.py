a= input("Enter the sentence: ") #take the input from user
vowels=set("aeiouAEIOU")  #define the set of vowels including both lower and Upper cases
count=0                   #initialize the initial value as 0 to sum the count
for v in a:            # loop each character from the input
    if v in vowels:    #check each input character if it is in vowels set
        count+=1       #if the character matches in the vowel set, then increment the count
print("Count of Vowels is :",count) #Print the no of vowels in the input string