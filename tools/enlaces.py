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

# ---- Domingo 18-oct-2026 (rutina diaria, sellado 06:13 ECU) ----
# LINK: una previa real publicada por partido (titular traducido al español, medio y enlace a la nota original).
LINK={
 'Osasuna|Racing Santander':("Osasuna vs Racing de Santander: previa, pronóstico, novedades y alineaciones","Sports Mole","https://www.sportsmole.co.uk/football/osasuna/preview/osasuna-vs-racing-prediction-team-news-lineups_607021.html"),
 'Cambuur|AZ':("Cambuur vs AZ: pronóstico y previa del 18 de octubre de 2026","FootballPredictions.com","https://footballpredictions.com/footballpredictions/netherlands-eredivisie-predictions/cambuur-vs-az-prediction-18-10-2026/"),
 'AFC Bournemouth|Sunderland':("Bournemouth vs Sunderland: pronóstico y previa (18/10/2026)","Football Whispers","https://footballwhispers.com/blog/bournemouth-vs-sunderland-prediction-18-10-2026/"),
 'Brighton & Hove Albion|Crystal Palace':("Brighton vs Crystal Palace: pronóstico y previa del 18 de octubre","FootballPredictions.com","https://footballpredictions.com/footballpredictions/premierleaguepredictions/brighton-vs-crystal-palace-prediction-18-10-2026/"),
 'Leeds United|Manchester United':("Leeds United vs Manchester United: previa, bajas y alineaciones","Khel Now","https://khelnow.com/football/leeds-united-vs-manchester-united-preview-premier-league-202610"),
 'Fiorentina|Como':("Fiorentina vs Como: previa, pronóstico, novedades y alineaciones","Sports Mole","https://www.sportsmole.co.uk/football/fiorentina/preview/fiorentina-vs-como-prediction-team-news-lineups_607028.html"),
 'Angers|Marseille':("Angers vs Marsella: previa, pronóstico, novedades y alineaciones","Sports Mole","https://www.sportsmole.co.uk/football/angers/preview/angers-vs-marseille-prediction-team-news-lineups_607039.html"),
 'Bayer Leverkusen|SC Freiburg':("Bayer Leverkusen vs Friburgo: pronóstico y previa (18/10/2026)","Football Whispers","https://footballwhispers.com/blog/bayer-leverkusen-vs-freiburg-prediction-preview-18-10-2026/"),
 'Celta Vigo|Alaves':("Celta vs Alavés: previa, pronóstico, novedades y alineaciones","Sports Mole","https://www.sportsmole.co.uk/football/celta-vigo/preview/celta-vigo-vs-alaves-prediction-team-news-lineups_607025.html"),
 'FC Groningen|Ajax':("Groningen vs Ajax: pronóstico y previa","Football Whispers","https://footballwhispers.com/blog/groningen-vs-ajax-prediction-18-10-2026/"),
 'Le Havre|Auxerre':("Le Havre vs Auxerre: previa, pronóstico, novedades y alineaciones","Sports Mole","https://www.sportsmole.co.uk/football/le-havre/preview/le-havre-vs-auxerre-prediction-team-news-lineups_607041.html"),
 'Lorient|Monaco':("Lorient vs Mónaco: previa, pronóstico, novedades y alineaciones","Sports Mole","https://www.sportsmole.co.uk/football/lorient/preview/lorient-vs-monaco-prediction-team-news-lineups_607009.html"),
 'Paris FC|Rennes':("Paris FC vs Rennes: previa, pronóstico, novedades y alineaciones","Sports Mole","https://www.sportsmole.co.uk/football/paris-fc/preview/paris-fc-vs-rennes-prediction-team-news-lineups_607008.html"),
 'Nottingham Forest|Arsenal':("Nottingham Forest vs Arsenal: pronóstico y previa (18/10/2026)","Football Whispers","https://footballwhispers.com/blog/nottingham-forest-vs-arsenal-prediction-18-10-2026/"),
 'Borussia Monchengladbach|Hoffenheim':("Gladbach vs Hoffenheim: previa, pronóstico, novedades y alineaciones","Sports Mole","https://www.sportsmole.co.uk/football/borussia-monchengladbach/preview/borussia-mbach-vs-hoffenheim-prediction-team-news-lineups_607011.html"),
 'AC Milan|Atalanta':("Milan vs Atalanta: previa, pronóstico, novedades y alineaciones","Sports Mole","https://www.sportsmole.co.uk/football/ac-milan/preview/ac-milan-vs-atalanta-prediction-team-news-lineups_607046.html"),
 'Sporting Cristal|Comerciantes Unidos':("A qué hora juega Sporting Cristal vs Comerciantes Unidos hoy, en el Gallardo por el Clausura","Infobae","https://www.infobae.com/peru/deportes/2026/10/18/a-que-hora-juega-sporting-cristal-vs-comerciantes-unidos-hoy-partido-gallardo-fecha-12-torneo-clausura-liga-1-2026-horario/"),
 'Malaga|Real Sociedad':("Málaga vs Real Sociedad: previa, pronóstico, novedades y alineaciones","Sports Mole","https://www.sportsmole.co.uk/football/real-sociedad/preview/malaga-vs-real-sociedad-prediction-team-news-lineups_607026.html"),
 'Delfín|Manta':("El descenso en Ecuador se aprieta y tres equipos encienden la disputa por la permanencia","El Comercio","https://www.elcomercio.com/deportes/futbol/descenso-ecuador-delfin-manta-futbol-hexagonal/"),
 'Racing Club|Independiente':("Racing recibe a Independiente en un clásico de Avellaneda con mucho en juego","MDZ","https://www.mdzol.com/deportes/2026/10/18/racing-recibe-a-independiente-en-un-clasico-de-avellaneda-con-mucho-en-juego-formaciones-hora-y-tv-1988891.html"),
 'NEC|Fortuna Sittard':("NEC vs Fortuna Sittard: pronóstico, alineaciones y previa","SportsGambler","https://www.sportsgambler.com/betting-tips/nec-nijmegen-vs-fortuna-sittard-prediction"),
 'FC Twente|FC Utrecht':("Twente vs Utrecht: previa, pronóstico, novedades y alineaciones","Sports Mole","https://www.sportsmole.co.uk/football/fc-twente/preview/fc-twente-vs-utrecht-prediction-team-news-lineups_607024.html"),
 'FC Cajamarca|CD Moquegua':("FC Cajamarca vs Moquegua, duelo directo por el descenso: qué pasa en el Acumulado","Balón Latino","https://balonlatino.net/cajamarca-vs-moquegua-descenso-liga-1-2026-acumulado/"),
 'Juventus|Lazio':("Juventus vs Lazio: previa, pronóstico, novedades y alineaciones","Sports Mole","https://www.sportsmole.co.uk/football/preview/juventus-vs-lazio-prediction-team-news-lineups_607051.html"),
 'Lyon|Nice':("Lyon vs Niza: previa, pronóstico, novedades y alineaciones","Sports Mole","https://www.sportsmole.co.uk/football/lyon/preview/lyon-vs-nice-prediction-team-news-lineups_607007.html"),
 'Real Madrid|Sevilla':("Real Madrid vs Sevilla: todo lo que hay que saber de la previa de LaLiga","GOAL","https://www.goal.com/en/news/real-madrid-sevilla-laliga-preview/blt8f29bd32e2724a59"),
 'Grêmio|Cruzeiro':("Grêmio x Cruzeiro: dónde ver, horario y alineaciones por el Brasileirão","O Tempo","https://www.otempo.com.br/sports/futebol-nacional/2026/10/17/gremio-x-cruzeiro-onde-assistir-horario-e-escalacoes-do-jogo-pelo-brasileirao"),
 'Fluminense|Santos':("Fluminense x Santos: dónde ver el partido de la 31.ª fecha del Brasileirão","Máquina do Esporte","https://maquinadoesporte.com.br/?p=244297"),
 'Leones del Norte|Emelec':("Emelec visita a Leones este domingo: qué se juega el Bombillo en el cuadrangular","El Universo","https://www.eluniverso.com/deportes/campeonato-ecuatoriano/emelec-visita-a-leones-este-domingo-que-se-juega-el-bombillo-en-el-cuadrangular-de-la-liga-ecuabet-nota/"),
 'Águilas Doradas|Tolima':("Posibles alineaciones de Águilas Doradas vs Deportes Tolima por la Liga BetPlay","Claro Sports","https://www.clarosports.com/colombia/liga-bet-play/aguilas-doradas-vs-deportes-tolima-previa/"),
 'Alianza Atlético|Universitario':("Capitán de Alianza Atlético minimiza el partido ante Universitario: 'Ya les ganamos en su casa'","Willax","https://willax.pe/deportes/capitan-alianza-atletico-minimiza-partido-universitario"),
 'Estudiantes LP|San Lorenzo':("San Lorenzo visita a Estudiantes en un duelo crucial por la clasificación a los playoffs","Diario Panorama","https://www.diariopanorama.com/noticia/569973/san-lorenzo-visita-estudiantes-duelo-crucial-clasificacion-playoffs"),
 'Estudiantes Rio Cuarto|Aldosivi':("El descendido Estudiantes de Río Cuarto enfrenta a un Aldosivi que sigue luchando por la permanencia","Diario Panorama","https://www.diariopanorama.com/noticia/569976/descendido-estudiantes-rio-cuarto-enfrenta-aldosivi-sigue-luchando-permanencia"),
 'Cincinnati|Columbus Crew':("Cincinnati y Columbus se miden en un duelo clave del derbi 'Hell Is Real'","MLSsoccer.com","https://www.mlssoccer.com/news/fc-cincinnati-columbus-crew-meet-for-critical-hell-is-real-battle-md31-2026"),
 'Bucaramanga|América de Cali':("¡Partidazo en el Montanini! Bucaramanga defiende su invicto ante América con el liderato en juego","Vanguardia","https://www.vanguardia.com/deportes/futbol/2026/10/17/partidazo-en-el-montanini-bucaramanga-defiende-su-invicto-ante-america-con-el-liderato-en-juego/"),
 'Bahia|Flamengo':("Bahia x Flamengo: pronóstico, dónde ver y alineaciones (18/10)","Trivela","https://trivela.com.br/onde-assistir/palpite-escalacoes-bahia-x-flamengo-18-10-2026/"),
 'Barcelona SC|Universidad Católica':("Barcelona SC no le gana a Universidad Católica desde el 2024","El Universo","https://www.eluniverso.com/deportes/campeonato-ecuatoriano/barcelona-sc-no-le-gana-a-universidad-catolica-desde-el-2024-nota/"),
 'Remo|Bragantino':("Remo x RB Bragantino: dónde ver, horario y alineaciones en el Brasileirão","Band","https://www.band.com.br/esportes/futebol/brasileirao-serie-a/remo-x-rb-bragantino-onde-assistir-horario-e-escalacoes-no-brasileirao"),
 'Llaneros|Santa Fe':("Posibles alineaciones de Llaneros vs Santa Fe por la Liga BetPlay","Claro Sports","https://www.clarosports.com/colombia/liga-bet-play/previa-llaneros-vs-santa-fe/"),
 'Belgrano|River Plate':("River visita a Belgrano y Estudiantes recibe a San Lorenzo: los partidos del domingo por el Clausura","Diario Neuquino","https://diarioneuquino.com.ar/river-visita-a-belgrano-y-estudiantes-recibe-a-san-lorenzo-los-partidos-del-domingo-por-el-torneo-clausura/"),
 'Cienciano|UTC':("Cienciano vs. UTC: ¿qué canal transmite la fecha 12 del Torneo Clausura?","RPP","https://rpp.pe/futbol/descentralizado/cienciano-vs-utc-en-vivo-horario-y-que-canal-pasa-fecha-12-torneo-clausura-2026-via-l1max-partidos-de-hoy-noticia-1713169"),
 'Monterrey|Pachuca':("Monterrey vs Pachuca en vivo: dónde ver y hora, jornada 12 del Apertura 2026","Fox Sports México","https://www.foxsports.com.mx/2026/10/15/monterrey-vs-pachuca-en-vivo-donde-ver-en-tv-online-y-hora-jornada-12-liga-mx-apertura-2026/"),
 'Deportivo Cali|Junior':("Deportivo Cali vs. Junior: hora y dónde ver el juego de la fecha 15 de la Liga BetPlay","El País","https://www.elpais.com.co/deportes/deportivo-cali-vs-junior-de-barranquilla-hora-y-donde-ver-el-juego-de-la-fecha-15-de-la-liga-betplay-dimayor-1737.html"),
}
import json as _j, os as _o
_P=_j.load(open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),'pron.json')))
PRED=[f"{p['local']}|{p['visita']}" for p in sorted(_P,key=lambda p:-p['over15']) if not p.get('sin') and round(p['over15'],1)>=79.5]
DEST=['Real Madrid|Sevilla','Barcelona SC|Universidad Católica','Leeds United|Manchester United','Racing Club|Independiente']
COL.update({'Osasuna':'#d91a21','Racing Santander':'#00843d','Cambuur':'#f6d11b','AZ':'#e30613','AFC Bournemouth':'#da291c','Sunderland':'#eb172b',
 'Brighton & Hove Albion':'#0057b8','Leeds United':'#ffffff','Manchester United':'#da291c','Fiorentina':'#5b2b82','Como':'#1d3f8f','Angers':'#1a1a1a',
 'Marseille':'#ffffff','Bayer Leverkusen':'#e32221','SC Freiburg':'#1a1a1a','Celta Vigo':'#8ac3ee','Alaves':'#1d4fa0','FC Groningen':'#00a650','Ajax':'#d2122e',
 'Le Havre':'#5aa5dc','Auxerre':'#ffffff','Lorient':'#f37021','Monaco':'#e51b22','Paris FC':'#1b2a4a','Rennes':'#e13327','Nottingham Forest':'#dd0000',
 'Arsenal':'#ef0107','Borussia Monchengladbach':'#ffffff','Hoffenheim':'#1961b5','Sporting Cristal':'#6cc4ec','Comerciantes Unidos':'#c8102e','Malaga':'#5fa8e0',
 'Real Sociedad':'#0067b1','Delfín':'#f7c600','Manta':'#1d5fb8','Racing Club':'#6cabdd','Independiente':'#e30613','NEC':'#c8102e','Fortuna Sittard':'#f6d11b',
 'FC Twente':'#e30613','FC Utrecht':'#ffffff','FC Cajamarca':'#1d3f8f','CD Moquegua':'#f39200','Juventus':'#1a1a1a','Lyon':'#ffffff','Real Madrid':'#ffffff',
 'Grêmio':'#0d80bf','Leones del Norte':'#f7c600','Emelec':'#1d3f8f','Águilas Doradas':'#f6b21b','Tolima':'#8a1538','Alianza Atlético':'#ffffff','Universitario':'#f5e6c8',
 'Estudiantes LP':'#e30613','San Lorenzo':'#1d3f8f','Estudiantes Rio Cuarto':'#1d5fb8','Aldosivi':'#f6d11b','Cincinnati':'#f05323','Columbus Crew':'#fedd00',
 'Bucaramanga':'#f6d11b','América de Cali':'#c8102e','Bahia':'#1d4fa0','Remo':'#1b2a6b','Llaneros':'#e30613','Santa Fe':'#c8102e','Belgrano':'#6cc4ec',
 'River Plate':'#ffffff','Cienciano':'#c8102e','UTC':'#1a1a1a','Monterrey':'#0b2a5b','Deportivo Cali':'#00843d','Junior':'#e30613','Santos':'#f2f2f2','Fluminense':'#7a1230','Flamengo':'#c3281e','Cruzeiro':'#1d3f8f','Bragantino':'#e8e8e8','Lazio':'#87cfee','Atlanta':'#1e3c8c','Atalanta':'#1e3c8c','AC Milan':'#c8102e','Universidad Católica':'#1d3f8f','Barcelona SC':'#f7c600','Sevilla':'#f4f4f4','Pachuca':'#1c3e72','Nice':'#b0101f','Crystal Palace':'#1b458f'})
