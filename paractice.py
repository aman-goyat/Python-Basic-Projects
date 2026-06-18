# # # # li = [1,2,43,4,5,6,7,8,9,"aman" , "goyat"]

# # # # print (li[4:9])

# # # # print (li[4:12])
# # # # print (li[4:9:3])
# # # # print (li[4:9:1])
# # # # print (li[-4])
# # # # print (li[-8:-2])
# # # # print (li[:-1])
# # # # print (li[-8:-2:1])
# # # # print (li[-8])





# # # #string

# # # s = "hey ,am aman goyat , i am pursuing btech from siet"
# # # print (s[:20])
# # # print (s[12:51])
# # # print (s[12:51:2])



# # #forwhile loop

# # s = " i am doing python programming from pisoft"
# # for i in s:
# #     continue
# # print(i)
   

# # lis = [1,2,3,4,5,6,7,8,9]

# # for i in lis:
    
# #     if i == 4:
# #         break
# #     print(i)

# # def calculator():
# #     a = int(input("Enter the first number: "))
# #     b = int(input("Enter the second number: "))

# #     if a > b:
# #         print("SUm" , a + b)
# #         print("I am the best")
# #         print("Division", a / b)
# #     elif a < b:
# #         print("I am king")
# #         print("Subtraction", a - b)
# #         print("Multiplication", a * b)
# #     else:
# #         print("I am coder")

# # calculator()

# i = 1
# while i < 100:
#     if i % 4 == 0 and i % 6 == 0:
#         print(i)
#     i += 1


s = (input("enter the student name: "))
r = int(input("enter the student roll number: "))
m = int(input("enter the student marks: "))
sub1 = input("enter the student subject 1: ") 
sub2 = input("enter the student subject 2: ")
sub3 = input("enter the student subject 3: ")
sub4 = input("enter the student subject 4: ")
sub5 = input("enter the student subject 5: ")
sub6 = input("enter the student subject 6: ")
total_marks = int(input("enter the student total marks: "))
percentage = (total_marks / 600) * 100
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

print("Student Name:", s)
print("Roll Number:", r)
print("Marks:", m)
print("Subject 1:", sub1)
print("Subject 2:", sub2)
print("Subject 3:", sub3)
print("Subject 4:", sub4)
print("Subject 5:", sub5)
print("Subject 6:", sub6)
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)
if percentage >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")