# f=open("30.py",'r')   file opening in the read mode 
# # print(f.read())       read the total file
# # print(type(f.read()))    stores the data in the string formate
# print(f.read(100))                 
# # read  the 100 characters from the file 
# print(f.read(50))
# # read the  50 character from the cursor where it stoped
# f=open("30.py",'r')
# print(f.readline())
# print(f.readline())
# read the line where the cursor is located
# the output is in the string formate
# print(f.readlines())
# read the all lines in the file 
# the output is in the list formate
# print(f.close()) that close the file we opened
# ----------------------------------------------------------------
# f=open('30.py','w')
# open the file in the write mode 
# print(f.write("hiiiiiiiiiiii"))   that rewrite the file 
# print(f.write("hiiiiiiiiiiii this  the second line using write mode"))
# write mode that write the data from the first line of the file
# f=open("30.py",'a')
# opened the file in append mode 
# print(f.write("hiiiiii"))
# -----------------------------------------------------------------------
# Q1. Write a Python program to create a file named "student.txt" and write 5 student names into it

# f=open("student.txt",'w')
# print(f.write("hello"))
# print(f.write("1.akanksha\n2.navya\n"))


# Q2. Write a Python program to open the file "student.txt" in read mode and display all the names on the screen.
# f=open("student.txt",'r')
# # print(f.read())
# print(f.readlines())

# Q3. Write a Python program to append two more names to "student.txt" and then read the complete file content and display it.
# f=open("student.txt",'+a')
# print(f.write("3.hhhhhh\n4.jjjjj\n"))



# Write a Python program that reads the content of a file named "story.txt" and prints:

# Total number of characters

# Total number of words

# Total number of lines
# f=open("student.txt",'r')
# length= f.read()
# print("number of characters:",len(length))
# print("number of words:",len(length.split()))
# print("number of lines:",len(length.split("\n")))