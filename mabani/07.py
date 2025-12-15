def is_prime (num):
    list_num = [True] * num
    list_num[0] = list_num[1] = False
    for i in range(int(num**0.5)):
        if list_num[i]:
            for i in range(i*i,num , i):
                list_num[i] = False
    return([i for i , y in enumerate(list_num) if y ])
print(is_prime(1_000_000_00))
