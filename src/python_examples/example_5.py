# Q1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print("Q1")
print(cal.value)



# Q2
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100


cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
cal.add(60) # 60 더하기

print("Q2")
print(cal.value) # 100 출력


# Q3
print("Q3")
print(all([1, 2, abs(-3)-3]))
print(chr(ord('a')) == 'a')


# Q4
nums = [1, -2, 3, -5, 8, -3]
filtered_nums = filter(lambda num: num >= 0, nums)
print("Q4")
print(list(filtered_nums))


# Q5
nums = [1, 2, 3, 4]
mapped = map(lambda num: num*3, nums)
print("Q5")
print(list(mapped))