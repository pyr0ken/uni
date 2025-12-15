def draw_tree():
    # گرفتن نام دانش‌آموز
    name = input("Enter your first and last name: ")
    
    # گرفتن ابعاد درخت (4 عدد: ارتفاع شاخه، ارتفاع تنه، عرض تنه، ارتفاع گلدان)
    branch_h, trunk_h, trunk_w, pot_h = map(int, input("Enter tree dimensions (branch height, trunk height, trunk width, pot height): ").split())
    
    # محاسبه عرض شاخه و گلدان
    branch_w = trunk_w * 2 - 1
    pot_w = max(len(name) + 2, trunk_w + 4)
    
    # عرض کل
    total_w = max(branch_w, pot_w)
    
    print("\n...Drawing your tree...\n")
    
    # رسم شاخه‌ها
    for i in range(branch_h):
        stars = '*' * (i * 2 + 1)
        print(stars.center(total_w))
    
    # رسم تنه
    trunk = '|' * trunk_w
    for _ in range(trunk_h):
        print(trunk.center(total_w))
    
    # رسم گلدان
    top_bottom = '=' * pot_w
    print(top_bottom.center(total_w))‍
    
    middle = (pot_h - 1) // 2
    for i in range(pot_h):
        if i == middle:
            inner = name.center(pot_w - 2)
            print(('|' + inner + '|').center(total_w))
        else:
            inner = ' ' * (pot_w - 2)
            print(('|' + inner + '|').center(total_w))
    
    print(top_bottom.center(total_w))

draw_tree()