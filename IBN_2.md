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
