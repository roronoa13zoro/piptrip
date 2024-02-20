def client(kyori, car):    
    
    kyori = int(kyori)
    kyorimoney = kyori * 20
    
    if car == "rental":
        money = 73276
    elif car == "share":
        carmoney = 31900 + 18700 + 1100
        money = kyorimoney + carmoney
    
    return money, car
