s = 'SDAhpinokiohFDFD'
a = s.find('h')
b = s.rfind('h')
l = s[a+1:b]
print(s.replace(l,l[::-1]))
