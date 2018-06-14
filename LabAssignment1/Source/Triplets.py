from itertools import combinations  #import combinations
text = list(combinations([1,3,6,2,-1,2,8,-2,9],3)) #take the input list
triplets = [] #define an empty list
b=0
length=len(text) #cal length to loop the combinations
for a in range(length):
  if (sum(text[b])==0):  #check if the sum is 0
    triplets.append(text[b]) #append to list
  b+=1
print("Triplets are: ",triplets)