# prime function

def prime(num):
    if num <= 1:
        print("Not Prime")
        return False

    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            return False

    print("Prime")
    return True

num = int(input("Enter a number: "))
prime(num)