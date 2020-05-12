#!/bin/bash

path="$1"
prefix="$2"

if [ ! -d "$path" ]
then
    printf '%s\n' "Error: Ungültiger Pfad" 1>&2
    exit 1
fi

if [ ! -r "$path" ]
then
    printf '%s\n' "Error: Pfad nicht lesbar" 1>&2
    exit 1
fi

# Die folgenden Befehle beruhen auf der Annahme, dass in den
# Dateinamen des untersuchten Verzeichnisses keine problematischen
# Zeichen, wie zum Beispiel ein Zeilenumbruch, enthalten ist.
#
# Es ist generell keine gute Idee, für die gestellten Anforderungen
# ein Shell-Skript zu schreiben. Eine höhere Sprache wie Perl oder
# Python wäre deutlich besser geeignet.
#
# Siehe auch: http://mywiki.wooledge.org/ParsingLs
#

while true
do

    printf '%s\n' "Die 5 größten Dateien:"
    # Detaillierte Liste von Dateien
    ls -l "$path" |
    # Nur Dateien beachten, keine Ordner etc.
    grep "^-" |
    # Uninteressante Spalten löschen
    awk '{ $1=$2=$3=$4=$6=$7=$8="" ; print $0 }' |
    # Nach den Zahlen der ersten Spalte absteigend sortieren
    sort -nr |
    # Erste Spalte entfernen
    awk '{ $1="" ; print $0 }' |
    # Whitespace entfernen
    awk '{ $1=$1 ; print $0 }' |
    # Nur die ersten 5 Zeilen behalten
    head -n 5

    printf '%s\n' "Die 5 zuletzt modifizierten Dateien beginnend mit \"$prefix\":"
    # Detaillierte Liste von Dateien nach mtime sortiert
    ls -lt "$path" |
    # Nur Dateien beachten, keine Ordner etc.
    grep "^-" |
    # Uninteressante Spalten löschen
    awk '{ $1=$2=$3=$4=$5=$6=$7=$8="" ; print $0 }' |
    # Whitespace entfernen
    awk '{ $1=$1 ; print $0 }' |
    # Nach Prefix filtern
    grep "^$prefix" |
    # Nur die ersten 5 Zeilen behalten
    head -n 5

    sleep 5

done
