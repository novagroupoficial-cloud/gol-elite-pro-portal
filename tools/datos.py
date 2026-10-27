# Tablas casa/fuera — miércoles 21-oct-2026 (bloque MAR20 con el martes 20 y Cincinnati-Columbus) · antes: martes 20-oct-2026 (bloque LUN19 con el lunes 19 y Monterrey-Pachuca) · antes: lunes 19-oct-2026 (antes de los partidos del día, incluye todo hasta el domingo 18-oct; bloque DOM18 al final): equipo: (PJ, GF, GC)
# Datos manuales (el Dashboard Gol 4.0 aún no expone /api/dia). Fuente de cada liga en su comentario.
L={}
# BRA: base tools/datos.py (valorfinal tabelas-por-recorte, tras 30ª rodada + Mirassol 2-0 Internacional 16/10) + 4 partidos del sábado 17/10 (31ª rodada): Botafogo 1-0 Chapecoense, Atletico MG 1-0 Coritiba, Athletico-PR 0-2 Palmeiras, São Paulo 1-0 Vasco da Gama. Fuentes: https://ptd.verdao.net/brasileirao-2026-resultados-de-sabado-pela-31a-rodada-classificacao-atualizada/ · https://www.supervasco.com/noticias/tabela-atualizada-da-serie-a-apos-os-jogos-deste-sabado-18-da-rodada-31-457982.html · https://365scores.com/pt-br/news/magazine/sao-paulo-vence-vasco-sobe-tabela-brasileirao · calendario https://valorfinal.com.br/brasileirao/2026/rodada-31 . Cotejada equipo por equipo (40/40 filas idénticas) con https://valorfinal.com.br/brasileirao/tabelas-por-recorte (lectura 18/10/2026 06:30). Corte: sábado 17/10/2026 incluido (pendientes 31ª: 4 de hoy + Corinthians–Vitória lun 19/10). 304 partidos · control: PJ 304=304, GF casa 465 = GC fuera 465, GC casa 342 = GF fuera 342
L['BRA']=dict(casa={'Flamengo':(15, 29, 10),'Palmeiras':(15, 28, 10),'Fluminense':(15, 28, 14),'Athletico-PR':(16, 27, 15),'Atletico MG':(16, 27, 17),'Vitória':(15, 22, 12),'São Paulo':(16, 25, 13),'Cruzeiro':(15, 26, 16),'Bahia':(15, 23, 14),'Grêmio':(15, 23, 17),'Mirassol':(16, 23, 21),'Bragantino':(15, 24, 17),'Vasco da Gama':(15, 21, 18),'Santos':(15, 22, 20),'Botafogo':(16, 26, 22),'Coritiba':(15, 20, 20),'Corinthians':(15, 15, 16),'Internacional':(15, 18, 17),'Remo':(15, 19, 20),'Chapecoense':(14, 19, 33)},
 fuera={'Flamengo':(15, 29, 15),'Palmeiras':(16, 26, 12),'Bahia':(15, 21, 22),'Athletico-PR':(15, 22, 22),'Cruzeiro':(15, 20, 28),'Santos':(15, 24, 25),'Coritiba':(16, 18, 29),'Bragantino':(15, 14, 18),'Atletico MG':(15, 15, 18),'Botafogo':(15, 18, 26),'Fluminense':(15, 20, 23),'Internacional':(16, 15, 23),'Corinthians':(15, 16, 22),'Vasco da Gama':(15, 15, 25),'Mirassol':(15, 13, 23),'Remo':(15, 14, 28),'São Paulo':(15, 11, 22),'Chapecoense':(16, 11, 29),'Grêmio':(15, 9, 23),'Vitória':(15, 11, 32)})
# ARG: base tools/datos.py (fechas 1-12 + Huracán 1-2 Gimnasia LP, jue 15/10 = 1er partido de la fecha 13; 181 partidos) + 7 partidos de la fecha 13 (los medios la llaman 'Fecha 13'): vie 16/10 Defensa y Justicia 0-1 Instituto, Boca 2-1 Talleres; sáb 17/10 Banfield 0-1 Argentinos, Platense 0-1 Lanús, Ind. Rivadavia 2-2 Tigre, Atl. Tucumán 2-3 Rosario Central, Vélez 1-0 Gimnasia Mendoza. Fuentes: https://unitel.bo/noticias/agencias/resultados-de-la-decimotercera-fecha-del-torneo-clausura-argentino-y-posiciones-AE24207502 (AFP) · https://www.noticiasdebariloche.com.ar/resultados-posiciones-y-como-sigue-la-fecha-13-del-torneo-clausura-central-gano-y-es-puntero-de-la-b-con-argentinos/ · https://442.perfil.com/noticias/futbol/boca-vs-talleres-por-el-torneo-clausura-2026.phtml · https://elgrafico.com.ar/articulo/1038/103382/la-cima-de-la-zona-a-en-juego-defensa-y-justicia-e-instituto-se-miden-en-varela . Corte: sábado 17/10/2026 incluido (pendientes fecha 13: 4 de hoy + 3 del lun 19/10). 188 partidos · control: PJ 188=188, GF casa 235 = GC fuera 235, GC casa 191 = GF fuera 191
L['ARG']=dict(casa={'Sarmiento':(6, 10, 6),'Belgrano':(6, 8, 6),'Defensa y Justicia':(7, 11, 4),'Gimnasia Mendoza':(6, 9, 3),'Racing Club':(7, 8, 11),'Velez Sarsfield':(7, 10, 5),'Huracan':(7, 6, 4),'Platense':(7, 5, 11),'Estudiantes Rio Cuarto':(6, 2, 5),'Newells Old Boys':(6, 8, 4),'River Plate':(7, 9, 7),'Lanus':(7, 8, 6),'Atletico Tucuman':(7, 6, 10),'Estudiantes LP':(6, 12, 3),'Deportivo Riestra':(6, 7, 6),'San Lorenzo':(6, 4, 4),'Banfield':(6, 7, 10),'Rosario Central':(6, 10, 4),'Argentinos Juniors':(5, 10, 4),'Barracas Central':(6, 4, 4),'Gimnasia LP':(6, 10, 7),'Instituto Cordoba':(6, 11, 5),'Talleres Cordoba':(7, 5, 10),'Independiente Rivadavia':(6, 14, 9),'Central Cordoba SdE':(6, 5, 8),'Independiente':(6, 3, 9),'Boca Juniors':(6, 11, 3),'Tigre':(6, 4, 4),'Union Santa Fe':(6, 11, 10),'Aldosivi':(6, 7, 9)},
 fuera={'Argentinos Juniors':(8, 7, 7),'Rosario Central':(7, 10, 7),'Aldosivi':(6, 6, 11),'Central Cordoba SdE':(6, 5, 8),'Gimnasia LP':(7, 9, 11),'Instituto Cordoba':(7, 9, 5),'Banfield':(7, 7, 9),'Union Santa Fe':(6, 6, 11),'Tigre':(7, 9, 11),'Talleres Cordoba':(6, 7, 10),'Barracas Central':(6, 6, 5),'San Lorenzo':(6, 1, 7),'Independiente Rivadavia':(7, 3, 12),'Independiente':(6, 8, 3),'Boca Juniors':(7, 10, 11),'Gimnasia Mendoza':(7, 6, 10),'Sarmiento':(6, 11, 12),'Racing Club':(5, 5, 8),'Estudiantes Rio Cuarto':(6, 4, 11),'Deportivo Riestra':(6, 2, 6),'River Plate':(5, 6, 6),'Platense':(6, 7, 8),'Velez Sarsfield':(6, 8, 8),'Huracan':(6, 6, 8),'Atletico Tucuman':(6, 6, 3),'Newells Old Boys':(6, 3, 5),'Estudiantes LP':(6, 3, 10),'Belgrano':(6, 6, 1),'Lanus':(6, 8, 3),'Defensa y Justicia':(6, 7, 8)})
# ENG: datos.py (J1-J6 hasta 12-oct-2026, 60 PJ) + 5 partidos de la J7 del sáb 17-oct (Everton 0-2 Chelsea, Brentford 1-2 Liverpool, Fulham 1-0 Hull City, Manchester City 3-2 Ipswich Town, Newcastle United 0-1 Aston Villa) según https://www.sportsmole.co.uk/football/premier-league/2026-27/ (resultados + Home/Away Table 2026-27, que coincide equipo por equipo con la suma) y futboltotal.futbol (data/2026-10-17/resultados-en-vivo.json); Tottenham–Coventry de la J7 es el lun 19-oct (https://www.footballwebpages.co.uk/premier-league/20261019, tabla actualizada sáb 17-oct 19:25 con 65 PJ) · corte: sáb 17-oct-2026 · 65 partidos · control: PJ 65=65, GF casa 102 = GC fuera 102, GC casa 87 = GF fuera 87
L['ENG']=dict(casa={'Coventry City':(3, 4, 7),'Liverpool':(3, 2, 5),'Crystal Palace':(3, 6, 8),'Hull City':(3, 4, 2),'Manchester United':(3, 6, 4),'Aston Villa':(3, 3, 5),'Chelsea':(3, 11, 6),'Ipswich Town':(3, 4, 4),'Sunderland':(3, 1, 4),'Arsenal':(3, 7, 2),'Fulham':(4, 6, 7),'AFC Bournemouth':(3, 3, 4),'Leeds United':(3, 5, 2),'Manchester City':(4, 11, 6),'Nottingham Forest':(3, 0, 2),'Brighton & Hove Albion':(3, 8, 1),'Everton':(4, 5, 4),'Newcastle United':(4, 6, 6),'Tottenham Hotspur':(3, 2, 5),'Brentford':(4, 8, 3)},
 fuera={'Newcastle United':(3, 4, 8),'Manchester City':(3, 8, 1),'Nottingham Forest':(3, 5, 6),'Everton':(3, 3, 3),'Tottenham Hotspur':(3, 1, 4),'Brentford':(3, 5, 5),'AFC Bournemouth':(3, 4, 9),'Fulham':(3, 1, 3),'Brighton & Hove Albion':(3, 10, 4),'Leeds United':(3, 3, 3),'Manchester United':(3, 3, 5),'Liverpool':(4, 7, 3),'Crystal Palace':(3, 3, 4),'Sunderland':(3, 5, 8),'Coventry City':(3, 1, 4),'Arsenal':(3, 3, 3),'Ipswich Town':(4, 7, 11),'Hull City':(4, 4, 5),'Aston Villa':(4, 4, 6),'Chelsea':(4, 6, 7)})
