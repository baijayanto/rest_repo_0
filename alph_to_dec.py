
L = {"a":"1","b":"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8","i":"9","j":"10","k":"11","l":"12","m":"13","n":"14","o":"15","p":"16","q":"17","r":"18","s":"19","t":"20","u":"21","v":"22","w":"23","x":"24","y":"25","z":"26"}
m=int(input("enter how many alphabets you want to enter \n"))
sum=0
for i in range (1,m+1,+1):
    n=input("enter alphas : \n")
    b = int(L[n])
    for j in range (m-1,0,-1):
        s=b*pow(26,j)
        sum=s+sum
print(sum)
