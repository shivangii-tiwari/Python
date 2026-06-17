# open('path','mode')
# types of Mode 
# read
# write
# append
g=open("hehe.txt",'w')
# g.write('this is file handleing')
# g.write('hello world')
g.write('weeeeeeeeee\n')#when you write multiple line then remove it it will also removed from your file or it will overwrite the last line of the code
g.writelines(['1. python\n','2.java\n','3.c++\n'])        #you can use double cote also anda write function also
g.writelines('''she is little bit messy  
don't know when where and what to speak
she laughs at wrong time always
she need some brain cells''')
g.close()
# it is the process of writing the data into the file or reading the data from the File 
# file is container which is use to store the data 
# base on the file extension it is possible to identify the type of data stored in file 
# before handling any file getting accessblity is mendatory
# in python open function is used to get the accessiblity of file 
# for that the syntax is 
# var_name=open('path/file_name','mode')
# syn2:
# with open('path/file_name','mode') as var
# in the mode of opration writing the data into the file or reading from the file for for that we have to use modes
# mode of operation classifide into three types
#  1.read
#  2.write => write(),writelines(),w+(we can do both)
#  3.append
# # write_mode
# write mode is use to write the content into the File 
# if file is not present then write mode create the File 
# if file is exsist the write mode will overwrite the content
# # write() (for single line)
# var_name.write(message/string)
# # writeline()  (used for multiple line)
# var_name.writelines([itrable])
# read mode:
# it is use to read the data from the file 
# in this case if file is not exsist the controler will throw error 
# in read mode we have three type of operation
# 1.read()
# 2.readline()
# 3.readlines()
g=open("hehe.txt",'r')
#print(g.read())
#print(g.read(5))#empty then try to read all file if integer is pass the it will follow the integer
# print(g.read(10))#first ten character
# print(g.read(10))#then next 10
#print(g.readline()) #it will read your first line
# print(g.readline(10))# if we want to print certain number of character
# print(g.read())
# g.close()
# \n is also a character
#print(g.readlines())
#print(g.readlines()[0])#we can perform indexing in it line by line
#print(g.readlines()[1])
g.close()
# mode of operation in read
# 1.read
# it is a function which is use to read the content which present inside the File 
# argument is not mandetory 
# it only accpet integer argument 
# if you pass an argument in it it will read only that number of character
# 2.readline
# it is a fuction which is use to read the particular line from the file and it is possible read line by line data
# 3.readlines
# in this function it will read all lines from a file and return a list of string
# APPEND 
# we pass 'a' in append
# syn 
# var=open('path/filr location','a')
# in appen we have two operation (it add lines without over writing)
# 1.write
# 2.writelines()
g=open("hehe.txt",'a')
g.write('\n hehehehehehehehehe\nphewwwwwwwwwwwwwwwwwwwwwwwwwww\nyeyyyyyyyyyyyyyyyyyy\nlalalalalalalalalalalalalalalalalalalalalalalalalalalalala')
g.close
# append mode is almost similar to write mode but if file is alread exsist then the controler will add new data in exsisting data without overwriting
# w+,r+,wb,rb,X,a+ research on these
# tell()
g=open("hehe.txt",'w')
print(g.tell()) #it tells you about position of cursor or pointer 
# seek()
g.seek(5)
print(g.tell())
g.write(' hehehehehehehehehe\nphewwwwwwwwwwwwwwwwwwwwwwwwwww\nyeyyyyyyyyyyyyyyyyyy\nlalalalalalalalalalalalalalalalalalalalalalalalalalalalala')
g.close()