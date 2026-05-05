def main():
    print("Hello from dsc190-hw5!")


if __name__ == "__main__":
    main()

#x = "commented out code"

x = 3
if x = 3:
    x++

funcs = []

for i in range(3):
    def f():
        return i
    funcs.append(f)

print([f() for f in funcs])
