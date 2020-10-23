from numpy import zeros
def fib(N):
    table=zeros((1,N),dtype="uint32")
    return helper(N-1,table)

def helper(N,table):
    if N==0 or N==1:
        return 1
    elif table[0][N]!=0:
        return table[0][N]

    table[0][N]=helper(N-2,table)+helper(N-1,table)
    print(table[0][N],"\t")
    return table[0][N]

N=20
fib(N)