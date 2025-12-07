# Q1
def is_palindrome(word):
    word_list = []
    for i in word:
        word_list.append(i)
    reverse_word_list = word_list[::-1]
    if word_list == reverse_word_list:
        return True
    else:
        return False

def count_palindromes(words):
    palindromes_word = 0
    for word in words:
        if is_palindrome(word):
            palindromes_word += 1
    return palindromes_word

def longest_word(words):
    my_dict = {}
    for i in words:
        my_dict[i] = len(i)
        
    my_dict_values = []
    for key, value in my_dict.items():
        my_dict_values.append(value)
    
    longest_words = []
    for key, value in my_dict.items():
        if value == max(my_dict_values):
            longest_words.append(key)
    
    return max(my_dict_values), longest_words

words = ["level", "apple", "radar", "banana", "civic", "python"]

print(count_palindromes(words))
# output: 3

print(longest_word(words))
# output: (6, ['banana', 'python'])


# Q2
my_items = {
    "apple": {
        "price": 5,
        "number": 20,
    }
}

def sell_item(item, amount):
    get_item = my_items.get(item)
    
    if get_item == None:
        print('کالای مورد نظر وجود ندارد')
    elif get_item['number'] < amount:
        print('موجودی کالا کافی نیست') 
    
    get_item['number'] -= amount
    print(get_item['price'] * amount)

def restock_item(item, amount):
    get_item = my_items.get(item)
    
    if get_item != None:
        get_item['number'] += amount
        print('موجودی کالا با موفقیت افزایش یافت.')
    else:
        my_items[item] = {
            "price": 0.0,
            "number": amount,
        }
        print('موجودی کالا با موفقیت افزایش یافت.')
    print(my_items)
    
sell_item('apple', 10)
# output: 50

restock_item('banana', 20)
# output:
# موجودی کالا با موفقیت افزایش یافت.
# {'apple': {'price': 5, 'number': 10}, 'banana': {'price': 0.0, 'number': 20}}