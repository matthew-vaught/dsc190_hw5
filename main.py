def main():
    print("Hello from dsc190-hw5!")
    x = 3
    if x == 3:
        x += 1

    funcs = []

    for i in range(3):
        def f(i=i):
            return i
        funcs.append(f)

    print([f() for f in funcs])

if __name__ == "__main__":
    main()
