####################################################################
def inttoroam(num):
    hashnum={1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
    result=''
    i=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    p=0
    while num:
        if num >= i[p]:
            num = num - i[p]
            result = result + hashnum[i[p]]
        else:
            p=p+1
    return result
####################################################################
a=19
result=inttoroam(a)

