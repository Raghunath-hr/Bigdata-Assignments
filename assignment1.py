#To find the factorial for any num

def find_factorial():
	n = int(input())
	print(type(n))
	a = 1

	for i in range(1, n+1):
		a = a*i

	print(a)

# find_factorial()

#check is the number is prime or not
def find_prime():
	# all_num = list(range(1,100))
	# print(type(all_num))
	int_input = int(input())
	for i in range(2, int_input):
		# print(all_num)
		if int_input % i == 0:
			
			print("this is not prime num")
			break

		else:
			print("this is prime num")
			break
	if int_input == 0 or int_input == 1:
		print("enter num greater than 1")

# find_prime()


#find num if cube of all digits matches the whole num

def find_armstrong():

	user_input = int(input())
	print(type(user_input))
	res = [int(x) for x in str(user_input)]
	print(res)
	print(type(res))
	total = 0

	for i in res:
		c = i*i*i
		print(c)
		print("_____")
		total += c
	print(total)
	if total == user_input:
		print("match found")
	else:
		print("Not armstrong ")

# find_armstrong()

def find_fibonacci(a):

	start = 0
	end = 1

	for i in range(2,a+1):
		calc = start+end
		start  = end
		end =  calc
	return end

# print(f'12th fab num:', find_fibonacci(12))

#Interchange first and last element from given list
def interchange_ele():
	a = list(map(int, input("enter nums: ").strip().split(',')))
	print(a)
	n = a[0]
	m = a[-1]
	a[0] = m
	a[-1] = n
	print(a)
	print("_________")

#From google
	new_list = list(map(int, input().strip().split()))
	start, *middle, end = new_list
	new_list = [end, *middle, start]

	print(f'This is new list by user: ', new_list)

# interchange_ele()


#swap elements from list
def swap_ele():
	list_input = list(map(int, input("specify nums").strip().split()))
	print(list_input)
	a = int(input("enter 1st ele: " ))
	b = int(input("enter 2nd ele: " ))

	ind_1 = list_input.index(a)
	
	ind_2 = list_input.index(b)

	list_input[ind_1], list_input[ind_2] = list_input[ind_2], list_input[ind_1]
	print(list_input)

# swap_ele()

#to find the largest element from list
def find_largest():
	list_input = list(map(int, input("enter list vals: " ).strip().split()))

	list_input.sort()
	print("biggest ele in this list is: ", list_input[-1])

# find_largest()


# cumulative sum of the list nums
def cumulative_sum(list_input):
	# list_input = list(map(int, input("enter your nums: ").strip().split()))

	total = 0
	total_list = []

	for i in list_input:
		total = total + i
		total_list.append(total)
	print(total_list)

# cumulative_sum(list(map(int, input("enter your nums: ").strip().split())))

#check word is palindrome or not
def palindrome_word():
	word = input("enter word to check: ", )
	print(type(word))
	reverse = word[::-1]
	if reverse == word:
		print("PLAINDROME")

	else:
		print("not found")
# palindrome_word()


#to remove num at specified index

# word = input("enter word: ")
def remove_alpha(num):
	print(num)
	remove_ip = int(input("give index to remove alpha: ", ))
	replace_word = num[remove_ip]
	print(replace_word)
	res_str = num.replace(replace_word, 'G')
	print(res_str)

# remove_alpha(word)

#check substring is present in main str 

def check_substr(str1):
	user_ip = input("str to find: ")
	print(user_ip in str1)

# check_substr(word) #line 150 input

def extract_unique():
	my_dict = {'1':"Raghu", '2':"sachin", '3':"Raghu"}

	print("dict_keys: ", my_dict.keys())
	print("dict vals: ", my_dict.values())
	print("dict items: ", my_dict.items()) # this will return tuple
	print(my_dict['1'])

	val_list = []
	for i in my_dict.values():
		val_list.extend(my_dict[i])
	val_list = list(set(val_list))
	print(val_list)
# extract_unique()

#Merge two dicts
def merge_dicts():
	dict1 = {1:10, 2:20, 3:30}
	dict2 = {4:40, 5:50, 6:60}

	dict1.update(dict2)

	print(dict1)

	dict3 = {  'Rahul': 4, 'Ram': 9, 'Jayant' : 10 }
	dict4 = {  'Jonas': 4, 'Niel': 9, 'Patel' : 10 }
	dict5 = {  'John': 8, 'Naveen': 11, 'Ravi' : 15}

	print("Merge using **kwargs")
	'''keyword arguments (**kwargs) also allows you to merge
		two or more dicts
	'''
	merged_dict = {**dict1, **dict2, **dict3, **dict4, **dict5}
	print(merged_dict)
# merge_dicts()

def list_tup_into_dict():
	new_dict = {}
	input_list = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
	for i in input_list:
		# print(i)
		# print(type(i))
		dict_key = i[0]
		dict_val = i[1]
		# new_dict = {}
		print("_______")
		if dict_key and dict_val: 
			new_dict[dict_key] = dict_val
	print(new_dict)

# list_tup_into_dict()


def list_of_tup():
	ip_list = [9, 5, 6]
	new_tup = []

	for i in ip_list:
		a = i
		b = i*i*i
		tup = (a, b)
		print(type(tup))
		new_tup.append(tup)
	print(new_tup)
	print(type(new_tup))
# list_of_tup()

def combinations_tuple():
	tup1 = (7,2)
	tup2 = (7,8)

	tup3 = [(a,b) for a in tup1 for b in tup2]
	tup4 = [(a,b) for b in tup1 for a in tup2]
	# print(tup3)
	# print(tup4)
	final_tup = tup3 + tup4
	final_tup = set(final_tup)
	print(final_tup)
# combinations_tuple()


def sort_tuple():
	tup = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
	sorted_tup = (sorted(tup, key = lambda x: x[1]))
	print(sorted_tup)
# sort_tuple()

#Python pattern programming

def left_triangle():
	star = 5
	for i in range(1, star+1):
		for j in range(1, i+1):
			print("*", end='')
		print()

# star = int(input())
# left_triangle()


def right_triangle():
	star = 5
	for i in range(star):

		for j in range(1, star-i):
			print(" ", end="")
		for k in range(0, i+1):
			print("*", end='')
		print()
# right_triangle()

def pyramid():
	n = 5
	for i in range(n):
		for j in range(n - i - 1):
			print(" ", end='')
		for j in range(2*i +1):
			print("*", end='')
		print()
# pyramid()

def right_triangle_num():
	n = 5
	# num = 1
	for i in range(0,n):
	 	num = 11
	 	for j in range(0, i+1):
	 		print(num, end=' ')

	 		num = num+1

	 	print()
# right_triangle_num()

def alpha_triangle():
	n = 5
	for i in range(n):
		for j in range(i+1):
			print(chr(j + 65), end=" ")
		print()
alpha_triangle()
