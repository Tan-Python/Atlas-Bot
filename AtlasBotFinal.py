# Created on iPad.
# How long did i take to make this??
# this mostly uses the UN countries with some others


a = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola",
     "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Aust",
     "Azerbaijan"]
b = ["Bahamas", "Bahrain", "Bhutan", "Bangladesh", "Barbados",
     "Belarus", "Belgium",
     "Belize", "Benin", "Bolivia", "Bosnia and Herzegovina", "Botswana",
     "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi"]
c = ["Cabo Verde", "Cambodia", "Cameroon", "Canada", "Cayman Islands",
     "Central African Republic", "Chad", "Chile", "China", "Colombia",
     "Comoros", "Congo", "Cook Islands", "Costa Rica", "Cote d'Iviore",
     "Croatia", "Cuba", "Cyprus", "Czechia"]
d = ["Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica",
     "Dominican Republic"]
e = ["Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea",
     "Estonia", "Eswatini", "Ethiopia"]
f = ["Fiji", "Finland", "France"]
g = ["Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Georgia",
     "Germany", "Ghana", "Greece", "Grenada", "Guatemala",
     "Guinea", "Guinea-Bassau", "Guyana"]
h = ["Haiti", "Honduras", "Hungary"]
i = ["Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland",
     "Israel", "Italy"]
j = ["Jamaica", "Japan", "Jordan"]
k = ["Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan"]
li = ["Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya",
      "Liechtenstein", "Lithuania", "Luxembourg"]
# WTH DOES AMBIGUOUS MEAN AND WHY IS MY CODE COMPILER SAYING THAT
m = ["Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta",
     "Marshall Islands", "Mauritius", "Mexico", "Micronesia", "Moldova",
     "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar"]
n = ["Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Niceragua",
     "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway"]
o = ["Oman"]
p = ["Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru",
     "Philippines", "Poland", "Portugal"]
q = ["Qatar"]
r = ["Romania", "Russia", "Rwanda"]
s = ["Saint Kitts and Nevis", "Saint Lucia",
     "Saint Vincent and the Grenadines",
     "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal",
     "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia",
     "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea",
     "South Sudan", "Spain", "Sri Lanka", "Sudan",
     "Suriname", "Sweden", "Switzerland", "Syria"]
t = ["Tajikistan", "Tanzania", "Thailand", "Timor Leste",
     "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkiye",
     "Turkmenistan", "Tuvalu"]
u = ["Uganda", "Ukraine", "United Arab Emirates",
     "United Kingdom", "United States of America", "Uruguay", "Uzbekistan"]
v = ["Vanuatu", "Venezuela", "Vietnam"]
w = ["No places with W"]
x = ["No places with X"]
y = ["Yemen"]
z = ["Zambia", "Zimbabwe"]

alol = []
alol.extend(a)
alol.extend(b)
alol.extend(c)
alol.extend(d)
alol.extend(e)
alol.extend(f)
alol.extend(g)
alol.extend(h)
alol.extend(i)
alol.extend(j)
alol.extend(k)
alol.extend(li)
alol.extend(m)
alol.extend(n)
alol.extend(o)
alol.extend(p)
alol.extend(q)
alol.extend(r)
alol.extend(s)
alol.extend(t)
alol.extend(u)
alol.extend(v)
alol.extend(w)
alol.extend(x)
alol.extend(y)
alol.extend(z)

atlas = {
    "a": a,
    "b": b,
    "c": c,
    "d": d,
    "e": e,
    "f": f,
    "g": g,
    "h": h,
    "i": i,
    "j": j,
    "k": k,
    "l": li,
    "m": m,
    "n": n,
    "o": o,
    "p": p,
    "q": q,
    "r": r,
    "s": s,
    "t": t,
    "u": u,
    "v": v,
    "w": w,
    "x": x,
    "y": y,
    "z": z
}

for key in list(atlas.keys()):
    atlas[key.upper()] = atlas[key]


llu = None
flu = None
llb = "s"
out = "placeholder"


def repeater(alol, flu, llu, llb, atlas, out):
    inp = input("Enter Place: ")
    llu = inp[-1]
    flu = inp[0]
    if llb is None:
        llb = "S"
    if inp in alol:
        print("valid place")
        alol.remove(inp)
        atlas[flu].remove(inp)
        if llu in atlas:
            out = atlas[llu][0]
            if out not in atlas[llu]:
                out = atlas[llu][1]
            print(out)
            atlas[llu].remove(out)
            alol.remove(out)
            llb = out[-1]
            print(llb)
    return alol, llu, llb, flu, atlas, out


start = False


# Stop trigger if ANY list in atlas_dict is empty
while True:
    if any(len(lst) == 0 for lst in atlas.values()):
        print("You Win")
        break
    alol1 = alol
    llu1 = llu
    llb1 = llb
    flu1 = flu
    atlas1 = atlas
    out1 = out
    if out != "placeholder":
        llb = out[-1]
    # Or return, depending on your setup
    repeater(alol1, llu1, llb1, flu1, atlas1, out1)
