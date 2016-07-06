# Proyecto de análisis exploratorio de datos
Descripción: destinado a cuantificar e identificar la población estadounidense que publica contenido discriminatorio y que hablan de los candidatos presidenciales @realDonaldTrump o @HillaryClinton

En el siguiente proyecto se ha realizado lo siguiente:

> Recolectando la data
Usando el api de twitter recolectamos datos desde _______ hasta _______ con cuatro scripts diferentes:
- Usando el "follow" del api al id del usuario @RealDonaldTrump
- Usando el "follow" del api al id del usuario @HillaryClinton
- Usando el "track" de las palabras ['Hillary','Clinton','HillaryClinton','Hillary2016','ImWither']
- Usando el "track" de las palabras ['trump','Donald Trump','realDonaldTrump','trump2016','MakeAmericaGreatAgain']

> Filtrando los datos
Toda la data recolectada fue almacenada en mongo en un database de nombre "twitter_db" que al final de la recolección pesaba 130 GB.
Por tanto tuvimos que filtrar los datos y lo hicimos en dos scripts:
- Tweets geolocalizados que contengan ambas listas del "track"
- Tweets que mencionen a cualquiera de los usarios usados en el follow
