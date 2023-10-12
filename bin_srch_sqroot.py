def sqrt(n):
    low=1
    high=n//2

    while(low<=high):
        mid=low+(high-low)//2
        if(mid*mid==n):
            return mid
        if(mid*mid<n):
            low=mid+1
            ans=mid
        else:
            high=mid-1
    return ans

m=int(input("enter number you want to root"))
print(sqrt(m))