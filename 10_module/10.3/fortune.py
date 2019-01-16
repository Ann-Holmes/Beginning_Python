#  骰子结果的分布研究
from random import randrange
from matplotlib import pyplot as plt

#  输入本局的骰子数和骰子的面数
num = int(input("How many dice?"))
sides = int(input("Howm many sides per die?"))


#  产生结果的函数
def result_dices(num, sides):
    sum = 0
    for i in range(num):
        sum += randrange(1, sides + 1)
    return sum


#  模拟1000次, 可以认为遍历到所有的情况
fortunes = []
for i in range(100000):
    fortunes.append(result_dices(num, sides))
print(fortunes)
#  保留所有可能的情况, 去掉重复
all_fortunes = set(fortunes)
all_fortunes = list(all_fortunes)
print(all_fortunes)
#  统计每一种情况出现的频率
frequency_fortunes = {}
for i in all_fortunes:
    frequency_fortunes.update({i:fortunes.count(i)})
print(frequency_fortunes)
#  画出频率分布图
plt.axis([0, 45, 0, 10000])
plt.scatter(frequency_fortunes.keys(), frequency_fortunes.values(), linewidths=1)
plt.xlabel('results')
plt.ylabel('frequency')
plt.title('Number: {}, Sides: {}'.format(num, sides))
plt.show()