# Aciertos de ayer (sábado 17): (partido, marcador real, nuestro Over 1.5, medio, url)
ACIERTOS=[
 ("Telstar vs Feyenoord","3-4","94,8 % · partido del día","Voetbalzone","https://www.voetbalzone.nl/nieuws/feyenoord-wint-knotsgekke-zevenklapper-op-bezoek-bij-telstar/blt50d85c1c2cc47b9a"),
 ("Bayern Múnich vs RB Leipzig","6-1","94,3 %","Fútbol Total","https://futboltotal.futbol/partido/bayern-munchen-vs-rb-leipzig-bundesliga-1575185"),
 ("ADO Den Haag vs PSV","2-1","94,1 %","Sporza","https://sporza.be/nl/sport/voetbal/~3338868/"),
 ("Elversberg vs Augsburg","4-3","93,5 %","Fútbol Total","https://futboltotal.futbol/partido/sv-elversberg-vs-fc-augsburg-bundesliga-1575193"),
 ("Manchester City vs Ipswich Town","3-2","92,2 %","Fútbol Total","https://futboltotal.futbol/partido/manchester-city-vs-ipswich-premier-league-2026-10-17"),
 ("Cruz Azul vs FC Juárez","5-0","91,2 %","Fútbol Total","https://futboltotal.futbol/partido/cruz-azul-vs-fc-juarez-liga-mx-2026-10-18"),
 ("Sparta Rotterdam vs Willem II","3-2","90,2 %","Voetbalprimeur","https://voetbalprimeur.nl/nieuws/2148090/sparta-doet-goede-zaken-en-verslaat-willem-ii.html"),
 ("Atlanta United vs Inter Miami","1-3","90,2 %","Fútbol Total","https://futboltotal.futbol/partido/atlanta-united-fc-vs-inter-miami-mls-2026-10-18"),
]
LLEGAN={
 'Borussia Monchengladbach|Hoffenheim':["Gladbach es último (18.º) con 0 puntos tras 5 derrotas seguidas: 7 goles a favor y 18 en contra en la liga.",
   "En casa, los partidos de Gladbach promedian 7 goles: 6 a favor y 8 en contra en 2 partidos.",
   "Hoffenheim (17.º, 3 puntos) perdió sus 4 últimos partidos; fuera lleva 3 goles a favor y 6 en contra en 2.",
   "Fuentes: Sports Mole (tabla de local y visitante y previa)."],
 'Cincinnati|Columbus Crew':["Cincinnati en casa: 36 goles a favor y 27 en contra en 13 partidos (4,8 goles por partido en su estadio).",
   "Columbus fuera recibió 30 goles en 14 partidos; es 13.º del Este, a 4 puntos de playoffs.",
   "Es el derbi 'Hell Is Real' de Ohio, en horario estelar del domingo.",
   "Fuentes: SoccerSTATS (más los resultados del sábado), Cincinnati Soccer Talk y MLSsoccer.com."],
 'Cambuur|AZ':["Cambuur recibe 3,25 goles por partido en casa: 13 en 4 partidos.",
   "AZ fuera: 9 goles a favor y 5 en contra en 4 partidos.",
   "En 11 enfrentamientos, AZ ganó 7 y empató 4; Cambuur nunca le ganó.",
   "Fuentes: Sports Mole (tabla de local y visitante) y FootballPredictions.com."],
 'FC Twente|FC Utrecht':["Twente tiene 12 de 12 puntos en casa: 9 goles a favor y 3 en contra.",
   "Utrecht fuera: 6 goles a favor y 11 en contra en 4 partidos.",
   "Twente solo perdió en la jornada 1 de esta Eredivisie.",
   "Fuentes: Sports Mole (tabla de local y visitante y previa)."],
}