# GER: datos.py (46 PJ hasta vie 16-oct) + 6 partidos del sáb 17-oct, J6 (Bayern Munich 6-1 RB Leipzig, Union Berlin 0-0 Borussia Dortmund, Hamburger SV 1-0 VfB Stuttgart, Werder Bremen 2-2 SC Paderborn, Schalke 04 0-1 Mainz 05, Elversberg 4-3 Augsburg) según https://www.sportsmole.co.uk/football/bundesliga/2026-27/ (resultados + Home/Away Table 2026-27, que coincide equipo por equipo con la suma) y futboltotal.futbol (data/2026-10-17/resultados-en-vivo.json); restan de la J6 solo los 2 del dom 18-oct · corte: sáb 17-oct-2026 · 52 partidos · control: PJ 52=52, GF casa 120 = GC fuera 120, GC casa 73 = GF fuera 73
L['GER']=dict(casa={'Augsburg':(3, 7, 4),'Bayern Munich':(3, 18, 2),'Bayer Leverkusen':(2, 6, 0),'Borussia Dortmund':(3, 7, 2),'Borussia Monchengladbach':(2, 6, 8),'Eintracht Frankfurt':(3, 4, 6),'Elversberg':(3, 8, 7),'1. FC Koln':(3, 6, 4),'SC Freiburg':(3, 11, 2),'Hamburger SV':(3, 3, 6),'Hoffenheim':(3, 6, 7),'Mainz 05':(3, 4, 7),'RB Leipzig':(3, 14, 0),'SC Paderborn':(3, 3, 4),'Schalke 04':(3, 0, 1),'VfB Stuttgart':(2, 4, 2),'Union Berlin':(4, 5, 6),'Werder Bremen':(3, 8, 5)},
 fuera={'Augsburg':(3, 9, 8),'Bayern Munich':(3, 4, 3),'Bayer Leverkusen':(3, 8, 8),'Borussia Dortmund':(3, 4, 2),'Borussia Monchengladbach':(3, 1, 10),'Eintracht Frankfurt':(3, 6, 10),'Elversberg':(3, 4, 4),'1. FC Koln':(3, 2, 7),'SC Freiburg':(2, 3, 2),'Hamburger SV':(3, 3, 9),'Hoffenheim':(2, 3, 6),'Mainz 05':(3, 10, 3),'RB Leipzig':(3, 2, 11),'SC Paderborn':(3, 2, 5),'Schalke 04':(3, 4, 6),'VfB Stuttgart':(4, 4, 8),'Union Berlin':(2, 0, 11),'Werder Bremen':(3, 4, 7)})
# ESP: base tools/datos.py (79 partidos, J1-J8 + Deportivo 1-1 Levante 16-oct) + 4 partidos del sáb 17-oct (J9) verificados en https://www.footballwebpages.co.uk/spanish-la-liga/fixtures-results/october (temporada 2026-2027): Espanyol 0-1 Atletico Madrid, Real Betis 2-5 Barcelona (también https://futboltotal.futbol/partido/real-betis-vs-barcelona-laliga-1570413), Valencia 0-0 Athletic Club, Villarreal 0-0 Elche (también https://futboltotal.futbol/partido/villarreal-vs-elche-la-liga-2026-10-17 y https://www.footballwebpages.co.uk/match/2026-2027/spanish-la-liga/villarreal/elche/593533). Corte: sáb 17-oct-2026 final; no hay más partidos entre el corte y hoy (Getafe-Rayo es lun 19-oct) = 83 partidos · control: PJ 83=83, GF casa 140 = GC fuera 140, GC casa 111 = GF fuera 111
L['ESP']=dict(casa={'Alaves':(5, 10, 5),'Sevilla':(4, 5, 7),'Racing Santander':(4, 9, 7),'Espanyol':(5, 6, 7),'Deportivo La Coruna':(5, 6, 5),'Atletico Madrid':(4, 10, 3),'Valencia':(5, 2, 9),'Real Madrid':(4, 13, 2),'Celta Vigo':(4, 7, 5),'Barcelona':(4, 17, 4),'Rayo Vallecano':(3, 6, 4),'Real Betis':(5, 10, 7),'Athletic Club':(4, 5, 4),'Getafe':(4, 4, 2),'Elche':(4, 4, 11),'Osasuna':(4, 2, 3),'Malaga':(4, 3, 5),'Levante':(3, 10, 9),'Real Sociedad':(4, 5, 6),'Villarreal':(4, 6, 6)},
 fuera={'Getafe':(4, 0, 8),'Rayo Vallecano':(4, 5, 12),'Villarreal':(5, 7, 7),'Levante':(5, 2, 7),'Elche':(5, 7, 6),'Malaga':(4, 1, 8),'Real Betis':(4, 6, 7),'Real Sociedad':(4, 7, 9),'Osasuna':(4, 6, 15),'Athletic Club':(3, 2, 2),'Alaves':(3, 2, 3),'Sevilla':(4, 8, 5),'Celta Vigo':(4, 1, 1),'Real Madrid':(4, 6, 6),'Racing Santander':(4, 4, 16),'Barcelona':(5, 22, 5),'Deportivo La Coruna':(4, 7, 7),'Espanyol':(4, 5, 5),'Atletico Madrid':(5, 9, 5),'Valencia':(4, 4, 6)})
# ITA: base tools/datos.py (61 partidos, J1-J6 + Frosinone 4-2 Sassuolo 16-oct, de https://www.soccerstats.com/homeaway.asp?league=italy) + 3 partidos del sáb 17-oct (J7, temporada 2026/27): Venezia 1-0 Napoli (https://futboltotal.futbol/partido/venezia-vs-napoli-serie-a-1550156), Bologna 1-3 Inter (https://futboltotal.futbol/partido/bologna-vs-inter-serie-a-1550149), Roma 2-0 Genoa (https://futboltotal.futbol/partido/as-roma-vs-genoa-serie-a-1550148 y https://www.sportytrader.com/en/results-live/roma-genoa-8522160/); cotejados con la jornada 7 en https://www.fantacalcio.it/serie-a/calendario/7/2026-27/monza-cagliari/18020. Corte: sáb 17-oct-2026 final (excluye Udinese-Lecce en juego hoy; Monza-Cagliari y Parma-Torino son lun 19-oct) = 64 partidos · control: PJ 64=64, GF casa 101 = GC fuera 101, GC casa 84 = GF fuera 84
L['ITA']=dict(casa={'Inter':(4, 15, 6),'Frosinone':(4, 9, 5),'Atalanta':(4, 7, 4),'Roma':(4, 10, 3),'Juventus':(3, 5, 1),'Lazio':(3, 6, 3),'Sassuolo':(3, 6, 4),'AC Milan':(2, 5, 0),'Napoli':(3, 5, 2),'Como':(2, 2, 1),'Parma':(3, 3, 3),'Cagliari':(3, 2, 2),'Genoa':(4, 4, 8),'Monza':(2, 4, 4),'Torino':(3, 3, 5),'Lecce':(3, 4, 8),'Bologna':(4, 4, 7),'Udinese':(3, 2, 4),'Fiorentina':(3, 2, 6),'Venezia':(4, 3, 8)},
 fuera={'Lazio':(3, 5, 1),'Cagliari':(3, 4, 1),'Roma':(3, 6, 0),'Como':(4, 7, 5),'AC Milan':(4, 6, 5),'Napoli':(4, 5, 5),'Inter':(3, 6, 3),'Frosinone':(3, 4, 4),'Juventus':(3, 4, 4),'Torino':(3, 4, 4),'Bologna':(3, 2, 3),'Udinese':(3, 7, 9),'Lecce':(3, 2, 4),'Fiorentina':(3, 5, 8),'Sassuolo':(4, 6, 10),'Monza':(4, 5, 11),'Genoa':(3, 1, 5),'Atalanta':(2, 1, 4),'Venezia':(3, 3, 8),'Parma':(3, 1, 7)})
# FRA: base tools/datos.py (soccerstats homeaway.asp?league=france, 2026/27, J1-J6 + Le Mans-Toulouse vie 16-oct = 55 partidos) + 3 partidos sab 17-oct (J7) sumados a mano: Strasbourg 1-3 Paris Saint-Germain (https://futboltotal.futbol/partido/strasbourg-vs-paris-saint-germain-ligue-1-2026-10-17), Troyes 1-3 Lens (https://futboltotal.futbol/partido/estac-troyes-vs-lens-ligue-1-2026-10-17 ; https://news.footeo.com/2026/10/17/troyes-lens-1-3-victoire-convaincante-mais-trois-blesses-pour-lens-avant-la-ligue-des-champions-15023), Lille 1-1 Brest (https://futboltotal.futbol/partido/lille-vs-stade-brestois-29-ligue-1-2026-10-17 ; https://www.flashscore.fr/actualites/lille-arrache-le-nul-a-domicile-contre-brest-et-continue-de-stagner/v1tFxrZQ/); solo 3 partidos L1 el sab 17-oct (https://www.sport-flash.com/sports/football/it/calendar/2026-10-17/ligue-1-2026-2027). Corte: sab 17-oct-2026 fin de jornada (antes de Angers-Marseille dom 18-oct 08:00 ECU) = 58 partidos · control: PJ 58=58, GF casa 93 = GC fuera 93, GC casa 77 = GF fuera 77
L['FRA']=dict(casa={'Rennes':(4, 10, 5),'Nice':(4, 5, 3),'Lyon':(3, 8, 2),'Paris FC':(3, 5, 1),'Monaco':(3, 6, 3),'Lille':(4, 6, 3),'Lens':(3, 7, 4),'Auxerre':(3, 4, 4),'Le Mans':(4, 6, 8),'Brest':(3, 7, 4),'Strasbourg':(3, 4, 5),'Lorient':(3, 4, 4),'Marseille':(3, 7, 5),'Paris Saint-Germain':(2, 4, 3),'Angers':(3, 3, 4),'Toulouse':(3, 3, 5),'Le Havre':(3, 1, 3),'Troyes':(4, 3, 11)},
 fuera={'Paris Saint-Germain':(5, 10, 6),'Monaco':(3, 4, 2),'Toulouse':(4, 9, 6),'Lille':(3, 4, 2),'Lyon':(3, 3, 2),'Brest':(4, 6, 6),'Paris FC':(3, 3, 3),'Lorient':(3, 2, 2),'Angers':(3, 4, 6),'Marseille':(3, 2, 3),'Strasbourg':(4, 8, 10),'Rennes':(2, 2, 5),'Troyes':(3, 2, 5),'Lens':(4, 7, 7),'Le Havre':(3, 3, 5),'Le Mans':(3, 4, 7),'Nice':(2, 0, 4),'Auxerre':(3, 4, 12)})
# MEX: base L['MEX'] de tools/datos.py (https://www.soccerstats.com/homeaway.asp?league=mexico, hasta J11 + 3 partidos del vie 16-oct: Necaxa-Atlas, Xolos-Puebla, Atlante-Pumas; 100 partidos) + 5 partidos del sáb 17-oct (J12): Santos 5-0 Querétaro (https://amexi.com.mx/deportes/santos-laguna-golea-5-0-queretaro-apertura-2026/), Chivas 1-1 Tigres (https://www.vavel.com/en-us/soccer/2026/10/17/1275489-chivas-vs-tigres-live-updates-liga-mx.html), León 3-5 América (https://www.foxsports.com.mx/2026/10/17/leon-3-5-america-resumen-del-partido-y-goles-del-partido-de-la-jornada-12-apertura-2026-liga-mx/), Toluca 1-1 San Luis (https://vavel.com/mx/futbol-mexicano/2026/10/17/1275492-toluca-vs-san-luis-en-vivo-y-en-directo-liga-mx.html), Cruz Azul 5-0 Juárez (https://futboltotal.futbol/partido/cruz-azul-vs-fc-juarez-liga-mx-2026-10-18). Jornada 12 completa hasta el sábado (calendario: https://www.excelsior.com.mx/deportes/liga-mx-dias-horarios-y-canales-jornada-12-apertura-2026); falta solo Monterrey-Pachuca (dom 18). Corte: sáb 17-oct. 105 partidos · control: PJ 105=105, GF casa 168 = GC fuera 168, GC casa 147 = GF fuera 147
L['MEX']=dict(casa={'Leon':(6, 12, 9),'Tijuana':(7, 10, 6),'America':(5, 11, 3),'Tigres UANL':(5, 9, 5),'Monterrey':(5, 11, 6),'Cruz Azul':(7, 17, 12),'Toluca':(6, 16, 9),'Guadalajara':(6, 10, 7),'Queretaro':(5, 7, 6),'Santos Laguna':(6, 8, 3),'Puebla':(5, 6, 6),'Atlante':(6, 7, 9),'Pumas UNAM':(6, 9, 11),'Atlas':(6, 6, 9),'Necaxa':(7, 8, 14),'A. San Luis':(6, 7, 10),'Juarez':(6, 5, 11),'Pachuca':(5, 9, 11)},
 fuera={'Queretaro':(6, 8, 7),'Atlas':(6, 13, 9),'Toluca':(6, 10, 7),'Pachuca':(6, 9, 3),'Guadalajara':(6, 9, 5),'America':(6, 16, 11),'Puebla':(7, 6, 7),'Cruz Azul':(5, 10, 9),'Pumas UNAM':(6, 10, 9),'A. San Luis':(6, 9, 11),'Leon':(6, 6, 8),'Santos Laguna':(6, 9, 13),'Atlante':(6, 6, 10),'Monterrey':(5, 6, 9),'Tijuana':(4, 5, 8),'Necaxa':(5, 7, 11),'Tigres UANL':(7, 5, 11),'Juarez':(6, 3, 20)})
