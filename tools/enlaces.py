# titular (en español), medio, url — lunes 12-oct-2026
LINK={
 'Levante|Sevilla':("Levante-Sevilla: previa y alineaciones probables de la jornada 8","Comuniate","https://www.comuniate.com/noticias/38270/levante-sevilla-previa-alineaciones-probables-y-consejos-fantasy-jornada-8-de-laliga"),
 'Chapecoense|Athletico-PR':("Chapecoense vs Athletico-PR: estadísticas y clasificación de la fecha 30","Valor Final","https://valorfinal.com.br/brasileirao/2026/jogos/chapecoense-x-athletico-pr"),
 'Coventry|Newcastle':("Coventry vs Newcastle: previa de la fecha 6 de la Premier League","VAVEL","https://www.vavel.com/en/football/2026/10/09/premier-league/1274500-newcastle-vs-coventry-preview.html"),
 'Coritiba|Botafogo':("Brasileirão: Athletico y Cruzeiro miran el G-4 en el cierre de la fecha","Futebol Interior","https://www.futebolinterior.com.br/brasileirao-2026-jogos-30a-rodada-segunda-feira/"),
 'Lanus|Velez Sarsfield':("Lanús vs Vélez: previa, horario y cómo llegan a la fecha 12 del Clausura","Todo Jujuy","https://www.todojujuy.com/lanus-vs-velez-previa-horario-y-como-llegan-la-fecha-12-del-clausura-n297238"),
 'Bragantino|Cruzeiro':("Bragantino vs Cruzeiro: estadísticas y clasificación de la fecha 30","Valor Final","https://valorfinal.com.br/brasileirao/2026/jogos/bragantino-x-cruzeiro"),
 'Gimnasia Mendoza|Newells Old Boys':("Gimnasia (Mendoza) vs Newell's: previa, horario y cómo llegan","Todo Jujuy","https://www.todojujuy.com/gimnasia-mendoza-vs-newells-previa-horario-y-como-llegan-la-fecha-12-del-clausura-n297239"),
}
PRED=['Levante|Sevilla','Chapecoense|Athletico-PR','Coventry|Newcastle','Coritiba|Botafogo']
DEST=['Lanus|Velez Sarsfield','Bragantino|Cruzeiro','Gimnasia Mendoza|Newells Old Boys']
COL={'Levante':'#1f2f6b','Sevilla':'#f4f4f4','Coventry':'#6cc3ee','Newcastle':'#1a1f3a','Coritiba':'#0b5d34','Botafogo':'#161616',
 'Chapecoense':'#0e7a3c','Athletico-PR':'#c8102e','Bragantino':'#e8e8e8','Cruzeiro':'#1d3f8f','Lanus':'#8a1538','Velez Sarsfield':'#1d4fa0',
 'Gimnasia Mendoza':'#141414','Newells Old Boys':'#d0102e',
 # anteriores (se conservan)
 'Crystal Palace':'#1b458f','Nottm Forest':'#c8102e','Atletico MG':'#161616','Santos':'#f2f2f2','Sassuolo':'#00a752','AC Milan':'#c8102e',
 'A. San Luis':'#c8102e','Santos Laguna':'#00704a','Lazio':'#87cfee','Monza':'#e30613','Pachuca':'#1c3e72','Necaxa':'#d6001c',
 'Universidad Católica':'#1d3f8f','Macará':'#6cc4ec','Nice':'#b0101f','Strasbourg':'#0a8fd6','Pumas UNAM':'#0b2a52','Cruz Azul':'#1d5fb8',
 'Racing':'#00843d','Valencia':'#f4f4f4','Liverpool':'#c8102e','Manchester City':'#6cabdd','LDU Quito':'#f6f6f6','Barcelona SC':'#f7c600',
 'Palmeiras':'#006437','Corinthians':'#141414','Flamengo':'#c3281e','Fluminense':'#7a1230'}

