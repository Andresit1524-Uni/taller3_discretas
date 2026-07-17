# Taller 3 discretas
Este es el repositorio para el taller 3 de discretas, con temas sobre teoría de grafos, criptografía y computación cuántica.

## Requerimientos
1. Python
2. [Typst](https://typst.app) 0.15 o superior (para compilar la documentación)

## Integrantes
- Hayran Andrés López
- Daniel Alejandro Durán

## Documentación
Para la documentación, encuentras PDFs compilados en [`docs`](/docs/), Aunque puedes compilarlos tú mismo:

1. [Instala Typst](https://typst.app/open-source/#download)
2. Ejecuta el script de compilación. Desde la carpeta del repo:

    ```bash
    cd docs
    ./compile.sh
    ```

    Los PDFs se compilarán en `docs/` sobrescribiendo los existentes.

## Asignación de problemas
Cada problema está en una carpeta diferente y sigue esta estructura:

```
○ (ejercicio)
┣━○ main.py   -> Archivo principal
┗━○ tests.py  -> Archivo con test (usando unittest)
``` 

Pueden haber archivos extra para código que no se quiera colocar en el archivo principal (por ejemplo, para que `main.py`) sea un orquestador solamente. Los ejercicios (con los nombres de las carpetas) están asignados de la siguiente manera:

- Daniel Durán:
    - 1 - Cifrado César (`caesar`)
    - 2 - RSA de juguete (`rsa`)
    - 3 - MPC básico (`mpc`)
    - 7 - Tablas de verdad y circuitos lógicos (`truth_table`)
    - 8 - Simplificación booleana (`simplifying`)

- Hayran Andrés López:
    - 4 - Ruta más corta (`dijkstra`)
    - 5 - Cierre de una estación (`dijkstra_if_closed`)
    - 6 - Coloreo de grafos (`coloring_graphs`)
    - 9 - Shannon (`shannon`)
    - 10 - Primer simulador cuántico (`qubits`)
