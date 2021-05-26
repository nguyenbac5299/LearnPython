demo = '01234567'
demo[0]  # 0
demo[7]  # 7
# [start:stop:stepover]
demo[0:3]  # 012
demo[0:7:2]  # 0246
demo[-1]  # 7 if stop is nagative index =>is caculator from the end of string
demo[-2]  # 6
demo[0:7:-1]  # if stepover is negative index => reverse : 76543210
demo[::-2]  # 7531 default value start: end
print(demo[::-2])
# string is immutable
demo[0] = '1'  # error
