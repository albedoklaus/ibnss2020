Betriebssysteme und Netzwerke (IBN)

# Übungsblatt 1

## Aufgabe 1

Für Version `v5.7-rc5` Zeile 632 in `include/linux/sched.h`: https://github.com/torvalds/linux/blob/v5.7-rc5/include/linux/sched.h#L632

Die Definition ist in Zeile 1307 beendet.

\lstinputlisting[language=Python]{IBN_03_1count.py}

Wir schätzen den Speicherbedarf auf `268 * 8 = 2144` Bytes.

\newpage

## Aufgabe 2

Eine Forkbomb, auch Rabbit genannt, ist ein Programm, dessen einziger Zweck es ist, rekursiv Kopien seiner selbst zu starten, alle verfügbaren Systemressourcen zu verbrauchen und so das System zu blockieren. Unter Unix geschieht das im einfachsten Fall mit dem Aufruf des Systemcalls fork in einer Endlosschleife.

In Pseudocode sieht eine Forkbomb etwa so aus:

ProgrammX {
  Rufe ProgrammX auf;
  Rufe ProgrammX auf;
  Warte bis ProgrammX beendet wurde;
}

Das Programm ruft zwei Kopien seiner selbst auf und wartet, bis sie wieder beendet wurden. Dieser Zustand wird jedoch niemals erreicht werden, da die Kopien genauso verfahren. Aus einem Programmaufruf werden somit zunächst 2, dann 4, dann 8 und nach nur 10 solcher Zyklen sind bereits über tausend Kopien gestartet und aktiv. Allgemein lässt sich festhalten, dass nach n Zyklen 2n Prozesse erzeugt worden sind, ihre Anzahl also exponentiell zunimmt. Diese verbrauchen, selbst wenn sie keinen komplizierten Code enthalten, CPU-Zeit und Speicher zur Verwaltung durch das Betriebssystem. Ein normaler Betrieb beziehungsweise normales Arbeiten ist bereits wenige Sekunden nach Aufruf der Forkbomb nicht mehr möglich.

Der konkrete Effekt einer Forkbomb hängt in erster Linie von der Konfiguration des Betriebssystems ab. Beispielsweise erlaubt PAM auf Unix- und Unix-ähnlichen Betriebssystemen die Zahl der Prozesse und den maximal zu verbrauchenden Speicher pro Benutzer zu beschränken. „Explodiert“ eine Forkbomb auf einem System, welches diese Möglichkeiten der Beschränkung nutzt, scheitert irgendwann der Versuch, neue Kopien der Forkbomb zu starten und das Wachstum ist eingedämmt.

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
 Kindprozess: 12
 Kindprozess: 13
 Elternprozess: 10
 Kindprozess: 14
 Elternprozess: 15
 Kindprozess: 16
 Kindprozess: 18
 Elternprozess: 17
 Kindprozess: 19
 Elternprozess: 20
 Kindprozess: 21
 Elternprozess: 22
 Kindprozess: 23
 Kindprozess: 25
 Kindprozess: 26
 Kindprozess: 27
 Elternprozess: 24
 Kindprozess: 28
 Kindprozess: 30
 Elternprozess: 29
 Kindprozess: 31
 Elternprozess: 32
 Kindprozess: 33
 Kindprozess: 35
 Kindprozess: 36
 Elternprozess: 34
 Kindprozess: 37
 Elternprozess: 38
 Kindprozess: 39
[...]
```

Erklärung:

\newpage

## Aufgabe 6
