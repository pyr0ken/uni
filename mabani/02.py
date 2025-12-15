def show_full_name():
    first_name = input("enter first name: ")
    last_name = input("enter last name: ")
    full_name = first_name + ' ' + last_name

    first_name_length = len(first_name)
    last_name_length = len(last_name)
    full_name_length = len(full_name)

    print("Your first name is: ", first_name)
    print("Your first name length is: ", first_name_length)
    print("Your last name is: ", last_name)
    print("Your last name length is: ", last_name_length)
    print("Your full name is: ", full_name)
    print("Your full name length is: ", full_name_length)

def total_pay():
    hour = input("enter the hour: ")
    rate = input("enter the rate: ")
    
    try:
        hour = float(hour)
        rate = float(rate)
        print(hour * rate)
    except:
        print('plz just enter number!!!')
        total_pay()


show_full_name()
print("===================================================")        
total_pay()
