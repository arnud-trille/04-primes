from math import sqrt

#### Fonction secondaire


def isprime(n):
    if n==1:
        return(False)
    for k in range (2,int(sqrt(n)+1)):
        if n%k==0:
            return(False)
    return(True)

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()