# ---- Lunes 19-oct-2026 (rutina diaria, sellado 05:38 ECU) ----
# LINK: una previa real publicada por partido (titular en español, medio y enlace a la nota original).
LINK={
 'Monza|Cagliari':("Monza vs Cagliari: horario y TV de la jornada 7 de la Serie A","Fútbol Total","https://futboltotal.futbol/partido/monza-vs-cagliari-serie-a-1550153"),
 'Parma|Torino':("Parma-Torino, probables alineaciones: vuelve Bernabé y Kulenovic arranca en el banco","TuttoMercatoWeb","https://www.tuttomercatoweb.com/probabili-formazioni/parma-torino-probabili-formazioni-2283912"),
 'Tottenham Hotspur|Coventry City':("Tottenham vs Coventry: previa, novedades de los equipos y pronóstico de la jornada 7","The Stats Zone","https://www.thestatszone.com/tottenham-vs-coventry-preview-team-news-prediction-2026-27-english-premier-league-230568"),
 'Getafe|Rayo Vallecano':("Getafe vs Rayo Vallecano: horario, TV y alineaciones previstas de la jornada 9","Fútbol Total","https://futboltotal.futbol/partido/getafe-vs-rayo-vallecano-la-liga-2026-10-19"),
 'Mushuc Runa|Orense':("Mushuc Runa vs Orense: previa, horario y cómo llegan a la fecha 3","Anecdotarios","https://anecdotarios.com/2026/10/17/mushuc-runa-vs-orense-previa-horario-y-como-llegan-para-la-fecha-3-del-torneo-ecuatoriano/"),
 'Newells Old Boys|Central Cordoba SdE':("Partidos de hoy, lunes 19 de octubre: Newell's vs Central Córdoba, horario y TV","Noticias de Bariloche","https://www.noticiasdebariloche.com.ar/partidos-de-futbol-de-hoy-lunes-19-de-octubre-horario-y-como-ver-por-tv-y-online/"),
 'Sarmiento|Barracas Central':("Partidos de hoy, lunes 19 de octubre: Sarmiento vs Barracas Central, horario y TV","Noticias de Bariloche","https://www.noticiasdebariloche.com.ar/partidos-de-futbol-de-hoy-lunes-19-de-octubre-horario-y-como-ver-por-tv-y-online/"),
 'Corinthians|Vitória':("Corinthians vs Vitória: previa de la jornada 31 del Brasileirão","Fútbol Total","https://futboltotal.futbol/partido/corinthians-vs-vitoria-brasileirao-2026-10-20"),
 'Deportivo Riestra|Union Santa Fe':("Partidos de hoy, lunes 19 de octubre: Riestra vs Unión, horario y TV","Noticias de Bariloche","https://www.noticiasdebariloche.com.ar/partidos-de-futbol-de-hoy-lunes-19-de-octubre-horario-y-como-ver-por-tv-y-online/"),
 'Pasto|Alianza (ex Alianza Petrolera)':("Liga BetPlay 2026-II: programación completa de la fecha 15, horarios y dónde ver","Vanguardia","https://www.vanguardia.com/deportes/futbol/2026/10/17/liga-betplay-2026-ii-programacion-de-la-fecha-15-con-bucaramanga-america-como-uno-de-los-partidos-destacados/"),
}
PRED=[f"{p['local']}|{p['visita']}" for p in sorted(_P,key=lambda p:-p['over15']) if not p.get('sin') and round(p['over15'],1)>=79.5]
DEST=['Getafe|Rayo Vallecano','Tottenham Hotspur|Coventry City','Mushuc Runa|Orense','Corinthians|Vitória']
COL.update({'Cagliari':'#9b1b30','Parma':'#ffd200','Torino':'#8b1a1a','Tottenham Hotspur':'#ffffff','Coventry City':'#6cc3ee','Getafe':'#005999','Rayo Vallecano':'#ffffff',
 'Central Cordoba SdE':'#1a1a1a','Sarmiento':'#00843d','Barracas Central':'#c8102e','Deportivo Riestra':'#1a1a1a','Union Santa Fe':'#c8102e','Vitória':'#c8102e','Pasto':'#c8102e'})
