import sys
if __name__ == '__main__':
    ans =''
    n = int(sys.stdin.readline().strip())
    a = sys.stdin.readline().strip()
    line = a.split()
    for i in range(n):
        ans=ans+str(n+1-int(line[i]))+' '
    print(ans[0:2*n-1])











