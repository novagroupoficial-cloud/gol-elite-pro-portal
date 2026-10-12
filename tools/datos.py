# Tablas casa/fuera (12-oct-2026, antes de los partidos del lunes): equipo: (PJ, GF, GC)
# ENG: resultados partido a partido (sportsmole.co.uk + footballwebpages.co.uk), cotejado con futboltotal.futbol. Incluye el 11-oct.
# ESP: futboltotal.futbol/league/la-liga/clasificacion (act. 11-oct-2026), cotejado partido a partido (sportsmole, betexplorer).
# BRA: meutimao.com.br mandantes/visitantes (act. 11-oct-2026 07:58; incluye el sábado 10, no el domingo 11).
# ARG: soccerstats.com latest.asp?league=argentina2 (Clausura 2026, hasta el domingo 11).
L={}
L['ENG']=dict(casa={
'Arsenal':(3,7,2),'Aston Villa':(3,3,5),'Bournemouth':(3,3,4),'Brentford':(3,7,1),'Brighton':(3,8,1),
'Chelsea':(3,11,6),'Coventry':(2,0,6),'Crystal Palace':(3,6,8),'Everton':(3,5,2),'Fulham':(3,5,7),
'Hull City':(3,4,2),'Ipswich Town':(3,4,4),'Leeds United':(3,5,2),'Liverpool':(3,2,5),'Manchester City':(3,8,4),
'Manchester United':(3,6,4),'Newcastle':(3,6,5),'Nottingham Forest':(3,0,2),'Tottenham':(3,2,5),'Sunderland':(3,1,4)},
fuera={
'Arsenal':(3,3,3),'Aston Villa':(3,3,6),'Bournemouth':(3,4,9),'Brentford':(3,5,5),'Brighton':(3,10,4),
'Chelsea':(3,4,7),'Coventry':(3,1,4),'Crystal Palace':(3,3,4),'Everton':(3,3,3),'Fulham':(3,1,3),
'Hull City':(3,4,4),'Ipswich Town':(3,5,8),'Leeds United':(3,3,3),'Liverpool':(3,5,2),'Manchester City':(3,8,1),
'Manchester United':(3,3,5),'Newcastle':(2,3,4),'Nottingham Forest':(3,5,6),'Tottenham':(3,1,4),'Sunderland':(3,5,8)})
L['ESP']=dict(casa={
'Barcelona':(4,17,4),'Real Madrid':(4,13,2),'Real Betis':(4,8,2),'Atletico Madrid':(4,10,3),'Alaves':(5,10,5),
'Racing Santander':(4,9,7),'Getafe':(4,4,2),'Rayo Vallecano':(3,6,4),'Real Sociedad':(4,5,6),'Sevilla':(4,5,7),
'Athletic Club':(4,5,4),'Deportivo La Coruna':(4,5,4),'Osasuna':(4,2,3),'Celta Vigo':(4,7,5),'Espanyol':(4,6,6),
'Levante':(2,7,6),'Villarreal':(3,6,6),'Malaga':(4,3,5),'Elche':(4,4,11),'Valencia':(4,2,9)},
fuera={
'Barcelona':(4,17,3),'Atletico Madrid':(4,8,5),'Sevilla':(3,5,2),'Real Betis':(4,6,7),'Real Madrid':(4,6,6),
'Real Sociedad':(4,7,9),'Elche':(4,7,6),'Deportivo La Coruna':(4,7,7),'Villarreal':(5,7,7),'Espanyol':(4,5,5),
'Celta Vigo':(4,1,1),'Valencia':(4,4,6),'Athletic Club':(2,2,2),'Osasuna':(4,6,15),'Alaves':(3,2,3),
'Levante':(4,1,6),'Rayo Vallecano':(4,5,12),'Malaga':(4,1,8),'Getafe':(4,0,8),'Racing Santander':(4,4,16)})
L['BRA']=dict(
 casa={'Fluminense':(15,28,14),'Flamengo':(14,28,10),'Palmeiras':(14,24,9),'Athletico-PR':(15,27,13),
       'Vitória':(15,22,12),'São Paulo':(15,24,13),'Atletico MG':(14,24,16),'Cruzeiro':(15,26,16),
       'Grêmio':(14,22,16),'Vasco da Gama':(15,21,18),'Bahia':(14,22,14),'Santos':(15,22,20),
       'Mirassol':(15,21,21),'Bragantino':(14,20,15),'Botafogo':(15,25,22),'Coritiba':(14,19,19),
       'Corinthians':(15,15,16),'Internacional':(15,18,17),'Remo':(15,19,20),'Chapecoense':(13,18,29)},
 fuera={'Flamengo':(15,29,15),'Palmeiras':(15,24,12),'Bahia':(15,21,22),'Cruzeiro':(14,18,24),
        'Santos':(14,23,23),'Coritiba':(15,18,28),'Athletico-PR':(14,18,21),'Bragantino':(15,14,18),
        'Atletico MG':(15,15,18),'Fluminense':(14,20,22),'Botafogo':(14,17,25),'Corinthians':(14,15,18),
        'Internacional':(14,14,20),'Vasco da Gama':(14,15,24),'Mirassol':(14,13,22),'Remo':(15,14,28),
        'São Paulo':(15,11,22),'Chapecoense':(15,11,28),'Grêmio':(15,9,23),'Vitória':(15,11,32)})
