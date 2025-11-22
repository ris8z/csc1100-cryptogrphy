import re
from collections import Counter

text = """
QVUEVAIOHJCFMINRCFIYTMPZTFGVKIEKSQAVLOXWVBEKCEOXTEXPKIQVXRHTRQI
SPZYBRSWEHJPOGHJYDXJGEJTWPHXEXRIESKVITHVJDVGXBMAMEBXQWEPIMMHS
KVEIAIFFCPTPHIMMPRFVEJTXQUIZPPNXHMXTKZMSTTKKVFEEUFCCPXJXVPUEOBP
VCEOXSKILGTYQWSTBXVDJJBWQDQDLXLCICGHJNWKLXBGQTLNLTKCKKBGCYASJ
PVTBIAILGUPXROUFMQWEUBRBKITLETBCHTXETVQKQVBSVAIOPRFGISTVUTAXCC
NBOBCIULSCTMVAIODJVAIJUSTMLBXVFTCPLITXPLCKDXJLGIVAIAPCUHJMWSVHKO
PTJLQVUMTLXCPREBIPGIITVAXRIPLXIXJXCTTVGEMHTAGKIRCVGTWLCEDECATVKO
IAUVQFXETMTMSJQWVHRBHXJXWEPTGHJQWINXXQTVUHRJNJCMLBGWITZBBICGS
ASMFXEQWEVAITPWCLURPVGLXLJXFTVHBEPPMQWGWKPVQPCVOEPMTYVLBXJX
GEPVCVXBGEPWXRGRQYXETMPLGOXTVBSKPPUHKBDVIBEKPAKYILUXJXEYDZGBH
OTACVLFAHKLLZDREEYPXSPMLXIQAFSQWITPEPUVGVOITHCGHPXGMECQDJKOIIX
XVEIPISPXPLOIPZIPTEEAEYDYVTJLDXCGHXWENYPLCKYAMZWAGKIXGVCGKBSMP
TRBPXTHAYTWKWIQWIKKKOPZGTRALITXWXRVGWXLILGFIJDVAHJCXZGEMQIPGUV
LILGKWLUQKGITWSITZBJTVKCFCKVHKBIENBZFCKGQGBTHKGKINICKPVXRVAEQJR
KOIOHENLXOJKIEIFPQKGHBQXGWJLGEDXPFTJKKIIXKKHYPACGGXBGXCBRBSXJTX
QWIAAEAPPNUIBCFQKRLCXJXMOQEEDWTXXJMLBXVJTRAHMPMLBXVVKSRHITLTL
ROGMWXCHJTHKTZGKXXZIPMLBBSWMMKILKLWQPXGHJBMMUMIKRIQNVPLEUMLB
BETLLZDYPMVVSSYGFVILGKMSTVYBXEXRCLXETVKOIOLSWGHQLIPMCJXPGLSCIL
GLIXBCHBVPIQQLXSXZKWEKSFTHEAXQRKIPHMQGSCILGBHBCXKMCLUXJBRDHWG
XQPISOXXLWEXXFBTRITMKTHQGEJTQQKEYAITTAXUXGKRLDRVHAXGHUXZBCMPZ
EQHYEAEQXQGBJLJRFHYQUSTVIOIEKGXEPXVAMPQPGTOMAEEXSSTVIKSTCAKML
KTXVEIPLEUMLBRLWKGENETWEKSXJTXMWMNBTMXVTBTIPXGHJQWMUIEOXWJTR
APPUHKBDVIBEKPAKYILUXJXEYDZGPIOTHGTHXCHDNVFTHCGHQWEVTPBMEPWIO
QETMLLASOXAXQVCAEJISDBEPPRFKSDTVKGJXCXEAMISVGGSCILGTJLGIUTMALIT
XEIHSFXEAPRFUYOXIFTRAILCMXETHCKOCAEVPMISITGIPHFGRSKSXJXGEJVEACX
GHKGXBGWGVXBSAKMLANOGLEKSQQNRAHEPWKXIIUPMQWWETXQTVGWGXIXNX
JBTHKGKLCMVPEPILGFEOHLGLEKSXJTXQWINHAITEFXRIXRGUIVDRFPEPILGKMSTV
CGHQWEVMLBSMUMEKIWCOEDTPCBVCGSOPLFRLVAITXRFPEPGYUAMKVACLXET
WGTEKSXJTXQWIUFEIAFWGHITSHLLFKITLKODAKGKXUVCBHLUMVTPIPRFUIDXRPB
RDISEKCTPWRBT
"""