# Atalanta–Venezia (agregado 06:25 ECU con las capturas del equipo)
LINK['Atalanta|Venezia']=("Atalanta-Venezia: ficha y probables alineaciones de la 6.ª jornada","Fantacalcio","https://www.fantacalcio.it/serie-a/calendario/6/2026-27/atalanta-venezia/18005")
DEST.insert(0,'Atalanta|Venezia')
COL.update({'Atalanta':'#1e3c8c','Venezia':'#111111'})

# Aciertos de ayer (domingo 11): (partido, marcador real, nuestro Over 1.5, medio, url)
ACIERTOS=[
 ("Atlético MG vs Santos","2-1","85,0 %","Partido del día · Boca","https://boca.com.br/esportes/atletico-vence-santos-virada-arena-mrv"),
 ("Crystal Palace vs Nottingham Forest","3-1","90,7 % · GOL ÉLITE","ESPN","https://www.espn.com/soccer/match/_/gameId/401879266/nottingham-forest-crystal-palace"),
 ("Betis vs Osasuna","5-2","77,3 %","Fox Sports","https://www.foxsports.com/soccer/la-liga-betis-vs-osasuna-oct-11-2026-game-boxscore-909022"),
 ("Pachuca vs Necaxa","3-3","83,7 %","Fox Sports México","https://www.foxsports.com.mx/2026/10/11/pachuca-3-3-necaxa-resumen-del-partido-y-goles-de-la-jornada-11-apertura-2026-liga-mx/"),
 ("Pumas vs Cruz Azul","3-3","81,5 %","VAVEL México","https://vavel.com/mx/futbol-mexicano/2026/10/11/1274558-pumas-vs-cruz-azul-en-vivo-liga-mx.html"),
 ("Lazio vs Monza","3-1","84,2 %","t-online","https://www.t-online.de/sport/live-ticker/fussball/serie-a/sdc_fm-57474/lazio-monza-serie-a-im-liveticker.html"),
 ("Real Sociedad vs Deportivo","3-2","74,5 %","Sporza","https://sporza.be/nl/sport/voetbal/real-sociedad-deportivo-la-coruna~3341075/"),
 ("Sassuolo vs Milan","1-1 · marcador exacto","84,9 %","Fútbol Total","https://futboltotal.futbol/partido/sassuolo-vs-ac-milan-serie-a-2026-10-11"),
]

# Cómo llegan (solo datos verificados con su fuente)
LLEGAN={
 'Levante|Sevilla':["Levante en casa: 7 goles a favor y 6 en contra en 2 partidos (6,5 goles por partido en su estadio).",
   "Sevilla fuera: 2 victorias y 1 empate, 5 goles a favor y 2 en contra.",
   "Sevilla viene de perder con el Barcelona en la jornada 7. Levante, sin Hugo Sotelo (esguince de rodilla).",
   "Fuentes: SoccerSTATS y Comuniate."],
 'Chapecoense|Athletico-PR':["Chapecoense es último (20.º, 18 puntos) y recibe 2,23 goles por partido en casa.",
   "Athletico-PR es 4.º con 50 puntos; fuera marca 1,29 y recibe 1,50 por partido.",
   "Athletico-PR viene de 3-3 con Coritiba y 3-3 con Fluminense: partidos abiertos.",
   "Fuente: Valor Final."],
 'Coventry|Newcastle':["Coventry recibió 6 goles en 2 partidos en casa y está en zona de descenso; viene de su primera victoria en liga.",
   "Newcastle solo perdió un partido de liga (4-1 con Leeds) y viene de ganar al Hull City.",
   "Coventry sin Awoniyi (sanción); en Newcastle, Osula y Elanga probablemente fuera.",
   "Fuentes: VAVEL y datos del partido."],
 'Coritiba|Botafogo':["Coritiba es 10.º (38 puntos) y llega con dos derrotas seguidas (0-4 y 0-5).",
   "Botafogo es 13.º (35 puntos), también con dos derrotas seguidas; fuera recibe 1,79 goles por partido.",
   "En casa de Coritiba hay 2,71 goles por partido (19 a favor y 19 en contra en 14).",
   "Fuente: Valor Final."],
}
