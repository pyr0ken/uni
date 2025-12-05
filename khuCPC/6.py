
MAX_LEN = 2001
C = [[0] * MAX_LEN for _ in range(MAX_LEN)]

def precompute_combinations():
    for i in range(MAX_LEN):
        C[i][0] = 1  
        for j in range(1, i + 1):
            C[i][j] = C[i-1][j-1] + C[i-1][j]

def main():
    n = int(input())
    s = input().strip()

    current_I = 0
    current_O = 0
    for char in s:
        if char == 'I':
            current_I += 1
        else:
            current_O += 1
        
        if current_O > current_I:
            print(0)
            return

    remaining_I = n - current_I
    remaining_O = n - current_O

    if remaining_I < 0 or remaining_O < 0 or remaining_O < remaining_I:
        print(0)
        return

    total_remaining = remaining_I + remaining_O
    
    total_paths = C[total_remaining][remaining_I]
    
    invalid_paths = 0
    if remaining_I > 0:
        invalid_paths = C[total_remaining][remaining_I - 1]

    result = total_paths - invalid_paths
    print(result)

precompute_combinations()
main()
