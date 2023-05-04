def binary_search(list,element):
    mid=0
    lo=0
    hi=len(list)-1

    while(lo<=hi):
        mid=(int)((lo+hi)/2)

        if element==list[mid]:
            return mid
        elif element<list[mid]:
            hi=mid-1
        else:
            lo=mid+1
            
    return -1


my_arr=[]
size=int(input("Enter the size of the list : "))
for i in range(0,size):
    el=int(input(f"Enter the {i+1} th element : "))
    my_arr.append(el)

find_el=int(input("Enter the target element to be found : "))

res=binary_search(my_arr,find_el)
if res != -1:
   print ("Element is present at index "+str(res))
else:
   print ("Element is not present in array")