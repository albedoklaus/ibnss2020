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