import json

fw = open('file/name.txt', 'w')
name_list = ['zhangsan', 'lisi']

# json.dumps() 序列化
names = json.dumps(name_list)  # 变成了字符串
fw.write(names)

fw.close()

# json.dump(name_list,fq) 等同于 names = json.dumps(name_list) + fw.write(names)

#---------------#

# json.loads 反序列化
fr = open('file/name.txt', 'r')
content = fr.read()
print(content)  # str类型
result = json.loads(content)
print(result)  # list类型

# json.load(fq) 等同于 content = fr.read() + json.loads(content)
