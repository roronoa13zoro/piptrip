menber = ["ginji","daiki","riki","miyu","hikaru","kana","ryuya","kai"]
lines = []
for i in range(8):
    with open("00_{}.txt".format(menber[i]), "r") as f:
        l = f.read().splitlines()
        lines.append(l)
print(lines)