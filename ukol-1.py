sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

#Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.
#Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. Následně součástku odeber ze slovníku, protože je vyprodaná.
#Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem.


kod = input("Zadej kód součástky: ")

if kod in sklad:
    pocet = int(input("Zadej množství součástek: "))
    if pocet <= sklad[kod]:
        print("Poptávku lze uspokojit v plné výši.")
        sklad[kod] -= pocet
        if sklad[kod] == 0:
            sklad.pop(kod)
    else:
        print("Lze prodat pouze omezené mnnžství součástek.")
else:
    print("Součástka není skladem.")