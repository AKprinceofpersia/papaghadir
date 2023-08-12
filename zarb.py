print("Be barname jadval zarb khosh omadid")

fnum = int(input("addad aval ra vared konid: "))
snum = int(input("addad dovom ra vared konid: "))
def table(x,y) :
    for i in range(x+1):
        if (i+1) != (x+1) :
            print((i), end=" ")
        else :
            print((i), end="\n")
    zarb = 1
    for n in range(y):
        print((n+1),end=" ")
        for l in range(x):
            if (l+1) != x :
                print((l+1)*zarb, end=" ")
            else :
                print((l+1)*zarb, end="\n")
        zarb += 1

table(fnum,snum)