# Aciertos de ayer (domingo 18): (partido, marcador real, nuestro Over 1.5, medio, url)
ACIERTOS=[
 ("M'gladbach vs Hoffenheim","1-2","97 % · partido del día · GOL ÉLITE","Fútbol Total","https://futboltotal.futbol/partido/borussia-monchengladbach-vs-1899-hoffenheim-bundesliga-2026-10-18"),
 ("FC Cincinnati vs Columbus Crew","0-2","96 % · GOL ÉLITE","Fútbol Total","https://futboltotal.futbol/partido/partido-fc-cincinnati-vs-columbus-crew-major-league-soccer-2026-10-19"),
 ("Cambuur vs AZ","2-2","93 % · GOLES PLATINO","Livescore","https://www.livescore.com/en/football/netherlands/eredivisie/cambuur-vs-az-alkmaar/1790248/"),
 ("FC Twente vs FC Utrecht","1-2","90 % · GOLES PLATINO","Voetbalprimeur","https://voetbal.headliner.nl/item/fc-twente-verzuimt-tweede-plek-over-te-nemen-na-nederlaag-tegen-fc-utrecht-voetbalprimeur-715087"),
 ("Alianza Atlético vs Universitario","1-4","89 % · GOLES ESTÁNDAR","El Comercio","https://elcomercio.pe/deporte-total/futbol-peruano/universitario-vs-alianza-atletico-en-vivo-online-gratis-por-torneo-clausura-de-la-liga-1-lbposting-noticia/"),
 ("Groningen vs Ajax","2-5","89 % · GOLES ESTÁNDAR","Sporza","https://sporza.be/nl/sport/voetbal/~3338823/"),
 ("NEC vs Fortuna Sittard","2-2","87 % · GOLES ESTÁNDAR","Fútbol Total","https://futboltotal.futbol/partido/nec-nijmegen-vs-fortuna-sittard-eredivisie-2026-10-18"),
 ("Sporting Cristal vs Comerciantes Unidos","4-2","87 % · GOLES ESTÁNDAR","El Diez","https://www.eldiez.com.pe/sporting-cristal-2/sporting-cristal-vs-comerciantes-unidos-en-vivo-por-liga-1-a-que-hora-y-donde-ver-resumen-goles-noticia/"),
]
LLEGAN={
 'Getafe|Rayo Vallecano':["Rayo Vallecano recibe 3 goles por partido fuera de casa: 12 en contra (y 5 a favor) en 4 partidos.",
   "Getafe en casa: 4 goles a favor y 2 en contra en 4 partidos.",
   "En los últimos 6 enfrentamientos, Rayo ganó 3 y hubo 3 empates; Getafe no ganó ninguno.",
   "Fuentes: tabla de LaLiga 2026-27 (Football Web Pages y Fútbol Total, partido a partido) y previa de Fútbol Total."],
 'Monza|Cagliari':["En casa, los partidos de Monza promedian 4 goles: 4 a favor y 4 en contra en 2 partidos.",
   "Cagliari fuera: 4 goles a favor y 1 en contra en 3 partidos.",
   "Cagliari llega con 3 victorias, 1 empate y 1 derrota en sus últimos 5 partidos.",
   "Fuentes: tabla de la Serie A 2026-27 (SoccerSTATS más resultados partido a partido) y ficha de Fútbol Total."],
 'Deportivo Riestra|Union Santa Fe':["Unión recibe 1,8 goles por partido fuera: 11 en contra en 6 partidos.",
   "Riestra en casa: 7 goles a favor y 6 en contra en 6 partidos.",
   "Es el cierre de la fecha 13 del Clausura, el lunes a las 19:15 de Ecuador.",
   "Fuentes: tabla del Clausura 2026 calculada partido a partido (AFP, Noticias de Bariloche) y agenda de Líbero y RPP."],
}

# ---- Martes 20-oct-2026 (rutina diaria, sellado 05:40 ECU) ----
# LINK: una previa real publicada por partido (titular en español, medio y enlace a la nota original).
LINK={
 'Deportivo Pereira|Boyacá Chicó':("Deportivo Pereira vs Chicó: ficha y previa de la fecha 15 de la Liga BetPlay","Fútbol Total","https://futboltotal.futbol/partido/deportivo-pereira-vs-chico-primera-a-2026-10-20"),
 'Internacional de Bogotá (ex La Equidad)|Fortaleza':("Partidos de hoy, martes 20 de octubre: Inter Bogotá vs Fortaleza y la agenda completa","Líbero","https://libero.pe/futbol-internacional/2026/10/19/partidos-de-hoy-martes-20-de-octubre-partidos-hay-de-champions-league-copa-sudamericana-1505123"),
 'Cúcuta|Atlético Nacional':("Cúcuta vs Atlético Nacional: ficha, forma y árbitro de la fecha 15","Fútbol Total","https://futboltotal.futbol/partido/cucuta-vs-atletico-nacional-primera-a-2026-10-21"),
 'Guadalajara|Necaxa':("Chivas vs Necaxa: previa, forma e historial de la jornada 13 del Apertura","Fútbol Total","https://futboltotal.futbol/partido/guadalajara-chivas-vs-necaxa-liga-mx-2026-10-21"),
 'A. San Luis|Queretaro':("Atlético San Luis vs Querétaro: previa y forma de la jornada 13","Fútbol Total","https://futboltotal.futbol/partido/atletico-san-luis-vs-club-queretaro-liga-mx-2026-10-21"),
 'Juarez|Atlante':("FC Juárez vs Atlante: previa de la jornada 13 del Apertura 2026","Fútbol Total","https://futboltotal.futbol/partido/fc-juarez-vs-atlante-fc-liga-mx-2026-10-21"),
 'Millonarios|Once Caldas':("Millonarios ya tiene nueva fecha para jugar ante Once Caldas: martes 20 a las 8:30 p. m.","Publimetro","https://www.publimetro.co/deportes/2026/10/14/millonarios-ya-tiene-nueva-fecha-para-jugar-ante-once-caldas-y-tambien-movio-el-partido-contra-jaguares/"),
 'Tigres UANL|Leon':("Tigres vs León: previa, forma e historial de la jornada 13","Fútbol Total","https://futboltotal.futbol/partido/tigres-uanl-vs-leon-liga-mx-2026-10-21"),
}
PRED=[f"{p['local']}|{p['visita']}" for p in sorted(_P,key=lambda p:-p['over15']) if not p.get('sin') and round(p['over15'],1)>=79.5]
DEST=['Millonarios|Once Caldas','Tigres UANL|Leon','Internacional de Bogotá (ex La Equidad)|Fortaleza','A. San Luis|Queretaro']
COL.update({'Deportivo Pereira':'#f6d11b','Boyacá Chicó':'#1d3f8f','Internacional de Bogotá (ex La Equidad)':'#c8102e','Fortaleza':'#ffffff',
 'Cúcuta':'#c8102e','Once Caldas':'#ffffff','Necaxa':'#d6001c'})
# Aciertos de ayer (lunes 19): (partido, marcador real, nuestro Over 1.5, medio, url)
ACIERTOS=[
 ("Getafe vs Rayo Vallecano","1-1 · marcador exacto","77 % · partido del día","Fútbol Total","https://futboltotal.futbol/partido/getafe-vs-rayo-vallecano-la-liga-2026-10-19"),
 ("Monza vs Cagliari","4-0","76 %","Quotidiano Sport","https://sport.quotidiano.net/calcio/monza/monza-cagliari-4-0-i-brianzoli-calano-il-poker-contro-i-sardi-d048db81"),
 ("Riestra vs Unión","1-1 · marcador exacto","73 %","Fútbol Total","https://futboltotal.futbol/partido/deportivo-riestra-vs-union-santa-fe-liga-profesional-argentina-2026-10-20"),
 ("Parma vs Torino","0-3","71 %","Fútbol Total","https://futboltotal.futbol/partido/parma-vs-torino-serie-a-2026-10-19"),
 ("Tottenham vs Coventry City","3-1","63 %","Fútbol Total","https://futboltotal.futbol/partido/tottenham-vs-coventry-premier-league-2026-10-19"),
 ("Newell's vs Central Córdoba","2-1","62 %","La Nación","https://www.lanacion.com.ar/deportes/canchallena/newells-old-boys-vencio-por-2-1-a-central-cordoba-santiago-del-estero-por-el-torneo-clausura-2026-nid19102026/"),
]
LLEGAN={
 'Guadalajara|Necaxa':["Necaxa recibe 2,2 goles por partido fuera de casa: 11 en contra (y 7 a favor) en 5 partidos.",
   "Chivas en casa: 10 goles a favor y 7 en contra en 6 partidos (2,8 goles por partido en su estadio).",
   "Necaxa llega con 1 empate y 4 derrotas en sus últimos 5; en 4 de esos 5 partidos hubo 2 goles o más (0-2, 3-3, 2-4, 3-1, 0-1).",
   "Fuentes: tabla del Apertura 2026 (SoccerSTATS más resultados partido a partido) y ficha de Fútbol Total."],
 'Cúcuta|Atlético Nacional':["Atlético Nacional fuera: 17 goles a favor y 8 en contra en 7 partidos (3,6 goles por partido).",
   "Cúcuta en casa: 11 goles a favor y 6 en contra en 6 partidos.",
   "Cúcuta ganó sus 3 últimos partidos; Nacional viene de golear 4-1 a Boyacá Chicó como visitante.",
   "Fuentes: tabla de la Liga BetPlay 2026-II (SoccerSTATS más resultados partido a partido), ficha de Fútbol Total y El Universal."],
 'Internacional de Bogotá (ex La Equidad)|Fortaleza':["En casa, los partidos de Inter Bogotá promedian 3 goles: 10 a favor y 11 en contra en 7 partidos.",
   "Fortaleza fuera: 6 goles a favor y 8 en contra en 6 partidos.",
   "Es uno de los 4 partidos de la Liga BetPlay de este martes (18:15, hora de Ecuador).",
   "Fuentes: tabla de la Liga BetPlay 2026-II (SoccerSTATS más resultados partido a partido) y agenda de Líbero."],
}

