# Api-Data-Pipeline-Integration
Uno de los principales objetivos para este proyecto es el enriquecimiento de los datos estáticos de Google Maps y Yelp, por medio de API´s.
<br>
<br>
<p align=center><img width="80%" src="https://github.com/volpo/PG_YELP_GOOGLE_MAPS/blob/main/src/data_pipeline.gif"></p><br>

## ✨ Elementos del Proceso
- [API Getter](#API-Getter)
- [ETL_API_Function](#ETL_API_Function)
- [Cloud Storage (Data Lake)](#Cloud-Storage-(Data-Lake))
- [Scheduler](#Scheduler)
<div id='Cloud-Scheduler1'/>

### <a href="https://github.com/volpo/PG_YELP_GOOGLE_MAPS/tree/main/API-Cassandra_Pipeline"> API getters</a>
<div id='API-getters'/>
El objetivo de los primeros módulos es obtener la información relevante y actual de los restaurantes y sus reviews. Para ello, se realizan dos procesos.
Por una parte, se consultan las tablas disponibles en el Data Lake con el objetivo de conocer aquellos locales que requieren actualizar las reviews disponibles en el Data Lake. Identificado un grupo de locales que tienen desactulizadas sus reviews, se realiza un llamado a Yelp Fusion API para obtener y almacenar nuevas reviews.
Por otra parta, es necesario mantener actualizados los locales en existencia. Con ello en mente, se consulta a Yelp Fusion API para obtener los locales que se han cargado en el último tiempo y también incluirlos en el Data Lake.
<br>
<p align=center><img width="80%" src="https://github.com/volpo/PG_YELP_GOOGLE_MAPS/blob/main/src/intro_2_gif.gif"></p><br>


<br>
<p align=center><img width="80%" src="https://github.com/volpo/PG_YELP_GOOGLE_MAPS/blob/main/src/pipes_2_gif.gif"></p><br>

Es importante mencionar que Yelp Fusion API es proporcionada por Yelp y requiere credenciales de API válidas para su correcto funcionamiento.
<br>




### <a href="https://github.com/volpo/PG_YELP_GOOGLE_MAPS/tree/main/API-Cassandra_Pipeline"> ETL_API_Function </a>
<div id='ETL_API_Function'/>
Los datos obtenidos a partir de Yelp Fusion API son provistos en formato JSON. Previamente a ser almacenados en nuestro Data Lake basado en Cassandra, estos datos son transformados para disponer del formato acorde a las tablas definidas en Cassandra.

<br>
<p align=center><img width="80%" src="https://github.com/volpo/PG_YELP_GOOGLE_MAPS/blob/main/src/pipe1_2_gif.gif"></p><br>

<br>
<p align=center><img width="80%" src="https://github.com/volpo/PG_YELP_GOOGLE_MAPS/blob/main/src/pipe2_2_gif.gif"></p><br>


### Cloud Storage (Data Lake) 
<div id='Cloud-Storage-(Data-Lake)'/>

Una vez transformados los datos provenientes de Yelp Fusion API se almacenan junto a la data estática en las tablas de Cassandra, es decir el Data Lake.

<br>
<p align=center><img width="80%" src="https://github.com/volpo/PG_YELP_GOOGLE_MAPS/blob/main/src/Api_pipeline.png"></p><br>




### Scheduler
<div id='Scheduler'/>
Los procesos mencionados son disparados mediante triggers temporales para que la carga sea de forma automática, para ello se utilizarons los triggers disponibles en la plataforma de Mage AI, el cual es nuestro gestor de pipelines.
En este sentido se definieron dos triggers. El primero se ejecuta a cada hora para obtener nuevas reviews de los locales, mientras que el segundo se ejecuta semanalmente, para obtener nuevos locales que hayan sido incorporados a la plataforma.
<br>
<p align=center><img width="80%" src="https://github.com/volpo/PG_YELP_GOOGLE_MAPS/blob/main/src/triggers_2_gif.gif"></p><br>

<br>
<p align=center><img width="40%" src="https://github.com/volpo/PG_YELP_GOOGLE_MAPS/blob/main/src/logs_2_gif.gif"></p><br>



## Material Adicional

A fin de brindar mayor claridad del funcionamiento de la plataforma desarrollada por INDATA se generaron distintos materiales audiovisuales presentando distintos elementos del mismo:

+[Pipeline From API to Cassandra](https://drive.google.com/file/d/1gKkr2OhIwR2iQGXp0PrRKW8tfif151HO/view?usp=sharing): En este video se presentan los bloques destinados a tomar información actualizada desde Yelp API Fusion e ingestarla en el Data Lake implementado en Cassandra. Este pipeline tiene por objetivo llevar los datos base de la aplicación a la fecha actual, tanto en locales existintes como de reviews realizadas por los usuarios.



##  🛠️ Tecnologías 

- Cassandra
- Mage AI
- Pandas
- Python

