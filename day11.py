with open("inputs/day11.txt", "r") as f:
    INPUT = [x.strip() for x in f.readlines()]

def loop(current, devices):
    if current == "out":
        return 1
    total = 0
    for v in devices[current]:
        total += loop(v, devices)
    return total

def partone():
    devices = {device: outputs.split() for device, outputs in (line.split(": ") for line in INPUT)}
    print(loop("you", devices))

cache = {}

def loop2(current, devices, dac, fft):
    cdf = (current, dac, fft)
    if cdf in cache:
        return cache[cdf]
    if current == "out":
        result = 1 if (dac and fft) else 0
        cache[cdf] = result
        return result
    if current == "dac":
        dac = True
    if current == "fft":
        fft = True
    total = 0
    for v in devices[current]:
        total += loop2(v, devices, dac, fft)
    cache[cdf] = total
    return total

def parttwo():
    devices = {device: outputs.split() for device, outputs in (line.split(": ") for line in INPUT)}
    print(loop2("svr", devices, False, False))
    

if __name__ == "__main__":
    #partone()
    parttwo()