# USA: base L['USA'] de tools/datos.py (https://www.soccerstats.com/homeaway.asp?league=usa, 435 partidos hasta jue 15-oct) + 14 partidos del sáb 17-oct (sin partidos MLS el vie 16): Philadelphia 2-2 Charlotte (https://www.inquirer.com/soccer/philadelphia-union-charlotte-fc-score-bruno-damiani-20261017.html), Minnesota 3-2 St. Louis (https://lanacion.com.ar/deportes/canchallena/minnesota-united-fc-vencio-3-2-a-st-louis-city-sc-por-la-mls-nid17102026), y en https://futboltotal.futbol/2026-10-18 : Atlanta 1-3 Miami, NE 1-0 Chicago, NYRB 0-2 Toronto, Orlando 4-1 DC, NYCFC 1-1 LAFC (https://futboltotal.futbol/partido/new-york-city-fc-vs-los-angeles-fc-mls-2026-10-18), Austin 1-2 Vancouver, Houston 2-2 Dallas, SKC 1-3 RSL, LA Galaxy 2-2 San Diego, Portland 0-0 Colorado, SJ 1-1 Nashville, Seattle 1-1 Montreal. 28 de 30 equipos jugaron el sábado; falta Cincinnati-Columbus (dom 18). Corte: sáb 17-oct. 449 partidos · control: PJ 449=449, GF casa 827 = GC fuera 827, GC casa 633 = GF fuera 633
L['USA']=dict(casa={'Nashville SC':(15, 45, 12),'St. Louis City':(15, 34, 19),'Los Angeles FC':(15, 29, 13),'Colorado Rapids':(15, 28, 15),'Vancouver':(15, 35, 14),'New England':(15, 27, 16),'Charlotte':(15, 29, 16),'Chicago Fire':(15, 28, 19),'Real Salt Lake':(15, 28, 21),'Houston Dynamo':(15, 19, 14),'Orlando City':(15, 30, 20),'Dallas':(14, 26, 20),'Inter Miami':(15, 41, 26),'Philadelphia':(15, 27, 16),'Cincinnati':(13, 36, 27),'Portland':(15, 31, 25),'Seattle':(15, 24, 21),'Toronto':(16, 34, 32),'Columbus Crew':(15, 22, 17),'LA Galaxy':(16, 22, 20),'San Diego':(15, 35, 27),'SJ Earthquakes':(15, 26, 23),'DC United':(15, 20, 26),'Austin':(15, 21, 21),'New York RB':(15, 22, 29),'CF Montreal':(15, 19, 21),'New York City':(15, 27, 22),'Atlanta United':(15, 21, 29),'Minnesota United':(15, 19, 20),'Sporting KC':(15, 22, 32)},
 fuera={'Inter Miami':(15, 32, 25),'SJ Earthquakes':(15, 26, 19),'Dallas':(16, 29, 27),'Vancouver':(15, 28, 17),'Nashville SC':(15, 19, 11),'Philadelphia':(15, 34, 32),'St. Louis City':(15, 22, 22),'Chicago Fire':(15, 24, 25),'New England':(15, 22, 25),'Houston Dynamo':(15, 22, 25),'Charlotte':(15, 24, 29),'Minnesota United':(15, 28, 35),'New York RB':(15, 17, 27),'Seattle':(15, 15, 16),'New York City':(15, 16, 19),'Atlanta United':(15, 16, 22),'LA Galaxy':(15, 21, 32),'Los Angeles FC':(16, 19, 20),'DC United':(14, 17, 25),'Austin':(15, 17, 35),'Cincinnati':(15, 24, 41),'Orlando City':(15, 28, 50),'San Diego':(15, 18, 29),'Columbus Crew':(14, 22, 30),'Portland':(15, 20, 31),'Toronto':(14, 12, 23),'Sporting KC':(15, 14, 43),'Colorado Rapids':(15, 13, 26),'CF Montreal':(15, 17, 39),'Real Salt Lake':(15, 17, 27)})
# NED: base L['NED'] de tools/datos.py (https://www.sportsmole.co.uk/football/eredivisie/2026-27/, 73 partidos hasta vie 16-oct incl. Heerenveen-Excelsior) + 3 partidos del sáb 17-oct (programa: https://www.fcupdate.nl/voetbalcompetities/nederland/eredivisie/programma-uitslagen): ADO Den Haag 2-1 PSV (https://sporza.be/nl/sport/voetbal/~3338868/), Telstar 3-4 Feyenoord (https://www.voetbalzone.nl/nieuws/feyenoord-wint-knotsgekke-zevenklapper-op-bezoek-bij-telstar/blt50d85c1c2cc47b9a), Sparta 3-2 Willem II (https://voetbalprimeur.nl/nieuws/2148090/sparta-doet-goede-zaken-en-verslaat-willem-ii.html). Corte: sáb 17-oct. 76 partidos · control: PJ 76=76, GF casa 135 = GC fuera 135, GC casa 153 = GF fuera 153
L['NED']=dict(casa={'FC Twente':(4, 9, 3),'PSV':(4, 13, 4),'AZ':(4, 9, 3),'Feyenoord':(4, 11, 4),'Go Ahead Eagles':(4, 11, 6),'FC Groningen':(4, 9, 6),'Heerenveen':(5, 7, 5),'Ajax':(5, 11, 9),'Fortuna Sittard':(4, 5, 9),'FC Utrecht':(4, 8, 14),'Excelsior':(4, 5, 10),'Cambuur':(4, 6, 13),'NEC':(4, 5, 8),'Sparta Rotterdam':(5, 8, 12),'Telstar':(5, 8, 15),'ADO Den Haag':(4, 6, 9),'Willem II':(4, 3, 10),'PEC Zwolle':(4, 1, 13)},
 fuera={'FC Twente':(4, 7, 5),'PSV':(5, 14, 8),'AZ':(4, 9, 5),'Feyenoord':(5, 20, 6),'Go Ahead Eagles':(4, 8, 11),'FC Groningen':(4, 11, 8),'Heerenveen':(4, 8, 6),'Ajax':(3, 11, 1),'Fortuna Sittard':(4, 9, 6),'FC Utrecht':(4, 6, 11),'Excelsior':(5, 11, 8),'Cambuur':(4, 5, 6),'NEC':(4, 8, 6),'Sparta Rotterdam':(4, 8, 10),'Telstar':(4, 2, 3),'ADO Den Haag':(5, 5, 11),'Willem II':(5, 6, 16),'PEC Zwolle':(4, 5, 8)})
# PER: base = tools/datos.py L['PER'] (101 partidos, corte vie 16-oct: soccerstats https://www.soccerstats.com/latest.asp?league=peru2 hasta 12-oct + Sport Huancayo 2-1 Cusco FC y Los Chankas 2-1 ADT del 16-oct) + 3 partidos del sáb 17-oct (fecha 12 Clausura) sumados a mano: Juan Pablo II 2-0 Sport Boys, Melgar 4-2 Deportivo Garcilaso, Alianza Lima 3-1 Atlético Grau (fuentes: https://depor.com/futbol-peruano/descentralizado/acumulado-liga-1-2026-peru-en-vivo-tabla-de-posiciones-en-directo-resultados-de-fecha-12-torneo-clausura-alianza-lima-universitario-sporting-cristal-noticia/ ; https://rpp.pe/futbol/descentralizado/alianza-lima-vs-atletico-grau-en-vivo-l1max-como-ver-desde-tu-celular-fecha-12-torneo-clausura-2026-partidos-de-hoy-noticia-1712979 ; https://www.infobae.com/peru/deportes/2026/10/17/juan-pablo-ii-vencio-2-0-a-sport-boys-en-chongoyape-goles-y-resumen-del-triunfo-papal-por-torneo-clausura-2026/ ; https://www.infobae.com/peru/deportes/2026/10/18/melgar-hace-respetar-arequipa-y-sigue-luchando-en-liga-1-2026-remonto-a-deportivo-garcilaso-para-vencerlo-4-2-por-el-torneo-clausura/). Corte: sáb 17-oct-2026 incluido = fechas 1-11 completas + 5/9 de la fecha 12; 104 partidos (faltan los 4 de hoy dom 18-oct). · control: PJ 104=104, GF casa 180 = GC fuera 180, GC casa 128 = GF fuera 128
L['PER']=dict(casa={'Sporting Cristal':(5, 15, 2),'Deportivo Garcilaso':(6, 16, 5),'Alianza Atlético':(5, 12, 5),'Sport Boys':(6, 11, 5),'Atlético Grau':(6, 8, 3),'Cusco FC':(6, 13, 5),'Alianza Lima':(7, 12, 6),'Juan Pablo II':(6, 14, 2),'Sport Huancayo':(6, 10, 7),'Universitario':(5, 10, 6),'Melgar':(6, 13, 9),'Los Chankas':(6, 10, 12),'Comerciantes Unidos':(5, 8, 8),'Cienciano':(5, 5, 6),'ADT':(6, 5, 8),'CD Moquegua':(6, 5, 11),'UTC':(6, 5, 11),'FC Cajamarca':(6, 8, 17)},
 fuera={'Sport Huancayo':(6, 9, 7),'Universitario':(6, 11, 12),'Melgar':(6, 9, 4),'FC Cajamarca':(5, 10, 7),'Juan Pablo II':(6, 9, 11),'Alianza Lima':(5, 7, 6),'Deportivo Garcilaso':(6, 4, 6),'Alianza Atlético':(6, 11, 13),'Sporting Cristal':(6, 6, 8),'Cienciano':(6, 9, 12),'Cusco FC':(6, 8, 13),'Comerciantes Unidos':(6, 10, 11),'Sport Boys':(6, 4, 7),'Atlético Grau':(6, 7, 13),'CD Moquegua':(5, 2, 8),'Los Chankas':(6, 3, 13),'ADT':(6, 3, 15),'UTC':(5, 6, 14)})