L['ARG']=dict(
 casa={'Defensa y Justicia':(6,11,3),'Instituto':(6,11,5),'Velez Sarsfield':(6,9,5),'Estudiantes LP':(6,12,3),
  'Boca Juniors':(5,9,2),'Argentinos Juniors':(5,10,4),'Independiente Rivadavia':(5,12,7),'Newells Old Boys':(6,8,4),
  'Huracan':(6,5,2),'San Lorenzo':(6,4,4),'Rosario Central':(6,10,4),'Gimnasia Mendoza':(5,8,3),
  'Gimnasia La Plata':(6,10,7),'Sarmiento':(5,9,5),'River Plate':(7,9,7),'Belgrano':(6,8,6),'Lanus':(6,6,6),
  'Union Santa Fe':(6,11,10),'Deportivo Riestra':(6,7,6),'Tigre':(6,4,4),'Barracas Central':(6,4,4),'Aldosivi':(6,7,9),
  'Racing Club':(7,8,11),'Talleres':(7,5,10),'Banfield':(5,7,9),'Central Cordoba':(6,5,8),'Estudiantes Rio Cuarto':(6,2,5),
  'Independiente':(6,3,9),'Platense':(6,5,10),'Atletico Tucuman':(6,4,7)},
 fuera={'Independiente':(6,8,3),'Belgrano':(6,6,1),'Atletico Tucuman':(6,6,3),'Rosario Central':(6,7,5),
  'Barracas Central':(6,6,5),'Instituto':(6,8,5),'Sarmiento':(6,11,12),'Argentinos Juniors':(7,6,7),'Boca Juniors':(7,10,11),
  'Defensa y Justicia':(6,7,8),'Banfield':(7,7,9),'Gimnasia La Plata':(6,7,10),'Lanus':(5,7,3),'Velez Sarsfield':(5,8,6),
  'Platense':(6,7,8),'Huracan':(6,6,8),'River Plate':(4,5,5),'Gimnasia Mendoza':(6,6,9),'Newells Old Boys':(5,3,4),
  'Central Cordoba':(6,5,8),'Independiente Rivadavia':(7,3,12),'Tigre':(6,7,9),'Racing Club':(5,5,8),'Union Santa Fe':(6,6,11),
  'Talleres':(5,6,8),'Deportivo Riestra':(6,2,6),'San Lorenzo':(6,1,7),'Aldosivi':(6,6,11),'Estudiantes Rio Cuarto':(6,4,11),
  'Estudiantes LP':(6,3,10)})
# Verificación obligatoria y medias de liga (calculadas, no escritas a mano)
for _k,_d in L.items():
    c,f=_d['casa'],_d['fuera']
    pj=sum(v[0] for v in c.values()); gfc=sum(v[1] for v in c.values()); gcc=sum(v[2] for v in c.values())
    assert pj==sum(v[0] for v in f.values()), (_k,'PJ')
    assert gfc==sum(v[2] for v in f.values()), (_k,'GF casa != GC fuera')
    assert gcc==sum(v[1] for v in f.values()), (_k,'GC casa != GF fuera')
    _d['HG'],_d['AG'],_d['PJ']=gfc/pj,gcc/pj,pj

# ITA: soccerstats.com latest.asp?league=italy (Serie A 2026/27, 56 partidos, act. 12-oct; Atalanta casa 2-1,1-0,1-2; Venezia fuera 0-2,2-3)
L['ITA']=dict(casa={'Atalanta':(3,4,3)},fuera={'Venezia':(2,2,5)},HG=86/56,AG=75/56)
