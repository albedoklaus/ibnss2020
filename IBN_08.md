Betriebssysteme und Netzwerke (IBN)

# Übungsblatt 8

## Aufgabe 1

Code:

\lstinputlisting[language=Python]{IBN_08_1.py}

Quelle: https://de.wikipedia.org/wiki/Bankieralgorithmus

Ausgabe:

\begin{lstlisting}[]
1 [3, 2, 2]
2 [3, 3, 3]
0 [3, 3, 3]
(True, [1, 2, 0])
\end{lstlisting}

Entsprechend muss die Reihenfolge P2, P3, P1 sein, sodass es nicht zu einer Verklemmung kommt.

Wird eine andere Reihenfolge gewählt, zum Beispiel P1, P3, P2, dann kommt es zu einem Deadlock, da vor Beenden der Prozesse Ressourcen benötigt werden, die wiederum durch andere Prozesse erst freigegeben werden müssten. Auch der Bankieralgorithmus findet unter Umständen keine Lösung.

\newpage

## Aufgabe 2

Die *Heartbeat*-Erweiterung RFC 6520 testet sichere TLS / DTLS-Kommunikationsverbindungen, indem ein Computer an einem Ende einer Verbindung eine *Heartbeat*-Anforderungsnachricht senden kann, die aus einer Nutzlast, normalerweise einer Textzeichenfolge, zusammen mit der Länge der Nutzlast als 16-Bit-Ganzzahl besteht. Der empfangende Computer muss dann genau die gleiche Nutzlast an den Absender zurücksenden.

Von dem Namen *Hearbeat* wurde für die Sicherheitslücke der Name *Heartbleed* abgeleitet, da mehr Informationen als nur ein Lebenszeichen übergeben werden können.

Die betroffenen Versionen von OpenSSL weisen einen Speicherpuffer für die zurückzugebende Nachricht basierend auf dem Längenfeld in der anfordernden Nachricht zu, unabhängig von der tatsächlichen Größe der Nutzdaten dieser Nachricht. Aufgrund dieses Fehlers bei der ordnungsgemäßen Überprüfung der Grenzen besteht die zurückgegebene Nachricht aus der Nutzlast, möglicherweise gefolgt von dem, was sich sonst noch im zugewiesenen Speicherpuffer befindet.

\newpage

## Aufgabe 3

\newpage

## Aufgabe 4

\newpage

## Aufgabe 5

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

\newpage

## Aufgabe 11

\newpage

## Aufgabe 12
