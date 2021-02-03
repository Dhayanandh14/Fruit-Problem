fruits = {
        'orange':50,
        'mango':40,
        'apple':30,
        'banana':20,
        'jackfruit':10,
        'watermelon':5
}
things={}
check = False
while not check:
    print("Enter stop to exit")
    item=input("Enter fruit or vegetable : ")
    if item != "stop":
       if item in fruits.keys():
         quan=int(input("Enter Quantity: "))
         things[item]=quan
       else:
         print("Invalid input")
    else:
       check=True
a=0
for i,j in things.items():
   a=a+fruits[i]*j
   print("fruit or vegetable Name: ",i)
   print("quantity: ",j)
   print("Rate: ",fruits[i]*j)
   print("Each fruit or vegetable: ",fruits[i])
print("Tot amount: ",a)

#    fruits = {
#         'Orange':50,
#         'Mango':40,
#         'Apple':30,
#         'Banana':20,
#         'Jackfruit':10,
#         'Watermelon':5
# }
# f=int(input("Enter Number Of Fruits: "))
# p=[]
# q=[]
# i=0
# while i<f:
#     item=input("Enter fruit: ")
#     quan=input("Enter Quantity: ")
#     p.append(item)
#     q.append(quan)
#     i=i+1
# j=0
# while j<f:
#     print("Fruit Name:",p[j]," ","Quantity:",q[j])
#     j=j+1

# for k in fruits.keys():
#    for l in range(0,f):
#         if p[l]==k:
#             print(p[l])
#             for s in range(0,f):
#                for v in fruits.values() :
#                    if q[s]==v:
#                       print("true")
