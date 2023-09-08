<p align="center">
<img src="https://user-images.githubusercontent.com/60153579/259791208-7272d632-6fb3-429c-8c01-af83e049b64e.jpg"  height=200>
</p>

<h1 align="center"> Restaurantes en USA </h1>

## Descripción del proyecto

<div style="text-align: justify"><p style="text-align: justify;">
	Nuestro proyecto tiene como objetivo llevar a cabo un exhaustivo análisis de los datasets de reviews de Google Maps y Yelp proporcionados por nuestra compañía, así como obtener información adicional mediante el uso de APIs. El propósito fundamental es determinar los rubros de restaurantes más populares en los Estados Unidos y identificar las zonas con menor cantidad de locales en esos rubros específicos.

Nuestra propuesta se enfoca en lograr una visión integradora al combinar los rubros más atractivos para los consumidores, teniendo en cuenta su contexto regional. Esto incluirá categorías como comida sudamericana, formato sandwich, comida al paso o para llevar, entre otros.

El análisis de datos resultante permitirá a nuestro consorcio obtener información valiosa sobre las zonas más competitivas para la apertura de nuevos restaurantes, así como determinar qué rubros específicos deben ser considerados. Además, nos enfocaremos en extraer las recomendaciones proporcionadas por los usuarios en sus comentarios negativos, con el objetivo de aplicar estas sugerencias y mejorar la calidad de nuestros servicios. Este mismo proceso se replicará utilizando las reviews de Uber Eats para optimizar nuestro servicio de delivery.

Mediante el uso de técnicas de análisis avanzadas y la consideración de la retroalimentación de los usuarios, nuestro proyecto busca brindar a nuestro consorcio una ventaja competitiva al tomar decisiones informadas en cuanto a la apertura de nuevos restaurantes y la mejora continua de nuestros servicios.

</p></div>

## Objetivos

<div style="text-align: justify"><p style="text-align: justify;">

+ Identificar los Rubros Populares: El objetivo principal de nuestro proyecto es identificar los rubros de comida más populares en los Estados Unidos. A través del análisis de los datasets de reviews de Google Maps y Yelp, así como la información obtenida mediante APIs adicionales, buscaremos determinar los rubros que gozan de mayor demanda entre los consumidores. Además, también nos enfocaremos en identificar las zonas geográficas con menor cantidad de restaurantes en dichos rubros específicos.

+ Apertura de Nuevos Locales: Utilizando los hallazgos del análisis realizado, nuestro objetivo es abrir nuevos locales de comida que integren los rubros identificados, considerando el contexto regional. Por ejemplo, si la comida sudamericana y los formatos de sándwich son rubros populares en ciertas zonas, buscaremos establecer locales que ofrezcan una combinación atractiva de estos elementos. Nuestro objetivo es aprovechar esta información para tomar decisiones estratégicas sobre dónde y qué tipo de restaurantes abrir.

+ Mejora del Servicio basada en Reviews Negativas: Implementaremos un modelo que extraiga las razones detrás de las reviews negativas de los usuarios. Utilizando técnicas de procesamiento de lenguaje natural, analizaremos los comentarios y opiniones negativas de los usuarios para identificar patrones y tendencias comunes. Estas razones se utilizarán como recomendaciones para mejorar la calidad y el servicio ofrecido por nuestros restaurantes. Nos enfocaremos en abordar los aspectos mencionados en las reviews negativas para impulsar una mejora continua.

</p></div>

## Alcance

<div style="text-align: justify"><p style="text-align: justify;">
Se encuentra en el alcance del proyecto:

+ Categorías Gastronómicas: El análisis se centrará exclusivamente en el rubro gastronómico, abarcando restaurantes, cafeterías y establecimientos similares. Otras categorías fuera de este ámbito no serán consideradas en el alcance del proyecto.

+ Área Geográfica: El análisis se limitará a cinco estados de los Estados Unidos que son reconocidos por su alta afluencia de turistas y su potencial para captar consumidores. Estos estados son: Nevada, California, Texas, Nueva York y Florida. Nuestro enfoque se centrará en estos estados, ya que ofrecen una mayor probabilidad de crecimiento y éxito para los nuevos locales de comida.

+ Fuentes de Datos: Utilizaremos los datos suministrados por la compañía procedentes de Yelp y Google Maps como fuentes principales. Estos conjuntos de datos nos proporcionarán información valiosa sobre las reviews de los usuarios y la ubicación de los restaurantes. Además, recurriremos a fuentes externas y haremos uso de APIs para obtener información adicional y enriquecer nuestro análisis.

+ Período de Tiempo: Los datos utilizados en el proyecto abarcarán un período a partir del año 2004. Utilizaremos el histórico de datos disponible para realizar análisis retrospectivos y obtener una visión más completa de las tendencias y patrones en el rubro gastronómico en los estados seleccionados.

