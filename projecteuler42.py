alfabe={"A":1,	"B":2,	"C":3,	"D":4,	"E":5,	"F":6	,"G":7	,"H":8,	"I":9,	"J":10,	"K":11,	"L":12,	"M":13,	"N":14,	"O":15,	"P":16,	"Q":17,	"R":18,	"S":19,	"T":20,	"U":21
        ,	"V":22,	"W":23,	"X":24,	"Y":25,	"Z":26}
with open(r"C:\Users\halil\OneDrive\Masaüstü\python test\projecteuler42word.txt") as r:
    a=r.read()
üçgen_sayılar=[]
for i in range(1,100):
    üçgen_sayılar.append(i*(i+1)/2)
t=0
b=a.split(",")
toplam=0
for i in b:
    for c in i:
      if c in alfabe:
        t+=(alfabe[c])
    if t in üçgen_sayılar:
        toplam+=1
        
    t=0
print(toplam)