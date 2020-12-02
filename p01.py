from bisect import bisect_left

f = open('input_01.txt', 'r')
w = [int(i) for i in f.readlines()]

[r1] = [i*j for i in w for j in w if (i+j) == 2020 and i<j]
[r2] = [i*j*k for i in w for j in w for k in w if (i+j+k) == 2020 and i<j<k]

print(r1)
print(r2)
