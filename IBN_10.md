Betriebssysteme und Netzwerke (IBN)

# Übungsblatt 10

## Aufgabe 1

- Consumer schreibt in einen Puffer, Producer liest heraus
- Um sicherzustellen, dass nur ein Prozess auf einmal auf gemeinsam benutzte Ressourcen zugreifen kann, gibt es den Lösungsansatz des wechselseitigen Anschlusses (mutual connection, oft mucon abgekürzt)
- Die zwei Operationen auf einen Semaphore heißen lock und unlock
- Variablen, die anzeigen, dass ein Prozess in einer kritischen Region ist und kein anderer Prozess eintreten darf, nennt man doors

Achtung, alles falsch!

\newpage

## Aufgabe 2

Das TCN-Protokoll basiert auf temporären Kontaktnummern (Temporary Contact Numbers, TCN), halbzufälligen Kennungen, die aus einem Startwert abgeleitet wurden. Wenn sich zwei Clients begegnen, wird ein eindeutiger TCN generiert, ausgetauscht und dann lokal in einem Kontaktprotokoll gespeichert. Sobald ein Benutzer positiv auf eine Infektion getestet hat, wird ein Bericht an einen zentralen Server gesendet. Jeder Client im Netzwerk sammelt dann die Berichte vom Server und überprüft unabhängig seine lokalen Kontaktprotokolle auf einen im Bericht enthaltenen TCN. Wenn eine passende TCN gefunden wird, ist der Benutzer in engen Kontakt mit einem infizierten Patienten gekommen und wird vom Client gewarnt. Da jedes Gerät Kontaktprotokolle lokal überprüft und Kontaktprotokolle daher niemals an Dritte übertragen werden, kann der zentrale Berichtsserver die Identität oder das Kontaktprotokoll eines Clients im Netzwerk nicht selbst ermitteln.

Nachteile: Die Entfernung der Beacons muss über Signalstärke abgeschätzt werden und muss nicht dem tatsächlichen Abstand der Personen entsprechen (und damit einem Infektionsrisiko). Außerdem müssen genug Personen am Programm teilnehmen und im Infektionsfall dann auch tatsächlich ihre Infektionen melden.

\newpage

## Aufgabe 3

\newpage

## Aufgabe 4

\newpage

## Aufgabe 5

Pseudocode für das Geh-Zurück-N-Protokoll:

\begin{lstlisting}[]
N  := window size
Rn := request number
Sn := sequence number
Sb := sequence base
Sm := sequence max

function receiver is
    Rn := 0
    Do the following forever:
        if the packet received = Rn and the packet is error free then
            Accept the packet and send it to a higher layer
            Rn := Rn + 1
        else
            Refuse packet
        Send a Request for Rn

function sender is
    Sb := 0
    Sm := N + 1
    Repeat the following steps forever:
        if you receive a request number where Rn > Sb then
            Sm := (Sm − Sb) + Rn
            Sb := Rn
        if no packet is in transmission then
            Transmit a packet where Sb <= Sn <= Sm.  
            Packets are transmitted in order.
\end{lstlisting}

1. Erste Iteration: $Sm = 4$, Sequenznummernbereich $= k \in {0,1,2,3,4}$

2. KP

\newpage

## Aufgabe 6

\newpage

## Aufgabe 7

\newpage

## Aufgabe 8

\newpage

## Aufgabe 9

\newpage

## Aufgabe 10