cipher = re.sub(r'\s+', '', text)

# both tot_same_pair, and tot_possible_pair should be halfed but
# that 2s get simplifed in the division anyways so we dont put it
def index_of_coincidence(text:str) -> float:
    freq: dict[str,int] = Counter(text)
    n: int = len(text)
    tot_same_pair: int = sum(x*(x - 1) for x in freq.values())
    tot_possible_pair: int = (n * (n - 1))
    return tot_same_pair / tot_possible_pair




# Let's try to gess the lenght
for keylen in range(1, 21):
    iocs: list[float] = [] 
    for i in range(keylen): 
        # per esmpio tutte le prime lettere se la key len = 2 e le seconde lettere etc
        group = cipher[i::keylen] # current_group_of_ith_letters_of_keylen
        iocs.append(index_of_coincidence(group))
    print(f"{keylen}: {sum(iocs)/len(iocs):.4f}")


# 1: 0.0459
# 2: 0.0495
# 3: 0.0567
# 4: 0.0497
# 5: 0.0459
# 6: 0.0657
# 7: 0.0462
# 8: 0.0495
# 9: 0.0562
# 10: 0.0499
# 11: 0.0458
# 12: 0.0658
# 13: 0.0454
# 14: 0.0501
# 15: 0.0565
# 16: 0.0506
# 17: 0.0448
# 18: 0.0646
# 19: 0.0463
# 20: 0.0493

# worth to try 6, 18 e 12 (in relta' sono tutti multipli di 6 quindi workano tutti)
# ti daranno la stessa key di 6 chars rieptuta

import string

def chi_squared(obs, exp):
    return sum((obs[c] - exp[c])**2 / exp[c] for c in string.ascii_uppercase)

english_freq = {
    'A':0.08167,'B':0.01492,'C':0.02782,'D':0.04253,'E':0.12702,
    'F':0.02228,'G':0.02015,'H':0.06094,'I':0.06966,'J':0.00153,
    'K':0.00772,'L':0.04025,'M':0.02406,'N':0.06749,'O':0.07507,
    'P':0.01929,'Q':0.00095,'R':0.05987,'S':0.06327,'T':0.09056,
    'U':0.02758,'V':0.00978,'W':0.02360,'X':0.00150,'Y':0.01974,'Z':0.00074
}


def bestShift(text):
    best_shift, best_score = 0, 1e9
    
    # brute force of all shift
    for shift in range(26):
        shifted = [(ord(c) - 65 - shift) % 26 + 65 for c in text]
        shifted_text = ''.join(chr(x) for x in shifted)
        counts = Counter(shifted_text)
        total = sum(counts.values())
        obs = {c: counts.get(c, 0)/total for c in string.ascii_uppercase}
        score = chi_squared(obs, english_freq)
        if score < best_score:
            best_score, best_shift = score, shift
    return best_shift





guess_len = 6
for i in range(guess_len):
    bs = bestShift(cipher[i::guess_len])
    print(chr(bs + ord('A')))
# this is the output
# E X P E C T 

def vigenere_decrypt(cipher, key):
    result = []
    key = key.upper()
    for i, c in enumerate(cipher):
        result.append(chr((ord(c) - 65 - (ord(key[i % len(key)]) - 65)) % 26 + 65))
    return ''.join(result)


print()
print()
print()

print(vigenere_decrypt(cipher, "EXPECT"))
