def client(kingaku, tatekae, n, name, kinds, sonota, delnumber):
    
    if tatekae == "ginji":
        number = 0
    elif tatekae == "daiki":
        number = 1
    elif tatekae == "riki":
        number = 2
    elif tatekae == "miyu":
        number = 3
    elif tatekae == "hikaru":
        number = 4
    elif tatekae == "kana":
        number = 5
    elif tatekae == "ryuya":
        number = 6
    elif tatekae == "kai":
        number = 7
    else:
        number = 8
    human = ["款次","大輝","理暉","未夢","輝","佳奈","龍也","海",""]
    menber = human[number]
    
    menberall = ["ginji","daiki","riki","miyu","hikaru","kana","ryuya","kai"]
    kingaku = int(kingaku)
    
    if n == 0:
        n = n
    elif n > 0:
        hitori = int(kingaku / n)
        if kinds == "sonota":
            with open("data/10_tatekae.txt", encoding="utf-8", mode="a") as f:
                f.write("{}\n".format(sonota))
        else:
            with open("data/10_tatekae.txt", encoding="utf-8", mode="a") as f:
                f.write("{}\n".format(kinds))
        with open("data/10_allpay.txt", encoding="utf-8", mode="a") as f:
            f.write("{}\n".format(kingaku))
        with open("data/10_hitori.txt", encoding="utf-8", mode="a") as f:
            f.write("{}\n".format(hitori))
        with open("data/10_menber.txt", encoding="utf-8", mode="a") as f:
            f.write("{}\n".format(menber))
        with open("data/10_menber2.txt", encoding="utf-8", mode="a") as f:
            f.write("{}\n".format(tatekae))
        
        for i in range(8):
            with open("data/01_{}.txt".format(menberall[i]), encoding="utf-8", mode="a") as f:
                f.write("{}\n".format(name[i]))
    
    if tatekae == "del":
        l1 = []
        with open("data/10_allpay.txt", encoding="utf-8", mode="r") as fp:
            l1 = fp.readlines()
            allpay_1 = l1[int(delnumber)]
        with open("data/10_allpay.txt", encoding="utf-8", mode="w") as fp:
            for number, line in enumerate(l1):
                if number not in [int(delnumber)]:
                    fp.write(line)
        with open("data/10_hitori.txt", encoding="utf-8", mode="r") as fp:
            l1 = fp.readlines()
            hitori_1 = l1[int(delnumber)]
        with open("data/10_hitori.txt", encoding="utf-8", mode="w") as fp:
            for number, line in enumerate(l1):
                if number not in [int(delnumber)]:
                    fp.write(line)
        with open("data/10_menber.txt", encoding="utf-8", mode="r") as fp:
            l1 = fp.readlines()
            menber_1 = l1[int(delnumber)]
        with open("data/10_menber.txt", encoding="utf-8", mode="w") as fp:
            for number, line in enumerate(l1):
                if number not in [int(delnumber)]:
                    fp.write(line)
        with open("data/10_menber2.txt", encoding="utf-8", mode="r") as fp:
            l1 = fp.readlines()
            menber2_1 = l1[int(delnumber)]
        with open("data/10_menber2.txt", encoding="utf-8", mode="w") as fp:
            for number, line in enumerate(l1):
                if number not in [int(delnumber)]:
                    fp.write(line)
        with open("data/10_tatekae.txt", encoding="utf-8", mode="r") as fp:
            l1 = fp.readlines()
            tatekae_1 = l1[int(delnumber)]
        with open("data/10_tatekae.txt", encoding="utf-8", mode="w") as fp:
            for number, line in enumerate(l1):
                if number not in [int(delnumber)]:
                    fp.write(line)
        delmenber = []
        for i in range(8):
            with open("data/01_{}.txt".format(menberall[i]), encoding="utf-8", mode="r") as f:
                l = f.readlines()
                lp = l[int(delnumber)]
                delmenber.append(lp)
            with open("data/01_{}.txt".format(menberall[i]), encoding="utf-8", mode="w") as f:
                for number, line in enumerate(l):
                    if number not in [int(delnumber)]:
                        f.write(line)
        print(menber_1)
        print(menber2_1)
        print(tatekae_1)
        a = 0
        menber = ["ginji","daiki","riki","miyu","hikaru","kana","ryuya","kai"]
        if menber[0] in menber2_1:
            a = 0
        elif menber[1] in menber2_1:
            a = 1
        elif menber[2] in menber2_1:
            a = 2
        elif menber[3] in menber2_1:
            a = 3
        elif menber[4] in menber2_1:
            a = 4
        elif menber[5] in menber2_1:
            a = 5
        elif menber[6] in menber2_1:
            a = 6
        elif menber[7] in menber2_1:
            a = 7
        menber_0 = menber[a]
        
        with open("data/00_{}.txt".format(menber_0), encoding="utf-8", mode="r") as f:
            lines = f.read().splitlines()
        f.close()
        for i in range(8):
            print(delmenber)
            if delmenber[i] == "1\n":
                lines[i] = int(lines[i]) - int(hitori_1)
        with open("data/00_{}.txt".format(menber_0), encoding="utf-8", mode="w") as f:
            for d in lines:
                f.write("%s\n" % d)
    
    if tatekae == "cancel":
        for i in range(8):
            with open("data/00_{}.txt".format(menberall[i]), encoding="utf-8", mode="w") as f:
                for i in range(8):
                    f.write("0\n")
        for i in range(8):
            with open("data/01_{}.txt".format(menberall[i]), encoding="utf-8", mode="w") as f:
                pass
        with open("data/10_allpay.txt", encoding="utf-8", mode="w") as f:
                pass
        with open("data/10_hitori.txt", encoding="utf-8", mode="w") as f:
                pass
        with open("data/10_tatekae.txt", encoding="utf-8", mode="w") as f:
                pass
        with open("data/10_menber.txt", encoding="utf-8", mode="w") as f:
                pass
        with open("data/10_menber2.txt", encoding="utf-8", mode="w") as f:
                pass
    
    elif kingaku > 0:
        
        with open("data/00_{}.txt".format(tatekae), encoding="utf-8", mode="r") as f:
            lines = f.read().splitlines()
        f.close()
        
        for i in range(8):
            if name[i] == 1:
                lines[i] = int(lines[i]) + hitori
        
        with open("data/00_{}.txt".format(tatekae), encoding="utf-8", mode="w") as f:
            for d in lines:
                f.write("%s\n" % d)
    return 0