def palindrome(a):
    if a==a[::-1]:
        print(True)
    else:
        print(False)
palindrome(a = input("Enter the desirable number: "))