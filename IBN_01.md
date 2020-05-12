Betriebssysteme und Netzwerke (IBN)

# Übungsblatt 1

## Aufgabe 1

Allgemeine Formel für den Erwartungswert einer diskreten reellen
Zufallsvariable:

$$
\operatorname{E}(X)=\sum_{i\in I} x_i p_i=\sum_{i \in I} x_i P(X=x_i)
$$

<!-- https://de.wikipedia.org/wiki/Erwartungswert#Definitionen -->

In unserem Fall ist die diskrete reelle Zufallsvariable gegeben als
erwartete Verzögerung $t_{ave}$ beim Zugriff auf den Speicher. Wir
unterscheiden folgende zwei Fälle:

|            | Wert für $t_{ave}$ | Wahrscheinlichkeit |
| ---------- | ------------------ | ------------------ |
| cache hit  | $t_+ = t_c$        | $p_+$              |
| cache miss | $t_- = t_c + t_r$  | $p_- = 1 - p_+$    |

Dabei ist $t_c$ die Dauer eines Cache-Zugriffs und $t_r$ die Dauer
eines RAM-Zugriffs.

\begin{align*}
\Rightarrow t_{ave} & = \sum_{i \in \{+, -\}} t_i p_i \\
                    & = t_+ p_+ + t_- p_- \\
                    & = t_c p_+ + (t_c + t_r)(1 - p_+) \\
                    & = t_c p_+ + t_c + t_r - t_c p_+ - t_r p_+ \\
                    & = t_c + t_r - t_r p_+ \\
                    & = t_c + t_r (1 - p_+) \\
                    & = t_c + t_r p_-
\end{align*}

Aspekte, die in realen Systemen die Wahrscheinlichkeit $p_+$
beeinflussen könnten:

- Ein größerer Cache könnte $p_+$ erhöhen. Je mehr Daten dort
  gespeichert werden, desto größer die Wahrscheinlichkeit, dass
  die gesuchten Daten vorhanden sind.
- Wiederholter Zugriff desselben Prozesses könnte $p_+$ ebenfalls
  erhöhen. Die benötigten Daten sind vom vorherigen Aufruf immer
  noch im Cache.

\newpage
## Aufgabe 2

Mit $t_c, t_r > 0$ folgt:

\begin{align*}
&                 & t_{ave}           & \leqslant 5 t_c \\
& \Leftrightarrow & t_c + t_r p_-     & \leqslant 5 t_c \\
& \Leftrightarrow & t_c + 100 t_c p_- & \leqslant 5 t_c \\
& \Leftrightarrow & 1 + 100 p_-       & \leqslant 5 \\
& \Leftrightarrow & 100 p_-           & \leqslant 4 \\
& \Leftrightarrow & p_-               & \leqslant 4 \;\% \\
& \Leftrightarrow & p_+               & \geqslant 96 \;\%
\end{align*}

\newpage
Aufgabe 3
---------

Datenregister einer x64-CPU:

| Register   | Größe                                  | Vergleich mit 1 GiB RAM           |
| ---------- | -------------------------------------- | --------------------------------- |
| GPR        | 64 bit $\times$ 16 = 1024 bit = 128 B  | 128 B / 1024$^3$ B = 0.0000119 \% |
| FPU$^1$    | 80 bit $\times$ 8 = 640 bit = 80 B     | 80 B / 1024$^3$ B = 0.0000075 \%  |
| MMX        | 64 bit $\times$ 8 = 512 bit = 64 B     | 64 B / 1024$^3$ B = 0.0000060 \%  |
| XMM        | 128 bit $\times$ 16 = 2048 bit = 256 B | 256 B / 1024$^3$ B = 0.0000238 \% |
| Gesamt$^2$ | 128 B + 64 B + 256 B = 448 B           | 448 B / 1024$^3$ B = 0.0000417 \% |

$^1$ Das MMX-Register liegt innerhalb des FPU-Registers. Die meisten
Compiler unterstützen nur die 64 bit des MMX-Registers, nicht 80
bit: "Note that most C/C++ compilers support the 32 and 64 bit types
as float and double, but not the 80-bit one available from
assembly."

$^2$ Deswegen hier als Summe von GPR, MMX und XMM zu verstehen.

\newpage
Aufgabe 4
---------

