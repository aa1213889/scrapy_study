from lxml import etree

# etree.parse 读取本地文件
# 注意： 读取的html文件 meta等标签都必须有闭标签


html = etree.parse('./src/xpath/test.html')
print(html)  # <lxml.etree._ElementTree object at 0x000002699A363B40>


# text() 获取标签里的内容('//body/xx/yy/text()')

# 路径查询 //x --- 查找所有x节点
# //body/x --- 查找body标签里的 儿子节点x   孙子节点及以下则找不到
li_list = html.xpath('//body/ul/li/text()')
print(li_list)
#['BeiJing', 'Toronto', 'Havana', 'Moscow', 'Capetown', 'Cairo']


# 谓词查询 查找所有有x属性的y标签 y[@x]
# //body//div[@id]   查找body标签的 div子节点 且有 id属性的标签
# 同理 [@id] 可以换为 [@class] 等
attr_list = html.xpath('//body//div[@id]/text()')
print(attr_list)  # ['233', '2334']


# 谓词查询 查找class = h1-title的标签的内容
h1_list = html.xpath('//body/h1[@class="h1-title"]/text()')
print(h1_list)  # ['Title1']


# 属性查询 获取指定标签x的属性值y   x/@y
lable_list = html.xpath('//body/div[@id="container1"]/@name')
print(lable_list)  # ['text']


# 模糊查询 比如查询h1 标签中 class包含了 字符 '-title' 的标签
# x[contains(@属性."模糊内容")]
fuzzy_list = html.xpath('//body/h1[contains(@class,"-title")]/@class')
print(fuzzy_list)  # ['h1-title', 'h1-title2']


# 模糊查询 查询id的值以'C'开头的标签
# x[starts-with(@属性."开头内容")]
start_list = html.xpath('//body/ul/li[starts-with(@id,"C")]/text()')
print(start_list)  # ['Capetown', 'Cairo']

# 逻辑运算 与  and
# 查询div标签 id模糊为"container" 且 name属性为"text" 的标签id
and_list = html.xpath(
    '//body/div[contains(@id,"container") and @name="text" ]/@id')
print(and_list)  # ['container1']

# 逻辑运算 或 |
# 查询div标签或h1标签
or_list = html.xpath('//body/div/text() | //body/h1/text()')
print(or_list)  # ['233', '2334', 'Title1', 'Title2']
