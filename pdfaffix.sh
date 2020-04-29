#!/bin/sh
[ -n "$4" ] || { printf '%s\n' "Usage: $0 <TeX prefix> <PDF input> <TeX suffix> <PDF output>" "Note: Omit the file extensions." "Example: $0 'This is the \TeX prefix' input 'This is the \TeX suffix' output"; exit 1; }
printf '%s\n' '\documentclass{article}\usepackage{pdfpages}\begin{document}'"$1"'\includepdf[pages=-]{'"$2"'}'"$3"'\end{document}' | pdflatex -jobname="$4" && rm "$4.log" "$4.aux"
