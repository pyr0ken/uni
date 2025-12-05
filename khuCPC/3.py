nums1 = input().split()
nums2 = input().split()
nums3 = input().split()

list1 = [int(nums1[0]), int(nums2[0]), int(nums3[0])]
list2 = [int(nums1[1]), int(nums2[1]), int(nums3[1])]

text1 = 0
text2 = 0

for i in list1:
    if list1.count(i) == 1:
        text1 = i

for i in list2:
    if list2.count(i) == 1:
        text2 = i

print(text1, text2)
