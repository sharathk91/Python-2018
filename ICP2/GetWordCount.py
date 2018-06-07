file=open("C:/Users/shara/Documents/test.txt","r+")
wordcount={}
f = open('C:/Users/shara/Documents/output.txt','w')
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
    f.write(k +","+str(v))
    f.write("\n")
f.close()