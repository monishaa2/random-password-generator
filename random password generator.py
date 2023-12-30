import random
import string

x = int(input("specify the number of letters: "))
y = int(input("specify the number of numbers: "))
z = int(input("specify the number of symbols: "))
rand_list = []

for i in range(y):
    rand_list.append(str(random.randint(0, 9)))

for i in range(x):
    rand_list.append(random.choice(string.ascii_letters))

for i in range(z):
    rand_list.append(random.choice(string.punctuation))

random.shuffle(rand_list)
password_1 = ''.join(rand_list)
print("The password is:", password_1)
