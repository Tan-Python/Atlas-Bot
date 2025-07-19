# Created on iPad.
# How long did i take to make this??

import string

a = ["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austira","Azerbaijan"]
b = ["Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium",
"Belize","Benin","Bolivia","Bosnia and Herzegovina","Botswana","Brazil"
,"Brunei","Bulgaria","Burkina Faso","Burundi"]
c = ["Cabo Verde","Cambodia","Cameroon","Canada","Cayman Islands",
"Central African Republic","Chad","Chile","China","Colombia","Comoros",
"Congo","Cook Islands","Costa Rica","Cote d'Iviore","Croatia","Cuba"
,"Cyprus","Czechia"]
d = ["Democratic Republic of the Congo","Denmark","Djibouti","Dominica","Dominican Republic"]
e = ["Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini","Ethiopia"]
f = ["Fiji","Finland","France"]
g = ["Gabon","Gambia","Georgia","Germany","Ghana","Georgia","Germany","Ghana","Greece",
"Grenada","Guatemala","Guinea","Guinea-Bassau","Guyana"]
h = ["Haiti","Honduras","Hungary"]
i = ["Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy"]
j = ["Jamaica","Japan","Jordan"]
k = ["Kazakhstan","Kenya","Kiribati","Kosovo","Kuwait","Kyrgyzstan"]
l = ["Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg"]
m = ["Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritius",
"Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique"]
n = ["Namibia","Nauru","Nepal","Netherlands","New Zealand","Niceragua","Niger","Nigeria","North Korea"
,"North Macedonia","Norway"]
o = ["Oman"]
p = ["Pakistan","Palau","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal"]
q = ["Qatar"]
r = ["Romania","Russia","Rwanda"]
s = ["Saint Kitts and Nevis","Saint Lucia","Saint Vincent Zand the Grenadines","Samoa",
"San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone"
,"Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Korea","South Sudan",
"Spain","Sri Lanka","Sudan","Suriname","Sweden","Switzerland","Syria"]
t = ["Tajikistan","Tanzania","Thailand","Timor Leste","Togo","Tonga","Trinidad and Tobago"
,"Tunisia","Turkiye","Turkmenistan","Tuvalu"]
u = ["Uganda","Ukraine","United Arab Emirates","United Kingdom","United States of America",
"Uruguay","Uzbekistan"]
v = ["Vanuatu","Venezuela","Vietnam"]
w = []
x = []
y = ["Yemen"]
z = ["Zambia","Zimbabwe"]

all = a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p + q + r + s + t + u + v + w + x + y + z
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
    "l": l,
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
llu = None
flu = None
llb = "S"
def repeater(all,flu,llu,llb):
	out = "placeholder"
	in = input(llb,":")
	llu = in[-1]
	flu = in[0]
	if flu != llb:
		print("Your place does not start with",llb)
	else:
		if in in all:
			print("valid place")
			all.remove(in)
			if flu in atlas:
			    atlas[flu].remove(in)
			if llu in atlas:
				out = [llu][0]
				print(out)
				atlas[llu].remove(out)
				all.remove(out)
				llb = out[-1]
		return all, llu, llb, flu
		
# Stop trigger if ANY list in atlas_dict is empty
while True:
    if any(len(lst) == 0 for lst in atlas_dict.values()):
		print("You Win")
        break  
    repeater(all,llu,llb,flu)# Continue doing your trigger action
    


	
		

    

