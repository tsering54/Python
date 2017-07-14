word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list=''

for i in word_list:
    if char in i:
        new_list += i

print list({new_list})
