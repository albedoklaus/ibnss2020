Betriebssysteme und Netzwerke (IBN)

# Übungsblatt 2

## Aufgabe 1

- ```bash
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

  Wir sehen die von uns gestartete bash Shell als PID 2184.

  Zunächst starten wir mit `./test &` das Programm im Hintergrund
  und erhalten den Prozess mit PID 2914. Das Programm forkt und
  wir erhalten einen Kindprozess mit PID 2915. Der Elternprozess
  behält seine PID.

  Im Elternprozess wird das `sleep` ausgeführt und der Prozess ist
  daher für die nächsten 1000 Sekunden im Status `S` für `interruptible
  sleep (waiting for an event to complete)`. Der Kindprozess hingegen
  beendet direkt mit `exit(0)` und wird daher zum Zombie mit Status
  `Z` für `defunct ("zombie") process, terminated but not reaped by its
  parent`. Der Elternprozess kann nicht ernten ("not reaped") da er ja
  gerade schläft.

  Der zweite Aufruf mit `./test` ist der Prozess mit PID 2916. Sofort
  wird - wie schon vorher - ein Kindprozess gestartet mit PID 2917.
  Dieser Kindprozess beendet - ebenfalls wie schon vorher - sofort
  wieder und ist im Zombie-Status. Den Elternprozess unterbrechen wir
  mit `CTRL+Z` durch ein `SIGSTOP` Signal. Der Prozess befindet sich
  daher im Status `T` für `stopped by job control signal`. (Wir haben
  `CTRL+Z` nicht schnell genug gedrückt, um den fork zu verhindern.)
  Mit dem Befehl `bg` (oder `fg`) könnte man den zuletzt gestoppten
  Prozess wieder im Hintergrund (oder Vordergrund) starten und er
  wird fortgesetzt.

- ```bash
$ ps -eH
   ...
      1 ?        00:11:07 systemd
   ...
   2179 ?        00:00:07   xterm
   2184 pts/0    00:00:00     bash
   2914 pts/0    00:00:00       test
   2915 pts/0    00:00:00         test <defunct>
   2916 pts/0    00:00:00       test
   2917 pts/0    00:00:00         test <defunct>
   ...
```

  Bei `...` wurden irrelevante Abschnitte entfernt. Man sieht den
  Wurzelprozess `systemd` mit PID 1 auf der nullten Ebene. Danach
  folgt der Terminal-Emulator `xterm` auf der ersten Ebene. Die
  `bash` Sitzung mit der bekannten PID 2184 vom vorherigen Aufruf
  von `ps` ist die zweite Ebene. Unsere Aufrufe des Test-Programms
  `test` finden folglich in der dritten Ebene statt. Die geforkten
  Kindprozesse in der vierten Ebene.

- `man ps`

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

