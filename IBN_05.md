Betriebssysteme und Netzwerke (IBN)

# Übungsblatt 5

## Aufgabe 1

a)

Die Seitengröße von 1 KB entspricht nach JEDEC-Standard 1024 B.

Minmales $M$ damit bei jeder Iteration eine neue Seite benötigt wird: $\frac{4 KB}{4 B} = \frac{4 \cdot 1024 B}{4 B} = 1024$

Dafür muss $N > M$ und $N, M \in \mathbb{N}$ sein.

b)

Die Antwort würde anders ausfallen, da die letzen Einträge nach der Am-wenigsten-Zuletzt-Benutzt Strategie (LRU = Least Recently Used) gespeichert werden.

Minimales $M$ damit die Einträge nicht mehr im TLB gespeichert werden: $\frac{4 KB}{4 B} \cdot 64 = \frac{4 \cdot 1024 B}{4 B} \cdot 64 = 1024 \cdot 64 = 65536$

Dafür muss $N > M$ und $N, M \in \mathbb{N}$ sein.

c)

Bonusaufgabe:

Anzahl der Seiten: $\left \lceil \frac{N \cdot 4 \text{B}}{4 \text{KB}} \right \rceil = \left \lceil \frac{N \cdot 4 \text{B}}{4 \cdot 1024 \text{B}} \right \rceil = \left \lceil \frac{N}{1024} \right \rceil$

\newpage

## Aufgabe 2

Die Seitengröße von 1 KiB entspricht nach IEC-Standard 1024 B.

Seitennummer: $\left \lfloor \frac{\text{logische Adresse}}{\text{Seitengröße}} \right \rfloor$

Offset: logische Adresse % Seitengröße

Es ergibt sich folgende Tabelle:

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

\newpage

## Aufgabe 3

Offset: $2 \text{KiB} = 2 \cdot 1024 \text{B} = 2 \cdot 2^{10} \text{B} = 2^{11} \text{B}$

Einträge direkte Seitentabelle: $\frac{2^{32}}{2^{11}} = 2^{21} = 2097152$

Einträge indirekte Seitentabelle: $\frac{256 \cdot 1024^2}{2 \cdot 1024} = 131072$

\newpage

## Aufgabe 4

Die zweistufige Seitentabelle ist ein Baum, somit müssen die Einträge einfach multipliziert werden.

Anzahl Einträge: $2^{9} \cdot 2^{11} = 2^20$

Bonusaufgabe:

Offset: $\frac{2^{32}}{2^{20}} = 2^{12} = 4096 \text{B}$

Seitengröße: $2^{12} \text{B} = 4 \text{KiB}$

\newpage

## Aufgabe 5

\newpage

## Aufgabe 6

a) Seitengröße bis zu 1 GiB im langen Modus.\footnote{https://en.wikipedia.org/wiki/Page\_(computer\_memory)}

b) Der Hauptgrund für die Suche nach kanonischen Adressen, anstatt die oberen Bits stillschweigend zu ignorieren, besteht darin, sicherzustellen, dass die Software mit zukünftiger Hardware, die mehr virtuelle Adressbits unterstützt, vorwärtskompatibel ist.\footnote{https://stackoverflow.com/questions/25852367/x86-64-canonical-address}

\newpage

## Aufgabe 7

\newpage

## Aufgabe 8

Zuerst wird Seite D als Opfer ausgewählt, da der R-Bit Wert 0 beträgt. Dann wird mit dem Second-Chance-Algorithmus Seite B ausgewählt, da es die erste Seite ist.

\newpage

## Aufgabe 9

Code:

\lstinputlisting[language=C]{IBN_05_9.py}

Ausgabe:

\begin{lstlisting}[]
A
7
7 0
7 0 1
0 1 2
0 1 2
0 2 3
0 2 3
0 3 4
0 4 2
4 2 3
2 3 0
2 3 0
2 3 0
2 3 1
2 3 1
2 1 0
2 1 0
1 0 7
1 0 7
1 0 7
B
2
2 3
2 3
2 3 1
2 1 5
2 1 5
2 5 4
2 5 4
5 4 3
5 3 2
5 3 2
5 3 2
\end{lstlisting}