# ---- Miércoles 21-oct-2026 (rutina diaria, sellado 05:33 ECU) ----
# LINK: una previa real publicada por partido (titular en español, medio y enlace a la nota original).
LINK={
 'Levante|Athletic Club':("El Levante-Athletic aplazado se juega hoy en el Ciutat de València","El Gol Digital","https://www.elgoldigital.com/futbol/athletic-club/levante-athletic-aplazado-nueva-fecha-21-octubre/"),
 'Cincinnati|DC United':("FC Cincinnati vs D.C. United: ficha, forma e historial del partido pendiente de la MLS","Fútbol Total","https://futboltotal.futbol/partido/fc-cincinnati-vs-dc-united-mls-2026-10-22"),
 'Llaneros|Deportivo Cali':("Llaneros vs Deportivo Cali: ficha y forma en el Bello Horizonte","Fútbol Total","https://futboltotal.futbol/partido/llaneros-vs-deportivo-cali-primera-a-2026-10-22"),
 'Toluca|Tijuana':("Toluca vs Tijuana: previa, forma e historial de la jornada 13","Fútbol Total","https://futboltotal.futbol/partido/toluca-vs-club-tijuana-liga-mx-2026-10-22"),
 'Atlas|America':("Atlas vs América: dónde ver el partido de la jornada 13 del Apertura 2026","Fox Sports México","https://www.foxsports.com.mx/2026/10/19/atlas-vs-america-donde-ver-el-partido-de-la-jornada-13-del-apertura-2026/"),
 'Puebla|Monterrey':("Puebla vs Monterrey: ficha y forma de la jornada 13 del Apertura","Fútbol Total","https://futboltotal.futbol/partido/puebla-vs-monterrey-liga-mx-2026-10-22"),
 'Santa Fe|Jaguares de Córdoba':("Santa Fe vs Jaguares: el partido aplazado se juega por fin en El Campín","Fútbol Total","https://futboltotal.futbol/partido/santa-fe-vs-jaguares-primera-a-2026-10-16"),
 'Pachuca|Cruz Azul':("Pachuca vs Cruz Azul: previa, forma e historial de la jornada 13","Fútbol Total","https://futboltotal.futbol/partido/pachuca-vs-cruz-azul-liga-mx-2026-10-22"),
 'Santos Laguna|Pumas UNAM':("Santos vs Pumas: horario, alineaciones y dónde ver la jornada 13","Claro Sports","https://www.clarosports.com/futbol/liga-mx/santos-vs-pumas-en-vivo-la-liga-mx-horario-alineaciones-y-donde-ver-el-partido-del-apertura-2026-jornada-13/"),
}
PRED=[f"{p['local']}|{p['visita']}" for p in sorted(_P,key=lambda p:-p['over15']) if not p.get('sin') and round(p['over15'],1)>=79.5]
DEST=['Santos Laguna|Pumas UNAM','Puebla|Monterrey','Santa Fe|Jaguares de Córdoba']
COL.update({'Athletic Club':'#e30613','Cincinnati':'#f05323','DC United':'#141414','Llaneros':'#e8b400','Deportivo Cali':'#0b7a3a',
 'Toluca':'#d0021b','Atlas':'#b0101f','America':'#f6d11b','Monterrey':'#0b2a52','Santa Fe':'#c8102e','Jaguares de Córdoba':'#0a7a3c','Levante':'#1f2f6b'})
# Aciertos de ayer (martes 20): (partido, marcador real, nuestro Over 1.5, medio, url)
ACIERTOS=[
 ("Inter Bogotá vs Fortaleza","2-1","76 %","El Deportivo","https://eldeportivo.com.co/futbol-colombiano/liga-betplay/internacional-impone-fortaleza-derbi-de-bogota/"),
 ("Atlético San Luis vs Querétaro","2-1","75 %","El Tiempo MX","https://eltiempomx.com/noticia/2026/san-luis-vence-2-1-a-queretaro-en-el-clasico-de-la-57.html"),
 ("Tigres vs León","0-2","73 %","SDP Noticias","https://www.sdpnoticias.com/deportes/tigres-se-sigue-hundiendo-en-la-liga-mx-tras-perder-con-leon/"),
 ("Millonarios vs Once Caldas","1-1","63 %","Fútbol Total","https://futboltotal.futbol/partido/millonarios-vs-once-caldas-primera-a-2026-10-21"),
 ("Deportivo Pereira vs Boyacá Chicó","2-0","63 %","El Deportivo","https://eldeportivo.com.co/futbol-colombiano/liga-betplay/deportivo-pereira-toma-respiro-vencer-boyaca-chico/"),
]
LLEGAN={
 'Pachuca|Cruz Azul':["En casa, los partidos de Pachuca promedian 4 goles: 9 a favor y 11 en contra en 5 partidos.",
   "Cruz Azul fuera: 10 goles a favor y 9 en contra en 5 partidos (3,8 goles por partido).",
   "Cruz Azul viene de golear 5-0 a FC Juárez y de empatar 3-3 con Pumas y con Toluca; Pachuca empató 3-3 con Necaxa y perdió 2-1 en Monterrey.",
   "Fuentes: tabla del Apertura 2026 (SoccerSTATS más resultados partido a partido) y ficha de Fútbol Total."],
 'Cincinnati|DC United':["En casa, los partidos de Cincinnati promedian 4,6 goles: 36 a favor y 29 en contra en 14 partidos.",
   "D.C. United fuera recibe 1,8 goles por partido: 25 en contra (y 17 a favor) en 14 partidos.",
   "D.C. United viene de perder 4-1 en Orlando y 4-0 en Miami; Cincinnati perdió 3-2 con New England y 0-2 con Columbus en casa.",
   "Fuentes: tabla de la MLS 2026 (SoccerSTATS más resultados partido a partido) y ficha de Fútbol Total."],
 'Toluca|Tijuana':["Toluca en casa: 16 goles a favor y 9 en contra en 6 partidos (4,2 goles por partido en su estadio).",
   "Tijuana fuera: 5 goles a favor y 8 en contra en 4 partidos.",
   "En los últimos 6 duelos hubo 3-3, 2-4 y 4-0; Toluca ganó 3, Tijuana 1 y hubo 2 empates.",
   "Fuentes: tabla del Apertura 2026 (SoccerSTATS más resultados partido a partido) y ficha de Fútbol Total."],
 'Atlas|America':["América fuera: 16 goles a favor y 11 en contra en 6 partidos (4,5 goles por partido).",
   "Atlas en casa: 6 goles a favor y 9 en contra en 6 partidos.",
   "América es líder del Apertura y viene de ganar 3-5 en León; Atlas ganó 2-0 a Necaxa.",
   "Fuentes: tabla del Apertura 2026 (SoccerSTATS más resultados partido a partido) y Fox Sports México."],
}

# ---- Viernes 23-oct-2026 (rutina recuperada por el refresco horario, sellado 16:18 ECU) ----
# LINK: una previa real publicada por partido (titular en español, medio y enlace a la nota original).
LINK={
 'Gimnasia Mendoza|Platense':("Gimnasia Mendoza vs Platense, por el Torneo Clausura 2026: horario, formaciones y TV","Minuto Uno","https://www.minutouno.com/c6335491"),
 'Cruzeiro|Remo':("Cruzeiro vs Remo: probabilidades y análisis de la 32.ª fecha del Brasileirão","Valor Final","https://valorfinal.com.br/brasileirao/2026/jogos/cruzeiro-x-remo"),
 'Tigre|Atletico Tucuman':("Tigre vs Atlético Tucumán: ficha, forma e historial de la fecha 14","Fútbol Total","https://futboltotal.futbol/partido/tigre-vs-atletico-tucuman-liga-profesional-argentina-2026-10-24"),
 'Necaxa|Juarez':("Necaxa vs FC Juárez: ficha, forma e historial de la jornada 14","Fútbol Total","https://futboltotal.futbol/partido/necaxa-vs-fc-juarez-liga-mx-2026-10-24"),
 'Atlante|A. San Luis':("Atlante vs Atlético San Luis: ficha, forma e historial de la jornada 14","Fútbol Total","https://futboltotal.futbol/partido/atlante-fc-vs-atletico-san-luis-liga-mx-2026-10-24"),
}
PRED=[f"{p['local']}|{p['visita']}" for p in sorted(_P,key=lambda p:-p['over15']) if not p.get('sin') and round(p['over15'],1)>=79.5]
DEST=['Cruzeiro|Remo','Atlante|A. San Luis']
COL.update({'Gimnasia Mendoza':'#141414','Platense':'#7a4a2a','Cruzeiro':'#1d3f8f','Remo':'#0b2a52','Tigre':'#1d3f8f','Atletico Tucuman':'#6cb4e4',
 'Necaxa':'#d6001c','Juarez':'#2c2c2c','Atlante':'#0b2a6b','A. San Luis':'#c8102e'})
