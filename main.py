txt=input("enter email address")
print(txt)
x=txt.replace(".","[DOT]").replace('@', '[AT]')
print(x)
txt2=x.replace('[DOT]','.').replace('[AT]','@')

print(txt2)