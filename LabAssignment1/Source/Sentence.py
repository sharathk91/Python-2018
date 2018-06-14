text = input("Enter the sentence: ") #take input from the user
text_split = text.split() #split each word by space
text_len = len(text_split) #take the length of each word
if  text_len%2 == 0: #check if the sentence contains even no of words
    mid = text_len/2 #take the mid value
    print("Middle words are:",text_split[int(mid-1)],text_split[int(mid)]) #middle word is value of mid term index and mid-1 index value

else: #if the sentence contains odd no of words
    mid = text_len/2
    print("Middle words are: ",text_split[int(mid)]) #middle word is mid term index value

sort_text = sorted(text_split,key=len)  #sort the input text with the its length so that the longest word will be last
print("Longest word is: ",sort_text[-1]) #print long word

rev_list = []
for word in text_split: #iterate each word
 rev_list.append(word[::-1]) #append to rev list with its reverse word
rev_text =  " ".join(rev_list) #append each word with the space
print("Sentence with reverse words is :",rev_text) #prints the reverse list
