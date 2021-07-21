import re
import csv
import time
start = time.time()
mydict={}
with open('C:/exeter/TranslateWords Challenge/french_dictionary.csv', mode='r') as fr_dict:
    reader = csv.reader(fr_dict)
    mydict = {rows[0]:rows[1] for rows in reader}
f=open("C:/exeter/TranslateWords Challenge/find_words.txt","r")
# content=''
# arr=[]
# with open("C:/exeter/TranslateWords Challenge/t8.shakespeare.txt","r+")as p:
#     for line in p:
#         arr.append(line)
#     content=''.join(arr)

p= open("C:/exeter/TranslateWords Challenge/t8.shakespeare.txt","r")
content=p.read()
para = re.split("\s|(?<!\d)[,.](?!\d)",content)
#print(f.read())
find = set(words for line in f for words in line.strip('\n\t').split(" "))
for words in find:
    if words in para:
        if words in mydict:
            content=content.replace(words,str(mydict[words])) 
print(content)          
end = time.time()
print("Execution time in seconds: ",(end - start))
