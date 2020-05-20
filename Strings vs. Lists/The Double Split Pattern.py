x = ['From', 'Stephen.marquard@uct.co.ac.za', 'Sat', 'Jan', 5, '09:14:16', 2008]

words = x.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

