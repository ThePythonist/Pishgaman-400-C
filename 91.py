# content = input("Content : ")
# output = f'<p>{content}</p>'
#
# open('home.html','w').write(output)
# print('Done')

content = input("Content : ")
tag = input("Tag : ")
output = f'<{tag}>{content}</{tag}>'

open('home.html','w').write(output)
print('Done')
