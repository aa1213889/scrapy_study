import json
import jsonpath

data = json.load(open('./src/jsonpath/data.json', 'r', encoding='utf8'))

author_list = jsonpath.jsonpath(data, '$.store.book[*].author')

print(author_list)
#['Nigel Rees', 'Evelyn Waugh', 'Herman Melville', 'J. R. R. Tolkien']
