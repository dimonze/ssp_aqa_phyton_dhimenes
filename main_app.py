def generate_fibonacci(n):
    if type(n) is not int:
        return False
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    f.pop(0)
    return f


def main():
    print(generate_fibonacci(5))
    print(generate_fibonacci(6))
    print(generate_fibonacci(0))
    print(generate_fibonacci(-5))
    print(generate_fibonacci('a'))


if __name__ == "__main__": main()
