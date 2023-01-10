# rows = 6
# # if you want user to enter a number, uncomment the below line
# # rows = int(input('Enter the number of rows'))
# # outer loop
# for i in range(rows):
#     # nested loop
#     for j in range(i):
#         # display number
#         print(i, end=' ')
#      # new line after each row
#     print('')





# fd = open(filename,"w")
# input = raw_input("user input")
# fd.write(input)

# userinput = input("Enter: ")
#
# fd = open("chinmay.txt","w")
# fd.write(userinput)
# fd.close()

fd = open("chinmay.txt","a")
l1 = "My name is Chinamy Nijamkar\n"
l2 = "I have completed my Bsc IT from APSCN \n"
l3 = "Currenty persuing Python and AWS Course from Cloud Impact\n"
l4 = "My skills are Python, Aws\n"
l5 = "My hobbies are Playing games, listening music \n"
fd.writelines([l1, l2, l3, l4,l5])
fd.close()

c=open("chinmay.txt","r+")
c.write()
d=c.read()
print(d)