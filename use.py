a= "python"
txt=a.replace('p','R')
name='ram'
y=name.maketrans('rm','RM')
b=slice(0,2)
c=slice(2,4)
d=slice(4,5)
e=slice(5,6)
print(name.translate(y))
print(txt[b]+txt[c].upper()+txt[d]+txt[e].upper())


c='adrien'
print(c.capitalize())
d='adrien shrestha'
print(d.title())
e='adrien shrestha'
print(e.upper())
f='AdrIen ShrEsthA'
print(f.lower())
g='AdrIen shrestha'
print(g.swapcase())
h='adrien shrestha'
print(h.islower())
i='adrien shrestha'
print(i.istitle())
j='adrien shrestha'
print(j.isalpha())
k='adrienshrestha1'
print(k.isalnum())
l='69'
print(l.isdigit())
m='  '
print(m.isspace())
n='adrien shrestha\n'
print(n.isprintable())
o='adrien_shrestha'
print(o.isidentifier())
p='adrien'
print(p.center(7))
q='*programming'
r=q.center(14,'*')
s='*'+r[0:13]
print(s)
t='programming'
print(t.ljust(15,'*'))
u='programming'
print(u.rjust(15,'*'))
v='programming'
print(v.count('g'))
w='python\tprogramming'.expandtabs(tabsize=6)
print(w)
x='programming'
print(x.rfind('o'))
print(x.rindex('o'))
print(x.zfill(15))
print(x.startswith('p'))
print(x.endswith('n'))




a='python'
print('a ')

