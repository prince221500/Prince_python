# filter is just like map function but the diffrence is the map function function works on every 
# element of the sequence whereas 
#filter function worrks on only True values 
# for example -

l=list(map(int,input("enter the list  ").split()))
# def kshitiz(x):
#     if x%2==0:
#         return True
#     else:
#         return False

# ls=list(filter(kshitiz,l))
# print(*ls)

# using the lambda in terms of the def

f=lambda x :  True if x%2==0  else False
l1=list(filter(f,l))
print(l1)
