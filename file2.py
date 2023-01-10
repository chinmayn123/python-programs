# extend function
n1=[1,2,3]
n2=[4,5,6]
n3=n1+n2
print(n3)

n1.extend(n2)
print(n1)

n2.extend(n1)
print(n2)



#inoperator
mylist3=[34,"apple","true",45,"cheery"]
print("apple"in mylist3)
print("taran"in mylist3)

#not operator
print("apple"not in mylist3)
print("taran"not in mylist3)


#nested list
college=["btech","bca",["mca","bba","hotelmanagment"],["taran","ramya","santosh","pallavi"]]
print(college[1])
print(college[2])
print(college[2][1])
print(college[2][2])
print(college[2][2][5])
