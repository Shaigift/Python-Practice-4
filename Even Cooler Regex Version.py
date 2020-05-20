From, stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

import  re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)', lin)
print(y)


## From - Starting at the beginning of the line, look for the string 'From'


