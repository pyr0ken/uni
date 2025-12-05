letter = input()

def main(letter: str):
    list_1 = []
    for i in letter:
        list_1.append(i) 
    
    list_1.reverse()
    
    text: str = ""
    
    for i in list_1:
        text += i    
    
    return text

print(main(letter))
