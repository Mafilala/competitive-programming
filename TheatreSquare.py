import math
input_list = input().split(" ")
m, n, a = map(int , input_list)
l = math.ceil(m / a)
w = math.ceil(n / a)
print(l * w)
