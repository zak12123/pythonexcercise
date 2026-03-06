#string indexing
#text = 'python'
#text = text [::-1]
#print (text)
#email slicer
email = input('Enter your email')
Index = email.index('@')
username = email[:Index]
domain = email [Index:]
print (f'Your username is {username} and yor domain is {domain} ')