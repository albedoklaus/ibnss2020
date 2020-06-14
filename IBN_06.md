Betriebssysteme und Netzwerke (IBN)

# Übungsblatt 6

## Aufgabe 1

\newpage

## Aufgabe 2

\newpage

## Aufgabe 3

- Symlinks/Softlinks werden erstellt mit:

\begin{lstlisting}[]
ln -s /Pfad/zur/originalen/Datei /Pfad/für/den/neuen/Symlink
\end{lstlisting}

Wird die originale Datei gelöscht, zeigt der Symlink "ins Leere". Die
Datei wurde aus dem Dateisystem entfernt und es existiert keine Referenz
für den Originalpfad mehr. Wird unter dem Originalpfad wieder eine Datei
angelegt, funktioniert der Symlink wieder.

- Hardlinks werden erstellt mit:

\begin{lstlisting}[]
ln /Pfad/zur/originalen/Datei /Pfad/für/den/neuen/Hardlink
\end{lstlisting}

(Alternativ funktioniert auch `cp --link`.)

Beide Dateinamen referenzieren dieselbe Datei im Dateisystem und sind
gleichwertig. Wird die Datei unter dem Originalpfad bearbeitet, ist die
Änderung auch am Hardlinkpfad sichtbar und andersherum. Wird jedoch einer
der Dateinamen gelöscht, besteht durch den jeweils anderen Dateinamen noch
eine Referenz auf die Datei im Dateisystem. Wird also die originale Datei
gelöscht, ändert sich am Hardlink nichts.

\newpage

## Aufgabe 4

\newpage

## Aufgabe 5

\newpage

## Aufgabe 6

Der Befehl `cd .` kann dazu benutzt werden, den aktuellen Status des aktuellen
Verzeichnisses herauszufinden. Wurde das Verzeichnis zwischenzeitlich gelöscht,
erscheint folgender Fehler:

\begin{lstlisting}[]
$ cd .
cd: error retrieving current directory: getcwd: cannot access parent directories: No such file or directory
\end{lstlisting}

Ist das Verzeichnis noch vorhanden, funktioniert `cd .` ohne Probleme und es
erscheint kein Fehler.

\newpage

## Aufgabe 7

\newpage

## Aufgabe 8

Im RAID 0 System werden beide Festplatten gemeinsam im Verbundsystems
genutzt. Daten sind auf beide Festplatten verteilt. Es gibt keine
Redundanz. Fällt eine der beiden Festplatten aus, so ist das ganze
System betroffen. Entsprechend kann man ausrechnen mit welcher
Wahrscheinlichkeit, das System keinen Ausfall hat und diesen Wert von
1 abziehen: $1 - (1 - p)^n$. Für $p = 0.1$ Ausfallwahrscheinlichkeit
einer Festplatte und $n = 2$ Festplatten erhalten wir eine
Gesamtausfallwahrscheinlichkeit des Systems von
$1 - (1 - 0.1)^2 = 1 - 0.9^2 = 1 - 0.81 = 0.19$.

Im RAID 1 System werden die Daten auf beide Festplatten gespiegelt. Es
gibt also eine einfache Redundanz. Fällt eine der beiden Festplatten aus,
so ist das System nicht betroffen, sofern die andere Festplatte noch
funktioniert. Erst wenn die zweite Festplatte auch ausfällt, ist das
System betroffen. Entsprechend muss die Kombination aller
Ausfallswahrscheinlichkeiten berechnet werden: $p^n$.
Für $p = 0.1$ Ausfallwahrscheinlichkeit
einer Festplatte und $n = 2$ Festplatten erhalten wir eine
Gesamtausfallwahrscheinlichkeit des Systems von $0.1^2 = 0.01$.

Durch weitere Festplatten im RAID 0 System erhöht sich die
Gesamtausfallwahrscheinlichkeit des Systems:

$1 - (1 - p)^n \xrightarrow{n \to \infty} 1$

Durch weitere Festplatten im RAID 1 System kann die Redundanz weiter
erhöht werden:

$p^n \xrightarrow{n \to \infty} 0$

\newpage

## Aufgabe 9

Falls der Controller des RAID 1 Systems es unterstützt, können die
angeforderten Daten von mehreren Festplatten gleichzeitig gelesen
werden, da ja auf allen Festplatten derselbe Inhalt gespeichert ist.
(Dabei muss natürlich darauf verzichtet werden, fehlerhaften Sektoren,
also Differenzen zwischen den einzelnen Festplatten, detektieren zu
können.) Es sollte also konstant die n-fache Lesegeschwindigkeit
erreicht werden.

Das kann unter Umständen schneller als ein RAID 0 System sein, da
bei diesem System die einzelnen "Stripes" zu den angeforderten Daten
auf derselben Festplatte (und *nur* auf dieser Festplatte) liegen
können - und nacheinander (mit entsprechend langsamerer
Lesegeschwindigkeit) gelesen werden müssen.