# Aciertos de ayer: el jueves 22 no hubo pronósticos (la rutina no corrió) y la auditoría del miércoles 21 está pendiente.
ACIERTOS=[]
LLEGAN={}

# ---- Sábado 24-oct-2026 (rutina diaria, sellado 05:59 ECU) ----
# LINK: previa o ficha real de cada partido (titular en español, medio y enlace). Donde no se halló una previa individual verificada,
# se enlaza la página real y abierta de la agenda/fecha de su liga (Fútbol Total, Football Web Pages, Ligue 1, Valor Final, Informador, VAVEL, Primicias).
_FT=("Agenda del sábado 24 de octubre: horarios de todos los partidos","Fútbol Total","https://futboltotal.futbol/2026-10-24")
_ESP=("LaLiga 2026-27: calendario y resultados de octubre (jornada 10)","Football Web Pages","https://www.footballwebpages.co.uk/spanish-la-liga/fixtures-results")
_GER=("Bundesliga 2026-27: calendario y resultados de octubre (jornada 7)","Football Web Pages","https://www.footballwebpages.co.uk/german-bundesliga/fixtures-results/october")
_NED=("Eredivisie 2026-27: calendario y resultados de octubre (jornada 10)","Football Web Pages","https://www.footballwebpages.co.uk/dutch-eredivisie/fixtures-results/october")
_FRA=("Ligue 1: programación de la jornada 8","Ligue 1 (LFP)","https://ligue1.com/en/articles/l1_article_5797-programmations-tv-j6-j7-et-j8-l1-2627")
_BRA=("Brasileirão 2026: los partidos de la 32.ª fecha","Valor Final","https://valorfinal.com.br/brasileirao/2026/rodada-32")
_MEX=("Liga MX: calendario de la jornada 14 del Apertura 2026, horarios y dónde verla","El Informador","https://www.informador.mx/deportes/liga-mx-calendario-de-partidos-de-la-jornada-14-del-apertura-2026-horarios-y-donde-verlos-en-vivo-20261022-0066.html")
_USA=("MLS 2026: calendario de la jornada del sábado 24 de octubre","VAVEL","https://www.vavel.com/en-us/data/mls/fixtures/")
_ARG=("Liga Profesional: la fecha 14 del Clausura 2026, partido por partido","Fútbol Total","https://futboltotal.futbol/league/liga-profesional-argentina/round/clausura-14")
_ECU=("LigaPro: horarios de la fecha 4 de la fase final","Primicias","https://www.primicias.ec/deportes/donde-ver-fecha/teleamazonas-fechas-partidos-horarios-fecha4-hexagonal-cuadrangular-ver-tv-135546/")
_LIGA={'ENG':_FT,'ITA':_FT,'COL':_FT,'ESP':_ESP,'GER':_GER,'NED':_NED,'FRA':_FRA,'BRA':_BRA,'MEX':_MEX,'USA':_USA,'ARG':_ARG,'ECU':_ECU}
LINK={f"{p['local']}|{p['visita']}":_LIGA[p['liga']] for p in _P if not p.get('sin')}
LINK.update({
 'Borussia Dortmund|Eintracht Frankfurt':("Dortmund vs Eintracht Frankfurt: ficha, forma e historial de la jornada 7","Fútbol Total","https://futboltotal.futbol/partido/borussia-dortmund-vs-eintracht-frankfurt-bundesliga-2026-10-24"),
 'Chelsea|Tottenham Hotspur':("Chelsea vs Tottenham: el derbi de Londres de la jornada 8","Fútbol Total","https://futboltotal.futbol/partido/chelsea-vs-tottenham-premier-league-2026-10-24"),
 'Napoli|Roma':("Napoli vs Roma: ficha y previa de la jornada 8 de la Serie A","Fútbol Total","https://futboltotal.futbol/partido/napoli-vs-as-roma-serie-a-2026-10-24"),
 'New York RB|Inter Miami':("Red Bulls vs Inter Miami: ficha del partido del sábado en la MLS","Fútbol Total","https://futboltotal.futbol/partido/new-york-red-bulls-vs-inter-miami-mls-2026-10-24"),
 'LDU Quito|Macará':("Liga de Quito vs. Macará: precios de las entradas para la fecha 4 del hexagonal final","Primicias","https://www.primicias.ec/deportes/ligapro/liga-de-quito/ldu-macara-venta-entradas-precios-fecha4-hexagonal-final-135400/"),
})
PRED=[f"{p['local']}|{p['visita']}" for p in sorted(_P,key=lambda p:-p['over15']) if not p.get('sin') and round(p['over15'],1)>=79.5]
DEST=['Chelsea|Tottenham Hotspur','Napoli|Roma','LDU Quito|Macará','New York RB|Inter Miami']
COL.update({'1. FC Koln':'#ed1c24','PEC Zwolle':'#1d4fa0','Eintracht Frankfurt':'#111111','Deportivo Cuenca':'#c8102e','Deportivo La Coruna':'#1d4fa0',
 'Heerenveen':'#1d4fa0','Orense':'#00843d','Internacional':'#d0021b','Mirassol':'#f6d11b','Toronto':'#b81137','Talleres Cordoba':'#0b2a52',
 'Defensa y Justicia':'#00843d','Orlando City':'#633492','New York City':'#6cace4','Huracan':'#ffffff','Houston Dynamo':'#f68712',
 'SJ Earthquakes':'#0d4c92','Austin':'#00b140','St. Louis City':'#d22630','Vancouver':'#00245e','San Diego':'#00205b',
 'Manta':'#1d3f8f','Delfín':'#f6d11b','Bucaramanga':'#f6d11b','Águilas Doradas':'#f6d11b','Junior':'#c8102e','Boyacá Chicó':'#1d3f8f'})
# Aciertos de ayer (viernes 23): (partido, marcador real, nuestro Over 1.5, medio, url)
ACIERTOS=[
 ("Necaxa vs FC Juárez","1-1 · marcador exacto","83 % · partido del día","Fox Sports México","https://www.foxsports.com.mx/2026/10/23/resumen-video-goles-empate-necaxa-fc-juarez-eliminado-liguilla-liga-mx-hoy/"),
 ("Gimnasia Mendoza vs Platense","1-2","66 %","Diario Uno","https://www.diariouno.com.ar/ovacion/futbol/gimnasia-y-esgrima-no-pudo-aguantarlo-y-platense-se-lo-dio-vuelta-el-final-n1609628"),
]
LLEGAN={
 'Borussia Dortmund|Eintracht Frankfurt':["Eintracht Frankfurt recibe 3,3 goles por partido fuera de casa: 10 en contra (y 6 a favor) en 3 partidos.",
   "Dortmund en casa: 7 goles a favor y 2 en contra en 3 partidos.",
   "Frankfurt perdió 6-0 en Leipzig el 10 de octubre; los dos últimos Dortmund–Frankfurt de Bundesliga terminaron 3-2 y 3-3.",
   "Fuentes: tabla de la Bundesliga 2026-27 (Sports Mole y Football Web Pages, partido a partido) y ficha de Fútbol Total."],
 'Augsburg|Union Berlin':["Union Berlin recibe 5,5 goles por partido fuera: 11 en contra y ningún gol a favor en 2 partidos.",
   "Augsburg en casa: 7 goles a favor y 4 en contra en 3 partidos (3,7 goles por partido en su estadio).",
   "Augsburg viene de perder 4-3 en Elversberg; Union empató 0-0 con Dortmund en casa.",
   "Fuentes: tabla de la Bundesliga 2026-27 (Sports Mole y Football Web Pages, partido a partido)."],
 'FC Utrecht|PEC Zwolle':["En casa, los partidos de Utrecht promedian 5,5 goles: 8 a favor y 14 en contra en 4 partidos.",
   "PEC Zwolle fuera: 5 goles a favor y 8 en contra en 4 partidos.",
   "Utrecht ganó 1-2 en Twente y PEC Zwolle goleó 4-1 a Go Ahead Eagles el domingo 18.",
   "Fuentes: tabla de la Eredivisie 2026-27 (Sports Mole y Football Web Pages, partido a partido)."],
}
LINK['Augsburg|Union Berlin']=("Augsburg vs Union Berlin: ficha, forma e historial de la jornada 7","Fútbol Total","https://futboltotal.futbol/partido/fc-augsburg-vs-union-berlin-bundesliga-2026-10-24")
LLEGAN['Augsburg|Union Berlin'][2]="Union perdió 7-0 en Múnich y 4-0 en Leverkusen; los 4 últimos partidos de Bundesliga de Augsburg tuvieron 4 goles o más (4-3, 2-2, 3-2 y 2-2)."
LLEGAN['Augsburg|Union Berlin'][3]="Fuentes: tabla de la Bundesliga 2026-27 (Sports Mole y Football Web Pages, partido a partido) y ficha de Fútbol Total."

