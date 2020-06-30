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

Es lassen sich sogenannte "guard pages" verwenden, die um den geschützten Speicherbereich herum angeordnet werden. Ein Buffer overflow und damit verbundenener Leseversuch anderer Stacks (und damit eventuell ein Zugriff auf sensible Daten) führt entsprechend zu einem segmentation fault, was wiederum zu einem Programmabsturz führt.

\newpage

## Aufgabe 4

Das Passwort wird "gesalzen" (mit dem Salt verbunden) in die Hashfunktion gegeben. Diese Funktion ist eine "one-way function" - kann also nicht umgekehrt werden. Bei aktuellen Hashfunktionen kann man also davon ausgehen, dass man sich zum Lösen in der Größenordnung der Dauer eines Brute-Force-Angriffs befindet. Eine Angriffsmöglichkeit ist also, nicht für jeden einzelnen Hashwert einen Brute-Force-Angriff auszuführen, sondern stattdessen sogenannte "Rainbow-Tables" zu verwenden, wo passend zum Hashwert mögliche Eingabewerte angegeben sind.

Solche "Rainbow-Tables" müssen umso umfangreicher werden, je länger der Salt ist. (Und existieren deshalb nicht für lange Salts.) Deshalb ist es wichtig, dass der Salt lang genug gewählt wird. 12 bit sind heute nicht mehr ausreichend.

\newpage

## Aufgabe 5

Um eine bestimmte Anzahl (beispielsweise 1000) Passwörter zum Einloggen zur Verfügung zu stellen, wird ein Initialpasswort $x$ und eine Einwegfunktion $F$ verwendet. $F^{1000}(x)$ muss für die erste Authentifizierung vorher auf dem Server abgelegt werden. Danach kann sich der Benutzer mit $F^{999}(x)$ einloggen, da $F(F^{999}(x)) = F^{1000}(x)$ ist, was ja genau der Wert ist, der dem Server bekannt ist und damit zur Überprüfung des gesendeten Passworts verwendet werden kann. Das gesendete Passwort $F^{999}(x)$ ist danach wiederum der Hash für das nächste Passwort $F^{998}(x)$ und so weiter - bis $x$ erreicht ist.

Es muss dabei die Reihenfolge $F^{1000}(x), F^{999}(x), ..., F^{1}(x)$ für die Hashes und $F^{999}(x), F^{998}(x), ..., x$ für die Passwörter verwendet werden (und nicht $F^{1}(x), F^{2}(x), ..., F^{1000}(x)$ beziehungsweise $x, F^{1}(x), ..., F^{999}(x)$), da die Rückrichtung der Einwegfunktion $F$ nicht schnell berechnet werden kann und sonst von einem Angreifer einfach alle nächsten Werte berechnet werden könnten, nachdem ein alter Wert zum Beispiel abgefangen wurde.

\newpage

## Aufgabe 6

Bei der angegebenen Bitrate darf ein CBR-kodiertes, einminütiges Video eine Größe von 40.8 $\frac{\text{kB}}{\text{s}} \cdot$ 60 s = 2448 kB nicht überschreiten.

Wir verwenden zum Testen folgendes Skript:

\lstinputlisting[language=bash]{IBN_08_6.sh}

Ausgabe:

\begin{lstlisting}[]
2144741 full_resolution.mp4
    Stream #0:0(und): Video: h264 (High) (avc1 / 0x31637661), yuv420p, 1280x720 [SAR 1:1 DAR 16:9], 206 kb/s, 23.98 fps, 23.98 tbr, 24k tbn, 47.95 tbc (default)
2347366 scaled.mp4
    Stream #0:0(und): Video: h264 (High) (avc1 / 0x31637661), yuv420p, 300x168 [SAR 224:225 DAR 16:9], 168 kb/s, 23.98 fps, 23.98 tbr, 24k tbn, 47.95 tbc (default)
\end{lstlisting}

Offensichtlich ist die Dateigröße nur bedingt von der Auflösung abhängig, denn wir können einfach die Bitrate ändern: Bei `full_resolution.mp4` bleiben wir mit 2144741 Bytes unterhalb der Grenze, indem wir die Video- beziehungsweise Audio-Bitrate auf 200K beziehungsweise 64K gesenkt haben - das Video hat allerdings immer noch eine Auflösung von 1280x720. Verwenden wir bei `scaled.mp4` allerdings die Standardeinstellung für die Komprimierung - dann stellen wir fest, dass die Auflösung auf etwa 300x168 gesenkt werden muss.

\newpage

## Aufgabe 7

Die Wahrscheinlichkeit, dass ein bestimmter Benutzer sendet ist $p$. Entsprechend
ist die Wahrscheinlichkeit, dass dieser Benutzer gerade nicht sendet $1-p$. Sind
gerade $X$ Benutzer am senden, kann die Anzahl der Benutzer, die gerade nicht senden,
ausgerechnet werden über die Gesamtanzahl $M$ der Benutzer: $M-X$.

Die kombinierte
Wahrscheinlichkeit dieser Situation aus $X$ sendenden und $M-X$ nicht sendenden
Benutzern ergibt sich zu $p^X \cdot (1-p)^{M-X}$.

Da es jedoch keine Rolle spielt,
in welcher Reihenfolge sich die einzelnen $p$, beziehungsweise $1-p$
Wahrscheinlichkeiten kombinieren (es kann $p^X \cdot (1-p)^{M-X}$, oder
$p^{X-1} \cdot (1-p)^{M-X} \cdot p$ oder $(1-p) \cdot p^{X-1} \cdot (1-p)^{M-X-1} \cdot p$
sein etc.), muss die kombinierte Wahrscheinlichkeit noch mit der Anzahl der Kombinationsmöglichkeiten
multipliziert werden. Diese Anzahl ergibt sich aus dem Binomialkoeffizienten $\binom{M}{X}$.

Als Gesamtwahrscheinlichkeit erhalten wir also: $\binom{M}{X} \cdot p^X \cdot (1-p)^{M-X}$.
Dies ist eine Binomialverteilung, siehe auch [https://de.wikipedia.org/wiki/Binomialverteilung](https://de.wikipedia.org/wiki/Binomialverteilung).

Um nun auszurechnen, wie groß die Wahrscheinlichkeit ist, dass *mindestens* $N$
Benutzer gleichzeitig senden, kann eine Summe der Wahrscheinlichkeiten für
$X=N, X=N+1, ..., X=M$ gebildet werden: $\sum_{X=N}^{M} \binom{M}{X} \cdot p^X \cdot (1-p)^{M-X}$.



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
