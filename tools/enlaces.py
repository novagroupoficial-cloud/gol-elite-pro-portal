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

# ---- Viernes 16-oct-2026 (rutina recuperada por el refresco de las 21:15 ECU; solo Liga MX de las 22:00) ----
LINK={
 'Tijuana|Puebla':("Tijuana recibe a Puebla en la jornada 12 del Apertura 2026","El Congresista","https://elcongresista.mx/tijuana-vs-puebla-jornada-12-apertura-2026"),
 'Atlante|Pumas UNAM':("Atlante vs Pumas: horario, alineaciones y dónde ver el partido de la jornada 12","Claro Sports","https://www.clarosports.com/futbol/liga-mx/atlante-vs-pumas-en-vivo-la-liga-mx-horario-alineaciones-y-donde-ver-el-partido-del-apertura-2026-jornada-12/"),
}
PRED=[]
DEST=['Atlante|Pumas UNAM','Tijuana|Puebla']
COL.update({'Tijuana':'#c8102e','Puebla':'#1d3f8f','Atlante':'#8b1a2b'})
LLEGAN={
 'Atlante|Pumas UNAM':["Atlante en casa: 6 goles a favor y 7 en contra en 5 partidos.",
   "Pumas fuera: 8 goles a favor y 8 en contra en 5 partidos (3,2 goles por partido).",
   "En la tabla general, Pumas es 12.º (17 GF, 19 GC) y Atlante 16.º (12 GF, 17 GC) tras 11 jornadas.",
   "Fuentes: SoccerSTATS y The Stats API."],
 'Tijuana|Puebla':["Tijuana en casa: 10 goles a favor y 6 en contra en 6 partidos.",
   "Puebla fuera: 6 goles a favor y 7 en contra en 6 partidos (2,2 goles por partido).",
   "Tijuana es 8.º y Puebla 9.º en la tabla general.",
   "Fuentes: SoccerSTATS y The Stats API."],
}