# COL: base = tools/datos.py L['COL'] (128 partidos; soccerstats https://www.soccerstats.com/homeaway.asp?league=colombia2 re-consultada 18-oct-2026: muestra Clausura 2026, 128/190 y cifras idénticas a la base; último resultado 14-oct Junior 1-1 Pereira y Bucaramanga 1-1 Águilas; Millonarios-Once Caldas 14-oct y Santa Fe-Jaguares 15-oct aplazados; nada el vie 16-oct) + 3 partidos del sáb 17-oct sumados a mano: Boyacá Chicó 1-4 Atlético Nacional (https://www.eluniversal.com.co/deportes/2026/10/17/atletico-nacional-se-afianza-en-lo-alto-de-la-liga-betplay-tras-goleada-a-boyaca-chico/ ; https://www.futbolperuano.com/futbol-internacional/colombia/resultados), Millonarios 4-1 Jaguares (https://www.futbolred.com/futbol-colombiano/liga-betplay/millonarios-golea-4-1-a-jaguares-con-doblete-de-estupinan-en-el-nemesio-camacho-274074 ; https://www.winsports.co/futbol-colombiano/noticias/millonarios-arrasa-con-jaguares-en-un-duelo-dominado-resumen-471534), Independiente Medellín 0-2 Once Caldas (https://www.futbolred.com/futbol-colombiano/liga-betplay/independiente-medellin-0-2-once-caldas-el-blanco-blanco-asalto-el-atanasio-girardot-con-goles-de-zapata-y-barrios-274083 ; https://www.winsports.co/futbol-colombiano/noticias/once-caldas-sorprende-y-vence-2-0-a-independiente-medellin-resumen-471567). Programación fecha 15 (sáb 17 a mar 20-oct): https://www.vanguardia.com/deportes/futbol/2026/10/17/liga-betplay-2026-ii-programacion-de-la-fecha-15-con-bucaramanga-america-como-uno-de-los-partidos-destacados/ . Corte: sáb 17-oct-2026 incluido; 131/190 partidos. · control: PJ 131=131, GF casa 187 = GC fuera 187, GC casa 156 = GF fuera 156
L['COL']=dict(casa={'América de Cali':(7, 17, 5),'Deportivo Cali':(6, 13, 4),'Independiente Medellín':(8, 10, 10),'Santa Fe':(7, 10, 7),'Tolima':(7, 9, 7),'Cúcuta':(6, 11, 6),'Atlético Nacional':(5, 8, 3),'Bucaramanga':(6, 10, 6),'Boyacá Chicó':(7, 9, 8),'Águilas Doradas':(6, 10, 7),'Once Caldas':(6, 9, 7),'Llaneros':(6, 8, 7),'Internacional de Bogotá (ex La Equidad)':(7, 10, 11),'Jaguares de Córdoba':(7, 10, 12),'Millonarios':(6, 10, 3),'Junior':(7, 10, 9),'Fortaleza':(7, 8, 11),'Alianza (ex Alianza Petrolera)':(8, 9, 17),'Pasto':(6, 3, 7),'Deportivo Pereira':(6, 3, 9)},
 fuera={'Bucaramanga':(6, 11, 5),'Millonarios':(9, 13, 10),'Atlético Nacional':(7, 17, 8),'América de Cali':(6, 8, 4),'Deportivo Cali':(7, 7, 5),'Santa Fe':(5, 9, 5),'Independiente Medellín':(6, 11, 9),'Tolima':(7, 8, 9),'Once Caldas':(8, 9, 9),'Deportivo Pereira':(7, 5, 9),'Cúcuta':(7, 5, 13),'Águilas Doradas':(7, 7, 11),'Alianza (ex Alianza Petrolera)':(5, 5, 9),'Fortaleza':(6, 6, 8),'Llaneros':(7, 7, 10),'Internacional de Bogotá (ex La Equidad)':(7, 6, 9),'Pasto':(6, 6, 11),'Junior':(6, 9, 14),'Boyacá Chicó':(6, 2, 15),'Jaguares de Córdoba':(6, 5, 14)})
# ECU: base = tools/datos.py L['ECU'] = fase regular completa 240/240 (soccerstats https://www.soccerstats.com/homeaway.asp?league=ecuador re-consultada 18-oct-2026: sigue mostrando solo 240/240, cifras idénticas) + 19 partidos de la FASE FINAL (hexagonal título, cuadrangular Sudamericana, hexagonal descenso) sumados a mano, local primero. Fecha 1 (18-21 sep; Barcelona SC-IDV APLAZADO, sin nueva fecha https://www.elcomercio.com/deportes/futbol/barcelona-independiente-valle-reprogramado-ecuador-causas-partidos-fecha/): Aucas 1-2 Macará (Chillogallo; https://www.primicias.ec/deportes/ligapro/aucas/envivo-macara-fecha1-primer-hexagonal-resultado-ver-partido-tv-132838/), Guayaquil City 1-1 Leones del Norte, Emelec 1-2 Libertad (https://elcrackdeportes.com/2026/09/macara-libertad-emelec-tabla-posiciones-hexagonales-cuadrangular-ligapro ; https://www.primicias.ec/deportes/ligapro/emelec/envivo-libertadfc-fecha1-cuadrangular-resultado-ver-partido-tv-132862/), Técnico Universitario 1-1 Delfín (Ambato; https://kchcomunicacion.com/2026/09/20/rivales-directos-delfin-se-lleva-un-valioso-empate-ante-tecnico-universitario-en-el-bellavista/), Deportivo Cuenca 1-1 Mushuc Runa (https://elmercurio.com.ec/deportes/2026/09/20/deportivo-cuenca-empata-mushuc-runa-hexagonal-permanencia/), LDU Quito 2-1 Universidad Católica (Casa Blanca; https://kchcomunicacion.com/?p=544864), Manta 2-1 Orense (Jocay; https://www.primicias.ec/deportes/ligapro/manta/envivo-orense-fecha1-hexagonal-descenso-resultado-ver-partido-tv-132845/). Fecha 2 (9-11 oct; https://elcrackdeportes.com/2026/10/queda-tabla-posiciones-hexagonales-cuadrangular-ldu-barcelona-ligapro-idv ; https://www.ecuraices.com/deporte/liga-pro-fases-finales-resultados/ ; https://www.extra.ec/noticia/deportes/asi-queda-tabla-posiciones-ligapro-fecha-semana-164528.html): Libertad 3-0 Leones del Norte, Delfín 3-2 Mushuc Runa, Independiente del Valle 2-1 Aucas, Manta 1-0 Técnico Universitario, Guayaquil City 3-2 Emelec, Universidad Católica 0-1 Macará, Orense 0-0 Deportivo Cuenca, LDU Quito 2-1 Barcelona SC. Fecha 3 hasta sáb 17-oct (https://elcrackdeportes.com/2026/10/aucas-liga-quito-tabla-posiciones-hexagonales-cuadrangular-ligapro): Deportivo Cuenca 2-1 Técnico Universitario (vie 16; https://www.primicias.ec/deportes/ligapro/cuenca/envivo-tecnico-universitario-fecha3-hexagonal-descenso-resultado-ver-partido-tv-134903/), Libertad 4-0 Guayaquil City (https://www.metroecuador.com.ec/deportes/2026/10/17/libertad-goleo-4-0-a-guayaquil-city-y-acaricia-la-clasificacion-a-la-copa-sudamericana-2027/), Macará 1-0 Independiente del Valle (https://kchcomunicacion.com/2026/10/17/el-campeon-debera-esperar-macara-vencio-1-0-a-independiente-del-valle-en-ambato/), Aucas 1-1 LDU Quito (https://www.expreso.ec/deportes/aucas-vs-liga-quito-empate-1-1-superclasico-capitalino-ligapro-2026-299789.html). Verificación cruzada: PJ y DG acumulados de los 16 equipos tras F1+F2 coinciden con la tabla de Teleamazonas del 12-oct (https://www.teleamazonas.com/deportes/futbol/ligapro/ligapro-2026-hexagonales-cuadrangular-tabla-posiciones-130180/). Corte: sáb 17-oct-2026 incluido; 259 partidos (240 regular + 19 fase final). Pendientes: Barcelona-IDV (F1) y Mushuc Runa-Orense (lun 19-oct). · control: PJ 259=259, GF casa 341 = GC fuera 341, GC casa 251 = GF fuera 251
L['ECU']=dict(casa={'Independiente del Valle':(16, 38, 16),'Universidad Católica':(16, 37, 15),'Barcelona SC':(15, 22, 10),'Macará':(16, 24, 14),'Emelec':(16, 18, 15),'Libertad':(17, 27, 15),'Aucas':(17, 21, 19),'Guayaquil City':(17, 20, 16),'Mushuc Runa':(15, 16, 14),'Leones del Norte':(15, 18, 13),'LDU Quito':(17, 17, 13),'Orense':(16, 23, 22),'Delfín':(16, 13, 12),'Técnico Universitario':(16, 19, 22),'Deportivo Cuenca':(17, 18, 20),'Manta':(17, 10, 15)},
 fuera={'Independiente del Valle':(16, 37, 19),'Aucas':(16, 15, 14),'LDU Quito':(16, 19, 14),'Macará':(17, 21, 20),'Universidad Católica':(16, 15, 15),'Deportivo Cuenca':(16, 10, 19),'Leones del Norte':(17, 14, 23),'Guayaquil City':(16, 17, 27),'Mushuc Runa':(17, 22, 28),'Libertad':(16, 15, 20),'Barcelona SC':(16, 11, 17),'Técnico Universitario':(17, 11, 24),'Orense':(16, 14, 27),'Emelec':(16, 10, 24),'Manta':(15, 10, 28),'Delfín':(16, 10, 22)})

