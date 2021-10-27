'''
try:
    可能会出现异常的代码
except 异常的类型:
    友好的提示
'''
try:
    fr = open('abc.txt', 'r')
    fr.read()
except FileNotFoundError:
    print('file not found')
