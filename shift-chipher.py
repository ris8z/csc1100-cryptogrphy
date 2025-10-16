input = "ZWPFLYRMVJLTTVJJWLCCPUVTIPGKVUKYZJDVJJRXVLJZEXRSILKVWFITVRKKRTBKYVEKIPUVTIPGKZEXZKLJZEXRWIVHLVETPRERCPJZJRKKRTBZEJKVRU"



def dec_word(word, n):
    ans = ""
    for c in word:
        pos = ord(c) - ord('A')
        pos = (pos - n) % 26
        new_c = chr(pos + ord('A'))
        ans += new_c 
    return ans



w1 = 'ZWPFLYRMVJLTTVJJWLCCPUVTIPGKVUKYZJDVJJ'

# found 17 as n to decrypt
#for i in range(1,26):
#    print(dec_word(w1, i), i)

print(dec_word(input, 17))

d = {}

for c in input:
    d[c] = d.get(c, 0) + 1

propabily_e_enrypted = max(d.items(), key=lambda x: x[1])[0]

print(propabily_e_enrypted)

print(abs(ord('E') - ord('V')) == 17)
