text1 = ["sharath","madhukar","harish"]  #define a list
text2 = ["sharath","madhukar","rohith","rahul"]  #define 2nd list
text1_len = len(text1) #take the length of list1
text2_len = len(text2)  #take the length of list2
index = 0
common_list = []
uncommon_list = []
for index in range(text1_len): #loop through each word of list1
    if text1[index] in text2: #check if each word of list1 is present in list2
        common_list.append(text1[index]) #Append the list1 index value to the common list
    else:
        uncommon_list.append(text1[index]) #if not present append it to the uncommon list
    index +=1
print("common students are :",common_list) #prints common list
index = 0
for index in range(text2_len): #loop through each word of list2
    if text2[index] not in text1:  #check if each word of list2 is not present in list1
        uncommon_list.append(text2[index]) #append to the uncommon list

    index +=1
print("uncommon students are",uncommon_list)  #prints uncommon list

