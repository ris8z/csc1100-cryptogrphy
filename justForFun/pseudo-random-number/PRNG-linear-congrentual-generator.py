

class LCG:
    def __init__(self, seed):
        self.seed = seed
        self.x_n = seed
        self.a = 777
        self.c = 619
        self.m = 123242342423423

    def get_netx_n(self):
        next_n = (self.a * self.x_n + self.c) % self.m
        self.x_n = next_n
        return self.x_n


    def get_random_number(self):
        return self.get_netx_n()


psng = LCG(seed=1234)

for i in range(24):
    print(psng.get_random_number())
    print(psng.get_random_number())
    print(psng.get_random_number())

psng = LCG(seed=123456789)


