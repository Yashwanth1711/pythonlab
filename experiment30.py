from collections import Counter
f1=open("30.txt","w")
f1.write(input("enter some text:"))
f1.close()
f2=open("30.txt","r")
t=f2.read().split()
print("the words in the file are:",t)
print("the most common word is :")
print(Counter(t).most_common(1))