# ---- Sábado 17-oct-2026 (rutina diaria, sellado 05:55 ECU) ----
# LINK: una previa real por partido (recolectada hoy). Brasil: 3 partidos sin previa encontrada (límite de búsquedas); enlazan a la tabla de Valor Final y el titular lo dice.
LINK={
"Botafogo|Chapecoense": [
"Botafogo x Chapecoense: probabilidades y análisis (previa estadística, 31ª rodada)",
"Valor Final",
"https://valorfinal.com.br/brasileirao/2026/jogos/botafogo-x-chapecoense.md"
],
"Atletico MG|Coritiba": [
"Brasileirão 2026: Atletico MG y Coritiba en la tabla de local y visitante (sin previa enlazada hoy)",
"Valor Final",
"https://valorfinal.com.br/brasileirao/tabelas-por-recorte"
],
"Athletico-PR|Palmeiras": [
"Brasileirão 2026: Athletico-PR y Palmeiras en la tabla de local y visitante (sin previa enlazada hoy)",
"Valor Final",
"https://valorfinal.com.br/brasileirao/tabelas-por-recorte"
],
"São Paulo|Vasco da Gama": [
"Brasileirão 2026: São Paulo y Vasco da Gama en la tabla de local y visitante (sin previa enlazada hoy)",
"Valor Final",
"https://valorfinal.com.br/brasileirao/tabelas-por-recorte"
],
"Banfield|Argentinos Juniors": [
"Banfield vs Argentinos Juniors: previa, horario y cómo llegan para la fecha 13 del Clausura",
"Todo Jujuy",
"https://www.todojujuy.com/banfield-vs-argentinos-juniors-previa-horario-y-como-llegan-la-fecha-13-del-clausura-n297419"
],
"Platense|Lanus": [
"Platense vs Lanús: previa, horario y cómo llegan para la fecha 13 del Clausura",
"Todo Jujuy",
"https://www.todojujuy.com/platense-vs-lanus-previa-horario-y-como-llegan-la-fecha-13-del-clausura-n297424"
],
"Independiente Rivadavia|Tigre": [
"Independiente Rivadavia (M) vs Tigre: previa, horario y cómo llegan para la fecha 13 del Clausura",
"Todo Jujuy",
"https://www.todojujuy.com/independiente-riv-m-vs-tigre-previa-horario-y-como-llegan-la-fecha-13-del-clausura-n297425"
],
"Velez Sarsfield|Gimnasia Mendoza": [
"Vélez vs Gimnasia (Mendoza): previa, horario y cómo llegan para la fecha 13 del Clausura",
"Todo Jujuy",
"https://www.todojujuy.com/velez-vs-gimnasia-mendoza-previa-horario-y-como-llegan-la-fecha-13-del-clausura-n297430"
],
"Atletico Tucuman|Rosario Central": [
"Atlético Tucumán vs Rosario Central: previa, horario y cómo llegan para la fecha 13 del Clausura",
"Todo Jujuy",
"https://www.todojujuy.com/atletico-tucuman-vs-rosario-central-previa-horario-y-como-llegan-la-fecha-13-del-clausura-n297429"
],
"Everton|Chelsea": [
"Everton vs Chelsea: previa de la jornada 7 de la Premier League",
"Fútbol Total",
"https://futboltotal.futbol/partido/everton-vs-chelsea-premier-league-2026-10-17"
],
"Brentford|Liverpool": [
"Previa: Brentford vs Liverpool – pronóstico, noticias de los equipos y alineaciones",
"Sports Mole",
"https://www.sportsmole.co.uk/football/brentford/preview/brentford-vs-liverpool-prediction-team-news-lineups_606921.html"
],
"Fulham|Hull City": [
"Previa: Fulham vs Hull City – pronóstico, noticias de los equipos y alineaciones",
"Sports Mole",
"https://www.sportsmole.co.uk/football/fulham/preview/fulham-vs-hull-city-prediction-team-news-lineups_606929.html"
],
"Manchester City|Ipswich Town": [
"Maresca busca la séptima victoria seguida con el City recibiendo al Ipswich",
"Manchester City (web oficial)",
"https://www.mancity.com/news/mens/city-v-ipswich-town-match-preview-pl-17-october-63927580"
],
"Newcastle United|Aston Villa": [
"Newcastle United vs Aston Villa: previa de la jornada 7 de la Premier League 2026-27",
"Khel Now",
"https://khelnow.com/football/newcastle-united-vs-aston-villa-preview-premier-league-202610"
],
"Espanyol|Atletico Madrid": [
"Simeone, que confirma las bajas de Koke y Cardoso, elogia a Manolo González antes del Espanyol – Atlético",
"La Grada",
"https://lagrada.org/simeone-rueda-prensa-espanyol-atletico-manolo-gonzalez-koke-cardoso/"
],
"Villarreal|Elche": [
"El Villarreal busca la regularidad en la Liga y el Elche ratificar su mejoría",
"Infobae (EFE)",
"https://www.infobae.com/espana/agencias/2026/10/16/el-villarreal-busca-la-regularidad-en-la-liga-y-el-elche-ratificar-su-mejoria/"
],
"Real Betis|Barcelona": [
"Betis vs Barcelona: previa, predicciones y alineaciones",
"Sports Illustrated Fútbol (si.com/es-us)",
"https://www.si.com/es-us/betis-vs-barcelona-previa-predicciones-y-alineaciones-17-10-2026"
],
"Valencia|Athletic Club": [
"Previa Valencia vs Athletic: objetivo recuperar Mestalla",
"VAVEL España",
"https://www.vavel.com/es/futbol/2026/10/16/valencia-cf/1275578-previa-valencia-vs-athletic-objetivo-recuperar-mestalla.html"
],
"Hamburger SV|VfB Stuttgart": [
"Hamburger SV vs Stuttgart: pronóstico, consejos de apuestas, alineaciones y cuotas | 17 oct 2026",
"Sportsgambler",
"https://www.sportsgambler.com/betting-tips/football/hamburger-sv-vs-stuttgart-prediction-lineups-odds-2026-10-17/"
],
"Werder Bremen|SC Paderborn": [
"Werder Bremen vs SC Paderborn 07: alineación probable",
"Starting11",
"https://starting11.com/fixtures/werder-bremen-vs-sc-paderborn-07-20261017"
],
"Union Berlin|Borussia Dortmund": [
"Union Berlin vs Borussia Dortmund: alineación probable",
"Starting11",
"https://starting11.com/fixtures/union-berlin-vs-borussia-dortmund"
],
"Schalke 04|Mainz 05": [
"Previa: Schalke 04 vs Mainz 05 – pronóstico, noticias del equipo y alineaciones",
"Sports Mole",
"https://www.sportsmole.co.uk/football/schalke-04/preview/schalke-vs-mainz-prediction-team-news-lineups_606979.html"
],
"Elversberg|Augsburg": [
"Previa: Elversberg vs Augsburg – pronóstico, noticias del equipo y alineaciones",
"Sports Mole",
"https://www.sportsmole.co.uk/football/elversberg/preview/elversberg-vs-augsburg-prediction-team-news-lineups_606909.html"
],
"Bayern Munich|RB Leipzig": [
"Bayern München vs RB Leipzig: previa de la jornada 6 · Bundesliga",
"futboltotal.futbol",
"https://futboltotal.futbol/partido/bayern-munchen-vs-rb-leipzig-bundesliga-2026-10-17"
],
"ADO Den Haag|PSV": [
"Previa: ADO Den Haag vs PSV Eindhoven – pronóstico, noticias del equipo y alineaciones",
"Sports Mole",
"https://www.sportsmole.co.uk/football/ado-den-haag/preview/ado-den-haag-vs-psv-prediction-team-news-lineups_606942.html"
],
"Telstar|Feyenoord": [
"Previa: Telstar vs Feyenoord – pronóstico, noticias del equipo y alineaciones",
"Sports Mole",
"https://www.sportsmole.co.uk/football/telstar/preview/telstar-vs-feyenoord-prediction-team-news-lineups_606943.html"
],
"Sparta Rotterdam|Willem II": [
"Previa: Sparta Rotterdam vs Willem II – pronóstico, noticias del equipo y alineaciones",
"Sports Mole",
"https://www.sportsmole.co.uk/football/sparta-rotterdam/preview/sparta-vs-willem-ii-prediction-team-news-lineups_606946.html"
],
"Venezia|Napoli": [
"Venezia-Napoli: probables alineaciones, estadísticas, cuándo y dónde verlo",
"Eurosport Italia",
"https://www.eurosport.it/calcio/serie-a/2026-2027/venezia-napoli-probabili-formazioni-statistiche-quando-e-dove-vederla_sto23346026/story.shtml"
],
"Bologna|Inter": [
"Rumbo al Bologna-Inter: la guía completa del partido",
"Inter.it (web oficial)",
"https://www.inter.it/it/notizie/guida-bologna-inter-serie-a-2026-27"
],
"Roma|Genoa": [
"Probables alineaciones Roma-Genoa | Cuotas: también se lesiona Manu Koné (Serie A, hoy 17 de octubre de 2026)",
"Il Sussidiario",
"https://www.ilsussidiario.net/news/probabili-formazioni-roma-genoa-quote-si-ferma-anche-manu-kone-serie-a-oggi-17-ottobre-2026/3008788/"
],
"Strasbourg|Paris Saint-Germain": [
"L1 (J7): Todo sobre el Strasbourg - PSG",
"Orange Sports",
"https://sports.orange.fr/football/ligue-1/avant-match/l1-j7-tout-savoir-sur-strasbourg-psg-exclu-CNT000002sZeVF.html"
],
"Lille|Brest": [
"Previa: Lille vs Brest - pronóstico, noticias de los equipos, alineaciones",
"Sports Mole",
"https://www.sportsmole.co.uk/football/lille/preview/lille-vs-brest-prediction-team-news-lineups_606902.html"
],
"Troyes|Lens": [
"PREVIA | Troyes vs Lens: noticias de los equipos, alineaciones, pronósticos (Ligue 1 17/10)",
"Playmakerstats vía Yahoo Sports",
"https://sports.yahoo.com/articles/preview-troyes-vs-lens-team-184500580.html"
],
"Santos Laguna|Queretaro": [
"Santos Laguna vs Querétaro: DÓNDE VER en vivo, canal TV, online y horario, Jornada 12 Liga MX 2026",
"Fox Sports México",
"https://www.foxsports.com.mx/2026/10/13/santos-laguna-vs-queretaro-donde-ver-en-vivo-canal-tv-online-y-horario-jornada-12-liga-mx-2026/"
],
"Guadalajara|Tigres UANL": [
"¿Por TV abierta? Chivas vs Tigres: DÓNDE VER en vivo, canal y horario, Jornada 12 Liga MX Apertura 2026",
"Fox Sports México",
"https://www.foxsports.com.mx/2026/10/14/chivas-vs-tigres-donde-ver-en-vivo-canal-tv-online-y-horario-jornada-12-liga-mx-apertura-2026/"
],
"Leon|America": [
"León vs América en vivo la Liga MX: horario, alineaciones y dónde ver el partido del Apertura 2026; jornada 12",
"Claro Sports",
"https://www.clarosports.com/futbol/liga-mx/leon-vs-america-en-vivo-la-liga-mx-horario-alineaciones-y-donde-ver-el-partido-del-apertura-2026-jornada-12/"
],
"Toluca|A. San Luis": [
"Toluca vs Atlético San Luis EN VIVO: Dónde ver en TV, online y hora Jornada 12 Liga MX Apertura 2026",
"Fox Sports México",
"https://www.foxsports.com.mx/2026/10/14/toluca-vs-atletico-san-luis-en-vivo-donde-ver-en-tv-online-y-hora-jornada-12-liga-mx-apertura-2026/"
],
"Cruz Azul|Juarez": [
"Cruz Azul vs FC Juárez: DÓNDE VER en vivo, canal TV, streaming y horario, Jornada 12 Liga MX 2026",
"Fox Sports México",
"https://www.foxsports.com.mx/2026/10/15/cruz-azul-vs-fc-juarez-donde-ver-en-vivo-canal-tv-streaming-y-horario-jornada-12-liga-mx-2026/"
],
"Philadelphia|Charlotte": [
"Philadelphia Union vs Charlotte F.C.: previa de jornada 30 · Major League Soccer",
"Futbol Total",
"https://futboltotal.futbol/partido/philadelphia-union-vs-charlotte-mls-2026-10-17"
],
"Minnesota United|St. Louis City": [
"Minnesota United F.C. vs St. Louis City S.C.: Jornada 30, Major League Soccer 2026",
"Futbol Total",
"https://futboltotal.futbol/partido/minnesota-united-fc-vs-st-louis-city-mls-2026-10-17"
],
"Atlanta United|Inter Miami": [
"Atlanta United F.C. vs Inter Miami C.F.: previa de jornada 30 · Major League Soccer",
"Futbol Total",
"https://futboltotal.futbol/partido/atlanta-united-fc-vs-inter-miami-mls-2026-10-18"
],
"New England|Chicago Fire": [
"New England Revolution vs Chicago Fire F.C.: previa de jornada 30 · Major League Soccer",
"Futbol Total",
"https://futboltotal.futbol/partido/new-england-revolution-vs-chicago-fire-mls-2026-10-18"
],
"New York RB|Toronto": [
"New York Red Bulls vs Toronto F.C.: previa de jornada 30 · Major League Soccer",
"Futbol Total",
"https://futboltotal.futbol/partido/new-york-red-bulls-vs-toronto-fc-mls-2026-10-18"
],
"Orlando City|DC United": [
"Orlando City S.C. vs D.C. United: previa de jornada 30 · Major League Soccer",
"Futbol Total",
"https://futboltotal.futbol/partido/orlando-city-sc-vs-dc-united-mls-2026-10-18"
],
"Houston Dynamo|Dallas": [
"Houston Dynamo vs F.C. Dallas: previa de jornada 30, Major League Soccer 2026",
"Futbol Total",
"https://futboltotal.futbol/partido/houston-dynamo-vs-fc-dallas-mls-2026-10-18"
],
"Sporting KC|Real Salt Lake": [
"Sporting Kansas City vs Real Salt Lake: previa de jornada 30 · Major League Soccer",
"Futbol Total",
"https://futboltotal.futbol/partido/sporting-kansas-city-vs-real-salt-lake-mls-2026-10-18"
],
"Austin|Vancouver": [
"Austin F.C. vs Vancouver Whitecaps F.C.: previa de jornada 30 · Major League Soccer",
"Futbol Total",
"https://futboltotal.futbol/partido/austin-vs-vancouver-whitecaps-mls-2026-10-18"
],
"SJ Earthquakes|Nashville SC": [
"San Jose Earthquakes vs Nashville S.C.: previa de jornada 30 · Major League Soccer",
"Futbol Total",
"https://futboltotal.futbol/partido/san-jose-earthquakes-vs-nashville-sc-mls-2026-10-18"
],
"Seattle|CF Montreal": [
"Seattle Sounders vs C.F. Montreal: previa de jornada 30 · Major League Soccer",
"Futbol Total",
"https://futboltotal.futbol/partido/seattle-sounders-vs-cf-montreal-mls-2026-10-18"
],
"LA Galaxy|San Diego": [
"Los Angeles Galaxy vs San Diego F.C.: previa de jornada 30 · Major League Soccer",
"Futbol Total",
"https://futboltotal.futbol/partido/los-angeles-galaxy-vs-san-diego-mls-2026-10-18"
],
"Portland|Colorado Rapids": [
"Portland Timbers vs Colorado Rapids: previa de jornada 30 · Major League Soccer",
"Futbol Total",
"https://futboltotal.futbol/partido/portland-timbers-vs-colorado-rapids-mls-2026-10-18"
],
"Libertad|Guayaquil City": [
"Libertad y Guayaquil City se encuentran en la fecha 3",
"Anecdotarios",
"https://anecdotarios.com/2026/10/15/libertad-vs-guayaquil-city-previa-horario-y-como-llegan-para-la-fecha-3-del-torneo-ecuatoriano/"
],
"Macará|Independiente del Valle": [
"LigaPro: Independiente del Valle busca consagrarse como campeón ante Macará a falta de siete fechas",
"Primicias",
"https://www.primicias.ec/deportes/ligapro/independiente-del-valle/partido-macara-campeon-135020/"
],
"Aucas|LDU Quito": [
"Liga de Quito y Aucas llegan al Superclásico capitalino separados por dos puntos y con 185 duelos en su historial",
"El Universo",
"https://www.eluniverso.com/deportes/otros-deportes/liga-de-quito-y-aucas-llegan-al-superclasico-capitalino-separados-por-dos-puntos-y-con-185-duelos-en-su-historial-nota/"
],
"Boyacá Chicó|Atlético Nacional": [
"Dónde y cómo ver en vivo y gratis Boyacá Chicó vs. Nacional hoy: TV y streaming online del partido por la Liga BetPlay 2026",
"Yahoo Noticias",
"https://es-us.noticias.yahoo.com/deportes/d%C3%B3nde-vivo-gratis-boyac%C3%A1-chic%C3%B3-080001663.html"
],
"Millonarios|Jaguares de Córdoba": [
"Millonarios vuelve a casa luego de 28 días y hace cuentas para clasificar: el cupo a los cuadrangulares está en El Campín",
"El Tiempo",
"https://www.eltiempo.com/deportes/futbol-colombiano/millonarios-vuelve-a-casa-luego-de-28-dias-y-hace-cuentas-para-clasificar-el-cupo-a-los-cuadrangulares-esta-en-el-campin-hora-y-tv-3594222"
],
"Independiente Medellín|Once Caldas": [
"Posibles alineaciones de Independiente Medellín vs Once Caldas por Liga BetPlay Dimayor 2026-II",
"ClaroSports",
"https://www.clarosports.com/colombia/liga-bet-play/posibles-alineaciones-de-independiente-medellin-vs-once-caldas-por-liga-betplay-dimayor-2026-ii/"
],
"Juan Pablo II|Sport Boys": [
"Sport Boys en alerta: Cueva podría perderse el duelo ante Juan Pablo II por el Clausura 2026",
"El Comercio",
"https://elcomercio.pe/deporte-total/futbol-peruano/sport-boys-en-alerta-christian-cueva-podria-perderse-el-duelo-ante-juan-pablo-ii-por-el-torneo-clausura-2026-liga-1-ultimas-noticia/"
],
"Melgar|Deportivo Garcilaso": [
"FBC Melgar recibe a Garcilaso y busca cortar mala racha en Arequipa",
"Diario Correo",
"https://diariocorreo.pe/deportes/fbc-melgar-recibe-a-garcilaso-y-busca-cortar-mala-racha-en-arequipa-noticia/"
],
"Alianza Lima|Atlético Grau": [
"Atlético Grau suma tres bajas para visitar a Alianza Lima por la fecha 12 del Clausura",
"Ahora",
"https://ahora.com.pe/deportes/atletico-grau-bajas-alianza-lima-clausura-2026"
]
}
LINK={k:tuple(v) for k,v in LINK.items()}
PRED=["Telstar|Feyenoord", "Bayern Munich|RB Leipzig", "ADO Den Haag|PSV", "Toluca|A. San Luis", "Elversberg|Augsburg", "Manchester City|Ipswich Town", "Cruz Azul|Juarez", "Sparta Rotterdam|Willem II", "Atlanta United|Inter Miami", "Hamburger SV|VfB Stuttgart", "Villarreal|Elche", "Union Berlin|Borussia Dortmund", "Seattle|CF Montreal", "Independiente Rivadavia|Tigre", "Portland|Colorado Rapids", "Fulham|Hull City", "Newcastle United|Aston Villa", "Troyes|Lens", "Venezia|Napoli", "Werder Bremen|SC Paderborn", "Espanyol|Atletico Madrid", "Atletico MG|Coritiba", "New England|Chicago Fire", "Leon|America", "Sporting KC|Real Salt Lake", "Philadelphia|Charlotte", "Everton|Chelsea", "Roma|Genoa"]
DEST=['Real Betis|Barcelona','Macará|Independiente del Valle','Aucas|LDU Quito','Newcastle United|Aston Villa']
COL.update({"Everton": "#003399", "Chelsea": "#034694", "Brentford": "#e30613", "Liverpool": "#c8102e", "Fulham": "#ffffff", "Hull City": "#f5a12d", "Manchester City": "#6cabdd", "Ipswich Town": "#0044a9", "Newcastle United": "#241f20", "Aston Villa": "#670e36", "Espanyol": "#0057b8", "Atletico Madrid": "#cb3524", "Villarreal": "#ffe114", "Elche": "#ffffff", "Real Betis": "#0bb363", "Barcelona": "#a50044", "Valencia": "#ffffff", "Athletic Club": "#ee2523", "Bayern Munich": "#dc052d", "RB Leipzig": "#ffffff", "Union Berlin": "#d4011d", "Borussia Dortmund": "#fde100", "Hamburger SV": "#ffffff", "VfB Stuttgart": "#ffffff", "Werder Bremen": "#1d9053", "SC Paderborn": "#005ca9", "Schalke 04": "#004d9d", "Mainz 05": "#c3141e", "Elversberg": "#000000", "Augsburg": "#ba3733", "ADO Den Haag": "#ffd700", "PSV": "#e3001b", "Telstar": "#ffffff", "Feyenoord": "#e30613", "Sparta Rotterdam": "#e2001a", "Willem II": "#e2001a", "Venezia": "#111111", "Napoli": "#12a0d7", "Bologna": "#a6192e", "Inter": "#0068a8", "Roma": "#8e1f2f", "Genoa": "#a6192e", "Strasbourg": "#0055a4", "Paris Saint-Germain": "#1e3f8f", "Lille": "#d2001f", "Brest": "#e30613", "Troyes": "#1f4e9c", "Lens": "#ffd400", "Santos Laguna": "#00843d", "Queretaro": "#ffffff", "Guadalajara": "#c8102e", "Tigres UANL": "#fdb913", "Leon": "#00843d", "America": "#ffe100", "Toluca": "#d50032", "A. San Luis": "#d50032", "Cruz Azul": "#0047ab", "Juarez": "#39b54a", "Philadelphia": "#0b1f41", "Charlotte": "#4b9cd3", "Minnesota United": "#111111", "New England": "#0a2240", "Chicago Fire": "#c8102e", "New York RB": "#111111", "DC United": "#111111", "Dallas": "#d11241", "Real Salt Lake": "#b30838", "Nashville SC": "#ece83a", "Seattle": "#5d9741", "LA Galaxy": "#ffffff", "Colorado Rapids": "#111111", "Independiente del Valle": "#111111", "Macará": "#5bc2e7", "LDU Quito": "#ffffff", "Aucas": "#ffd100", "Guayaquil City": "#ffffff", "Millonarios": "#0a2a66", "Independiente Medellín": "#d0021b", "Atlético Nacional": "#00843d", "Atletico MG": "#161616", "Coritiba": "#0b5d34", "São Paulo": "#e8e8e8", "Vasco da Gama": "#161616", "Athletico-PR": "#c8102e", "Palmeiras": "#006437", "Botafogo": "#161616", "Chapecoense": "#0e7a3c", "Independiente Rivadavia": "#1d3f8f", "Tigre": "#1d3f8f", "Banfield": "#0b6b3a", "Argentinos Juniors": "#c8102e", "Platense": "#5a3a22", "Lanus": "#8a1538", "Velez Sarsfield": "#e8e8e8", "Gimnasia Mendoza": "#141414", "Atletico Tucuman": "#6cc3ee", "Rosario Central": "#1d3f8f", "Atlanta United": "#a1192e", "Inter Miami": "#f5b6cd", "Sporting KC": "#91b0d5", "Portland": "#00482b", "CF Montreal": "#111111"})
# Aciertos de ayer (viernes 16): (partido, marcador real, nuestro Over 1.5, medio, url)
ACIERTOS=[("Atlante vs Pumas","1-2","79,3 % · partido del día","Excélsior","https://www.excelsior.com.mx/deportes/pumas-resurge-suena-con-liguilla-y-deja-atlante-borde-abismo")]
LLEGAN={
 'Telstar|Feyenoord':["Feyenoord es líder invicto tras 8 jornadas con 27 goles, el ataque más goleador de la Eredivisie.",
   "Feyenoord fuera: 16 goles a favor y 3 en contra en 4 partidos.",
   "Telstar, 15.º, no ganó en sus 4 partidos de local: 5 goles a favor y 11 en contra.",
   "Fuentes: Sports Mole y tabla de local y visitante de Sports Mole."],
 'Bayern Munich|RB Leipzig':["Bayern, 3.º con 11 puntos e invicto: en casa marcó 12 y recibió 1 en 2 partidos.",
   "RB Leipzig perdió sus 2 salidas: 1 gol a favor y 5 en contra fuera de casa.",
   "En el último duelo, Bayern ganó 1-5 en Leipzig (17-ene-2026).",
   "Fuentes: Sports Mole, hessenschau.de y Fútbol Total."],
 'ADO Den Haag|PSV':["PSV fuera: 13 goles a favor y 6 en contra en 4 partidos.",
   "ADO Den Haag es penúltimo, recibió 8 goles en 3 partidos de local y no le gana al PSV desde 2011.",
   "ADO sin Milan Hokke (sancionado); PSV sin Plaa ni Sildillia.",
   "Fuente: Sports Mole."],
 'Toluca|A. San Luis':["Toluca, 2.º con 20 puntos, marcó 15 goles en 5 partidos de local.",
   "Atlético San Luis, 15.º con 12 puntos, recibió 10 goles en 5 salidas.",
   "Toluca viene de perder 3-2 con Tigres; Paulinho suma 4 goles.",
   "Fuentes: SoccerSTATS y Fox Sports México."],
}
