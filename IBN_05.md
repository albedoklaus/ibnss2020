Betriebssysteme und Netzwerke (IBN)

# Übungsblatt 5

## Aufgabe 1

a)

Die Seitengröße von 1 KB entspricht nach JEDEC-Standard 1024 B.

Minmales $M$ damit bei jeder Iteration eine neue Seite benötigt wird: $\frac{4 KB}{4 B} = \frac{4 \cdot 1024 B}{4 B} = 1024$

Dafür muss $N > M$ und $N, M \in \mathbb{N}$ sein.

b)

Die Antwort würde anders ausfallen, da die letzen Einträge nach der Wenigstens-Zuletzt-Benutzt Strategie gespeichert werden.

Minimales $M$ damit die Einträge nicht mehr im TLB gespeichert weden: $\frac{4 KB}{4 B} \cdot 64 = \frac{4 \cdot 1024 B}{4 B} \cdot 64 = 1024 \cdot 64 = 65536$

Dafür muss $N > M$ und $N, M \in \mathbb{N}$ sein.

c)

Bonusaufgabe:

Anzahl der Seiten: $\left \lceil \frac{N \cdot 4}{4 \cdot 1024} \right \rceil$

## Aufgabe 2

Die Seitengröße von 1 KiB entspricht nach IEC-Standard 1024 B.

Offset: logische Adresse % Seitengröße

Seitennummer: $\left \lfloor \frac{\text{logische Adresse}}{\text{Seitengröße}} \right \rfloor$

| logische Adresse | Seitennummer | Offset |
| ---------------- | ------------ | ------ |
| 2456             | 2            | 408    |
| 16382            | 15           | 1022   |
| 30000            | 29           | 304    |
| 4385             | 4            | 289    |

Code:

\lstinputlisting[language=C]{IBN_05_2.c}

Ausgabe:

\begin{lstlisting}[]
logical_address=2456, page_number=2, offset=408
logical_address=16382, page_number=15, offset=1022
logical_address=30000, page_number=29, offset=304
logical_address=4385, page_number=4, offset=289
\end{lstlisting}

## Aufgabe 3

Offset: $2 KiB = 2 \cdot 1024 B = 2 \cdot 2^10 B = 2^11 B$

Einträge direkte Seitentabelle: $\frac{2^{32}}{2^{11}} = 2^{21} = 2097152$

Einträge indirekte Seitentabelle: $\frac{256 \cdot 1024^2}{2 \cdot 1024} = 131072$