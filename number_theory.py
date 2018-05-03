
#is power of 2
def is_power_of_two(x):
    return x&(x-1)==0

#最大公约数
def gcd(a,b):
    # O(logmax(a,b))
    if b==0: return a
    return gcd(b,a%b)

# 求x,y 使得 ax+by=gcd(a,b)
d=gcd(a,b)
def extgcd(a,b,d):
    if b==0: return d/a,1
    x,y=extgcd(b,a%b)
    return y,x-int(a/b)*y

#最大公约数
def gcd(a,b):
    # O(logmax(a,b))
    if b==0: return a
    return gcd(b,a%b)
#最小公倍数 least common multiple
def lcm(a,b):
    return a*b//gcd(a,b)
def lcm(args):
    ret=lcm(args[0],args[1])
    for num in args[2:]:
        ret=lcm(ret,num)
    return ret 



# 最小互质 
#relative primes 

def rg(a,b):
    g = abs(gcd(a,b))
    assert g
    return a // g, b // g





#判定prime number
def is_prime(n):
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1 
    return n!=1 
def divisor(n):
    res=[]
    i=1
    while i*i<=n:
        if n%i==0:
            res.append(i)
            if i!=n/i: 
                res.append(n/i)
        i+=1
    return res
def prime_factor(n):
    res=[]
    i=2
    while i*i<=n:
        while n%i==0:
            res.append(i)
            n/=i
        i+=1 
    if n!=1: res.append(n)
    return res 

# Sieve of Eratosthenes
# 枚举n 以内素数 包括n 
# O(nloglogn) ~ O(n)
def sieve(n):
    is_prime=[True]*(n+1)
    is_prime[0]=False
    is_prime[1]=False
    limit=int(n**0.5)+1
    for i in range(2,limit):
        if is_prime[i]:
            j=2*i
            while j<=n:
                is_prime[j]=False
                j+=i
    return [i for i,val in enumerate(is_prime) if val]  
# 枚举 [a,b) 内素数
def segment_sieve(a,b):
    limit=int(b**0.5)
    prime_small=sieve(limit) 
    is_prime=[True]*(b-a)
    for i in prime_small:
        j=math.ceil(a/i)*i
        while j<b:
            is_prime[j-a]=False 
            j+=i 
    return [i+a for i,val in enumerate(is_prime) if val] 

# is carmicheal number
# find pow(x,y) under given modulo mod 
def is_prime(n):
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1 
    return n!=1 
def gcd(a,b):
    # O(logmax(a,b))
    if b==0: return a
    return gcd(b,a%b)
def power_mod(x,y,mod):
    if y==0: return 1 
    res=power_mod(x*x%mod,int(y/2),mod)
    if y%2==1:
        res=(res*x)%mod 
    return res
def is_carmicheal_number(n):
    if is_prime(n) or n==1: return False 
    for x in range(2,n):
        if gcd(x,n)==1:
            if power_mod(x,n-1,n)!=1: return False 
    return True 
    
