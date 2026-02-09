'''
# 1
result = [n * n for n in range(1,5)]
print(result)

# 2 
nums = [3,5,10,15,20,25,30]
evens = [n for n in nums if n % 2==0]
print(evens)

# 3
names = ["dan", "sara","noa"]
upper_names = [name.upper() for name in names]
print(upper_names)

# 4
nums = [20,55,70,10,90]
result = [num/2 for num in nums if num > 50]

# 5
words = ["hi", "python","is","awsome"]
lengths = [w for w in words if len(w)>2]

# 6 
squares = []
for i in range(10):
    squares.append(i*i)
print(squares)

# 7
evens = []
for i in range(50):
    if i % 2==0:
        evens.append(i)

# 8
names = ["Alice","Bob","Charlie"]
first_letters = []
for name in names:
    first_letters.append(name[0])

# 9
num = [123,34,4,456,235,324,23,54,657]
small_nums = []
for num in nums:
    if num < 100:
        small_nums.append(num)

# 10
nums = [123,34,4,456,235,324,23,54,657]
modified =[]
for num in nums:
    if num > 10:
        modified.append(num+5)
    else:
        modified.append(num)

# 11
mult_list = []
for num in range(1,20):
    mult_list.append(num*3)

mult_list = [num*3 for num in range(1,20)]

# 12
nums = [123,34,4,456,235,324,23,54,657]
new_list = []
for num in nums:
    if num % 5 ==0:
        new_list.append(num)

new_list = [num for num in nums if num % 5 ==0]

# 13
words = ["hesd","gsufd","suufh","su"]

#14
select_square_numbers = [i*i for i in range(1,30) if i%3==0]

#15
even_nums =[num for num in range(1,15) if num%2==0]

#16
temp_list = [34,14,56,0,22]
temp = ["hot" if temp>30 else "ok" if 20<temp<30 else "cold" for temp in temp_list]

#17
first_names = ["Dan","Noa","Yossi"]
last_names = ["Levi", "Cohen", "Mizrahi"]
combined_list = [f+" "+l for f,l in zip(first_names,last_names)]

#18
first_coordinates = [(0,0),(0,1),(0,2)]
second_coordinates = [(1,0),(1,1),(1,2)]
combined_coordinates = [(f[0]+s[0],f[1]+s[1]) for f,s in zip(first_coordinates,second_coordinates)]

#19
special_list = [(a,b) for a in range(1,10) for b in range(1,10) if (a+b)%4==0]
'''
#20
users = [{"name": "Dan","age": 17},{"name": "Noa","age":25},{"name":"Yossi","age":15},{"name":"Maya","age":31}]
over_eighteen = [user for user in users if user["age"]>=18]
print(over_eighteen)