# ===== Actualización lun 19-oct-2026 (05:45 ECU): partidos del DOMINGO 18-oct sumados a mano (local en casa, visitante fuera), cada uno con su fuente.
# Resultados del refresco horario (data/2026-10-18/resultados-en-vivo.json) + Udinese 0-3 Lecce. Cobertura del domingo verificada por liga:
# ENG J7: 4 del domingo (Tottenham–Coventry es hoy) · ESP J9: 4 (Getafe–Rayo es hoy) · ITA J7: 4 incl. Udinese–Lecce (Monza–Cagliari y Parma–Torino son hoy)
# BRA 31ª: 4 (Corinthians–Vitória es hoy) · ARG fecha 13: 4 (Newell's–Central Córdoba, Sarmiento–Barracas y Riestra–Unión son hoy)
# COL fecha 15: 4 del domingo (programación https://www.vanguardia.com/deportes/futbol/2026/10/17/liga-betplay-2026-ii-programacion-de-la-fecha-15-con-bucaramanga-america-como-uno-de-los-partidos-destacados/; Pasto–Alianza hoy, 3 el martes)
# ECU fase final fecha 3: 3 del domingo (Mushuc Runa–Orense es hoy). Corte nuevo: dom 18-oct-2026 final.
DOM18=[
 ('ESP','Osasuna',2,0,'Racing Santander'),  # https://www.lanacion.com.ar/deportes/canchallena/osasuna-vencio-2-0-a-racing-de-santander-por-la-liga-de-espana-2026-nid18102026/
 ('ENG','AFC Bournemouth',2,0,'Sunderland'),  # https://futboltotal.futbol/partido/bournemouth-vs-sunderland-premier-league-2026-10-18
 ('ENG','Brighton & Hove Albion',5,0,'Crystal Palace'),  # https://futboltotal.futbol/partido/brighton-vs-crystal-palace-premier-league-2026-10-18
 ('ENG','Leeds United',1,1,'Manchester United'),  # https://futboltotal.futbol/partido/leeds-vs-manchester-united-premier-league-2026-10-18
 ('ITA','Fiorentina',1,3,'Como'),  # https://futboltotal.futbol/partido/fiorentina-vs-como-serie-a-2026-10-18
 ('ESP','Celta Vigo',2,1,'Alaves'),  # https://futboltotal.futbol/partido/celta-vigo-vs-alaves-la-liga-2026-10-18
 ('ENG','Nottingham Forest',0,1,'Arsenal'),  # https://futboltotal.futbol/partido/nottingham-forest-vs-arsenal-premier-league-2026-10-18
 ('ITA','AC Milan',3,2,'Atalanta'),  # https://futboltotal.futbol/partido/ac-milan-vs-atalanta-serie-a-1550147
 ('ESP','Malaga',2,5,'Real Sociedad'),  # https://futboltotal.futbol/partido/malaga-vs-real-sociedad-la-liga-2026-10-18
 ('ECU','Delfín',4,2,'Manta'),  # https://www.eldiario.ec/deportes/delfin-sc-vencio-4-2-a-manta-fc-en-el-clasico-mantense-y-toma-aire-en-el-hexagonal-por-la-permanencia-18102026
 ('ARG','Racing Club',1,1,'Independiente'),  # https://www.losandes.com.ar/deportes/racing-e-independiente-empataron-1-1-un-apasionante-clasico-avellaneda-n6010706
 ('ITA','Juventus',0,3,'Lazio'),  # https://www.vavel.com/en-us/soccer/2026/10/18/1275823-juventus-vs-lazio-live-score-serie-a-calcio.html
 ('ESP','Real Madrid',4,1,'Sevilla'),  # https://futboltotal.futbol/partido/real-madrid-vs-sevilla-la-liga-2026-10-18
 ('BRA','Fluminense',1,2,'Santos'),  # https://futboltotal.futbol/partido/fluminense-vs-santos-brasileirao-2026-10-18
 ('ECU','Leones del Norte',1,3,'Emelec'),  # https://www.fotmob.com/nl/matches/emelec-vs-leones-del-norte/c0m6mzqx
 ('BRA','Grêmio',2,4,'Cruzeiro'),  # https://futboltotal.futbol/partido/gremio-vs-cruzeiro-campeonato-brasileno-de-serie-a-2026-10-18
 ('COL','Águilas Doradas',2,1,'Tolima'),  # https://www.noticiascaracol.com/golcaracol/futbol-colombiano/asi-quedo-la-tabla-de-posiciones-de-la-liga-betplay-ii-2026-tras-aguilas-doradas-2-1-tolima-so35
 ('ARG','Estudiantes LP',1,2,'San Lorenzo'),  # https://futboltotal.futbol/partido/partido-estudiantes-lp-vs-san-lorenzo-liga-profesional-argentina-2026-10-18
 ('ARG','Estudiantes Rio Cuarto',2,1,'Aldosivi'),  # https://futboltotal.futbol/partido/partido-estudiantes-de-rio-cuarto-vs-aldosivi-liga-profesional-argentina-2026-10-18
 ('COL','Bucaramanga',1,1,'América de Cali'),  # https://www.vanguardia.com/deportes/futbol/2026/10/18/atletico-bucaramanga-y-america-de-cali-empataron-en-el-montanini-en-el-clasico-de-la-fecha-15-de-la-liga-betplay/
 ('BRA','Bahia',0,3,'Flamengo'),  # https://futboltotal.futbol/partido/partido-bahia-vs-flamengo-campeonato-brasileno-de-serie-a-2026-10-18
 ('ECU','Barcelona SC',1,1,'Universidad Católica'),  # https://studiofutbol.com.ec/2026/10/18/video-barcelona-sc-rescato-un-empate-en-un-final-de-infarto-ante-catolica/
 ('BRA','Remo',1,1,'Bragantino'),  # https://futboltotal.futbol/partido/remo-vs-rb-bragantino-campeonato-brasileno-de-serie-a-2026-10-18
 ('COL','Llaneros',1,0,'Santa Fe'),  # https://futboltotal.futbol/partido/llaneros-vs-santa-fe-primera-a-2026-10-18
 ('ARG','Belgrano',0,3,'River Plate'),  # https://futboltotal.futbol/partido/belgrano-cordoba-vs-river-plate-liga-profesional-argentina-2026-10-19
 ('COL','Deportivo Cali',0,0,'Junior'),  # https://futboltotal.futbol/partido/deportivo-cali-vs-junior-primera-a-2026-10-19
 ('ITA','Udinese',0,3,'Lecce'),  # https://futboltotal.futbol/partido/udinese-vs-lecce-serie-a-2026-10-18
]
for _lg,_a,_ga,_gb,_b in DOM18:
    _c=L[_lg]['casa'][_a]; L[_lg]['casa'][_a]=(_c[0]+1,_c[1]+_ga,_c[2]+_gb)
    _f=L[_lg]['fuera'][_b]; L[_lg]['fuera'][_b]=(_f[0]+1,_f[1]+_gb,_f[2]+_ga)

# ===== Actualización mar 20-oct-2026 (rutina diaria): partidos del LUNES 19-oct y Monterrey-Pachuca (dom 18, faltaba en MEX), local en casa, visitante fuera.
# Lunes 19: resultados del refresco horario (data/2026-10-19/resultados-en-vivo.json), cada uno con su fuente. Corte nuevo: lun 19-oct-2026 final.
LUN19=[
 ('MEX','Monterrey',2,1,'Pachuca'),  # https://futboltotal.futbol/partido/monterrey-vs-pachuca-liga-mx-2026-10-19 · https://livesoccer.planetsport.com/live/soccer/match-detail/mexico-liga-mx-apertura-monterrey-vs-cf-pachuca/2026-10-19/3291764/teamhistory (dom 18, 19:00 CDMX)
 ('ITA','Monza',4,0,'Cagliari'),  # https://sport.quotidiano.net/calcio/monza/monza-cagliari-4-0-i-brianzoli-calano-il-poker-contro-i-sardi-d048db81
 ('ITA','Parma',0,3,'Torino'),  # https://futboltotal.futbol/partido/parma-vs-torino-serie-a-2026-10-19
 ('ENG','Tottenham Hotspur',3,1,'Coventry City'),  # https://futboltotal.futbol/partido/tottenham-vs-coventry-premier-league-2026-10-19
 ('ESP','Getafe',1,1,'Rayo Vallecano'),  # https://futboltotal.futbol/partido/getafe-vs-rayo-vallecano-la-liga-2026-10-19
 ('ECU','Mushuc Runa',1,1,'Orense'),  # https://www.eldiario.ec/deportes/reparto-de-puntos-en-echaleche-mushuc-runa-igualo-con-orense-en-el-torneo-por-la-permanencia-en-la-a-19102026
 ('ARG','Newells Old Boys',2,1,'Central Cordoba SdE'),  # https://www.lanacion.com.ar/deportes/canchallena/newells-old-boys-vencio-por-2-1-a-central-cordoba-santiago-del-estero-por-el-torneo-clausura-2026-nid19102026/
 ('ARG','Sarmiento',1,1,'Barracas Central'),  # https://www.lanacion.com.ar/deportes/canchallena/sarmiento-y-barracas-central-empataron-1-1-por-el-torneo-clausura-2026-nid19102026/
 ('BRA','Corinthians',1,1,'Vitória'),  # https://www.cnnbrasil.com.br/esportes/brasileirao/corinthians-empata-com-vitoria-e-evita-nona-derrota-seguida-no-brasileirao/
 ('ARG','Deportivo Riestra',1,1,'Union Santa Fe'),  # https://futboltotal.futbol/partido/deportivo-riestra-vs-union-santa-fe-liga-profesional-argentina-2026-10-20
 ('COL','Pasto',0,1,'Alianza (ex Alianza Petrolera)'),  # https://futboltotal.futbol/partido/deportivo-pasto-vs-alianza-petrolera-primera-a-2026-10-20
]
for _lg,_a,_ga,_gb,_b in LUN19:
    _c=L[_lg]['casa'][_a]; L[_lg]['casa'][_a]=(_c[0]+1,_c[1]+_ga,_c[2]+_gb)
    _f=L[_lg]['fuera'][_b]; L[_lg]['fuera'][_b]=(_f[0]+1,_f[1]+_gb,_f[2]+_ga)

# ===== Actualización mié 21-oct-2026 (rutina diaria 05:2x ECU): partidos del MARTES 20-oct (resultados del refresco horario, data/2026-10-20/resultados-en-vivo.json, 8/8 terminados con fuente)
# + Cincinnati 0-2 Columbus Crew (MLS, dom 18-oct, faltaba en USA). Corte nuevo: mar 20-oct-2026 final. Local en casa, visitante fuera.
MAR20=[
 ('COL','Deportivo Pereira',2,0,'Boyacá Chicó'),  # https://eldeportivo.com.co/futbol-colombiano/liga-betplay/deportivo-pereira-toma-respiro-vencer-boyaca-chico/
 ('COL','Internacional de Bogotá (ex La Equidad)',2,1,'Fortaleza'),  # https://eldeportivo.com.co/futbol-colombiano/liga-betplay/internacional-impone-fortaleza-derbi-de-bogota/
 ('COL','Cúcuta',1,0,'Atlético Nacional'),  # https://www.vavel.com/colombia/futbol-colombiano/2026/10/20/1276182-cucuta-vs-nacional-en-vivo-liga-betplay.html
 ('COL','Millonarios',1,1,'Once Caldas'),  # https://futboltotal.futbol/partido/millonarios-vs-once-caldas-primera-a-2026-10-21
 ('MEX','Guadalajara',1,0,'Necaxa'),  # https://www.clarosports.com/futbol/liga-mx/chivas-vence-a-necaxa-con-un-autogol-y-escala-al-segundo-lugar-del-apertura-2026/
 ('MEX','A. San Luis',2,1,'Queretaro'),  # https://eltiempomx.com/noticia/2026/san-luis-vence-2-1-a-queretaro-en-el-clasico-de-la-57.html
 ('MEX','Juarez',0,1,'Atlante'),  # https://www.foxsports.com.mx/2026/10/20/juarez-vs-atlante-hoy-resumen-goles-y-resultado-0-1-de-liga-mx-en-la-jornada-13-apertura-2026/
 ('MEX','Tigres UANL',0,2,'Leon'),  # https://www.sdpnoticias.com/deportes/tigres-se-sigue-hundiendo-en-la-liga-mx-tras-perder-con-leon/
 ('USA','Cincinnati',0,2,'Columbus Crew'),  # https://futboltotal.futbol/partido/fc-cincinnati-vs-columbus-crew-mls-2026-10-19 (dom 18-oct, 17:00 Nueva York, jornada 30)
]
for _lg,_a,_ga,_gb,_b in MAR20:
    _c=L[_lg]['casa'][_a]; L[_lg]['casa'][_a]=(_c[0]+1,_c[1]+_ga,_c[2]+_gb)
    _f=L[_lg]['fuera'][_b]; L[_lg]['fuera'][_b]=(_f[0]+1,_f[1]+_gb,_f[2]+_ga)

# ===== Actualización vie 23-oct-2026 (rutina diaria recuperada por el refresco de las 16:1x ECU; la de 05:24 del 22 y del 23 no corrió): partidos del MIÉRCOLES 21-oct, local en casa, visitante fuera.
# MEX J13 (cierre de la fecha doble; no hubo Liga MX el jue 22): https://news.jointly.mx/tabla-general-jornada-13-apertura-2026-resultados-miercoles/ · Atlas 2-5 América también en https://heraldodemexico.com.mx/deportes/2026/10/22/america-goleo-atlas-2-5-en-la-jornada-13-de-la-liga-mx-913469.html · Pachuca 1-2 Cruz Azul también en https://heraldodemexico.com.mx/deportes/2026/10/22/cruz-azul-vencio-pachuca-1-2-en-la-jornada-13-de-la-liga-mx-913785.html y https://www.clarosports.com/futbol/liga-mx/la-maquina-pita-en-hidalgo-cruz-azul-vence-a-pachuca-y-asalta-el-tercer-lugar-de-la-tabla-general-del-apertura-2026/
# BRA: 31ª rodada completa (309 PJ; queda 1 partido atrasado sin fecha); la 32ª empieza hoy con Cruzeiro x Remo (https://valorfinal.com.br/brasileirao/2026/rodada-32). ARG: fecha 13 completa (195 PJ); la 14 empieza hoy.
# Partidos del mié 21 de ESP/USA/COL no se suman aquí (no hay pronósticos de esas ligas hoy); quedan para la rutina siguiente. Corte MEX: mié 21-oct final.
MIE21=[
 ('MEX','Atlas',2,5,'America'),
 ('MEX','Toluca',2,2,'Tijuana'),
 ('MEX','Puebla',1,4,'Monterrey'),
 ('MEX','Pachuca',1,2,'Cruz Azul'),
 ('MEX','Santos Laguna',2,0,'Pumas UNAM'),
]
for _lg,_a,_ga,_gb,_b in MIE21:
    _c=L[_lg]['casa'][_a]; L[_lg]['casa'][_a]=(_c[0]+1,_c[1]+_ga,_c[2]+_gb)
    _f=L[_lg]['fuera'][_b]; L[_lg]['fuera'][_b]=(_f[0]+1,_f[1]+_gb,_f[2]+_ga)

