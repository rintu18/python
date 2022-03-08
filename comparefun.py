def comapre(str1,str2,n):
    count=0
    for i in range(0,n):
        if str1[i]==str2[i]:
            count=count+1

    if count==n:
        return True
    else:
        return False



