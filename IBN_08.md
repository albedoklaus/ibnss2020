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

Von dem Namen *Heartbeat* wurde für die Sicherheitslücke der Name *Heartbleed* abgeleitet, da mehr Informationen als nur ein Lebenszeichen übergeben werden können.

Die betroffenen Versionen von OpenSSL weisen einen Speicherpuffer für die zurückzugebende Nachricht basierend auf dem Längenfeld in der anfordernden Nachricht zu, unabhängig von der tatsächlichen Größe der Nutzdaten dieser Nachricht. Aufgrund dieses Fehlers bei der ordnungsgemäßen Überprüfung der Grenzen besteht die zurückgegebene Nachricht aus der Nutzlast, möglicherweise gefolgt von dem, was sich sonst noch im zugewiesenen Speicherpuffer befindet.

\newpage

## Aufgabe 3

Es lassen sich sogenannte "guard pages" verwenden, die um den geschützten Speicherbereich herum angeordnet werden. Ein Buffer overflow und damit verbundenener Leseversuch anderer Stacks führt entsprechend zu einem segmentation fault, was wiederum zu einem Programmabsturz führt.

\newpage

## Aufgabe 4

Das Passwort wird "gesalzen" (mit dem Salt verbunden) in die Hashfunktion gegeben. Diese Funktion ist eine "one-way function" - kann also nicht umgekehrt werden. Bei aktuellen Hashfunktionen kann man also davon ausgehen, dass man sich zum Lösen in der Größenordnung der Dauer eines Brute-Force-Angriffs befindet. Eine Angriffsmöglichkeit ist also, nicht für jeden einzelnen Hashwert einen Brute-Force-Angriff auszuführen, sondern stattdessen sogenannte "Rainbow-Tables" zu verwenden, wo passend zum Hashwert mögliche Eingabewerte angegeben sind.

Solche "Rainbow-Tables" müssen umso umfangreicher werden, je länger der Salt ist. (Und existieren deshalb nicht für lange Salts.) Deshalb ist es wichtig, dass der Salt lang genug gewählt wird. 12 bit sind heute nicht mehr ausreichend.

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
