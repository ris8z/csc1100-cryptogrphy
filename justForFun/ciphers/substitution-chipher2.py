import re
from collections import Counter
import string


text = "A lodhst lwzlmomwmogf eohitk ofxgsxtl lwzlmomwmofu txtkb hsaofmtvm eiakaemtk ygk a royytktfm eohitkmtvm eiakaemtk Om royytkl ykgd mit lioym eohitk of miam mit eohitk ashiaztm ol fgm dtktsb mit ashiaztm lioymtr om ol egdhstmtsb pwdzstr".lower()
cipher = re.sub(r"\s+", "", text)

freq = Counter(cipher)


for c in string.ascii_lowercase:
    if c in freq:
        print(c + " : " + "*" * freq[c])
    else:
        print(c + " : " + "*" * 0)



# E -> T

# Q,R,S,T
# J,K,L,M

#hbtlmovtt
#onetimepad
