list1 = [[10,20,30,40], 
         [40,522,33,44], 
         [90,45,21,11]]

# ans = [10,20,30,40,40,522,33,44,.....]


list2 = [10,20,30,40,50,60,70]

# ans =  [(10,), (10,20), (10,20,30), (10,20,30,40), (10,20,30,40,50) .....]
# ans1 = [[10,10], [10,20], [10,30], [10,40], [10,50]....]


import re
 
string = "GeeksforGeeks"
# vowels = r'[aeiouAEIOU]'
# count = re.findall(vowels, string)
# print(count)


vowels = r'[aeiouAEIOU]'
count = len(re.findall(vowels, string))
print(count)