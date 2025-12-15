
def get_number_one_by_on(num: int):
    if num > 9999999999:
        return None
    
    number_length = len(str(num))

    for _ in range(number_length):
        num = int(num)
        
        a = num % 10
        num = num // 10
        
        print(f'{a}: {a*"*"}')

num = int(input("Enter a number: "))
get_number_one_by_on(num)
