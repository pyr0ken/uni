
n = int(input())
a = list(map(int, input().split()))

required_t = 0
carry = 0

for i in range(n):
    current_load = a[i] + carry
    
    toilets_remaining = n - i + 1
    current_min_t = (current_load + toilets_remaining - 1) // toilets_remaining
    required_t = max(required_t, current_min_t)
    carry = max(0, current_load - required_t)

required_t = max(required_t, carry)

print(required_t)

