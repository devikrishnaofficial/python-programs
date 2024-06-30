def reverse_digits(n):
    return int(str(n)[::-1])

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_and_add_until_palindrome(n):
    original_number = n
    while True:
        reversed_number = reverse_digits(original_number)
        sum_number = original_number + reversed_number
        print(f"{original_number} + {reversed_number} = {sum_number}")
        if is_palindrome(sum_number):
            print(f"{sum_number} is a palindrome.")
            break
        else:
            print(f"{sum_number} is not a palindrome. Repeating...")
            original_number = sum_number

number = 123
reverse_and_add_until_palindrome(number)
