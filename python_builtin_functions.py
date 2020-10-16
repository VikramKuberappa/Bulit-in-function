def myabs(number):
    """ Implementation of built-in `abs` function """
    if number<0:
        return -number
    return number


def myall(iterable):
    """ Implementation of built-in `all` function """
    for item in iterable:
        if not item:
            return False
    return True


def myany(iterable):
    """ Implementation of built-in `any` function """
    for item in iterable:
        if item:
            return True
    return False


def mylen(s):
    """ Implementation of built-in `len` function """
    i=0
    for _ in s:
        i+=1
    return i


def mysum(iterable):
    """ Implementation of built-in `sum` function """
    i=0
    for x in iterable:
        i+=x
    return i


def mymax(iterable):
    """ Implementation of built-in `max` function """
    i=0
    for x in iterable:
        if x>i:
            i=x
        else:
            continue
    return i


def mymin(iterable):
    """ Implementation of built-in `min` function """
    i=1000**1000
    for x in iterable:
        if x<i:
            i=x
        else:
            continue
    return i


def mydivmod(a, b):
    """ Implementation of built-in `divmod` function """
    q=a//b
    r=a%b
    return (q,r)


def mybool(x):
    """ Implementation of built-in `bool` function """
    if x:
        return True
    return False


def mypow(base, exp):
    """ Implementation of built-in `pow` function """
    i=base**exp
    return i


def myreversed(seq):
    """ Implementation of built-in `reversed` function """
    str1=''
    for i in range (1,len(seq)+1):
        str1+=seq[-i]
    return str1


def myenumerate(iterable, start=0):
    """ Implementation of built-in `enumerate` function """
    lst=[]
    tup=()
    for x in range (0,len(iterable)):
        tup=(x,iterable[x])
        lst.append(tup)
    return lst


def mybin(x):
    """ Implementation of built-in `bin` function """
    lst=['0b']
    while x>0:
        r=x%2
        x=x//2
        lst.insert(1,str(r))
    return ''.join(lst)


def myhex(x):
    """ Implementation of built-in `hex` function """
    lst=['0x']
    while int(x>0):
        r=x%16
        x=x//16
        if r==10:
            r='a'
        elif r==11:
            r='b'
        elif r==12:
            r='c'
        elif r==13:
            r='d'
        elif r==14:
            r='e'
        elif r==15:
            r='f'
        else:
            pass
        lst.insert(1,str(r))
    return ''.join(lst)


def myoct(x):
    """ Implementation of built-in `oct` function """
    lst=['0o']
    while int(x>0):
        r=x%8
        x=x//8
        lst.insert(1,str(r))
    return ''.join(lst)


def myisinstance(object, classinfo):
    """ Implementation of built-in `isinstance` function """
    t1=type(object)
    t2=str(t1).find(classinfo)
    if t2>=0:
        return True
    return False


def myround(number, ndigits=None):
    """ Implementation of built-in `round` function """
    dot='.'
    lst=list(str(number))
    f=str(number).find(dot)
    t=f+ndigits+1
    if int(lst[t])>5:
        lst[t-1]=str(int(lst[t-1])+1)
    return  ''.join(lst[0:t])


def mysorted(iterable, reverse=False):
    """ Implementation of built-in `sorted` function """
    iterable=list(iterable)
    for i in range(len(iterable)):
        for j in range(len(iterable)):
            if iterable[i]<iterable[j]:
                temp=iterable[i]
                iterable[i]=iterable[j]
                iterable[j]=temp
    return iterable