Betriebssysteme und Netzwerke (IBN)

# Übungsblatt 5

## Aufgabe 1

a)

Nach JEDEC-Standard:

Minmales $M$ damit bei jeder Iteration eine neue Seite benötigt wird: $ \frac{4 KB}{4 B} = \frac{4 \cdot 1024 B}{4 B} = 1024 $

Dafür muss $N > M$ und $N,M \in \mathbb{N}$ sein.

b)

Die Antwort würde anders ausfallen, da die letzen Einträge nach der Wenigstens-Zuletzt-Benutzt Strategie gespeichert werden.

Minimales $M$ damit die Einträge nicht mehr im TLB gespeichert weden: $ \frac{4 KB}{4 B} \cdot 64 = \frac{4 \cdot 1024 B}{4 B} \cdot 64 = 1024 \cdot 64 = 65536 $

Dafür muss $N > M$ und $N,M \in \mathbb{N}$ sein.

c)

Bonusaufgabe:

Anzahl der Seiten $ = \left \lceil \frac{N \cdot 4}{4 \cdot 1024} \right \rceil $

## Aufgabe 2

Nach IEC-Standard:

Seitengröße: 1 KiB $= 1024$

Offset: logische Adresse % Seitengröße

Seitennummer: $\left \lfloor \frac{\text{logische Adresse}}{\text{Seitengröße}} \right \rfloor $

logische Adresse | Seitennummer | Offset |
| -------------- | ------------ | ------ |
| 2456           | 2            | 408    |
| 16382          | 15           | 1022   |
| 30000          | 29           | 304    |
| 4385           | 4            | 289    |