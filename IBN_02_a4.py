def calculate(to_create, to_execute=0):
    if not to_create and not to_execute:
        # Es müssen keine neuen Threads erstellt werden und es
        # existiert auch kein Thread mehr, der abgearbeitet werden
        # müsste. Dieser Pfad ist vollständig und stellt eine
        # Möglichkeit dar.
        return 1
    if to_create and not to_execute:
        # Es sind noch Threads geplant, die erstellt werden müssen,
        # aber es gibt keinen Thread, der ausgeführt werden könnte.
        # Wir müssen also neuen Thread erstellen. Die Anzahl der
        # geplanten Threads nimmt ab, die Anzahl der abzuarbeitenden
        # Threads nimmt zu.
        return calculate(to_create - 1, to_execute + 1)
    if not to_create and to_execute:
        # Es müssen keine Threads mehr erstellt werden, aber es sind
        # noch Threads abzuarbeiten. Da die Reihenfolge, in welcher
        # die Threads abgearbeitet werden, beliebig ist, ist die
        # Anzahl der Möglichkeiten gleich der Anzahl der Threads.
        return to_execute * calculate(to_create, to_execute - 1)
    if to_create and to_execute:
        # Sind sowohl weitere Threads geplant, als auch bereits
        # erstellte Threads bereit zur Abarbeitung, dann müssen
        # beide Möglichkeiten berücksichtigt werden und die Anzahl
        # beider Pfade addiert sich.
        return calculate(to_create - 1, to_execute + 1) + to_execute * calculate(to_create, to_execute - 1)

number_of_threads = 3
print(calculate(3))

print("Probe:")

import itertools
a = ["c1", "c2", "c3", "p1", "p2", "p3"]
good = []
for p in itertools.permutations(a, 6):
    if p.index("c2") < p.index("c1"):
        continue
    if p.index("c3") < p.index("c1"):
        continue
    if p.index("c3") < p.index("c2"):
        continue
    for i in range(1, 4):
        if p.index(f"p{i}") < p.index(f"c{i}"):
            break
    else:
        good.append(p)

print("Anzahl aller Möglichkeiten:", len(list(itertools.permutations(a, 6))))
print("Anzahl erlaubter Möglichkeiten:", len(good))
print("Erlaubte Möglichkeiten:", good)

print("Markdown:")

for i, pp in enumerate(good):
    print(f"Fall {i+1})\n")
    print("```none")
    for p in pp:
        if "c" in p:
            p = "In main: creating thread " + p[1]
        else:
            p = "It's me, dude! I am number " + p[1] + "!"
        print(p)
    print("```\n")
