<p align="center">
<img src="https://user-images.githubusercontent.com/60153579/259791208-7272d632-6fb3-429c-8c01-af83e049b64e.jpg"  height=200>
</p>

<h1 align="center"> Restaurantes en USA </h1>

## Descripción del proyecto

<div style="text-align: justify"><p style="text-align: justify;">
	Realizar el análisis de los datasets de reviews de Google Maps y Yelp suministrados por la compañía y la información adicional conseguida mediante APIs, con el fin de determinar los rubros de restaurantes más populares en los Estados Unidos y las zonas con menos cantidad de esos locales. La propuesta que se propone lograr es integradora, combinando los rubros que resulten más atractivos para los consumidores según su contexto regional, como podrían ser: comida sudamericana, formato sandwich, comida al paso o para llevar, etc. 

  El análisis permitirá al consorcio conocer las zonas más competitivas para abrir nuevos restaurantes y que rubro abrir. Además, se extraerán las recomendaciones que realicen los usuarios que dejen comentarios negativos para que puedan ser aplicadas y mejorar la calidad de su servicio, el mismo proceso se realizará con las reviews de Uber Eats para mejorar el servicio de delivery.

</p></div>

## Objetivos

<div style="text-align: justify"><p style="text-align: justify;">

- Identificar los rubros más populares de comida de los Estados Unidos y las zonas con menos restaurantes de dichos rubros para abrir nuevos locales en los que se integren tomando en cuenta el contexto regional, por ejemplo: comida sudamericana, formato sandwich, comida para llevar, entre otros.

- Crear un modelo que extraiga las razones de las reviews negativas y utilizarlas como recomendaciones para mejorar el servicio.

</p></div>

## Alcance

<div style="text-align: justify"><p style="text-align: justify;">
Se encuentra en el alcance del proyecto:

- Categorías: el análisis se centrará en el rubro gastronómico (restaurantes, cafeterías, etc.). Por lo tanto, otras categorías no serán consideradas.
- Geográfico: el análisis se limitará a los 5 estados con mayor cantidad de turistas de los Estados unidos, pues son los que tienen mayor probabilidad de captar consumidores y crecer. Los estados son: Nevada, California, Texas, Nueva York y Florida.
- Datos: se utilizarán los datos de Yelp y Google Maps suministrados por la compañía, así como datos externos conseguidos mediante APIs.
- Tiempo: los datos empleados en el proyecto están a partir del año 2004.

</p></div>

## Tecnologías

<div style="text-align: justify"><p style="text-align: justify;">
Se utilizarán las siguientes tecnologías para el desarrollo del proyecto:

- Github para alojar el repositorio donde se encontrará toda la documentación del proyecto.
- Python como lenguaje de programación para realizar el análisis exploratorio de los datos y la creación del modelo.
- Cassandra como base de datos NO-SQL para almacenar toda la información y realizar las consultas a los datos.
- Power BI para realizar el dashboard que permitirán mostrar los KPIs planteados.
- mage.ai para desarrollar el flujo de procesamiento de los datos.

</p></div>

## Metodología

<div style="text-align: justify"><p style="text-align: justify;">
El proyecto está basado en la metodología SCRUM para fomentar el trabajo en equipo y poder alcanzar los objetivos planteados en el tiempo que dura cada uno de los Sprints.

Se utilizará un Diagrama de Gantt para distribuir las tareas de forma secuencial y equitativa, el Diagrama será realizado en Google Sheets y será actualizado por cada integrante una vez terminada la tarea. 

</p></div>

## Material Adicional

#### Soporte AudioVisual 

A fin de brindar mayor claridad del funcionamiento de la plataforma desarrollada por INDATA se generaron distintos materiales audiovisuales presentando distintos elementos del mismo:

+[Pipeline From API to Cassandra](https://drive.google.com/file/d/1gKkr2OhIwR2iQGXp0PrRKW8tfif151HO/view?usp=sharing): En este video se presentan los bloques destinados a tomar información actualizada desde Yelp API Fusion e ingestarla en el Data Lake implementado en Cassandra. Este pipeline tiene por objetivo llevar los datos base de la aplicación a la fecha actual, tanto en locales existintes como de reviews realizadas por los usuarios.

## Colaboradores

- [Sebastian Saenz](https://github.com/nine-o-one), Data Engineer.
- [Alba Castillo](https://github.com/AlbaCastillo), Data Analyst.
- [Alejandro Volponi](https://github.com/volpo), Data Analyst.
- [Marco Carnaghi](https://github.com/MarcoCarnaghi-fi), Data Scientist.
- [Luis Torres](https://github.com/luissgtorres), Data Scientist.
