def recur(m,n):
    if(n == 1): return m
    else: return m + recur(m, n - 1)

# print(recur(5,10))

def recursivefunc1(a,b):
    if b==0:
        return a
    else:
        return recursivefunc1(a+b,b-1)

def moreVowels(w):
    vowels = ["a", "e", "i", "o", "u"]

    def _moreVowels(l, c = 0, v = 0):
        if l == len(w): return v > c
        else:
            if w[l] in vowels: return _moreVowels(l + 1, c, v + 1)
            else: return _moreVowels(l + 1, c + 1, v)
    return _moreVowels(0)

def main():
    print(recursivefunc1(3,5))
    print(moreVowels("dictionary"))
    print(moreVowels("ahaha"))

if __name__=='__main__':

    main()
