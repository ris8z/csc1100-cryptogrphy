import hashlib
from pathlib import Path

# Modulus p (hex senza spazi)
p_hex = (
    "b59dd79568817b4b9f6789822d22594f376e6a9abc0241846de426e5dd8f6edd"
    "ef00b465f38f509b2b18351064704fe75f012fa346c5e2c442d7c99eac79b2bc"
    "8a202c98327b96816cb8042698ed3734643c4c05164e739cb72fba24f6156b6f"
    "47a7300ef778c378ea301e1141a6b25d48f1924268c62ee8dd3134745cdf7323"
)

g_hex = (
    "44ec9d52c8f9189e49cd7c70253c2eb3154dd4f08467a64a0267c9defe4119f2"
    "e373388cfa350a4e66e432d638ccdc58eb703e31d4c84e50398f9f91677e8864"
    "1a2d2f6157e2f4ec538088dcf5940b053c622e53bab0b4e84b1465f5738f5496"
    "64bd7430961d3e5a2e7bceb62418db747386a58ff267a9939833beefb7a6fd68"
)

p = int(p_hex, 16)
g = int(g_hex, 16)
p_minus_1 = p - 1

# Leggi y, r, s dalle rispettive txt
def read_hex_file(path: str) -> int:
    txt = Path(path).read_text().strip()
    return int(txt, 16)

y = read_hex_file("y.txt")
r = read_hex_file("r.txt")
s = read_hex_file("s.txt")

# Controlla i range
print("Checking ranges...")
print(f"0 < r < p     ? {0 < r < p}")
print(f"0 < s < p-1   ? {0 < s < p_minus_1}")
print()

# Calcola H(m) = SHA-256(Assignment2.class)
class_bytes = Path("Assignment2.class").read_bytes()
H_bytes = hashlib.sha256(class_bytes).digest()
H = int.from_bytes(H_bytes, byteorder="big", signed=False)

print(f"H(m) (hex): {H:064x}")
print()

# Verifica: g^{H(m)} mod p  ==  y^r * r^s mod p
lhs = pow(g, H, p)
rhs = (pow(y, r, p) * pow(r, s, p)) % p

print(f"g^H(m) mod p        = {lhs}")
print(f"y^r * r^s mod p      = {rhs}")
print()
print("Signature valid? ", lhs == rhs)