# ===== Actualización sáb 24-oct-2026 (rutina diaria 05:2x ECU): partidos pendientes del dom 18 (GER/FRA/NED), del mié 21 (ESP/USA/COL) y del vie 23 (todas), local en casa, visitante fuera.
# Fuentes por liga: GER, ESP, NED, POR -> footballwebpages.co.uk (temporada 2026-2027, fixtures-results/october); FRA -> https://www.vavel.com/en-us/data/ligue-1/results/ ; USA -> https://www.vavel.com/en-us/data/mls/results/ (451 partidos, cuadra con 450+1);
# viernes 23 de MEX/BRA/ARG -> data/2026-10-23/resultados-en-vivo.json (cada uno con fuente). Pendiente sin sumar: COL Santa Fe–Jaguares (mié 21, sin informe final hallado) e IDV–Católica (ECU, vie 23): no juegan hoy, solo afectan levemente las medias de liga.
SAB24=[
 ('MEX','Necaxa',1,1,'Juarez'),  # https://www.foxsports.com.mx/2026/10/23/resumen-video-goles-empate-necaxa-fc-juarez-eliminado-liguilla-liga-mx-hoy/
 ('MEX','Atlante',0,1,'A. San Luis'),  # https://www.sdpnoticias.com/deportes/san-luis-se-impone-al-atlante-y-mantiene-sus-posibilidades-de-clasificar-a-la-liguilla/
 ('BRA','Cruzeiro',1,0,'Remo'),  # https://www.diarioceleste.com.br/noticias-do-cruzeiro/cruzeiro-vence-o-remo-em-casa-e-assume-o-terceiro-lugar-do-brasileirao/
 ('ARG','Gimnasia Mendoza',1,2,'Platense'),  # https://www.diariouno.com.ar/ovacion/futbol/gimnasia-y-esgrima-no-pudo-aguantarlo-y-platense-se-lo-dio-vuelta-el-final-n1609628
 ('ARG','Tigre',0,1,'Atletico Tucuman'),  # https://www.ellitoral.com/deportes/tigre-atleticotucuman-futbol-afa-ligaprofesional_0_2fUwQBvy0w.html
 ('ARG','Gimnasia LP',2,0,'Sarmiento'),  # https://futboltotal.futbol/partido/gimnasia-lp-vs-sarmiento-junin-liga-profesional-argentina-2026-10-24
 ('ENG','Ipswich Town',1,1,'Nottingham Forest'),  # https://futboltotal.futbol/partido/ipswich-vs-nottingham-forest-premier-1557443
 ('GER','Bayer Leverkusen',2,1,'SC Freiburg'),  # dom 18 · https://www.footballwebpages.co.uk/german-bundesliga/fixtures-results/october
 ('GER','Borussia Monchengladbach',1,2,'Hoffenheim'),  # dom 18 · idem
 ('GER','VfB Stuttgart',2,3,'Borussia Monchengladbach'),  # vie 23 · idem
 ('ESP','Levante',3,1,'Athletic Club'),  # mié 21 · https://www.footballwebpages.co.uk/spanish-la-liga/fixtures-results
 ('ESP','Alaves',1,1,'Malaga'),  # vie 23 · idem
 ('ITA','Torino',3,2,'Monza'),  # vie 23 · https://futboltotal.futbol/partido/torino-vs-monza-serie-a-2026-10-23
 ('FRA','Lyon',2,1,'Nice'),  # dom 18 · https://www.vavel.com/en-us/data/ligue-1/results/
 ('FRA','Le Havre',1,3,'Auxerre'),  # dom 18 · idem
 ('FRA','Lorient',1,0,'Monaco'),  # dom 18 · idem
 ('FRA','Paris FC',4,3,'Rennes'),  # dom 18 · idem
 ('FRA','Angers',2,5,'Marseille'),  # dom 18 · idem
 ('FRA','Brest',1,2,'Nice'),  # vie 23 · https://futboltotal.futbol/partido/stade-brestois-29-vs-nice-ligue-1-2026-10-23
 ('NED','FC Groningen',2,5,'Ajax'),  # dom 18 · https://www.footballwebpages.co.uk/dutch-eredivisie/fixtures-results/october
 ('NED','FC Twente',1,2,'FC Utrecht'),  # dom 18 · idem
 ('NED','NEC',2,2,'Fortuna Sittard'),  # dom 18 · idem
 ('NED','PEC Zwolle',4,1,'Go Ahead Eagles'),  # dom 18 · idem
 ('NED','Cambuur',2,2,'AZ'),  # dom 18 · idem
 ('NED','Go Ahead Eagles',3,2,'Telstar'),  # vie 23 · idem
 ('USA','Cincinnati',2,1,'DC United'),  # mié 21 · https://futboltotal.futbol/partido/fc-cincinnati-vs-dc-united-mls-2026-10-22
 ('COL','Llaneros',0,3,'Deportivo Cali'),  # mié 21 · https://futboltotal.futbol/partido/llaneros-vs-deportivo-cali-primera-a-2026-10-22
]
for _lg,_a,_ga,_gb,_b in SAB24:
    _c=L[_lg]['casa'][_a]; L[_lg]['casa'][_a]=(_c[0]+1,_c[1]+_ga,_c[2]+_gb)
    _f=L[_lg]['fuera'][_b]; L[_lg]['fuera'][_b]=(_f[0]+1,_f[1]+_gb,_f[2]+_ga)

# ===== Actualización dom 25-oct-2026 (rutina diaria 05:4x ECU): partidos del SÁBADO 24-oct (data/2026-10-24/resultados-en-vivo.json, 55/57 terminados, cada uno con su fuente)
# + Boyacá Chicó 1-0 Bucaramanga y Junior 1-0 Águilas Doradas (COL, vie 23-oct, Semana). Local en casa, visitante fuera. Corte nuevo: sáb 24-oct-2026 final.
# Pendientes sin sumar (no juegan hoy; solo afectan levemente las medias): COL Santa Fe–Jaguares (mié 21), ECU IDV–Católica (vie 23), FRA posible partido PSG/Lyon del fin de semana.
SAB24F=[
 ('ENG','Aston Villa',2,1,'Manchester City'),  # https://futboltotal.futbol/partido/aston-villa-vs-manchester-city-premier-league-2026-10-24
 ('ESP','Rayo Vallecano',0,3,'Elche'),  # https://futboltotal.futbol/partido/rayo-vallecano-vs-elche-cf-laliga-1570429
 ('ITA','Como',2,0,'Sassuolo'),  # https://futboltotal.futbol/partido/como-vs-sassuolo-serie-a-2026-10-24
 ('ITA','Cagliari',0,2,'Bologna'),  # https://futboltotal.futbol/partido/cagliari-vs-bologna-serie-a-2026-10-24
 ('GER','Mainz 05',2,3,'Werder Bremen'),  # https://www.colombia.com/futbol/alemania/bundesliga/resultados
 ('GER','SC Paderborn',1,0,'Hamburger SV'),  # https://www.colombia.com/futbol/alemania/bundesliga/resultados
 ('GER','RB Leipzig',4,0,'Elversberg'),  # https://www.colombia.com/futbol/alemania/bundesliga/resultados
 ('GER','1. FC Koln',0,0,'Schalke 04'),  # https://www.colombia.com/futbol/alemania/bundesliga/resultados
 ('GER','Augsburg',1,1,'Union Berlin'),  # https://www.colombia.com/futbol/alemania/bundesliga/resultados
 ('ENG','Arsenal',2,0,'Everton'),  # https://futboltotal.futbol/partido/arsenal-vs-everton-premier-league-2026-10-24
 ('ENG','Coventry City',0,1,'Fulham'),  # https://futboltotal.futbol/partido/coventry-vs-fulham-premier-1557440
 ('ESP','Racing Santander',2,1,'Espanyol'),  # https://futboltotal.futbol/partido/racing-santander-vs-espanyol-laliga-1570428
 ('NED','FC Utrecht',1,1,'PEC Zwolle'),  # https://sporza.be/nl/sport/voetbal/~3338962/
 ('ITA','Napoli',3,3,'Roma'),  # https://futboltotal.futbol/partido/napoli-vs-as-roma-serie-a-2026-10-24
 ('ESP','Valencia',1,2,'Villarreal'),  # https://www.footballwebpages.co.uk/match/2026-2027/spanish-la-liga/valencia/villarreal/593788
 ('GER','Borussia Dortmund',1,0,'Eintracht Frankfurt'),  # https://futboltotal.futbol/partido/borussia-dortmund-vs-eintracht-frankfurt-bundesliga-2026-10-24
 ('ENG','Chelsea',0,2,'Tottenham Hotspur'),  # https://futboltotal.futbol/partido/chelsea-vs-tottenham-premier-1557439
 ('ITA','Lazio',2,1,'Parma'),  # https://futboltotal.futbol/partido/lazio-vs-parma-serie-a-2026-10-24
 ('USA','CF Montreal',0,2,'Nashville SC'),  # https://futboltotal.futbol/partido/cf-montreal-vs-nashville-sc-mls-2026-10-24
 ('NED','Willem II',1,6,'Cambuur'),  # https://sporza.be/nl/sport/voetbal/~3338861/
 ('ARG','Banfield',1,1,'Lanus'),  # https://www.cadena3.com/noticia/deportes/banfield-y-lanus-igualaron-en-un-intenso-clasico-del-sur-por-el-torneo-clausura_606780
 ('FRA','Lens',2,1,'Paris FC'),  # https://futboltotal.futbol/partido/lens-vs-paris-fc-ligue-1-2026-10-24
 ('ESP','Atletico Madrid',1,0,'Deportivo La Coruna'),  # https://futboltotal.futbol/partido/atletico-madrid-vs-deportivo-la-coruna-laliga-1570425
 ('NED','ADO Den Haag',2,3,'Heerenveen'),  # https://sporza.be/nl/sport/voetbal/~3338922/
 ('BRA','Mirassol',1,1,'São Paulo'),  # https://www.lance.com.br/futebol-nacional/mirassol-x-sao-paulo-como-foi-o-jogo-pelo-brasileirao-2026.html
 ('USA','Columbus Crew',4,2,'Toronto'),  # https://futboltotal.futbol/partido/columbus-crew-vs-toronto-fc-mls-2026-10-24
 ('ECU','Manta',0,2,'Deportivo Cuenca'),  # https://www.eluniverso.com/deportes/campeonato-ecuatoriano/deportivo-cuenca-vence-2-0-al-manta-fc-que-sigue-ultimo-en-el-hexagonal-por-la-permanencia-de-la-liga-ecuabet-2026-nota/
 ('ECU','Orense',4,0,'Delfín'),  # https://www.eluniverso.com/deportes/campeonato-ecuatoriano/orense-golea-4-0-a-delfin-y-lo-supera-en-la-tabla-de-descenso-de-la-liga-ecuabet-2026-nota/
 ('BRA','Internacional',3,0,'Botafogo'),  # https://www.terra.com.br/esportes/futebol/internacional-vence-o-botafogo-e-deixa-o-z4-do-brasileirao,4e8b044f12ff708025a0746fcaf42ec09kjalil8.html
 ('BRA','Vitória',1,1,'Athletico-PR'),  # https://aratuon.com.br/futebol/com-gols-no-primeiro-tempo-vitoria-e-athletico-pr-empatam-em-1-a-1-no-barradao/
 ('BRA','Palmeiras',2,0,'Bragantino'),  # https://futboltotal.futbol/partido/palmeiras-vs-rb-bragantino-brasileirao-2026-10-24
 ('BRA','Vasco da Gama',3,2,'Corinthians'),  # https://futboltotal.futbol/partido/vasco-da-gama-vs-corinthians-brasileirao-2026-10-24
 ('USA','New York RB',2,0,'Inter Miami'),  # https://futboltotal.futbol/partido/new-york-red-bulls-vs-inter-miami-mls-2026-10-24
 ('ARG','Talleres Cordoba',1,2,'Defensa y Justicia'),  # https://losandes.com.ar/deportes/defensa-y-justicia-vencio-talleres-cordoba-clasifico-los-playoffs-y-suena-la-sudamericana-2027-n6011594
 ('ECU','LDU Quito',1,2,'Macará'),  # https://www.extra.ec/noticia/deportes/asi-quedo-tabla-posiciones-ligapro-triunfo-macara-2-1-liga-quito-165915.html
 ('ARG','San Lorenzo',0,0,'Newells Old Boys'),  # https://www.mejorinformado.com/deportes/san-lorenzo-empato-newell-s-quedo-complicado-pelea-playoffs_1792850078
 ('BRA','Chapecoense',2,1,'Fluminense'),  # https://www.correiobraziliense.com.br/esportes/2026/10/7527223-fluminense-perde-para-a-chapecoense-e-segue-fora-do-g4.html
 ('USA','DC United',0,2,'Cincinnati'),  # https://futboltotal.futbol/partido/dc-united-vs-fc-cincinnati-major-league-soccer-2026-10-25
 ('USA','Atlanta United',2,3,'Chicago Fire'),  # https://futboltotal.futbol/partido/atlanta-united-fc-vs-chicago-fire-major-league-soccer-2026-10-25
 ('MEX','Leon',1,1,'Toluca'),  # https://www.vavel.com/mx/futbol-mexicano/2026/10/24/1276461-leon-vs-toluca-en-vivo-liga-mx.html
 ('COL','América de Cali',3,1,'Cúcuta'),  # https://www.elpais.com.co/deportes/america-de-cali-asumio-el-liderato-de-la-liga-betplay-tras-su-triunfo-en-el-pascual-guerrero-asi-quedo-la-tabla-de-posiciones-2431.html
 ('USA','Philadelphia',1,2,'New England'),  # https://www.bostonglobe.com/2026/10/24/sports/mls-revolution-philadelphia-union-score/
 ('USA','Sporting KC',1,2,'Austin'),  # https://kcsoccerjournal.com/10/24/2026/miscues-doom-sporting-kansas-city-in-loss-to-austin-fc/
 ('ARG','Rosario Central',2,0,'Huracan'),  # https://portalciudad.com.ar/rosario-central-vencio-2-0-a-huracan-por-el-torneo-clausura-2026-y-alcanzo-la-cima-de-la-tabla-anual/
 ('USA','Orlando City',2,2,'New York City'),  # https://themaneland.com/2026/10/24/orlando-city-vs-new-york-city-fc-final-score-2-2-as-lions-throw-away-two-points-on-games-last-kick/
 ('USA','Houston Dynamo',0,0,'Minnesota United'),  # https://fieldlevelmedia.com/mls/houston-pulls-out-scoreless-draw-vs-desperate-minnesota-united/
 ('USA','Dallas',3,0,'SJ Earthquakes'),  # https://www.sportytrader.com/en/results-live/fc-dallas-san-jose-earthquakes-7934591/
 ('MEX','Monterrey',0,1,'Guadalajara'),  # https://www.clarosports.com/futbol/liga-mx/monterrey-vs-chivas-en-vivo-el-partido-de-la-jornada-14-de-la-liga-mx-resultado-y-goles-hoy-apertura-2026/
 ('BRA','Santos',1,1,'Bahia'),  # https://placar.com.br/brasileirao/santos-empata-em-1-a-1-com-o-bahia-no-fim-pelo-brasileirao/
 ('USA','Real Salt Lake',3,0,'St. Louis City'),  # https://fieldlevelmedia.com/mls/real-salt-lake-pick-up-crucial-win-blank-st-louis-city/
 ('COL','Once Caldas',1,1,'Deportivo Pereira'),  # https://www.eldiario.com.co/deportes/once-caldas-y-deportivo-pereira-empataron-1-1-en-el-clasico-del-eje-cafetero/
 ('USA','Colorado Rapids',1,0,'Vancouver'),  # https://futboltotal.futbol/partido/colorado-rapids-vs-vancouver-whitecaps-mls-2026-10-25
 ('USA','San Diego',2,2,'Seattle'),  # https://futboltotal.futbol/partido/san-diego-vs-seattle-sounders-mls-2026-10-25
 ('USA','Portland',3,2,'Charlotte'),  # https://futboltotal.futbol/partido/portland-timbers-vs-charlotte-mls-2026-10-25
 ('MEX','Pumas UNAM',1,1,'Tigres UANL'),  # https://www.infobae.com/mexico/deportes/2026/10/25/pumas-empata-con-tigres-y-amarga-el-homenaje-a-hugo-sanchez-en-cu/
 ('COL','Boyacá Chicó',1,0,'Bucaramanga'),  # vie 23 · https://www.semana.com/deportes/articulo/la-tabla-de-la-liga-betplay-tras-derrota-del-bucaramanga-ante-el-chico-y-victoria-del-junior/202622/
 ('COL','Junior',1,0,'Águilas Doradas'),  # vie 23 · idem (Semana)
]
for _lg,_a,_ga,_gb,_b in SAB24F:
    _c=L[_lg]['casa'][_a]; L[_lg]['casa'][_a]=(_c[0]+1,_c[1]+_ga,_c[2]+_gb)
    _f=L[_lg]['fuera'][_b]; L[_lg]['fuera'][_b]=(_f[0]+1,_f[1]+_gb,_f[2]+_ga)

