# # def prime(num):
# #     if num <= 1:
# #         print("Not Prime")
# #         return False

# #     for i in range(2, num):
# #         if num % i == 0:
# #             print("Not Prime")
# #             return False

# #     print("Prime")
# #     return True


# # n = int(input("Enter a number: "))
# # prime(n)     # Function call


# def calculator(a, b):
#     print("Sum", a + b)

# calculator(10, 20)



electricity_bill = int(input("Enter the electricity bill amount: "))
if electricity_bill <= 1000:
    bill = electricity_bill * 5
elif electricity_bill <= 2000:
    bill = electricity_bill * 8
else:
    bill = electricity_bill * 10

print("Total bill:", bill)
