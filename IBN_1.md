1.Übung zur Vorlesung Betriebssysteme und Netzwerke (IBN)
=========================================================

Aufgabe 1
---------

$$E(X) = P(X=+) + P(X=-)$$
$$P(X=+): t_+ = t_c$$
$$P(X=-): t_- = t_c + t_r$$
$$ t_{ave} =  P(X=+) * t_c + P(X=-) * (t_c + t_r)$$ gdw. $P(X=-) = 1 - P(X=+)$

- Ein größerer Cache könnte $P_+$ erhöhen.
- Wiederholter Zugriff des selben Prozesses könnte $P_+$ ebenfalls erhöhen, da eventuell die benötigten Daten schon im Cache sind.

Aufgabe 2
---------

$$ 5t_c \geqslant P_+ * t_c + (1 - P_+) * (t_c + 100t_c)$$
$$ 5t_c \geqslant P_+t_c + 101t_c - 101t_cP_+$$
$$ 5 \geqslant P_+ + 100 - 101P_+$$ gdw. $t_c \neq 0$
$$ 5 \geqslant 100 - 100P_+$$
$$ P_+ \geqslant 0.95$$
