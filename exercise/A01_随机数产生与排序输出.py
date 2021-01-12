import random
num_list = [random.randint(1,100) for i in range(10)]
num_list.sort(reverse=True)
print(num_list)
