def initnp(n):
    np = n*[0]
    return np
def printnp(np):
    np_text = "".join(map(str,np))
    return np_text

def sinhnp(n,np):

    i = n - 1
    while i > -1 and np[i] == 1:
        i -= 1
    np[i] = 1
    if i > -1:
        for j in range(i+1, n):
            np[j] = 0
    return i, np

def nhiphan(n):
    np = initnp(n)
    print(printnp(np))
    while True:
        i,np = sinhnp(n,np)
        if i == -1:
            break
        print(printnp(np))
nhiphan(2)
