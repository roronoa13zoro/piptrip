def client(menber):
    
    if menber == "ginji":
        number = 0
    elif menber == "daiki":
        number = 1
    elif menber == "riki":
        number = 2
    elif menber == "miyu":
        number = 3
    elif menber == "hikaru":
        number = 4
    elif menber == "kana":
        number = 5
    elif menber == "ryuya":
        number = 6
    elif menber == "kai":
        number = 7
    
    human = ["款次","大輝","理暉","未夢","輝","佳奈","龍也","海",""]
    menber = human[number]
    
    menberall = ["ginji","daiki","riki","miyu","hikaru","kana","ryuya","kai"]
    lines = []
    input = []
    output = []
    for i in range(8):
        with open("data/00_{}.txt".format(menberall[i]), encoding="utf-8", mode="r") as f:
            l = f.read().splitlines()
            lines.append(l)
    for n in range(8):
        if number == n:
            del human[n]
        else:
            input.append(int(lines[number][n]))
            output.append(int(lines[n][number]))
    return menber, input, output, human

def All():
    
    menberall = ["ginji","daiki","riki","miyu","hikaru","kana","ryuya","kai"]
    lines = []
    allpay = []
    hitori = []
    tatekae = []
    menber = []
    menber1,menber2,menber3,menber4,menber5,menber6,menber7,menber8 = [],[],[],[],[],[],[],[]
    with open("data/10_allpay.txt", encoding="utf-8", mode="r") as f:
            l = f.read().splitlines()
            allpay.append(l)
    with open("data/10_hitori.txt", encoding="utf-8", mode="r") as f:
            l = f.read().splitlines()
            hitori.append(l)
    with open("data/10_tatekae.txt", encoding="utf-8", mode="r") as f:
            l = f.read().splitlines()
            tatekae.append(l)
    with open("data/10_menber.txt", encoding="utf-8", mode="r") as f:
            l = f.read().splitlines()
            menber.append(l)
    num = len(allpay[0])
    
    for i in range(8):
        with open("data/00_{}.txt".format(menberall[i]), encoding="utf-8", mode="r") as f:
            l = f.read().splitlines()
            lines.append(l)
    for n in range(8):
            menber1.append(int(lines[0][n]))
            menber2.append(int(lines[1][n]))
            menber3.append(int(lines[2][n]))
            menber4.append(int(lines[3][n]))
            menber5.append(int(lines[4][n]))
            menber6.append(int(lines[5][n]))
            menber7.append(int(lines[6][n]))
            menber8.append(int(lines[7][n]))
    return menber1,menber2,menber3,menber4,menber5,menber6,menber7,menber8,allpay,hitori,tatekae,num,menber