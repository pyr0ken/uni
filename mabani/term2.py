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
        print('item amount increase successfully !')
    else:
        my_items[item] = {
            "price": 0.0,
            "number": amount,
        }
        print('item added successfully !')
    print(my_items)
    
sell_item('apple', 10)
# output: 50

restock_item('banana', 20)
# output:
# item added successfully !
# {'apple': {'price': 5, 'number': 10}, 'banana': {'price': 0.0, 'number': 20}}موجودی کالا با موفقیت افزایش یافت.