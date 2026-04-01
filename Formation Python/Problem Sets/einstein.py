def main():
    masse = int(input("Entrez une masse (en kg) : "))
    print(convert(masse))

def convert(m):
    c = 300000000
    return m*c*c

main()