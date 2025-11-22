import re
from collections import Counter

text = "Gur npgvba bs n fuvsg pvcure vf gb ercynpr rnpu cynvagrkg yrggre jvgu n qvssrerag bar ng n svkrq ahzore bs cynprf qbja gur nycunorg".lower()

cipher = re.sub(r"\s+", "", text)

print(cipher)

freq = list(Counter(cipher).items())
freq.sort() # sort in ordine alfabetico

for (letter, cnt) in freq:
    print(letter, " : ", "*" * cnt)



def decrypt_shifter_by(text, k):
    ans = ""
    for c in text:
        ans += (chr((ord(c) - ord('a') - k) % 26 + ord('a')))
    return ans

for word in text.split():
    print(decrypt_shifter_by(word, 13), end=" ")
print()

