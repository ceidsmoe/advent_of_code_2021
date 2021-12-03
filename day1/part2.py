if __name__ == "__main__":
    larger_sums = 0
    with open("input") as f:
        prev_window = []
        for _ in range(3):
            prev_window.append(int(f.readline()))
    
        line = f.readline()
        while line:
            if int(line) - prev_window[2] > 0:
                larger_sums += 1
            prev_window = [int(line)] + prev_window[:2]
            line = f.readline()
    print(larger_sums)