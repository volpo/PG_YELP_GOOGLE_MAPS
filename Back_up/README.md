<h1 align="center"> Back up </h1>

Con la finalidad de tener los datos siempre disponibles, se crea un respaldo de los datos en un servidor en la nube, esto permitirá acceder a los datos en caso de que existan fallos en el servidor local. Para el proyecto se decidió trabajar con el servicio en la nube de Amazon (AWS), utilizando como almacenamiento su servicio Amazon S3.

## Amazon S3

Amazon S3 es un servicio de almacenamiento de objetos que ofrece escalabilidad, disponibilidad, seguridad y alto rendimiento. Permite almacenar objetos de diferentes tipos como csv, parquet o json. 

El servicio de Amazon S3 es de bajo costo y se puede acceder a el en diferentes regiones en todo el mundo. Es un servicio que cuenta con una interfaz que facilita la organización de los objetos al almacenarlos en Buckets. Dentro de los Buckets se pueden almacenar directamente los objetos o carpetas que cuenten con los objetos.

El servicio de Amazon S3, permite integrarse con una gran variedad de servicios disponibles en AWS, entre ellos AWS Glue y AWS Athena.

## AWS Glue

El servicio de AWS Glue es serverless y permite a los usuarios descubrir, preparar, integrar y migrar datos de diferentes fuentes: tanto internas en la nube de Amazon como fuentes externas.

Es un servicio sumamente útil para realizar las tareas referentes a ELT ya que cuenta con una interfaz en la que no se necesita código, que permite crear los pasos del ETL arrastrando y uniendo diferentes bloques que realizan las actividades del ETL. Además, cuenta con notebooks y scripts en caso de que el usuario desee utilizar su propio código. 

En este servicio se pueden crear bases de datos que se conectan con el servicio serverless de AWS Athena para realizar análisis de las tablas almacenadas en dichas bases de datos.

## AWS Athena

AWS Athena es un servicio de consulta que facilita el análisis de datos directamente sobre los datos que están presentes en Amazon S3 o sobre los datos que estén almacenados en las diferentes opciones de bases de datos que ofrece Amazon.

Con este servicio se puede realizar el análisis exploratorio de los datos utilizando queries en lenguaje SQL. Además es serverless, por lo que no es necesario configurar un servidor para utilizarlo.

---

En el caso de INDATA, se almacenó inicialmente los datos sucios en un bucket de Amazon S3, estos datos fueron cargados a una base de datos con Crawlers de AWS Glue, donde fueron limpiados, transformados y, posteriormente, los datos fueron cargados en la base de datos de AWS Glue y en el Bucket de Amazon S3. El flujo de datos queda de la siguiente manera:

![Flujo de datos]()

Para la limpieza y transformación de los datos, se utilizó un [**notebook the Apache Spark**]() en la plataforma de AWS Glue