- Mehrere Prozesse müssen sich in fairer Weise auf der CPU
  abwechseln, damit alle ihre Aufgabe erfüllen können. Dabei muss
  es eine zentrale Stelle geben, die den fairen Wechsel durchsetzt.
  Das betrifft auch den Stackspeicherplatz.

- Jeder einzelne Prozess besitzt eigene Daten, und es muss dafür
  gesorgt werden, dass nur der berechtigte Prozess Zugriff auf
  diese Daten hat. Für alle anderen Prozesse muss sichergestellt
  sein, dass sie keinen unberechtigten Zugriff auf fremde Daten
  besitzen. Genauso betroffen ist die Ausführung von Schadcodes
  durch böswillige Benutzer.

\newpage
Aufgabe 5
---------

\lstinputlisting[language=bash]{IBN_01_a5.sh}

\newpage
Aufgabe 6
---------

- Der Rückgabewert: Die PID des Kindprozesses wird in den
  Elternprozess gegeben, in den Kindprozess die Null.

- Das Beendigungssignal des Kindprozesses ist immer `SIGCHLD`.

- Der CPU-Zeit-Zähler wird im Kindprozess auf Null gesetzt.

\newpage
Aufgabe 7
---------

Die zwei beschriebenen Modi:

- **Fokusmodus**: Ein Problem wird durch bekannte Denkmuster
  gelöst, z.B. eine Additionsaufgabe. Man weiss, wie man an die
  Aufgabe herangehen muss, um sie zu lösen.
- **Diffusmodus**: Man ist sich nicht bewusst, wie man das
  Problem Lösen soll; es ist neu und noch kein passendes
  Denkmuster vorhanden. Das Gehirn probiert *diffus* verschiedene
  Ansätze aus.

Beispiele:

- Vokabeln lernen: Fokusmodus, man ist sich der generellen Strategie
  bewusst, wie man sich eine neue Vokabel aneignet. Es sei denn, es
  ist das erste mal, dass man Vokabeln lernt oder man muss erst noch
  ein Gefühl für die Fremdsprache entwickeln.
- Ein völlig neues Konzept aneignen: Diffusmodus, Begründung siehe
  Diffusmodus. Für das neue Konzept fehlen noch die Denkmuster.
- Eine bestimmte Art von Rechenaufgabe trainieren: Fokusmodus,
  trainieren impliziert dass man sich einer Herangehensweise bewusst
  ist.
- Auf die Klausur in IBN lernen: Fokusmodus, generell hat man in
  seinem bisherigen Leben schon viele Klausuren geschrieben und hat
  eine Strategie. Außerdem ist der Lernstoff nicht neu.

Salvador Dali und Thomas Edison nutzen die Entspannung und Ruhe vor
und durch Sekundenschlaf aus, um sich bewusst in den Diffusmodus zu
versetzen. Um von den dabei gewonnen Erkenntnissen zu profitieren
wird der Modus durch ein lautes Geräusch abrupt verlassen und
anschließend kann im Fokusmodus produktiv weitergearbeitet werden.

John Cleese über Kreativität:

- **Offenmodus**: Analog zum Diffusmodus. Entspannt, verspielt und
  ohne Druck Aufgaben zu erledigen. Zum Beispiel gut zum Besinnen
  und Nachdenken. Gut geeignet für kreative Inventionen.
- **Geschlossenmodus**: Analog zum Fokusmodus. Zum Beispiel bei der
  Arbeit, eventuell gehetzt, viele Aufgaben zielstrebig zu
  erledigen. Eventuell mit Stress verbunden. Aber keine Kreativität
  möglich.

Alexander Flemings Entdeckung von Penicillin war zufällig und durch
ein nicht vorhergesehenes Ereignis entstanden. Im Fokusmodus oder
Geschlossenmodus würde das als Hindernis wahrgenommen werden, auf
dem Weg die gestellten Aufgaben zu erfüllen. Durch den Diffusmodus
oder Offenmodus war er jedoch neugierig und wollte der Ursache
nachgehen.

Alfred Hitchcock erzählte scheinbar belanglose oder zumindest
irrelevante Geschichten, um den Fokusmodus oder Geschlossenmodus zu
verlassen und in den Diffusmodus oder Offenmodus zu gelangen. Für
den kreativen Prozess war das zwingend notwendig, sobald sich ein
Problem ergab, das nicht mit Zielstrebigkeit, sondern durch Fantasie
gelöst werden musste.
