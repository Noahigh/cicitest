"""
敏感词汇筛选
找出敏感词汇，并反馈
"""
file_url = r'text_test\filtered.txt'

st_string = []
rs = ''
with open(file_url) as file_object:
	lines = file_object.readlines()
	for line in lines:
		rs += line

		if('\n' in rs):
			st_string.append(rs.rstrip())
			rs = ''


print(st_string)

'''单个词的判断'''
abc = input('Please input a word: ')

if(abc in st_string):
        print('Freedom')
else:
        print('Human Rights')

fgh = input('Please input a word: ')
'''语句判断'''
for value in st_string:
        if(value in fgh):
            print('freedom')
        else:
            print('human rights')
            