</p></div>

## Tecnologías

<div style="text-align: justify"><p style="text-align: justify;">
Se utilizarán las siguientes tecnologías para el desarrollo del proyecto:

Github: Se utilizará Github para alojar el repositorio del proyecto donde se encontrará toda la documentación y el código fuente.

Python: Se utilizará Python como lenguaje de programación principal para realizar el análisis exploratorio de los datos y la creación del modelo.

Cassandra (Data Lake): Se empleará Cassandra como base de datos NoSQL para almacenar toda la información y realizar consultas a los datos. Cassandra es conocida por su capacidad de escalar horizontalmente y su rendimiento en operaciones de escritura masiva.

Power BI: Se utilizará Power BI para crear el dashboard que mostrará los indicadores clave de rendimiento (KPI) planteados en el proyecto. Power BI es una herramienta de visualización de datos poderosa y ampliamente utilizada.

mage.ai: Se empleará mage.ai para desarrollar el flujo de procesamiento de datos. Esta herramienta permite integrar y sincronizar datos de fuentes externas, y construir pipelines en tiempo real y por lotes utilizando Python, SQL y R.

AWS S3: Se utilizará Amazon S3 (Simple Storage Service) como un servicio de almacenamiento en la nube para realizar copias de seguridad y almacenar los datos del proyecto de manera segura.

Streamlit: Se utilizará Streamlit para implementar una aplicación web de NLP (Procesamiento del Lenguaje Natural) que permitirá interactuar con los datos y realizar análisis específicos relacionados con el lenguaje.

Looker: Se utilizará Looker para crear un dashboard de información geográfica. Looker es una herramienta de visualización de datos y generación de informes que permitirá explorar y presentar datos geográficos de manera interactiva.

MySQL DataWarehouse: Se utilizará MySQL como Data Warehouse para almacenar y gestionar datos a gran escala, proporcionando capacidades de consulta y análisis avanzadas.
</p></div>

## Metodología

<div style="text-align: justify"><p style="text-align: justify;">
La metodología de desarrollo del proyecto se basará en SCRUM, una metodología ágil que fomenta la colaboración en equipo, la adaptabilidad y la entrega iterativa de resultados. SCRUM se divide en sprints, que son intervalos de tiempo fijos y cortos en los que se lleva a cabo el desarrollo del proyecto.

Se utilizará un Diagrama de Gantt para planificar y distribuir las tareas de forma secuencial a lo largo de los sprints. El Diagrama de Gantt es una herramienta visual que muestra las tareas, su duración y las dependencias entre ellas. Google Sheets se utilizará como la plataforma para crear y actualizar el Diagrama de Gantt.

Cada miembro del equipo será responsable de actualizar el Diagrama de Gantt una vez que haya completado una tarea asignada. Esto permitirá mantener un seguimiento actualizado del progreso del proyecto y asegurarse de que las tareas se completen en los plazos establecidos.

Al utilizar SCRUM y el Diagrama de Gantt, se busca promover la transparencia, la colaboración y la gestión efectiva del tiempo y los recursos del equipo. Esto permitirá un desarrollo más eficiente y controlado del proyecto, asegurando que se alcancen los objetivos planteados en cada sprint.

</p></div>

## Material Adicional

Mayor detalle respecto a los distintos apartados del proyecto pueden encontrarse en el repositorio:

+ [Pipeline API - Cassandra](https://github.com/volpo/PG_YELP_GOOGLE_MAPS/tree/main/API-Cassandra_Pipeline)
+ [Pipeline Cassandra - MySQL](https://github.com/volpo/PG_YELP_GOOGLE_MAPS/tree/main/Cassandra_SQL_DataPipeline)
+ [EDA](https://github.com/volpo/PG_YELP_GOOGLE_MAPS/tree/main/PRELIMINARY%20EDA)
+ [Dashboard](https://github.com/volpo/PG_YELP_GOOGLE_MAPS/tree/main/PRELIMINARY%20EDA)
+ [Machine Learning Model](https://github.com/volpo/PG_YELP_GOOGLE_MAPS/tree/main/ML_Model)
+ [Streamlit NLP Web App](https://github.com/volpo/PG_YELP_GOOGLE_MAPS/tree/main/Streamlit_INDATA_WebApp)
+ [Back UP en AWS](https://github.com/volpo/PG_YELP_GOOGLE_MAPS/tree/main/Back_up)


## Colaboradores

- [Sebastian Saenz](https://github.com/nine-o-one), Data Engineer.
- [Alba Castillo](https://github.com/AlbaCastillo), Data Analyst.
- [Alejandro Volponi](https://github.com/volpo), Data Analyst.
- [Marco Carnaghi](https://github.com/MarcoCarnaghi-fi), Data Scientist.
- [Luis Torres](https://github.com/luissgtorres), Data Scientist.
