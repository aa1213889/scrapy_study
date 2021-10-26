# open( filePath , mode )
# filePath：路径 可以绝对路径和相对路径
# mode: w 可写   r 可读   a 追加  r 读取数据
f = open('file/test.txt', 'w')

# write( 内容 )
f.write('hello world\n')

# close() 文件的进程关闭 不然会一直存在内存
f.close()

# mode: a 追加数据
fa = open('file/test.txt', 'a')
fa.write('i am append data\n' * 5)
fa.close()

# read() 读取文件类容
fr = open('file/test.txt', 'r')
content = fr.read()
print(content)