# ---- Sábado 24-oct, 09:45 ECU: Marco pidió tomar como referencia los partidos de SportyTrader (sus capturas) ----
_ST=['Banfield|Lanus','Talleres Cordoba|Defensa y Justicia','San Lorenzo|Newells Old Boys','Rosario Central|Huracan','Racing Santander|Espanyol',
 'Valencia|Villarreal','Atletico Madrid|Deportivo La Coruna','América de Cali|Cúcuta','Once Caldas|Deportivo Pereira','Borussia Dortmund|Eintracht Frankfurt',
 'CF Montreal|Nashville SC','Columbus Crew|Toronto','New York RB|Inter Miami','Orlando City|New York City','DC United|Cincinnati','Dallas|SJ Earthquakes',
 'Portland|Charlotte','San Diego|Seattle','Lens|Paris FC','Mirassol|São Paulo','Internacional|Botafogo','Palmeiras|Bragantino','Chapecoense|Fluminense',
 'Monterrey|Guadalajara','Pumas UNAM|Tigres UANL','Napoli|Roma','Lazio|Parma']
_PI={f"{p['local']}|{p['visita']}":p for p in _P if not p.get('sin')}
PRED=[k for k in sorted(_ST,key=lambda k:-_PI.get(k,{'over15':0})['over15']) if k in _PI and round(_PI[k]['over15'],1)>=79.5]
DEST=['Borussia Dortmund|Eintracht Frankfurt','New York RB|Inter Miami','Portland|Charlotte','DC United|Cincinnati','Chapecoense|Fluminense']
COL.update({'America de Cali':'#c8102e','América de Cali':'#c8102e','Cúcuta':'#c8102e','Once Caldas':'#ffffff','Deportivo Pereira':'#f6d11b',
 'Portland':'#004812','Charlotte':'#1a85c8','DC United':'#111111','Cincinnati':'#f05323','Chapecoense':'#00843d','Fluminense':'#7a1230'})
LINK.update({
 'New York RB|Inter Miami':("Red Bulls vs Inter Miami: previa, bajas y alineaciones","Sports Mole","https://www.sportsmole.co.uk/football/red-bulls/preview/ny-red-bulls-vs-inter-miami-prediction-team-news-lineups_607389.html"),
 'Portland|Charlotte':("Portland vs Charlotte: ficha, forma e historial de la jornada 31","Fútbol Total","https://futboltotal.futbol/partido/portland-timbers-vs-charlotte-mls-2026-10-25"),
 'DC United|Cincinnati':("D.C. United vs Cincinnati: previa y números de la temporada","Doc's Sports","https://www.docsports.com/free-picks/soccer/2026/d-c-united-vs-fc-cincinnati-prediction-10-24-2026-soccer-pick-tips-and-odds.html"),
 'Chapecoense|Fluminense':("Chapecoense vs Fluminense: tabla, forma y probabilidades de la fecha 32","Valor Final","https://valorfinal.com.br/brasileirao/2026/jogos/chapecoense-x-fluminense"),
})
LLEGAN={
 'Borussia Dortmund|Eintracht Frankfurt':["Eintracht Frankfurt recibe 3,3 goles por partido fuera de casa: 10 en contra (y 6 a favor) en 3 partidos.",
   "Dortmund en casa: 7 goles a favor y 2 en contra en 3 partidos; es 2.º con 14 puntos y Frankfurt 11.º con 8.",
   "Dortmund ganó 2-1 en Champions el martes con doblete de Guirassy; el último Dortmund–Frankfurt terminó 3-2.",
   "Fuentes: tabla de la Bundesliga 2026-27 (Sports Mole y Football Web Pages, partido a partido) y On Tour Football."],
 'New York RB|Inter Miami':["Inter Miami fuera: 2,1 goles a favor por partido (32 en 15); es el ataque más goleador de la MLS (2,4 por partido).",
   "Red Bulls en casa recibe 1,9 goles por partido (29 en 15) y perdió 3 de sus últimos 4.",
   "Miami llega con 3 victorias seguidas y Messi viene de un doblete ante Atlanta.",
   "Fuentes: tablas de local y visitante de la MLS (SoccerSTATS) y previa de Sports Mole."],
 'Portland|Charlotte':["Portland en casa: 31 goles a favor y 25 en contra en 15 partidos (3,7 goles por partido).",
   "Charlotte fuera: 24 a favor y 29 en contra en 15 partidos.",
   "Ojo: Portland suma 4 partidos sin ganar y no marcó en 2 de los últimos 3; Charlotte ganó los 2 duelos previos.",
   "Fuentes: tablas de local y visitante de la MLS (SoccerSTATS) y ficha de Fútbol Total."],
 'DC United|Cincinnati':["Cincinnati fuera: 24 a favor y 41 en contra en 15 partidos (2,7 goles recibidos por partido).",
   "Cincinnati suma 59 goles a favor y 70 en contra en la temporada; D.C. United recibió 51.",
   "Las casas de apuestas ponen la línea de goles en 3.",
   "Fuentes: tablas de local y visitante de la MLS (SoccerSTATS) y Doc's Sports."],
 'Chapecoense|Fluminense':["Chapecoense en casa recibe 2,4 goles por partido (33 en 14).",
   "Chapecoense es 20.ª con 18 puntos y 3 derrotas seguidas; Fluminense 5.º con 51 puntos, en pelea por la Libertadores.",
   "Fluminense fuera: 1,3 goles a favor y 1,5 en contra por partido (15 partidos).",
   "Fuentes: tabla del Brasileirão 2026 (local y visitante) y Valor Final."],
}

