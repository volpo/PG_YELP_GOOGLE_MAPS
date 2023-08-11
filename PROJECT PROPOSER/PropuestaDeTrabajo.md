## PROPUESTA DE TRABAJO

### Presentación de objetivos
En este trabajo vamos a concentrarnos en identificar *tendencias en el rubro gastronómico* y *redirigir clientes o captar clientes interesados en experimentar sabores pertenecientes a estas tendencias*. 

Para ello el proyecto se centrará en dos aspectos:

1. Por una parte, estudiar patrones que permitan identificar categorías del rubro gastronómico con crecimiento potencial. Para ello se buscarán  categorías  que sean populares y bien apreciadas por los clientes y que estén viendo un crecimiento en su presencia en los últimos años. Una vez identificadas las categorías de interés, se estudiarán locaciones potenciales donde establecer locales para captar usuarios del segmento de mercado que tengan poca oferta o una competencia pobre (mal calificada).

    1. El primer paso radica en encontrar las mencionadas tendencias o rubros en crecimiento. Para lo cual, se propone estudiar los siguientes KPIs:
        + *Número promedio de reviews por unidad de tiempo*: Este KPI nos permite estimar el volumen promedio de clientes normalizado por unidad de tiempo, evitando el sesgo del factor antigüedad de la categoría en el mercado. De esta forma, nos brindará información para evaluar e identificar los rubros con mayor flujo de clientes.

        + *Tasa de variación en el número de reviews*: Este KPI nos permitirá identificar rubros donde esté creciendo el interés por parte de los usuarios. Una alta tasa de crecimiento en el nro de reviews nos habla de un creciente nro de clientes visitando estos locales. En otras palabras, permite evaluar cómo ha evolucionado la popularidad de distintos rubros.

        + *Calificación promedio*: Este KPI nos habla de la percepción que tienen los clientes sobre una determinada categoría. Categorías con alta puntuación promedio son de interés por su buena apreciación por parte de los consumidores. En conjunto con los anteriores KPIs, este valor nos habla del desempeño de un dado rubro frente a los clientes. Rubros donde el número de clientes sea elevado y creciente pero tengan una pobre calificación promedio, habla de interés por parte de los clientes pero una pobre oferta por parte de otras compañías en el sector.

        + *Engagement*: Este KPI consiste en evaluar el número de interacciones que surgen a consecuencia de cada review que recibe un local, hablando de uno de los aspectos más importante en el marketing digital, el engagement. A mayor sea el número de interacciones generadas entre clientes o entre clientes y el local, mayor interés despierta un local. 


        Así los KPIs anteriormente mencionados trabajan en conjunto para identificar aquellos rubros y tendencias que son atractivas para los clientes y cuya popularidad está en creciemiento y respecto a los cuales los clientes están interesados en conocer más y dar una retroalimentación.

    2. Una vez identificadas las tendencias de interés para los clientes, es necesario identificar puntos potenciales donde desplegar los locales de la marca. Para lo cual es importarte idenfiticar zonas con poca oferta por parte de la compentencia o, bien, zonas donde la competencia no tiene una buena percepción por parte de los clientes. Así, se proponen dos KPIs para identificar estas zonas:

        + *Densidad de locales per cápita*: Esta métrica nos permite evaluar el desempeño o avance de la competencia en cubrir la demanda en una zona dada. Identificados rubros que llaman la atención de los clientes, aquellas zonas donde existan pocos locales atendiendo su demanda son zonas donde será más sencillo captar a los clientes.

        + *Calificación promedio de locales en la zona*: Este indicador evaluará el desempeño de los locales en la región bajo análisis. Una baja calificación por parte de los clientes, nos indica que los mismos asisten a los lugares puesto existe interés, pero la oferta existente es pobre en calidad de servicio. 

        Así ambos KPIs en conjunto evaluarán zonas atractivas para desplegar sucursales.


2. El segundo paso consiste en redirigir clientes hacia estos “sabores en tendencia”. En este sentido, es necesario desarrollar un sistema de recomendación que permita identificar a los clientes potenciales y sugerirle alguno de los locales. Mediante los datos provistos por Yelp! Es posible generar medidas de similitud entre los usuarios. En base a los datos disponibles y a esta similitud, es posible identificar usuarios que hayan visitado y disfrutado comiendo en algún local perteneciente a las categorías de interés y buscar usuarios que tengan gustos similares. Luego, la próxima vez que un usuario busque un lugar recomendable para cenar será posible sugerir alguno de los locales establecidos.


### Acotando el Scope:
+ Categorías: En primer lugar, el análisis se centrará en el rubro gastronómico ( restaurants, cafeterías, etc.). Por lo tanto, otras categorías no serán consideradas para determinar locales atractivos a abrir.
+ Geográfico: Nos limitaremos a los 5 estados con mayor afluente turístico en USA. Ya que serán los que tendrán mayor potencialidad de captar estos consumidores. Así, basándonos en el siguiente dataset, el foco está puesto en los estados de: New York, California, Florida, Nevada y Texas.

### Tareas:

1. Obtención de los datos
    1. Creación de un Data Lake a partir de datasets de Google Maps y Yelp!.

2. EDA
    1. Realizar un EDA para evaluar la calidad de los datos.
    2. Identificar atributos de utilidad para el proyecto.
    3. Identificar los proceso de cruza de datasets necesarios.

3. Creación de Data Warehouse
    1. Desarrollo de flujo de procesamiento de datos basado en Mage.
    2. Desarrollo de bloques de código para acondicionar los datos en el Data Lake al DataWarehouse en Cassandra.
    3. Desarrollo de procesos para atención a eventos o triggers para carga incremental.

4. Cálculo de KPIs
    1. Desarrollo de scripts en Python para consultar datos del DataWarehouse
    2. Desarrollo de código Python para calcular los KPIs.
        + Desarrollo de proceso NLP para análisis de sentimientos en comentarios y reviews.

5. Identificación de rubros de interés
    1. Visualización de indicadores en contexto temporal.
    2. Extracción de conclusiones.
    

6. Identificación de potenciales locaciones para los nuevos locales
    1. Visualización de indicadores en contexto geográfico.
    2. Extracción de conclusiones.

7. Sistema de recomendación
    1. Definir métrica de similitud basada en locales visitados.
        + Proceso NLP para definir sentimientos en las review y comentarios.
    2. Definir sugerencias de interés basada en similitud e historial de usuarios asociados.
