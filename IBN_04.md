Betriebssysteme und Netzwerke (IBN)

# Übungsblatt 4

## Aufgabe 1

a) `files_struct` enthält Informationen zu allen Dateien, die ein Prozess verwendet und enthält Zeiger auf **bis zu 256 Dateidatenstrukturen**, von denen jede eine Datei beschreibt, die von diesem Prozess verwendet wird.
Heutiges System: Maximale Anzahl offener Dateien: 8192, aber maximal 1024 pro Prozess bzw. pro User. Die Gesamtanzahl kann im `/proc/sys/fs/file-max` angepasst werden. Root kann per »ulimit« den Wert erhöhen.\footnote{https://www.nextop.de/linuxfibel/limits.htm\#datei}

b)

\begin{lstlisting}[language=C,firstnumber=912]
	/* Open file information: */
	struct files_struct		*files;
\end{lstlisting}

c) `Z. 936 - Z. 975`\footnote{https://elixir.bootlin.com/linux/v5.6.13/source/include/linux/fs.h\#L936}, geschätzter Speicherbedarf: $4*24$ Bytes $=96$ Bytes.

d) Der Dateidescriptor findet sich in `Z. 977 struct file_handle`. Das hängt vermutlich mit dem durch einen mutex geschützten Bereich im `struct file` zusammen.

## Aufgabe 2

Unser Code:

\lstinputlisting[language=C]{IBN_04_2.c}

Beispielausgabe:

\begin{lstlisting}[]
Unencrypted: Hello Corona 2020!
Encrypted: Mjqqt%Htwtsf%7575&
\end{lstlisting}

## Aufgabe 3

a) Die Fragmentierung heißt "Huge Page Fragmentation". Sie tritt auf, wenn eine Page nicht ans Betriebssystem zurückgegeben werden kann, da sie durch ein long-lived object benutzt wird. Dies ist kein Problem bei "normalen" Pages von beispielsweise 4 KiB, da dort die Wahrscheinlichkeit pro Seite sehr gering ist, dass ein long-lived object enthalten ist, und kann ignoriert werden. Bei huge pages von beispielsweise 2 MiB steigt die Wahrscheinlichkeit allerdings auf fast 100 %.

b)

## Aufgabe 4

a) 

- Mindestgröße: Adressraum - Offset + mind. 4 Bits Seitenattribute: $26 - 12 + 4 = 18$ Bit. Da Einträge immer ganze Bytes sind also $\approx 24$ Bit $=3$ Byte.

- Anzahl Einträge: Adressraum - Seitengröße: $2^{26} - 2^{10} = 2^{16} = 65536$.

- Mindestgröße der Seitentabelle: $3 * 65536 = 192$ kB.

b)

Analog zu Blatt 1:

|                      | Wahrscheinlichkeit                                            |
| -------------------- | ------------------------------------------------------------- |
| Page hit             | $\frac{65536} {\frac{2^{26}}{8}} = 0.0078125 \approx 0.78 \%$ |
| Page miss TLB hit    | $\frac{64}{\frac{2^{26}}{8}} = 9.5367431640625e-07$           |
| Page miss TLB Miss   | $\approx 99.22 \%$                                            |

Erwartete Zugriffszeit:

\begin{align*}
t_{ave} & = 0.9922 \cdot 1 \mu s + 0.0078 \cdot 0.5 \mu s \\
        & \approx 0.9961 \mu s
\end{align*}

c)

Die meisten Prozesse greifen sehr oft auf wenige Adressen zu, wodurch der kleine TLB seine Berechtigung erhält.

## Aufgabe 5

a) Matrikelnummer entspricht Seitennummer, Wohnadresse entspricht Rahmennummer, Verzeichnis entspricht Seitentabelle. Das Offset in diesem Fall wäre die Zimmernummer im Wohnheim. (Wir nehmen an, dass wir Matrikelnummern - und damit anteilmäßig auch deren Offset - passend zu den Zimmernummer vergeben können, was in der Realität nicht der Fall ist.)

b) Es gibt etwa $\frac{4800}{65} = 73.8$ Studierende pro Wohnheim. Für unsere Analogie verwenden wir daher 4-stellige Matrikelnummern: Die ersten beiden Ziffern der Matrikelnummer ($p \in [00, 99]$) beschreiben die Wohnheimadresse ($f$), die jeweils letzten beiden Ziffern beschreiben die Zimmernummer (Offset). Wir können also alles von 0000 bis 9999 darstellen, was 10000 Einträgen entspricht. Der Anteil an relevanten Einträgen ist also $\frac{4800}{10000} = 48\%$.

c) Mit einer invertierten Seitentabelle indizieren wir nur Matrikelnummern, die auch einem Zimmer zugeordnet sind. Das Verzeichnis wäre also maximal 65 Einträge lang. Die Übersetzung wäre somit $\frac{100}{65} \approx 1.5$ mal effizienter.
