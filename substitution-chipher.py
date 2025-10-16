# Biagram most common in english
# TH	2.9%	HE	2.48%	IN	1.87%	ER	1.73%
# AN	1.65%	RE	1.38%	ES	1.35%	ST	1.19%
# ON	1.17%	ND	1.14%	EN	1.13%	AT	1.08%
# NT	1.08%	ED	1.04%	EA	1.01%	TO	1%
# OR	0.96%	TI	0.96%	HA	0.94%	AR	0.89%
# NG	0.89%	IS	0.89%	IT	0.88%	TE	0.88%
# OU	0.85%	ET	0.84%	OF	0.82%	AL	0.82%
# AS	0.8%	LE	0.74%	SE	0.73%	HI	0.72%
# SA	0.68%	RA	0.64%	RO	0.64%	NE	0.64%
# VE	0.63%	ME	0.62%	RI	0.62%	SO	0.6%
# DE	0.59%	LL	0.58%	TA	0.58%	LI	0.57%
# SI	0.57%	EL	0.55%	EC	0.52%	CO	0.52%
# NO	0.52%	OT	0.51%	MA	0.5%	DI	0.5%
# IC	0.49%	LA	0.49%	HO	0.49%	OM	0.48%
# TT	0.48%	NA	0.48%	SH	0.47%	CH	0.46%
# BE	0.46%	SS	0.46%	RT	0.46%	EE	0.45%
# EM	0.45%	NS	0.44%	RS	0.44%	CE	0.43%
# UR	0.42%	EI	0.41%	CA	0.41%	IO	0.41%
# AC	0.4%	TS	0.4%	DA	0.39%	LO	0.39%
# US	0.39%	WA	0.38%	NI	0.38%	DT	0.38%
# PE	0.38%	FO	0.38%	EW	0.37%	UT	0.37%
# WI	0.36%	IL	0.36%	EO	0.36%	LY	0.36%
# WH	0.36%	AD	0.35%	UN	0.34%	OW	0.34%
# TR	0.34%	NC	0.33%	FT	0.33%	DO	0.32%
# GE	0.32%	EP	0.32%	MO	0.32%	WE	0.31%


translate = {}

input = "AKBP AKBP PSKFG KUC ZWJSQ KB SADSFCF LVC HVCIUVH GC AIOV CT BSL OZCHVSG HVKH VS GDSBH KZZ VWG ACBSP WB CFQSF HC CMHKWB HVSA VWG CBZP KAMWHWCB LKG HC MS KZLKPG LSZZ QFSGGSQ VS QWQ BCH OKFS TCF VWG GCZQWSFG KBQ HVS HVSKHFS QWQ BCH KAIGS VWA HVS CBZP HVWBU WB TKOH VS HVCIUVH KBPHVWBU CT LKG HC QFWJS CIH KBQ GVCL K BSL GIWH CT OZCHVSG VS VKQ K OCKH TCF SJSFP VCIF CT HVS QKP KBQ KG CBS LCIZQ GKP CT K YWBU VS WG WB VWG OKMWBSH GC CBS OCIZQ GKP CT VWA HVS SADSFCF WG WB VWG QFSGGWBU FCCA"

d = {}
for c in input:
    if c == " ":
        continue
    d[c] = d.get(c, 0) + 1

items = [x for x in d.items()] 
items.sort(key=lambda x:x[1], reverse=True)

print(items)

biagrams = {}
for word in input.split():
    i = 0
    while i < len(word) - 1:
        b = word[i:i+2]
        biagrams[b] = biagrams.get(b, 0) + 1 
        i += 1

print()
print()
print()
bi_items = [x for x in biagrams.items()] 
bi_items.sort(key=lambda x:x[1], reverse=True)
print(bi_items)

def printTra(input, d):
    ans = ""
    for c in input:
        if c == " ":
            ans += " "
        elif c in translate:
            ans += d[c].upper()
        else:
            ans += c.lower()
    print()
    print()
    print()
    print(ans)

translate["H"] = "T"
translate["V"] = "H"
translate["S"] = "E"
translate["K"] = "A" # maybe

translate["C"] = "O"
translate["T"] = "F"
translate["Q"] = "D"
translate["O"] = "C"
translate["B"] = "N"
translate["L"] = "W"
translate["I"] = "U"
translate["U"] = "G"
translate["F"] = "R"
translate["W"] = "I"
translate["G"] = "S"
translate["P"] = "Y"
translate["Z"] = "L"
translate["A"] = "M"
translate["D"] = "P"
translate["J"] = "V"
translate["M"] = "B"
translate["Y"] = "K"

printTra(input, translate)