# ===== Actualización lun 26-oct-2026 (rutina diaria 05:2x ECU): partidos del DOMINGO 25-oct (data/2026-10-25/resultados-en-vivo.json, 44/44 terminados, cada uno con su fuente)
# + Santa Fe 2-1 Jaguares de Córdoba (COL, mié 21, pendiente; fotmob + futbol24). Local en casa, visitante fuera. Corte nuevo: dom 25-oct-2026 final.
# BRA: la 32ª rodada no tuvo partidos el domingo (8 jugados vie/sáb; Coritiba–Grêmio y Flamengo–Atlético MG son hoy).
DOM25=[
 ('NED','Fortuna Sittard',1,0,'Excelsior'),  # https://sporza.be/nl/sport/voetbal/~3338994/
 ('ITA','Inter',2,1,'Fiorentina'),  # https://futboltotal.futbol/partido/inter-vs-fiorentina-serie-a-2026-10-25
 ('ESP','Athletic Club',4,0,'Getafe'),  # https://futboltotal.futbol/partido/athletic-club-vs-getafe-la-liga-2026-10-25
 ('NED','PSV',1,1,'Feyenoord'),  # https://nltimes.nl/2026/10/25/game-title-candidates-psv-feyenoord-finishes-1-1-eindhoven
 ('NED','NEC',2,2,'FC Groningen'),  # https://sporza.be/nl/sport/voetbal/~3338893/
 ('ENG','Liverpool',2,0,'Brighton & Hove Albion'),  # https://futboltotal.futbol/partido/liverpool-vs-brighton-premier-league-2026-10-25
 ('ENG','Manchester United',0,3,'AFC Bournemouth'),  # https://futboltotal.futbol/partido/manchester-united-vs-bournemouth-premier-league-2026-10-25
 ('ENG','Hull City',1,1,'Brentford'),  # https://futboltotal.futbol/partido/hull-city-vs-brentford-premier-1557442
 ('ENG','Crystal Palace',0,2,'Newcastle United'),  # https://futboltotal.futbol/partido/crystal-palace-vs-newcastle-premier-league-2026-10-25
 ('ITA','Genoa',1,0,'Venezia'),  # https://futboltotal.futbol/partido/genoa-vs-venezia-serie-a-2026-10-25
 ('ITA','Atalanta',4,4,'Frosinone'),  # https://futboltotal.futbol/partido/atalanta-vs-frosinone-serie-a-2026-10-25
 ('FRA','Monaco',1,1,'Lille'),  # https://futboltotal.futbol/partido/monaco-vs-lille-ligue-1-2026-10-25
 ('GER','Hoffenheim',3,0,'Bayer Leverkusen'),  # https://futboltotal.futbol/partido/1899-hoffenheim-vs-bayer-leverkusen-bundesliga-2026-10-25
 ('ESP','Celta Vigo',0,0,'Real Betis'),  # https://futboltotal.futbol/partido/celta-vigo-vs-real-betis-laliga-1570427
 ('NED','Sparta Rotterdam',1,2,'Ajax'),  # https://sporza.be/nl/sport/voetbal/~3338935/
 ('FRA','Rennes',3,0,'Strasbourg'),  # https://futboltotal.futbol/partido/rennes-vs-strasbourg-ligue-1-2026-10-25
 ('FRA','Auxerre',1,1,'Le Mans'),  # https://futboltotal.futbol/partido/rennes-vs-strasbourg-ligue-1-2026-10-25
 ('GER','SC Freiburg',1,3,'Bayern Munich'),  # https://futboltotal.futbol/partido/sc-freiburg-vs-bayern-munchen-bundesliga-2026-10-25
 ('ENG','Sunderland',0,0,'Leeds United'),  # https://futboltotal.futbol/partido/sunderland-vs-leeds-premier-league-2026-10-25
 ('FRA','Toulouse',0,0,'Troyes'),  # https://futboltotal.futbol/partido/toulouse-vs-estac-troyes-ligue-1-2026-10-24
 ('FRA','Angers',0,0,'Lorient'),  # https://futboltotal.futbol/partido/angers-vs-lorient-ligue-1-2026-10-25
 ('FRA','Marseille',4,3,'Le Havre'),  # https://futboltotal.futbol/partido/marseille-vs-le-havre-ligue-1-2026-10-25
 ('ECU','Leones del Norte',4,1,'Libertad'),  # https://kchcomunicacion.com/2026/10/25/meten-presion-al-cuadrangular-leones-fc-goleo-a-libertad-en-el-olimpico-de-ibarra/
 ('ITA','Lecce',0,2,'Juventus'),  # https://futboltotal.futbol/partido/lecce-vs-juventus-serie-a-2026-10-25
 ('ESP','Real Sociedad',2,1,'Levante'),  # https://futboltotal.futbol/partido/real-sociedad-vs-levante-la-liga-2026-10-25
 ('ARG','Aldosivi',1,0,'Belgrano'),  # https://futboltotal.futbol/partido/partido-aldosivi-vs-belgrano-cordoba-liga-profesional-argentina-2026-10-25
 ('NED','AZ',0,2,'FC Twente'),  # https://www.fcupdate.nl/voetbalnieuws/2026/10/az-verliest-en-verspeelt-voor-derde-keer-op-rij-punten-in-de-eredivisie
 ('ECU','Emelec',0,1,'Guayaquil City'),  # https://studiofutbol.com.ec/2026/10/25/video-golpe-ciudadano-guayaquil-city-gano-al-emelec-en-el-capwell/
 ('COL','Fortaleza',1,1,'Deportivo Cali'),  # https://www.espn.com/soccer/match/_/gameId/401877906/deportivo-cali-fortaleza-ceif
 ('ITA','Udinese',0,2,'AC Milan'),  # https://futboltotal.futbol/partido/udinese-vs-ac-milan-serie-a-2026-10-25
 ('ESP','Barcelona',1,2,'Real Madrid'),  # https://libero.pe/futbol-internacional/liga-espanola/2026/10/25/partido-de-barcelona-vs-real-madrid-link-gratis-en-vivo-en-directo-online-mirar-clasico-espanol-1714125
 ('ARG','Independiente',0,1,'Boca Juniors'),  # https://www.ellitoral.com/deportes/boca-independiente-facundoherrera-torneoclausura2026_0_i8SmOAqXAg.html
 ('COL','Alianza (ex Alianza Petrolera)',1,0,'Internacional de Bogotá (ex La Equidad)'),  # https://www.espn.com/soccer/match/_/gameId/401878036/internacional-de-bogota-alianza-fc
 ('ECU','Aucas',0,4,'Barcelona SC'),  # https://www.extra.ec/noticia/deportes/barcelona-sc-bailo-aucas-quito-asi-golazos-duelo-ligapro-video-165975.html
 ('ARG','River Plate',1,0,'Racing Club'),  # https://futboltotal.futbol/partido/river-plate-vs-racing-club-liga-profesional-argentina-2026-10-25
 ('MEX','Atlas',4,3,'Puebla'),  # https://www.foxsports.com.mx/2026/10/25/atlas-vs-puebla-hoy-resumen-goles-en-video-y-resultado-4-3-jornada-14-liga-mx-apertura-2026/
 ('COL','Atlético Nacional',2,1,'Independiente Medellín'),  # https://futboltotal.futbol/partido/atletico-nacional-vs-independiente-medellin-primera-a-2026-10-26
 ('ARG','Central Cordoba SdE',0,5,'Velez Sarsfield'),  # https://www.dobleamarilla.com.ar/liga-/velez-aplasto-a-central-cordoba-en-santiago-del-estero-y-se-prende-en-la-lucha-por-la-tabla-anual_a6adeb3b394c8ca83be266779
 ('ARG','Barracas Central',2,1,'Estudiantes Rio Cuarto'),  # https://www.puntal.com.ar/estudiantes-rio-cuarto/estudiantes-no-pudo-aguantar-la-ventaja-y-perdio-visitante-frente-barracas-central-n267123
 ('COL','Tolima',0,1,'Pasto'),  # https://futboltotal.futbol/partido/deportes-tolima-vs-deportivo-pasto-primera-a-2026-10-25
 ('MEX','Queretaro',1,3,'Cruz Azul'),  # https://www.elimparcial.com/deporte/2026/10/25/cruz-azul-vence-a-queretaro-con-tres-goles-en-el-primer-tiempo-y-se-coloca-a-un-punto-del-america-en-la-pelea-por-el-liderato/
 ('USA','Los Angeles FC',2,2,'LA Galaxy'),  # https://www.foxsports.com/articles/soccer/leo-waltas-goal-erases-galaxys-lead-lafc-clinches-playoff-spot-in-22-el-trafico-draw
 ('MEX','America',1,2,'Pachuca'),  # https://www.mediotiempo.com/futbol/liga-mx/resumen-partido-america-vs-pachuca-jornada-14-apertura-2026
 ('MEX','Tijuana',4,1,'Santos Laguna'),  # https://www.foxsports.com.mx/2026/10/25/xolos-4-1-santos-resumen-del-partido-y-goles-de-la-jornada-14-del-apertura-2026-liga-mx/
 ('COL','Santa Fe',2,1,'Jaguares de Córdoba'),  # mié 21 (pendiente) · https://www.fotmob.com/match/3652834/matchfacts/santa-fe-vs-cd-jaguares · https://www.futbol24.com/match/2026/08/26/national/Colombia/Primera-A/2026/Finalizacion/Santa-Fe/vs/Jaguares-COL
]
for _lg,_a,_ga,_gb,_b in DOM25:
    _c=L[_lg]['casa'][_a]; L[_lg]['casa'][_a]=(_c[0]+1,_c[1]+_ga,_c[2]+_gb)
    _f=L[_lg]['fuera'][_b]; L[_lg]['fuera'][_b]=(_f[0]+1,_f[1]+_gb,_f[2]+_ga)

