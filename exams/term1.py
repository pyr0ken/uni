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
