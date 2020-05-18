Betriebssysteme und Netzwerke (IBN)

# Übungsblatt 1

## Aufgabe 1

Für Version `v5.7-rc5` Zeile 632 in `include/linux/sched.h`: https://github.com/torvalds/linux/blob/v5.7-rc5/include/linux/sched.h#L632

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

\newpage

## Aufgabe 4

\newpage

## Aufgabe 5

\lstinputlisting[language=C]{IBN_03_a5.c}

Merkwürdiger Output:

```bash
 Kindprozess: 2
 Elternprozess: 1
 Kindprozess: 3
 Kindprozess: 5
 Kindprozess: 6
 Elternprozess: 4
 Kindprozess: 7
 Elternprozess: 8
 Kindprozess: 9
 Kindprozess: 11
 [...]
 Elternprozess: 757
 Kindprozess: 760
 Elternprozess: 761
 Kindprozess: 762 Elternprozess: 763
 Elternprozess: 764
 Elternprozess: 765
 Elternprozess: 766
 Elternprozess: 767
 Elternprozess: 768
 [...]
```

Erklärung:

\newpage

## Aufgabe 6

a) Mehr Schreibarbeit.

b) Beispiel aus der Vorlesung:

```bash
ls –R | grep –ci '\.jpg$'
```

Umgeschrieben:

```bash
mkfifo mypipe
ls –R  > mypipe &
grep –ci '\.jpg$' < mypipe
```

c) Eigenes Beispiel:

```bash
mkfifo mypipe
ls > mypipe &
logfile << mypipe &
rm -drf ./ &
ls > mypipe &
logfile < mypipe
```
