import re

f = open('input_02.txt', 'r')

def policy1(low, high, c, password):
        count = sum([1 for ch in password if ch==c])
        if low<=count<=high:
                return 1
        else:
                return 0

def policy2(low, high, c, password):
        return policy1(1, 1, c, password[low-1]+password[high-1])

def check_line(line, policy):
        o = re.search('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)', line)
        low = int(o.group(1))
        high = int(o.group(2))
        c = o.group(3)
        password = o.group(4)
        return policy(low, high, c, password)

lst = f.readlines()
r1 = sum([check_line(i, policy1) for i in lst])
r2 = sum([check_line(i, policy2) for i in lst])

print(r1)
print(r2)
