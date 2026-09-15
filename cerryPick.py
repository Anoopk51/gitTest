try:
   
    result = "11" + 2
except TypeError:
    print("Enter a valid input")



stu = ["Ajeet","Rahul","Harshit"]
try:
    result = stu[len(stu)]
except IndexError:
    print("Index out bound.")