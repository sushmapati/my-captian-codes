import operator
def most_frequent():
    str=input("Please enter a string")
    d={}
    for i in str:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1;
    sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
    for i in sorted_d:
        print("{}={num:02d}".format(i,num=sorted_d[i]))
most_frequent()
