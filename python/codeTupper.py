import sys

number_bits = 17

def tupper(x, y):
    return (1/2 < ((y//number_bits) * 2**(-number_bits*x - y%number_bits)) % 2)

if len(sys.argv) == 0:
    sys.exit(1)

k = int(sys.argv[1])


width = 80  # ajustado al tamaño real
for y in range(k+16, k-1, -1):
    for x in range(width-1, -1, -1):
        print('█' if tupper(x, y) else ' ', end='')
    print()
