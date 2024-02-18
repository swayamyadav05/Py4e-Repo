# The Double Split Pattern

# Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

words = line.split()
print(words)
email = words[1]
print(email)
pieces = email.split('@')
print(pieces[1])
