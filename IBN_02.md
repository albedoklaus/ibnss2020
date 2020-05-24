Betriebssysteme und Netzwerke (IBN)

# Übungsblatt 2

## Aufgabe 1

- ```bash
$ ./test &
[1] 2914
$ ./test
^Z
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

\newpage

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

- In `man ps` finden wir folgende Beschreibungen für die uns
  vorliegenden Prozessstatus:

  - `S`: Prozess schläft, wartet auf Ereignis und kann unterbrochen
    werden
  - `s`: Dieser Prozess der Sitzungsführer der Shell-Sitzung
  - `Z`: Prozess ist terminiert aber vom Elternprozess noch nicht
    geerntet
  - `T`: Prozess durch Kontrollsignal beendet
  - `R`: Prozess läuft gerade
  - `+`: Prozess wird im Vordergrund ausgeführt

\newpage

## Aufgabe 2

Ein Prozess ist die konkrete Instanziierung eines Programms zur
Laufzeit. Er wird vom Betriebssystem kontrolliert, welches ihn durch
bestimmte Aktionen in verschiedene Zustände setzten kann. Die
Prozesse werden vom Prozess-Scheduler des Betriebssystems verwaltet.
Dieser kann einen Prozess entweder so lange laufen lassen, bis er
endet oder blockiert, oder dafür sorgen, dass nach jeweils einer
kurzen Zeitdauer der gerade ablaufenden Prozess unterbrochen wird,
und der Scheduler so zwischen verschiedenen aktiven Prozessen
hin und her wechseln kann. Eine nebenläufige Ausführungseinheit
innerhalb eines Prozesses wird Thread genannt. Meistens werden
nicht Prozesse nebenläufig ausgeführt, sondern nur dessen Threads.

\newpage

## Aufgabe 3

- Nur eine Möglichkeit der Ausführungsreihenfolge für den
  Anfangsteil, wenn Bibliotheken geladen werden und die Thread-Routine
  und in der `main` Funktion lokale Variablen definiert werden.

\lstinputlisting[language=C,lastline=19]{IBN_02_a2.c}

- Es folgt die Erstellung der Threads, wobei laut Aufgabenstellung
  angenommen wird, dass jede Iteration vollständig abläuft, also
  also atomic anzusehen ist. Nach Ablauf einer
  Iteration kann jedoch die Task-Routine eines
  bereits erstellten Threads dazwischenkommen, was man zum Beispiel
  am `printf` Befehl aus `TaskCode` auf der Konsole sieht.

\lstinputlisting[language=C,firstnumber=20,firstline=20,lastline=25]{IBN_02_a2.c}

- Abschließend wird auf die Beendigung der Threads gewartet. Hier
  ist die Reihenfolge durch den Verlauf von `i` gegeben und es gibt
  nur eine Möglichkeit.

\lstinputlisting[language=C,firstnumber=26,firstline=26]{IBN_02_a2.c}

- Man kann insgesamt also 15 verschiedene Fälle unterscheiden:

Fall 1)

```none
In main: creating thread 1
In main: creating thread 2
In main: creating thread 3
It's me, dude! I am number 1!
It's me, dude! I am number 2!
It's me, dude! I am number 3!
```

Fall 2)

```none
In main: creating thread 1
In main: creating thread 2
In main: creating thread 3
It's me, dude! I am number 1!
It's me, dude! I am number 3!
It's me, dude! I am number 2!
```

Fall 3)

```none
In main: creating thread 1
In main: creating thread 2
In main: creating thread 3
It's me, dude! I am number 2!
It's me, dude! I am number 1!
It's me, dude! I am number 3!
```

Fall 4)

```none
In main: creating thread 1
In main: creating thread 2
In main: creating thread 3
It's me, dude! I am number 2!
It's me, dude! I am number 3!
It's me, dude! I am number 1!
```

Fall 5)

```none
In main: creating thread 1
In main: creating thread 2
In main: creating thread 3
It's me, dude! I am number 3!
It's me, dude! I am number 1!
It's me, dude! I am number 2!
```

Fall 6)

```none
In main: creating thread 1
In main: creating thread 2
In main: creating thread 3
It's me, dude! I am number 3!
It's me, dude! I am number 2!
It's me, dude! I am number 1!
```

Fall 7)

```none
In main: creating thread 1
In main: creating thread 2
It's me, dude! I am number 1!
In main: creating thread 3
It's me, dude! I am number 2!
It's me, dude! I am number 3!
```

Fall 8)

```none
In main: creating thread 1
In main: creating thread 2
It's me, dude! I am number 1!
In main: creating thread 3
It's me, dude! I am number 3!
It's me, dude! I am number 2!
```

Fall 9)

```none
In main: creating thread 1
In main: creating thread 2
It's me, dude! I am number 1!
It's me, dude! I am number 2!
In main: creating thread 3
It's me, dude! I am number 3!
```

Fall 10)

```none
In main: creating thread 1
In main: creating thread 2
It's me, dude! I am number 2!
In main: creating thread 3
It's me, dude! I am number 1!
It's me, dude! I am number 3!
```

Fall 11)

```none
In main: creating thread 1
In main: creating thread 2
It's me, dude! I am number 2!
In main: creating thread 3
It's me, dude! I am number 3!
It's me, dude! I am number 1!
```

Fall 12)

```none
In main: creating thread 1
In main: creating thread 2
It's me, dude! I am number 2!
It's me, dude! I am number 1!
In main: creating thread 3
It's me, dude! I am number 3!
```

Fall 13)

```none
In main: creating thread 1
It's me, dude! I am number 1!
In main: creating thread 2
In main: creating thread 3
It's me, dude! I am number 2!
It's me, dude! I am number 3!
```

Fall 14)

```none
In main: creating thread 1
It's me, dude! I am number 1!
In main: creating thread 2
In main: creating thread 3
It's me, dude! I am number 3!
It's me, dude! I am number 2!
```

Fall 15)

```none
In main: creating thread 1
It's me, dude! I am number 1!
In main: creating thread 2
It's me, dude! I am number 2!
In main: creating thread 3
It's me, dude! I am number 3!
```

Ausgabe A und B sind beides mögliche Ausgaben des auf den Folien
vorgestellten Codes. Die Ausführungsreihenfolge der Threads ist
nicht garantiert gleich der Erstellungsreihenfolge. Allerdings
ist das Programm so ausgelegt, dass die Daten für einen Thread
einzeln gespeichert und übergeben werden. Es werden also keine
Daten übersprungen und alle Nummern genau ein Mal angezeigt.

Ausgabe C hätte passieren können, wenn die Daten (Argumente) für die
einzelnen Threads nicht separat gespeichert werden. Falls also
`thread_args` kein Array wäre, dessen einzelne Elemente
(beziehungsweise genauer gesagt die Adresse der einzelnen Elemente)
an den Thread übergeben werden, sondern eine simple einzelne
Variable vom Typ Integer - denn dann könnte sich der Wert von
`thread_args` bereits geändert haben bis `printf` innerhalb der
Thread-Routine ausgeführt wird. In
der Folge können mehrere Thread-Routinen denselben Wert lesen und
ausgeben - genau wie in Ausgabe C zu sehen.

\newpage

## Aufgabe 4

Siehe folgenden Python-(Pseudo-)Code:

\lstinputlisting[language=Python,firstline=1,lastline=29]{IBN_02_a4.py}

\newpage

## Aufgabe 5

a) Wenn `wait` und `signal` vertauscht werden, beginnt die Routine mit `signal`, `S` wird
   über den Initialwert hinaus inkrementiert und es wartet keiner der Prozesse/Threads.
   Folglich ist die kritische Section nicht geschützt und wird parallel ausgeführt.
   Anschließend wird bei `wait` nicht gewartet wegen der vorherigen zusätzlichen
   Inkrementierung von `S` und der Zyklus beginnt von vorne. Man kann also sagen, dass sich
   die Routine so verhält, als wäre überhaupt kein Semaphor implementiert. Eine Ausnahme
   könnte sein, wenn durch das zusätzliche Inkrementieren die Grenze des Datentyps von `S`
   erreicht wird, siehe "Integer Overflow". Dann könnte der Wert in einen negativen Bereich
   oder Null springen und es kommt möglicherweise zu einem Deadlock.

b) Wird `signal` durch `wait` ersetzt, kommt es zu einem Deadlock, denn es gibt dann keine
   Möglichkeit mehr `S` zu inkrementieren und andere Threads/Prozesse aus der Warteschlange
   zu holen. Die bis dahin ausgeführten Befehle der critical section sind zwar
   geschützt - passieren aber eben nur ein Mal.

c) - Wird der Aufruf von `wait` ausgelassen, dann wartet keiner der Prozesse/Threads und geht
     sofort in die critical section über. Diese ist also nicht geschützt. Anschließend wird `S`
     inkrementiert, was aber keine Rolle spielt, da sowieso kein `wait` und damit keine Abfrage
     des Werts von `S` vorhanden ist. Der Code verhält sich so, als wäre kein Semaphor implementiert.
   - Wird der Aufruf von `signal` ausgelassen, wird `S` nicht mehr inkrementiert. Dieser Fall
     verhält sich identisch zu b), da es keine Rolle spielt, ob nun `signal` ausgelassen wird
     oder durch `wait` ersetzt wird, was direkt der nächste Befehl im nächsten Zyklus wäre.

\newpage

## Aufgabe 6

a) Man muss die Bedingungsvariablen selbst verwalten. Bei einem Semaphor enthält der Semaphor selbst den Zähler. Im Gegensatz zu einem Lock kann der Semaphor sowohl für Mutex (mutual exclusion) als auch Synchronisierung verwendet werden. Bedingungsvariable merkt sich das Signal nicht, es kann also sein, dass ein Thread "für immer" wartet. Die Lösung ist eine Zustands-/Bedingungsvariable, die "done" speichert und so der Zustand (das Signal) gemerkt werden kann.
b) Sonst kann es zu "Naked notify" kommen - einer Race condition.

\newpage

## Aufgabe 7

- Es wird unterschieden zwischen "Long term memory" vs "working memory". Beim "working memory" geht es darum, was man im Moment gerade im Gehirn verarbeitet wird. Es kann etwa 4 "chunks of information" enthalten. Informationen können gruppiert werden, sodass die Anzahl an Informationen größer erscheinen kann. Das "long term memory" ist wie ein Lagerhaus, wo sehr, sehr viel Platz zur Verfügung steht und Artikel (Informationen) an verschiedenen Stellen abgelegt werden können. Das kann allerdings auch zu Durcheinander führen und man muss den Weg durch das Lagerhaus trainieren um schnell und effektiv zur Information zu gelangen.
- Das "working memory" verhält sich bezüglich Größe, Geschwindigkeit und Flüchtigkeit etwa wie ein CPU-Register oder CPU-Cache, wohingegen das "long term memory" sich eher wie ein Speichermedium wie Festplatte oder SSD verhält. (RAM wäre irgendwo dazwischen, denn Information im Arbeitsspeicher kann heute in großen Menge abgelegt werden - mehrere Gigabytes - geht dann aber beim Ausschalten des Computers verloren.)
- Die Einheiten werden "Chunks of information" genannt. Nur etwa 4 Einheiten im "working memory". (Informationen können gruppiert werden, sodass die Anzahl an Informationen größer erscheinen kann.) Im "long term memory" Milliaren von Einheiten.
- Wenn die Informationen im "Lagerhaus" gut zugänglich sind (also trainiert wurden) können sie sehr schnell ins "working memory" übertragen werden. Die Informationen können aber auch versteckt sein und müssen dann öfter "aufgerufen" werden um den Pfad zur Information zu lernen. Eine vorgestellte Methode ist "Spaced Repetition": Informationen sollen vom "working memory" ins "long term memory" übertragen und dazu in immer größer werdenden Abständen wiederholt werden um den "Pfad zur Speicherstelle" im "long term memory" zu trainieren. Es bringt dabei nichts, viele Wiederholungen in einen kurzen Zeitraum zu packen - die zeitlichen Abstände sind wichtig für die Effizienz.
