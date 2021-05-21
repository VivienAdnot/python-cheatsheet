# L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
# file1 = open("myfile.txt","w")
# file1.writelines(L)
# file1.close()
# file1 = open("myfile.txt","r+")
# print("Output of Read function is ")
# print(file1.read())
# print()
# file1.close()

# file1 = open("myfile.txt","w")
# file1.writeline("hello")
# file1.writeline("toto")
# file1.close()

with open("myfile.txt","w") as the_file:
  the_file.write("hello\n")
  the_file.write("toto\n")