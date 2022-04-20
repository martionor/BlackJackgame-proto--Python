from random import randrange

# Made by Martin Balogh
class player :
    def __init__(self):
        self.nimi = "player1"
        self.vuoro = 0



gameplayers = []
gameplayers.vuoro = 0
gameplayers.append(player)
for x in (gameplayers):
    nimi =  input("Kirjoita nimi: ")
    gameplayers.nimi = nimi
    gameplayers.vuoro += 1

cards52 = [2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11]
summa = 0
while summa < 21:
    print(nimi ,'Sinulla', summa, 'pisteita')
    vastaus = input('Otatko uusi kortti? ')
    if vastaus == 'kylla' or vastaus == 'k':
        korttiindexi = randrange(0, len(cards52)-1)
        kortti = cards52 [korttiindexi]
        cards52.pop(korttiindexi)
        print('Otit kortti ', kortti)
        summa = summa + kortti
        if summa == 11 and kortti == 11:
            summa = 21
    elif vastaus == 'ei':
        break
    else:
        print(nimi,'en ymmärrä sano kylla,k tai ei.')

if summa == 21:
    print(nimi,'sina voitit')
elif summa > 21:
    print(nimi, 'harmi', summa, ' sinulla on liikaa pisteita')
else:
    print(nimi,'sinulle puutui', 21 - summa, 'pisteet!')
gameplayers.vuoro = 2



