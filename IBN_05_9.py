def least_recently_used(page_references, page_count):
    """Least Recently Used (LRU) Seitenersetzungsalgorithmus"""

    # Komma oder Whitespace als Trennzeichen
    page_references = page_references.replace(",", " ").split()

    pages = {}
    for i, page in enumerate(page_references):

        page_fault = page not in pages
        full_capacity = len(pages) == page_count

        # Falls Page fault und kein Platz mehr frei, muss ein Opfer entfernt werden
        if page_fault and full_capacity:
            victim = min(pages, key=pages.get)
            del pages[victim]

        # Page einfügen falls nicht vorhanden und Zeitpunkt des Zugriffs notieren
        pages[page] = i

        # Aktuelle Pages ausgeben
        print(*pages)


if __name__ == "__main__":

    print("A")
    A = "7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1"
    least_recently_used(A, 3)

    print("B")
    B = "2,3,2,1,5,2,4,5,3,2,5,2"
    least_recently_used(B, 3)