# ===== POR y CHI (lun 26-oct-2026, rutina diaria): ligas nuevas en datos.py, tablas casa/fuera de SoccerSTATS (página verificada: muestra la liga pedida y la temporada).
# POR: https://www.soccerstats.com/homeaway.asp?league=portugal — 'Portugal - Liga Portugal 2026/27', 76 partidos; Santa Clara y Benfica con 8 PJ (J1–J8 completas; se enfrentan hoy por la J9). Control GF casa=GC fuera=99, GC casa=GF fuera=108.
L['POR']=dict(casa={'FC Porto': (4, 9, 2), 'Sporting CP': (4, 10, 5), 'Benfica': (4, 9, 4), 'Arouca': (4, 8, 3), 'Guimaraes': (5, 7, 2), 'Santa Clara': (4, 7, 2), 'Gil Vicente': (5, 4, 3), 'Sporting Braga': (4, 4, 5), 'Academico Viseu': (4, 4, 6), 'Alverca': (5, 5, 6), 'Estrela Amadora': (5, 6, 9), 'Moreirense': (4, 5, 8), 'Maritimo': (4, 4, 7), 'Rio Ave': (4, 6, 11), 'Nacional': (4, 5, 10), 'Estoril': (4, 2, 5), 'Famalicao': (4, 3, 7), 'Casa Pia': (4, 1, 13)},
 fuera={'FC Porto': (5, 12, 2), 'Santa Clara': (4, 5, 2), 'Benfica': (4, 15, 3), 'Sporting CP': (4, 10, 4), 'Academico Viseu': (4, 7, 4), 'Arouca': (5, 4, 4), 'Casa Pia': (5, 4, 4), 'Gil Vicente': (4, 4, 4), 'Alverca': (4, 8, 7), 'Famalicao': (4, 7, 4), 'Estrela Amadora': (4, 8, 8), 'Sporting Braga': (4, 5, 5), 'Moreirense': (4, 3, 7), 'Maritimo': (5, 5, 12), 'Rio Ave': (4, 2, 6), 'Nacional': (4, 4, 8), 'Guimaraes': (4, 3, 8), 'Estoril': (4, 2, 7)})
# CHI: https://www.soccerstats.com/homeaway.asp?league=chile — 'Chile - Liga de Primera 2026', 196 partidos; U. de Chile y Everton con 24 PJ (fecha 25 en curso; se enfrentan hoy). Control GF casa=GC fuera=328, GC casa=GF fuera=239.
L['CHI']=dict(casa={'U. de Chile': (12, 27, 9), 'Colo-Colo': (12, 28, 10), 'Palestino': (13, 27, 14), 'D. Limache': (12, 25, 15), 'U. Catolica': (11, 29, 16), 'Audax Italiano': (13, 20, 14), 'Huachipato': (12, 23, 22), 'La Serena': (13, 22, 19), 'Everton': (13, 19, 16), 'Concepcion': (13, 17, 14), 'Cobresal': (12, 19, 17), 'Nublense': (13, 17, 17), 'Coquimbo Unido': (11, 18, 11), 'OHiggins': (12, 12, 15), 'U. Concepcion': (11, 8, 12), 'Union La Calera': (13, 17, 18)},
 fuera={'Colo-Colo': (13, 23, 18), 'U. Catolica': (13, 22, 20), 'Everton': (11, 21, 11), 'U. de Chile': (12, 14, 10), 'Nublense': (12, 13, 21), 'Coquimbo Unido': (13, 19, 24), 'La Serena': (12, 17, 23), 'Concepcion': (12, 10, 16), 'Palestino': (12, 12, 22), 'D. Limache': (12, 20, 22), 'OHiggins': (13, 17, 24), 'Huachipato': (12, 11, 18), 'Audax Italiano': (11, 7, 18), 'Cobresal': (13, 17, 29), 'U. Concepcion': (13, 10, 28), 'Union La Calera': (12, 6, 24)})

# ===== Actualización mar 27-oct-2026 (rutina diaria 05:2x ECU): partidos del LUNES 26-oct (data/2026-10-26/resultados-en-vivo.json, 10/10 terminados, cada uno con su fuente). Local en casa, visitante fuera. Corte nuevo: lun 26-oct-2026 final.
# ITA: J8 completa (80 PJ, 10 por jornada); hoy empieza la J9 (Sassuolo–Lazio, Roma–Cagliari, Torino–Como). ARG: fecha 14 con 14/15 jugados (falta Argentinos–Ind. Rivadavia, hoy). PER: sin actualizar desde el 17-oct (ver lista SIN de portal.py).
LUN26=[
 ('POR','Santa Clara',1,2,'Benfica'),  # https://executivedigest.sapo.pt/i-liga-benfica-da-a-volta-ao-resultado-e-vence-na-visita-ao-santa-clara/
 ('FRA','Paris Saint-Germain',2,0,'Lyon'),  # https://www.footmercato.net/live/7347100937878128418-paris-saint-germain-vs-lyon
 ('ESP','Sevilla',2,0,'Osasuna'),  # https://futboltotal.futbol/partido/sevilla-vs-osasuna-laliga-1570431
 ('CHI','U. de Chile',4,1,'Everton'),  # https://www.cooperativa.cl/noticias/deportes/futbol/liga-de-primera/la-u-goleo-a-everton-para-acortar-distancia-con-el-lider-y-llegar/2026-10-26/200238.html
 ('ARG','Union Santa Fe',3,1,'Estudiantes LP'),  # https://www.ellitoral.com/actualidad-tatengue/union-estudiantes-plata-victoria-tabla-posiciones-liga-profesional-fecha-14_0_tXCdklXTpN.html
 ('BRA','Coritiba',0,1,'Grêmio'),  # https://placar.com.br/brasileirao/gremio-vence-coritiba-por-1-a-0-nos-acrescimos-pelo-brasileirao/
 ('BRA','Flamengo',3,2,'Atletico MG'),  # https://www.metropoles.com/esportes/brasileirao-flamengo-vence-atletico-mg-e-retoma-a-lideranca-no-maracana
 ('COL','Jaguares de Córdoba',1,0,'Llaneros'),  # https://www.noticiascaracol.com/golcaracol/futbol-colombiano/asi-quedo-la-tabla-de-posiciones-de-liga-betplay-ii-2026-tras-jaguares-1-0-llaneros-so35
 ('ARG','Instituto Cordoba',1,0,'Deportivo Riestra'),  # https://portalciudad.com.ar/instituto-de-cordoba-vencio-1-0-a-deportivo-riestra-y-se-consolido-en-la-cima-de-la-zona-a-del-torneo-clausura-2026/
 ('COL','Santa Fe',2,1,'Bucaramanga'),  # https://www.elespectador.com/deportes/futbol-colombiano/santa-fe/santa-fe-vencio-2-1-a-bucaramanga/
]
for _lg,_a,_ga,_gb,_b in LUN26:
    _c=L[_lg]['casa'][_a]; L[_lg]['casa'][_a]=(_c[0]+1,_c[1]+_ga,_c[2]+_gb)
    _f=L[_lg]['fuera'][_b]; L[_lg]['fuera'][_b]=(_f[0]+1,_f[1]+_gb,_f[2]+_ga)

# Verificación obligatoria y medias de liga (calculadas, no escritas a mano)
for _k,_d in L.items():
    c,f=_d['casa'],_d['fuera']
    pj=sum(v[0] for v in c.values()); gfc=sum(v[1] for v in c.values()); gcc=sum(v[2] for v in c.values())
    assert pj==sum(v[0] for v in f.values()), (_k,'PJ')
    assert gfc==sum(v[2] for v in f.values()), (_k,'GF casa != GC fuera')
    assert gcc==sum(v[1] for v in f.values()), (_k,'GC casa != GF fuera')
    _d['HG'],_d['AG'],_d['PJ']=gfc/pj,gcc/pj,pj
