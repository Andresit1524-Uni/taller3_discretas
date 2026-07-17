#import "/docs/_template/style.typ": style
#show: style

= Título 1
== Título 2
=== Título 3
==== Título 4
#lorem(30)

https://zdescargas.org

$
  integral.cont_lambda P d x + Q d y = integral.double_D (partial Q)/(partial x) - (partial P)/(partial y) d A
$

```typ
/// Calculates the Mandelbrot escape time for a certain point
///
/// - x (float): X coordinate for current point
/// - y (float): Y coordinate for current point
/// -> int
#let mandelbrot = (x, y) => {
  let z = (x: 0, y: 0)
  let i = 0

  while i != max {
    if z.x * z.x + z.y * z.y > 2 { break }
    z = (
      x: z.x * z.x - z.y * z.y + x,
      y: 2 * z.x * z.y + y,
    )

    i += 1
  }

  if i == max { 0 } else { calc.sqrt(i) }
}
```
