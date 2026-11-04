# Prompts de carrusel · miércoles 4 de noviembre de 2026

Modelo oficial: `tools/plantilla-carrusel.md`. **Hoy ningún partido llega a 80 % en Over 1.5**, así que no corresponde ningún prompt de la serie "80 % o más". Se deja solo el prompt del **partido del día** (lámina 1 del carrusel), con su categoría real, **GOLES OPTIMISTAS**, sin inflar nada. Hoy no se arma `noticias.json` ni `ultimos5.json` (solo se registran para partidos de 80 % o más).

---

## 1 · Botafogo vs Atlético-MG · Brasileirão · miércoles 4 de noviembre · 19:30 ECU (partido del día)

**PROMPT**
> Póster deportivo vertical 4:5 (1080x1350), estilo infografía premium. Estadio de noche con reflectores verdes, césped brillante y partículas doradas; paleta negro, verde neón y dorado metálico. Arriba, el logo "GOL ÉLITE PRO" (ÉLITE en dorado) con corona; debajo, la etiqueta "GOLES OPTIMISTAS". Título dorado: "BOTAFOGO vs ATLÉTICO-MG". Subtítulo verde: "BRASILEIRÃO · MIÉRCOLES 4 DE NOVIEMBRE · 19:30 HORA ECUADOR". A la izquierda, una mujer joven adulta (~27 años), sonriente, de medio cuerpo, con la camiseta titular del Botafogo: rayas verticales negras y blancas, con el escudo de la estrella solitaria en el pecho; debajo de ella, el nombre "BOTAFOGO". A la derecha, otra mujer joven adulta con la camiseta titular del Atlético Mineiro: rayas verticales negras y blancas, con el escudo del club en el pecho; debajo de ella, el nombre "ATLÉTICO-MG" (los dos equipos visten parecido, por eso se pone el nombre bajo cada chica). Camisetas con el escudo del club, sin logos de patrocinadores ni marcas de ropa. Junto al título, el escudo oficial de cada equipo, fiel al real, sin deformar.
> En el centro, un panel negro con borde dorado titulado "ESTADÍSTICAS CLAVE", con íconos dorados y estas líneas:
> • BOTAFOGO EN CASA: marca 1,62 y recibe 1,38 goles por partido
> • Los partidos del Botafogo en casa promedian 3,0 goles (16 partidos)
> • ATLÉTICO-MG DE VISITA: marca 1,06 y recibe 1,31 goles por partido
> • Botafogo 13.º (39 pts) · Atlético-MG 7.º (50 pts) · los dos vienen de 2 derrotas
> Después, un recuadro destacado con fondo café oscuro, borde dorado brillante y un ícono de periódico, titulado "LA NOTICIA DEL PARTIDO", con el titular corto en mayúsculas "EL FOGÃO SE JUEGA LA PERMANENCIA" y la frase "El riesgo de descenso del Botafogo sube de 9 % a 19 % si pierde; el Galo busca entrar a zona de Libertadores.", y en letra muy pequeña "Fuente: Valor Final".
> Al final, un panel destacado más grande titulado "NUESTRO PRONÓSTICO": "PROBABILIDAD OVER 1.5: 76%" (número enorme en verde neón), "Over 2.5: 50%" (más pequeño) y "MARCADOR SUGERIDO: 1-1" (grande, en dorado).
> Abajo, un botón dorado "¡SÍGUENOS!" y en letra pequeña "Over 1.5 = 2 goles o más en el partido, sin importar quién gane · +18 · Probabilidades estadísticas, no garantías". Texto en español, legible y sin errores.

**ANTI-PROMPT**
> Sin logos de patrocinadores, marcas de ropa deportiva ni casas de apuestas; sin escudos deformados, inventados o de otros clubes; sin caras de futbolistas reales; sin poses provocativas ni ropa reveladora; sin números distintos a los indicados; sin "apuesta segura", "gana seguro", "dinero fácil" ni promesas de ganancia; sin texto en inglés; sin marcas de agua.

---

## Verificación de datos
- Estadísticas de casa y fuera: `tools/datos.py` (corte martes 3-nov final; control GF casa = GC fuera en la liga). Botafogo en casa 16 PJ, 26 GF, 22 GC; Atlético-MG fuera 16 PJ, 17 GF, 21 GC.
- Posición, puntos, racha y riesgo de descenso: [Valor Final · Botafogo x Atlético-MG](https://valorfinal.com.br/brasileirao/jogos/botafogo-x-atletico-mg) (consultado el 4-nov).
- Fecha y hora: [Valor Final · rodada 34](https://valorfinal.com.br/brasileirao/2026/rodada-34): miércoles 4/11, 21:30 de Brasília = 19:30 de Ecuador. El 4-nov-2026 es miércoles.
- Uniformes de la temporada: Botafogo, camiseta alvinegra a rayas 2026-27 ([Diário do Pará, 22-may-2026](https://diariodopara.com.br/bola/botafogo-divulga-novo-uniforme-2026-27-veja-fotos-oficiais-e-precos/)); Atlético-MG, camiseta titular 2026 a rayas verticales alvinegras ([Footy Headlines](https://www.footyheadlines.com/pt/vaza-dos-equipamentos-nike-atletico-mineiro-2026-para-a-camisa-titular-e-a-camisa-reserva-chega-de-adidas.html)); el club lanzó además el "Manto da Massa" 2026-27 con rayas horizontales ([NC News, 22-oct-2026](https://ncnews.com.br/?p=66379)). No se confirmó cuál camiseta usará el Galo de visitante: revisar la foto oficial del club antes de publicar.
