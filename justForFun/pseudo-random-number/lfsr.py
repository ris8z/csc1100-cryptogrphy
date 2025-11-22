state = 0b1001
dim = 2 ** 4

for i in range(dim - 1):
    print("{:04b} -> {}".format(state, state))
    new_bit = (state ^ (state >> 1)) & 0b1
    new_state = (new_bit << 3) | (state >> 1)
    state = new_state
