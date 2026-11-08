def parity_generator():
    while True:
        yield "Парне"
        yield "Непарне"


if __name__ == "__main__":
    generator = parity_generator()

    for _ in range(6):
        print(next(generator))
