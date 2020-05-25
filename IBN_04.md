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

## Aufgabe 4

## Aufgabe 5

a) Matrikelnummer entspricht Seitennummer, Wohnadresse entspricht Rahmennummer, Verzeichnis entspricht Seitentabelle. Das Offset in diesem Fall wäre die Zimmernummer im Wohnheim. (Wir nehmen an, dass wir Matrikelnummern - und damit anteilmäßig auch deren Offset - passend zu den Zimmernummer vergeben können, was in der Realität nicht der Fall ist.)

b) Es gibt etwa 4800 / 65 = 73,8 Studierende pro Wohnheim. Für unsere Analogie verwenden wir daher 4-stellige Matrikelnummern: Die ersten beiden Ziffern der Matrikelnummer ($p \in [00, 99]$) beschreiben die Wohnheimadresse ($f$), die jeweils letzten beiden Ziffern beschreiben die Zimmernummer (Offset). Wir können also alles von 0000 bis 9999 darstellen, was 10000 Einträgen entspricht. Der Anteil an relevanten Einträgen ist also 4800 / 10000 = 48%.

c) Mit einer invertierten Seitentabelle indizieren wir nur Studenten, die auch ein Zimmer belegen. Das Verzeichnis wäre also maximal 65 Einträge lang. Die Übersetzung wäre somit $\frac{64}{99}\cdot100 \approx 64.65%$ effizienter.
