broi_more_ekskurzii = int(input())
broi_planina_ekskurzii = int(input())

cena_paket_more = 680
cena_paket_planina = 499
pechalba = 0
command = input()

while command != 'Stop':
    ime_paket = command

    if ime_paket == 'sea' and broi_more_ekskurzii != 0:
        pechalba += cena_paket_more
        broi_more_ekskurzii -= 1
    elif ime_paket == 'mountain' and broi_planina_ekskurzii != 0:
        pechalba += cena_paket_planina
        broi_planina_ekskurzii -= 1

    if broi_planina_ekskurzii == 0:
        if broi_more_ekskurzii == 0:
            print(f'Good job! Everything is sold.')
            break
    if broi_more_ekskurzii == 0:
        if broi_planina_ekskurzii == 0:
            print(f'Good job! Everything is sold.')
            break
 
    command = input()

print(f'Profit: {pechalba} leva.')
