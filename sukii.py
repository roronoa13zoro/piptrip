def client(lift1, wear1, chose1, change1, lift2, wear2, chose2, change2):    
    
    money = 6500 + 3000 + 5000 + 4000
        
    if wear1 == "上のみ":
        money = money + 3000
    elif wear1 == "下のみ":
        money = money + 3000
    elif wear1 == "上下セット":
        money = money + 5000
    elif wear1 == "なし":
        money = money
        
    if change1 == "あり":
        money = money + 1000
    elif change1 == "なし":
        money = money + 0
    
    if wear2 == "上のみ":
        money = money + 3000
    elif wear2 == "下のみ":
        money = money + 3000
    elif wear2 == "上下セット":
        money = money + 5000
    elif wear2 == "なし":
        money = money
        
    if change2 == "あり":
        money = money + 1000
    elif change2 == "なし":
        money = money

    
    return lift1, wear1, chose1, change1, lift2, wear2, chose2, change2, money
