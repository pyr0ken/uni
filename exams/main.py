# Mini Project: Todo list
def get_data():
    print("****************************************************")
    print("1. add a new job ************** 2. exit")
    menu_num = int(input("Enter: "))
    return menu_num

def create_todo():
    title = input("Enter title: ")
    date = input("Enter date: ")
    status = input("Enter the status of job(done, doing): ")

    job = {
    'title': title,
    'date': date,
    'status': status,
    }

    todo.append(job)
    
    print(todo)
    
def main():
    while True:
        
        create_todo()
        get_data()
        
        if menu_num == 2: 
            break
        while menu_num not in [1,2]:
            print("****************************************************")
            menu = "1. add a new job ************** 2. exit"
            print(menu)    
            menu_num = int(input("Enter: ")) 


todo = []
menu_num = get_data()

if menu_num == 1:
    main()

# loops
for i in range(10):
    print(i)

x = 0
while x < 10:
    if x == 5:
        x = x + 1
        pass
    else:
        print(x)
        x = x + 1


# think python examples
text = "Hello"

def show_name(word):
    word_length = len(word)
    space_length = 40 - word_length
    print(space_length * " " + word)
    
show_name(text)


# str and list methods: reverse, clear, index, append, ....
# learn join
def get_letter(word):
    my_list = list(word) # ['H', 'e', 'l', 'l', 'o']
    
    # my_list.reverse()
    # my_list.clear()
    
    print(my_list)
    
    # new_string = "".join()
    # print(new_string)
    
get_letter("Hello")


# talking about variables and class
# method need call after a point: str.method(), list.method() => my_str.upper(), my_list.append()
# function need call: print(), input(), len()
name = 'ali'
age = 19
a = 123.32423
my_list = ['ali', 'ali']
print(my_list.index('ali'))
print()
list.append()


# SAYAD OFFICINAL quiz :)))))


### basic patterns
num = '256'
for i in num:
    print(int(num) * "*")


### professional patterns 
a = input("Enter number: ")
def get_digits(num):
    my_list = list(num)
    my_list.reverse()
    my_num_str = "".join(my_list)
    my_num_int = int(my_num_str)
    
    if len(my_num_str) > 10:
        return None
    
    for i in range(len(my_num_str)):
        last_digit = my_num_int % 10
        my_num_int = my_num_int // 10
        print(last_digit)
        
get_digits(a)


# return statement and global keyword
# using a variable from outside of a function inside the function
def a():
    global name
    name = "aziz"
    return name
    
def b():
    name = a()
    
    print(name)


# fibo: 0, 1, 1, 2, 3, 5, 8,
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fibo(n-1) + fibo(n-2)
    

print(fibo(10))




# pass: every statement that does nothing
# continue: skip the current iteration of a loop and go to the next iteration
# break: exit the loop completely

i = 0
while i < 10:
    print("Hello") 
    i += 1
    
    if i == 5:
        break
