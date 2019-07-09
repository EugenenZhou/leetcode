####################################################################
def numtoenglish(num):
    if num == 0:
        return 'Zero'
    hashnum={1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9 : 'Nine',10:'Ten',
             11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
             17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',20: 'Twenty', 30: 'Thirty', 40: 'Forty',
             50: 'fifty', 60: 'sixty', 70: 'Seventy', 80: 'Eighty', 90: 'ninety', 100: 'Hundred',
             1000: 'Thousand',1000000:'Million',1000000000:'Billion'}
    result=''
    i=[1000000000, 1000000, 1000]
    p=0
    while num >= 1000:
        if num >= i[p]:
            set = num // i[p]
            h_set = set // 100
            if h_set != 0:
                result = result +' '+ hashnum[h_set] +' '+ hashnum[100]
            h_get = set % 100
            if h_get > 20:
                if h_get % 10 == 0:
                    result = result + ' ' + hashnum[h_get]
                else:
                    result = result + ' ' + hashnum[h_get - (h_get % 10)] + ' ' + hashnum[h_get % 10]
            elif h_get > 0:
                result = result +' '+ hashnum[h_get]
            result = result +' '+ hashnum[i[p]]
            num = num % i[p]
            p = p + 1
        else:
            p = p + 1
    if num // 100 != 0:
        result = result +' '+ hashnum[num // 100] +' '+ hashnum[100]
    num = num % 100
    if num > 20:
        if num % 10 == 0:
            result = result + ' ' + hashnum[num]
        else:
            result = result +' '+ hashnum[num-(num % 10)] +' '+ hashnum[num % 10]
    elif num > 0:
        result = result +' '+ hashnum[num]
    if result[0] == ' ':
        return result[1:]
    else:
        return result
####################################################################
a=0
result=numtoenglish(a)