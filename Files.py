#Read mode 'r','rb','r+','rb+'
"""fp = open("python.txt",'r')
fp.write("Python is the Best")
fp.close()"""

#Write mode 'w',wb','w+','wb+'
"""fp = open("python.txt",'w')
fp.write("Python is the Best")
fp.close()"""

#Append mode 'a','ab','a+','ab+'
"""fp = open("python.txt",'a')
fp.write("Python is the Best")
fp.close()"""

#Manipulating the pointer

fp = open("data.txt",'w')
fp.write("PythonX makes your python journey very easy")
fp.close()
fp = open("data.txt",'r')
print("Pointer position before reading is:",fp.tell())
print(fp.read())
print("Pointer position after reading is:",fp.tell())
fp.close()

fp = open("data.txt",'r')
print("Pointer position is:",fp.tell())
fp.seek(5)
print("Pointer position after manipulating is:",fp.tell())
fp.close()