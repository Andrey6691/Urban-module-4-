from fake_math import divide as divide_1
from true_math import divide as divide_2



result1 = divide_1(9, 3)
result2 = divide_1(3, 0)
result3 = divide_2(9, 3)
result4 = divide_2(9, 0)
print(result1)
print(result2)
print(result3)
print(result4)