# ---- Domingo 25-oct-2026 (rutina diaria, sellado 05:40 ECU) ----
# LINK: previa o ficha real de cada partido (titular en español, medio y enlace). Donde no se halló una previa individual verificada,
# se enlaza la página real y abierta de la agenda/fecha de su liga (Fútbol Total, Football Web Pages, Ligue 1, sport-flash, VAVEL, Primicias).
_FT=("Agenda del domingo 25 de octubre: horarios de todos los partidos","Fútbol Total","https://futboltotal.futbol/2026-10-25")
_ESP=("LaLiga 2026-27: calendario y resultados de octubre (jornada 10)","Football Web Pages","https://www.footballwebpages.co.uk/spanish-la-liga/fixtures-results")
_GER=("Bundesliga 2026-27: calendario y resultados de octubre (jornada 7)","Football Web Pages","https://www.footballwebpages.co.uk/german-bundesliga/fixtures-results/october")
_NED=("Eredivisie 2026-27: calendario y resultados de octubre (jornada 10)","Football Web Pages","https://www.footballwebpages.co.uk/dutch-eredivisie/fixtures-results/october")
_FRA=("Ligue 1: programación de la jornada 8","Ligue 1 (LFP)","https://ligue1.com/en/articles/l1_article_5797-programmations-tv-j6-j7-et-j8-l1-2627")
_MEX=("Liga MX: los partidos del domingo 25 de octubre (jornada 14 del Apertura 2026)","sport-flash","https://www.sport-flash.com/sports/football/mx/calendar/2026-10-25/liga-mx-apertura-2026")
_USA=("MLS 2026: calendario del domingo 25 de octubre","VAVEL","https://www.vavel.com/en-us/data/mls/fixtures/")
_ECU=("LigaPro: horarios de la fecha 4 de la fase final","Primicias","https://www.primicias.ec/deportes/donde-ver-fecha/teleamazonas-fechas-partidos-horarios-fecha4-hexagonal-cuadrangular-ver-tv-135546/")
_LIGA={'ENG':_FT,'ITA':_FT,'COL':_FT,'ARG':_FT,'ESP':_ESP,'GER':_GER,'NED':_NED,'FRA':_FRA,'MEX':_MEX,'USA':_USA,'ECU':_ECU}
LINK={f"{p['local']}|{p['visita']}":_LIGA[p['liga']] for p in _P if not p.get('sin')}
LINK.update({
 'Hoffenheim|Bayer Leverkusen':("Hoffenheim vs Bayer Leverkusen: forma, tabla e historial de la jornada 7","On Tour Football","https://ontourfootball.com/fixtures/1899-hoffenheim-vs-bayer-leverkusen-2026-10-25"),
 'Barcelona|Real Madrid':("Confirman la hora y dónde ver el Clásico Barcelona-Real Madrid","Excélsior","https://www.excelsior.com.mx/deportes/confirman-hora-y-donde-ver-clasico-barcelona-real-madrid"),
 'Sparta Rotterdam|Ajax':("Sparta Rotterdam vs Ajax: ficha del partido de la jornada 10","Fútbol Total","https://futboltotal.futbol/partido/sparta-rotterdam-vs-ajax-eredivisie-2026-10-25"),
 'Aucas|Barcelona SC':("Duelo de necesitados: Aucas recibe a Barcelona SC en la fecha 4 del hexagonal por el título","El Universo","https://www.eluniverso.com/deportes/campeonato-ecuatoriano/duelo-de-necesitados-aucas-recibe-a-barcelona-sc-en-la-fecha-4-del-hexagonal-por-el-titulo-de-la-liga-pro-nota/"),
})
PRED=[f"{p['local']}|{p['visita']}" for p in sorted(_P,key=lambda p:-p['over15']) if not p.get('sin') and round(p['over15'],1)>=79.5]
DEST=['Barcelona|Real Madrid','Aucas|Barcelona SC','Crystal Palace|Newcastle United','Independiente|Boca Juniors']
COL.update({'Fortuna Sittard':'#f6d11b','Excelsior':'#d0021b','Inter':'#0b3d91','Fiorentina':'#5b2a86','Athletic Club':'#d0021b','Getafe':'#1d4fa0',
 'PSV':'#d0021b','Feyenoord':'#c8102e','NEC':'#c8102e','FC Groningen':'#00843d','Liverpool':'#c8102e','Brighton & Hove Albion':'#0057b8',
 'Manchester United':'#da291c','AFC Bournemouth':'#b50e12','Hull City':'#f5a12d','Brentford':'#e30613','Newcastle United':'#1a1f3a',
 'Genoa':'#a6192e','Venezia':'#111111','Frosinone':'#f6d11b','Monaco':'#e30613','Lille':'#c8102e','Hoffenheim':'#1961b5','Bayer Leverkusen':'#e32221',
 'Celta Vigo':'#8ac3ee','Real Betis':'#00954c','Sparta Rotterdam':'#d0021b','Ajax':'#d2122e','Auxerre':'#ffffff','Le Mans':'#c8102e',
 'Toulouse':'#5b2a86','Troyes':'#1d4fa0','Rennes':'#d0021b','Angers':'#111111','Lorient':'#f58220','Marseille':'#2faee0','Le Havre':'#5aa0d6',
 'Sunderland':'#eb172b','Leeds United':'#ffffff','SC Freiburg':'#d0021b','Bayern Munich':'#dc052d','Leones del Norte':'#0b2a52','Libertad':'#f6d11b',
 'Lecce':'#f6d11b','Juventus':'#111111','Real Sociedad':'#0067b1','Aldosivi':'#00843d','Belgrano':'#6cc4ec','AZ':'#d0021b','FC Twente':'#e30613',
 'Fortaleza':'#c8102e','Deportivo Cali':'#00843d','Emelec':'#1d4fa0','Guayaquil City':'#6cc4ec','Udinese':'#111111','Barcelona':'#a50044',
 'Real Madrid':'#f4f4f4','Independiente':'#d0021b','Boca Juniors':'#0b3d91','Alianza (ex Alianza Petrolera)':'#f6d11b',
 'Internacional de Bogotá (ex La Equidad)':'#c8102e','Aucas':'#d0021b','Barcelona SC':'#f7c600','River Plate':'#ffffff','Racing Club':'#6cc4ec',
 'Atlas':'#c8102e','Puebla':'#1d4fa0','Atlético Nacional':'#00843d','Independiente Medellín':'#c8102e','Central Cordoba SdE':'#111111',
 'Velez Sarsfield':'#1d4fa0','Barracas Central':'#d0021b','Estudiantes Rio Cuarto':'#ffffff','America':'#f6d11b','Pachuca':'#1c3e72',
 'Queretaro':'#1d4fa0','Cruz Azul':'#1d5fb8','Los Angeles FC':'#111111','LA Galaxy':'#00245d','Tijuana':'#c8102e','Santos Laguna':'#00704a'})
# Aciertos de ayer (sábado 24): (partido, marcador real, nuestro Over 1.5, medio, url)
ACIERTOS=[
 ("Augsburg vs Union Berlin","1-1","93,2 % · partido del día","colombia.com","https://www.colombia.com/futbol/alemania/bundesliga/resultados"),
 ("Portland vs Charlotte","3-2","90,6 %","Fútbol Total","https://futboltotal.futbol/partido/portland-timbers-vs-charlotte-mls-2026-10-25"),
 ("Mainz vs Werder Bremen","2-3","88,7 %","colombia.com","https://www.colombia.com/futbol/alemania/bundesliga/resultados"),
 ("ADO Den Haag vs Heerenveen","2-3","88,5 %","Sporza","https://sporza.be/nl/sport/voetbal/~3338922/"),
 ("RB Leipzig vs Elversberg","4-0","87,4 %","colombia.com","https://www.colombia.com/futbol/alemania/bundesliga/resultados"),
 ("Willem II vs Cambuur","1-6","81,0 %","Sporza","https://sporza.be/nl/sport/voetbal/~3338861/"),
 ("Napoli vs Roma","3-3","66,9 %","Fútbol Total","https://futboltotal.futbol/partido/napoli-vs-as-roma-serie-a-2026-10-24"),
 ("Orense vs Delfín","4-0","69,7 %","El Universo","https://www.eluniverso.com/deportes/campeonato-ecuatoriano/orense-golea-4-0-a-delfin-y-lo-supera-en-la-tabla-de-descenso-de-la-liga-ecuabet-2026-nota/"),
]
LLEGAN={
 'Hoffenheim|Bayer Leverkusen':["Bayer Leverkusen ganó sus últimos 5 partidos (2-0 en Grecia ante OFI el jueves, 2-1 a Friburgo el domingo 18) y es 4.º con 13 puntos.",
   "Leverkusen fuera de casa: 8 goles a favor y 8 en contra en 3 partidos (5,3 goles por partido en sus visitas).",
   "Hoffenheim en casa: 6 a favor y 7 en contra en 3 partidos; viene de golear 3-0 a Lyon el jueves.",
   "Fuentes: tabla de la Bundesliga 2026-27 (Sports Mole y Football Web Pages, partido a partido) y On Tour Football."],
 'Sparta Rotterdam|Ajax':["Ajax fuera de casa: 16 goles a favor y solo 3 en contra en 4 partidos.",
   "Sparta en casa recibe 2,4 goles por partido (12 en 5).",
   "Fuentes: tabla de la Eredivisie 2026-27 (Sports Mole y Football Web Pages, partido a partido) y ficha de Fútbol Total."],
 'Barcelona|Real Madrid':["Barcelona en casa: 17 goles a favor y 4 en contra en 4 partidos de LaLiga.",
   "Real Madrid fuera: 6 a favor y 6 en contra en 4 partidos.",
   "Primer Clásico de la temporada 2026-27, jornada 10, en el Spotify Camp Nou.",
   "Fuentes: tabla de LaLiga 2026-27 (Football Web Pages, partido a partido) y Excélsior."],
}
