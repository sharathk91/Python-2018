#load modules for natural language kit to import ngrams,word & sentence tokenizer
import nltk
from nltk.util import bigrams
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
""""
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
"""
#load input file
input_data=open('input.txt',"r")
#read the data
data=input_data.read()
#get each word from sentence
words=word_tokenize(data)
#apply lemmitizer
lemm=WordNetLemmatizer()
list=[]
list1=[]
print("Lemmitizor:"+"\n")
#print lemmitizer module for each word
for k in words:
    print("Lemmatizor for word "+k+" is "+lemm.lemmatize(k))

print("\n")
print("Bigrams:"+"\n")
#print bigram from the data loaded
for x in bigrams(words):
    print(x)
    list.append(x)
print("\n")
#append each word in bigram to a list to calc frequencies
for y in list:
    for z in y:
        list1.append(z)
#calc bigram word frequency and top 5 repeated words
count=Counter(list1)
count_most=count.most_common(5)
most=[i[0] for i in count_most]
#print bigram word frequency and top 5 repeated words
print("\n Bigram word frequencies\n")
print(count)
print("\nTop 5 repeated words\n")
print(count_most)
#calc Senteces with repeated bigrams
cat=""
repeated_sent=sent_tokenize(data)
print("\n Senteces with repeated bigrams:\n ")
for m in repeated_sent:
    if any(word in m for word in most):
        print(m)
        cat=cat+m
#print Senteces with repeated bigrams
print("\n Sentence after concatenation is: \n"+cat)

