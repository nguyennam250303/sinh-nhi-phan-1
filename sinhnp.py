def initnp(n):
    np = n*[0]
    return np
def printnp(np):
    np_text = "".join(map(str,np))
    print(np_text)

def nhiphan(n):
    np = initnp(n)
    printnp(np)

    while True:
        i = n - 1
        while i > -1 and np[i] == 1:
            i-=1
        np[i] = 1
        for j in range(i+1,n):
            np[j] = 0
        if i == -1:
            break
        printnp(np)

nhiphan(4)