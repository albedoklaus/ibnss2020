def bankierAlgorithmus(E,A,C,R):
    n,m = len(C), len(C[0])
    beendeteProzesse = []
    verklemmung = False
    while len(beendeteProzesse) < n and not(verklemmung):
        verklemmung = True
        for i in range(n):
            if i in beendeteProzesse:
                continue
            elif all([R[i][j] <= A[j] for j in range(m)]):
                # Angeforderte Ressourcen werden Prozess i zugewiesen
                # Prozess i wird beendet und gibt alle seine Ressourcen frei
                A = [C[i][j] + A[j] for j in range(m)]
                beendeteProzesse.append(i)
                verklemmung = False
                print(i, A)
    return not(verklemmung), beendeteProzesse

E = [ 3, 3, 3 ]
A = [ 2, 0, 2 ]
C = [ [0,0,0], [1,2,0], [0,1,1] ]
R = [ [2,1,0], [1,0,1], [1,1,0] ]

print(bankierAlgorithmus(E,A,C,R))