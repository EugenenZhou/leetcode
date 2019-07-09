####################################################################
def roamtoint(roamstr):
    roamhash={'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}
    result=0
    for i in range(len(roamstr)):
        if i ==len(roamstr)-1:
            result=result+roamhash[roamstr[i]]
        else:
            if roamhash[roamstr[i]] >= roamhash[roamstr[i+1]]:
                result=result+roamhash[roamstr[i]]
            else:
                result = result - roamhash[roamstr[i]]
    return result
####################################################################
a='IX'
result=roamtoint(a)
d={'z':1}

# sum(d.get(a[max(i-1,0):i+1],d[n]) for i,n in enumerate(a))