Betriebssysteme und Netzwerke (IBN)

# Übungsblatt 2

## Aufgabe 1

```bash
$ ./test &
[1] 2914
$ ./test
STRG+Z
[2]+  Stopped                 ./test
$ ps T -H
    PID TTY      STAT   TIME COMMAND
   2184 pts/0    Ss     0:00 bash
   2914 pts/0    S      0:00   ./test
   2915 pts/0    Z      0:00     [test] <defunct>
   2916 pts/0    T      0:00   ./test
   2917 pts/0    Z      0:00     [test] <defunct>
   2921 pts/0    R+     0:00   ps T -H
```

`2184`: Der Wurzelprozess die Bash-Shell, in der die weiteren Prozesse gestartet werden. Befindet sich im unterbrechbaren Schlafmodus (`S`, wartet auf Ereignisse). `s` identifiziert sie als Sitzungsleiter.

`2914`: Abgelöster `./test`-Prozess (`$ ./test &`).

`2916`: Abgelöster `./test`-Prozess.

`2915` & `2917`: Gegabelter `$ ./test` defunktionaler ("zombie") Prozess, beendet, aber nicht von den Eltern geerntet.

```bash
$ ps -eH
   ...
   2179 ?        00:00:07   terminal
   2184 pts/0    00:00:00     bash
   2914 pts/0    00:00:00       test
   2915 pts/0    00:00:00         test <defunct>
   2916 pts/0    00:00:00       test
   2917 pts/0    00:00:00         test <defunct>
   ...
```
Meine Sitzung findet in Tiefe null statt.

## Aufgabe 2

Reference: https://de.wikipedia.org/wiki/Prozess_(Informatik)

Ein Prozess (in manchen Betriebssystemen auch Task genannt) ist ein Computerprogramm zur Laufzeit. Genauer ist ein Prozess die konkrete Instanziierung eines Programms zu dessen Ausführung innerhalb eines Rechnersystems, ergänzt um weitere (Verwaltungs-)Informationen und Ressourcenzuteilungen des Betriebssystems für diese Ausführung.

Ein Prozess ist die Ablaufumgebung für ein Programm auf einem Rechnersystem, sowie der darin eingebettete Binärcode des Programmes während der Ausführung. Ein Prozess wird vom Betriebssystem dynamisch kontrolliert durch bestimmte Aktionen, mit denen das Betriebssystem ihn in entsprechende Zustände setzt. Als Prozess bezeichnet man auch die gesamte Zustandsinformation eines laufenden Programms. Im Gegensatz dazu handelt es sich bei einem Programm um die (statische) Verfahrensvorschrift für eine Verarbeitung auf einem Rechnersystem.

Die Prozesse werden vom Prozess-Scheduler des Betriebssystems verwaltet. Dieser kann einen Prozess entweder so lange rechnen lassen, bis er endet oder blockiert (nicht-unterbrechender Scheduler), oder dafür sorgen, dass nach jeweils einer kurzen Zeitdauer der gerade ablaufenden Prozess unterbrochen wird, und der Scheduler so zwischen verschiedenen aktiven Prozessen hin und her wechseln kann (unterbrechender Scheduler), wodurch der Eindruck von Gleichzeitigkeit entsteht, auch wenn zu jedem Zeitpunkt nicht mehr als nur ein Prozess verarbeitet wird. Letzteres ist die vorherrschende Scheduling-Strategie heutiger Betriebssysteme.

Eine nebenläufige Ausführungseinheit innerhalb eines Prozesses wird Thread genannt. Bei modernen Betriebssystemen gehört zu jedem Prozess mindestens ein Thread, der den Programmcode ausführt. Oftmals werden nun nicht mehr Prozesse nebenläufig ausgeführt, sondern nur die Threads innerhalb eines Prozesses.

## Aufgabe 3

TODO

## Aufgabe 4

TODO

## Aufgabe 5

a) Die kritische Section ist nicht geschützt, da das Signal vorher das Freizeichen gibt und erst nach der kritischen Sektion auf Warten setzt.

b) Die kritische Sektion wäre zwar geschützt, allerdings wird die Schließung nicht mehr Freigegeben.

c) Siehe a) und b)

## AUfgabe 6

## Aufgabe 7

TODO
