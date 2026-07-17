#!/bin/bash

for file in docs/source/*.typ; do
    typst compile --root . "$file" "docs/$(basename "${file%.typ}.pdf")"
    echo "Compilado: $file"
done
