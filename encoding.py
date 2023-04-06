
import re
#  THERE IS ALREADY A MODUL THAT MAKES ALL THAT SHIT. BUT I'LL DO IT ANYWAY. (SOMETHING CALLED BASE64IO)
# ANASINI AVRADNI SİKEYİM AZ MATEMATİK BİLGİM OLSAYDI KEŞKE. ! KAFAM SİKİLDİ İNTERNETTEN PARÇA PARÇA MATEMATİK ÖĞRENMEYE ÇALIŞIRKEN


"""
This code will be the best thing I have ever done so far.
I was always wondering how people do encrpytion despite the fact that is not an encryption, it is something like that.
I will turn ASCII characters into Binary then Decimal and finally ASCII again. which is called as Base64 Encoding.
I am still thinking of the way to do it but I will find out.
"""


#   ASCII 18 MART 2023

"""Find the character you wish to convert
Write down 0 + the first three binary bits on the top
Write down the last four binary bits for that letter on the left"""

A, B, C, D,E, F= "01000001", "01000010", "01000011", "01000100", "01000101", "01000110"
G = "01000111" # BURASI BİRAZ AMELE İŞİ TEK TEK UĞRAŞMAK GEREKİR DE SİKTİR ET.
H = "01001000"
I = "01001001"
J = "01001010"
K = "01001011"
L = "01001100"
M = "01001101"
N = "01001110"
O = "01001111" 
P = "01010000"
Q = "01010001"
R = "01010010"
S = "01010011" 
T = "01010100" 
U = "01010101"
V = "01010110"
W = "01010111"
X = "01011000"
Y = "01011001"
Z = "01011010"
a = "01100001"
b = "01100010"
c = "01100011"
d = "01100100"
e = "01100101"
f = "01100110"
g = "01100111"
h = "01101000"
i = "01101001"
j = "01101010"
k = "01101011"
l = "01101100"
m = "01101101"
n = "01101110"
o = "01101111"
p = "01110000"
q = "01110001"
r = "01110010"
s = "01110011"
t = "01110100"
u = "01110101"
v = "01110110"
w = "01110111"
x = "01111000"
y = "01111001"
z = "01111010"



"""After you type your word with binary, you need to sum up the ones and zeros
and than you should ensure that the result can divided to 6 if not add two more
0s and again if not add two more 0s again. So you either add 2 or 4 zeros."""
liste =[]
def first (*letters):
    for letter in letters:
        liste.append(letter)
        
    #print(liste) >>> bu print bize her binary bloğunu ayrı ayrı veriyor. (tek satırda)


# That is GREAT I've made it. So far this code takes letters from this function and sums it up.
# Then it divides it to 6 and if the remainder is not equal to 0 it adds two 0s and again if its not 
# equal to 0 it adds two more 0s again.

first(T,E,M,E,L,D,E,S,T,E,K)
str = ""
for li in liste:
    str+= li

#print(str) >>> bu bize 6 ya bölünüp bölünmediği check edilmeden önceki halini veriyor.

if len(str) % 6 != 0:
    str += "00"

    if len(str) % 6 != 0:
        str += "00"
    else:
        pass
else:
    pass
#print(str) # bu bize son halini veriyor.
gecici_dep = []
next_step = re.findall('......?', str)
#print(next_step)
for i in next_step:
    decrary = int(i,2)
    gecici_dep.append(decrary)
print(gecici_dep)    





