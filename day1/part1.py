if __name__ == "__main__":
    how_many_larger = 0
    with open("input") as f:
        prev = None
        for line in f.readlines():
            if prev and int(line) > prev:
                how_many_larger += 1
            prev = int(line)
    print(how_many_larger)