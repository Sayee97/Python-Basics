import re
phone=re.compile(r'\+91?\d\d\d\d')
mo=phone.search('The number is +911234')
print(mo.group())
