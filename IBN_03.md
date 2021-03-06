Betriebssysteme und Netzwerke (IBN)

# Übungsblatt 3

## Aufgabe 1

Für Version `v5.7-rc5` Zeile 632 in `include/linux/sched.h`:

https://github.com/torvalds/linux/blob/v5.7-rc5/include/linux/sched.h#L632

Die Definition ist in Zeile 1307 beendet.

\lstinputlisting[language=Python]{IBN_03_1count.py}

Wir schätzen den Speicherbedarf auf `268 * 8 = 2144` Bytes.

\newpage

## Aufgabe 2

Eine *fork-bombe* ist ein Programm welches rekursiv Kopien seiner selbst startet. Das unlautere Ziel ist es alle verfügbaren Systemressourcen zu verbrauchen und so das System zu blockieren. Dazu kann z.B. der Systemcall `fork` genutzt werden, daher der Name.

Zutaten:

- Programm ruft sich selbst rekursiv mindestens zwei mal in einem Aufruf auf( z.B. mit fork)
- Dann wartet es bis es beendet wurde (was nicht passiert.)

Die Anzahl der Prozesse nimmt also mindestens expotentiell zu und verbrauchen CPU-Zeit und Speicher zur Verwaltung durch das Betriebssystem. Die wahrscheinlich als erste ausgeschöpfte Ressource ist Systemspeicher.

\newpage

## Aufgabe 3

\lstinputlisting[language=C]{IBN_03_a3.pseudocode}

\newpage

## Aufgabe 4

a)

Der aktualisierte Code:

\lstinputlisting[language=C]{IBN_03_pc2.c}

\newpage

b)

Die Zeit wurde mit folgendem Schnippel gemessen:

\lstinputlisting[language=Python]{IBN_03_a4_zeitmesser.py}

Die Ausgabe:

\begin{lstlisting}
./pc 2.4206025123596193
./pc2 2.409065341949463
\end{lstlisting}

Unsere Optimierung sorgt also für eine deutlich messbare schnellere
Laufzeit des Programms. (Der Hauptteil der Laufzeit fällt natürlich
auf die Berechnung der Fibonacci-Zahlen und ist daher nicht von der
Optimierung betroffen.) Übeträgt man das Producer-Consumer-Problem
auf einen größeren Maßstab, wird klar, dass dieser Laufzeitgewinn
viel ausmachen kann.

\newpage

## Aufgabe 5

Die Erklärungen der Befehle finden sich in den Kommentaren:

\lstinputlisting[language=C]{IBN_03_a5.c}

Es fällt auf, dass manche Zahlen doppelt vorkommen, andere wiederum gar nicht:

\begin{lstlisting}
$ gcc IBN_03_a5.c && ./a.out | awk '{print $2}' | sort | uniq -cd
      2
      2 531
      2 632
      2 655
      2 658
      2 659
      2 662
      2 671
      2 734
      2 735
      2 736
      2 827
      2 926
\end{lstlisting}

Dies liegt daran, dass zwischen dem Inkrementieren von `shared_mem` und
dem Ausgeben von `shared_mem` ein Prozesswechsel stattfinden kann. Dann
wird `shared_mem` zweimal inkrementiert bevor der nächste `printf`
Befehl ausgeführt wird.

Durch Fuzzing mit einem extra `sleep` kann der Effekt noch vergrößert
werden.

\newpage

## Aufgabe 6

a)

- Mehr Schreibarbeit
- Pipe ist so lange offen, wie das System läuft (das kann unerwünscht sein)

b) Beispiel aus der Vorlesung:

\begin{lstlisting}[language=bash]
ls -R | grep -ci '\.jpg$'
\end{lstlisting}

Umgeschrieben:

\begin{lstlisting}[language=bash]
mkfifo mypipe
ls -R  > mypipe &
grep -ci '\.jpg$' < mypipe
\end{lstlisting}

c) Eigenes Beispiel:

\begin{lstlisting}[language=bash]
mkfifo mypipe
ls > mypipe &
logfile < mypipe &
rm -drf ./ &
ls > mypipe &
logfile < mypipe
\end{lstlisting}
