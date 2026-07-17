#let style(content) = {
  // Títulos principales
  show heading.where(level: 1): it => {
    it.body
    v(-0.5em)
    line(length: 100%)
  }

  // Tamaños
  show heading.where(level: 1): set text(size: 1.4em)
  show heading.where(level: 2): set text(size: 1.25em)
  show heading.where(level: 3): set text(size: 1.1em)
  show heading.where(level: 4): set text(size: 1em)

  // Colores
  show link: set text(fill: blue.darken(40%))
  show heading.where(level: 4): set text(fill: luma(40%))

  // Fuentes
  set text(font: "Ancizar Sans")
  show raw: set text(font: "Google Sans Code NF")
  show math.equation: set text(font: "Erewhon Math", size: 1.1em)

  // Código
  show raw: set block(fill: olive.lighten(95%), inset: 0.8em, radius: 1em, width: 100%)

  content
}
