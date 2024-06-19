##nested loop
# softwarica_building=['Floor1','Floor2']
# room=[1,2,3]
# for i in softwarica_building:
    
#     for j in room:
#         if i=='Floor2':
#             if j==1 or j==3:
#                 continue
#             print(j)
#             break


# a=[1,2,3]
# a.apend(5)
# print (a)
# a.extend ([5])
# print (a)

a={1,2,3,4}
# a.pop(0)
a.discard(1)
a.remove(2)
print (a)

a={1,2,3}
b={3,2,8}
c=a^b
print(c)
