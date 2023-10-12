#list1=[1,2,3,4]
#expected output:-[1,4,9,16]

list1=[1,2,3,4]
out=[]
for i in list1:
  a=i**2
  out.append(a)
print(out)
