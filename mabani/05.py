def histogram_of_digits():
    """
    print the histogram of digits with start
    """
    print(num)
    
    for digit in num:
        print(f"{digit}: {"*" * int(digit)}")

def check_digit_count_even_or_odd():
    """
    return the digits counts is even or odd 
    """
    return "even" if len(num) % 2 == 0 else "odd"


num = input("enter num: ") # input result class is str in python

if len(num) >= 10:
    print("plz enter valid num")
else:
    try:
        histogram_of_digits()
    
        digits_status = check_digit_count_even_or_odd()
        number_status = "even" if int(num) % 2 == 0 else "odd"

        print(f"digits odd or even: {digits_status} , input number even or odd: {number_status}")

        # check the digits status and number status is equal and print the message
        if digits_status == number_status:
            print("Blast off")
    except:
        print("Error: the program exit with 0 code")
