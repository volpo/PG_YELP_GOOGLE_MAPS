# INDATA NLP Web APP

## ✨ Indice

- [Introducción](#introduccion)
- [Uso](#modo-de-uso)
    - [Review Analysis](#review-analysis)
    - [Strengths and Weaknesses Analysis](#s-and-w)
- [Modelo de Machine Learning](#modelo-de-machine-learning)
    - [LDA](#LDA)
    - [BERT](#BERT)
- [Tecnologías utilizadas](#tecnologias)   
- [Contribuciones](#Contribuciones)

<br>
<p align=center><img width="80%" src="https://github.com/volpo/PG_YELP_GOOGLE_MAPS/blob/main/src/indata_web_app_mainmenu.PNG"></p><br>


# **Introducción**
<div id='introduccion'/>
A fin de complementar el análisis provisto en el Dashboard del proyecto, se desarrolló una NLP Web App que puede ser consumida tanto por empresas que brinda atención al cliente, tienen una firma de loclaes o usuarios finales.
Este sistema brinda dos funcionalidades principales:
1. Review Analysis: Esta primera funcionalidad toma una reseña (en idioma inglés) y analiza si tiene una connotación positiva, negativa o neutra. Además, analizará la preponderacia de distintos tópicos en la reseña.
2. Strengths and Weaknesses: En esta segunda funcionalidad, la aplicación se centra en mostrar las fortalezas y debilidades de los distintos locales existentes en las plataformas consideradas en este proyecto. Pudiendo analizar lo que otros usuarios han remarcado como destacable o por mejorar en un local.


# **Modo de Uso**
<div id='modo-de-uso'/>

La Web App de INDATA se encuentra disponible en [Streamlit](https://indatanlpgastronomics.streamlit.app/).
Tal como lo presenta la App, podemos utilizarla de dos maneras.

## **Review Analysis**
<div id='review-analysis'/>
La primera como analizados de Topicos y Sentimientos en base a una reseña dada. Para ello indicamos en el menú del sidebar **Review Analysis**. Luego, indicamos una reseña (en idioma inglés) cuya connotación y temas queremos obtener o analizar. Esperamos unos breves instantes luego de darle al botón de **Get Review** y la App nos mostrará el resultado.
En esta primera funalidad nos indicará si la reseña es positiva, negativa o neutra seguido de un gráfico de barras (bar plot) y un gráfico de torta (pie plot) mostrandonos la preponderancia de ciertos tópicos dentro de la reseña. En este caso, aquellos tópicos con mayor preponderaci serán los más destacables en
 la reseña.

<br>
<p align=center><img width="80%" src="https://github.com/volpo/PG_YELP_GOOGLE_MAPS/blob/main/src/indata_web_app_menu.PNG"></p><br>

<br>
<p align=center><img width="80%" src="https://github.com/volpo/PG_YELP_GOOGLE_MAPS/blob/main/src/indata_web_app_review_1.PNG"></p><br>

<br>
<p align=center><img width="80%" src="https://github.com/volpo/PG_YELP_GOOGLE_MAPS/blob/main/src/indata_web_app_review_result.PNG"></p><br>


## **Strengths and Weaknesses Analysis**
<div id='s-and-w'/>
La segunda opción que nos brinda el menú principal del sidebar es **Stores Strengths and Weaknesses**. En este caso, dada la inmensa cantidad de locales que existen en USA, la applicación comienza realizando una proceso de filtrado guiado por y para el usuario. En primer instancia, en el seleccionamos el estado en **Choose your state**. Luego, seleccionamos alguna de las tantas catergorías de local que tenemos disponibles dentro de ese estado en **Choose your category**. Una vez que hayamos elegido nuestro estado y nuestra categoría, tendremos disponible un listado con todos los restaurants que entran dentro de ambas condiciones.

Una vez hayamos seleccionado nuestro restaurant de interés en **Choose your Restaurant**, la aplicación nos mostrará: Las principales fortalezas y debilidades del local (si existieran). Además, nos mostrará un Radar chart con los tópicos que los usuarios o clientes han mencionado anteriormente en reseñas del local junto con su concepción promedio. Debajo del gráfico disponemos de una descripción de cada tópico.


<br>
<p align=center><img width="80%" src="https://github.com/volpo/PG_YELP_GOOGLE_MAPS/blob/main/src/indata_web_app_menu2.PNG"></p><br>

<br>
<p align=center><img width="80%" src="https://github.com/volpo/PG_YELP_GOOGLE_MAPS/blob/main/src/indata_web_app_sw_result.PNG"></p><br>

<br>
<p align=center><img width="80%" src="https://github.com/volpo/PG_YELP_GOOGLE_MAPS/blob/main/src/indata_web_app_review_result_topic.PNG"></p><br>

>**Nota:** Aquellos locales que tienen menos de 10 categorias es porque no hay registro de reseñas para ese local que hayan mencionado ese aspecto.

# **Modelo de Machine Learning**
<div id='modelo-de-machine-learning'/>
Para nuestro modelo NLP hemos considerado dos bloques fundamentales: LDA para reconocimiento de temáticas o topic modelling y BERT para analisis de sentimientos o sentiment analysis.

### <a href="https://github.com/volpo/PG_YELP_GOOGLE_MAPS/tree/main/ML_Model"> **LDA**
<div id='LDA'/>
LDA es un modelo probabilístico utilizado en el campo del procesamiento del lenguaje natural para descubrir temas o tópicos subyacentes en un conjunto de documentos. El objetivo principal de LDA es asignar palabras a tópicos de manera automática, sin la necesidad de etiquetas o anotaciones previas.

El modelo LDA se basa en la idea de que un documento está compuesto por una mezcla de varios tópicos, y cada tópico está caracterizado por una distribución de palabras. La intuición detrás de LDA es que, si tenemos un conjunto de documentos y conocemos las palabras presentes en cada uno, podemos inferir los tópicos subyacentes más probables en el corpus y la distribución de palabras para cada tópico.

El proceso de inferencia en LDA se realiza mediante el uso de técnicas de aprendizaje automático y análisis estadístico. En resumen, el modelo LDA sigue los siguientes pasos:

1. Preparación de datos: Primero, se realiza un preprocesamiento de los documentos, que puede incluir la eliminación de palabras vacías, la normalización del texto y la tokenización.

2. Construcción del modelo: Luego, se define el número de tópicos que se desea extraer del corpus. Este número puede ser determinado de antemano o explorado mediante técnicas de validación cruzada u otras medidas. Es decir, es un hiperparámetro que debemos tunear.

3. Entrenamiento del modelo: Una vez definido el número de tópicos, se entrena el modelo LDA utilizando técnicas de inferencia probabilística. Durante el entrenamiento, el modelo asigna palabras a tópicos y actualiza las distribuciones de palabras y tópicos iterativamente para maximizar la probabilidad de generar los documentos observados.

4. Inferencia de tópicos: Después de entrenar el modelo, se pueden inferir los tópicos más probables para nuevos documentos o para documentos existentes en el corpus. Esto implica asignar una distribución de tópicos a cada documento y una distribución de palabras a cada tópico.

5. Interpretación de resultados: Finalmente, se pueden interpretar los resultados del modelo LDA examinando las distribuciones de palabras en cada tópico y las asignaciones de tópicos a los documentos. Esto permite identificar y comprender los temas predominantes en el conjunto de documentos analizados. 

Notar que el modelo realiza un análisis probabilistico, mas no nos devuelve el significado de cada tópico identificado. Es labor nuestra determinarlo. Basandonos en un análisis de coherencia, se determinó que 10 tópicos era un número que maximizaba la coherencia intra tópico mientras que brindaba variedad de temas.
Luego se determinaron los siguientes significados para cada tópico:

1. "Familiar"
2. "Negocio familiar - Pequeño y Acogedor"
3. "Calidad de los postres"
4. "Variedad del menú"
5. "Tiempo de espera (tomar el pedido, responder preguntas y traer la comida)"
6. "Calidad de la comida (comida internacional)"
7. "Calidad de la comida (sabrosa y abundante)"
8. "Local tradicional"
9. "Ambiente nocturno divertido"
10. "Atención al cliente, ambiente agradable y asequible"


### **BERT**
<div id='BERT'/>
El análisis de sentimientos es una tarea fundamental en el procesamiento del lenguaje natural, y el modelo BERT (Bidirectional Encoder Representations from Transformers) ha demostrado ser una herramienta poderosa para abordar esta tarea. BERT se basa en la arquitectura de transformers, que es conocida por su capacidad para capturar relaciones de largo alcance en el texto.

El enfoque de BERT para el análisis de sentimientos implica el pre-entrenamiento y el ajuste fino del modelo. En el pre-entrenamiento, BERT se entrena en grandes cantidades de texto sin etiquetas, lo que le permite aprender representaciones contextuales del lenguaje. Durante este proceso, el modelo adquiere un conocimiento general del lenguaje y captura sutilezas semánticas y sintácticas.

Una vez que BERT ha sido pre-entrenado, se realiza un ajuste fino en un conjunto de datos específico para el análisis de sentimientos.
En este case, el ajuste fino se realizó en base a las reviews disponibles y la clasificación o estrellas que el usuario daba al local como forma de obtener indirectamente los valores objetivos. Durante este proceso, el modelo ajusta sus pesos y aprende a asociar características del texto con las etiquetas de sentimiento correspondientes.

Una vez BERT ha sido entrenado con un conjunto de datos de análisis de sentimientos, se puede utiliza para determinar si la connotación de las reseñas de los usuarios es positiva, negativa o neutra. 

# 🛠️ **Tecnologías**
<div id='tecnologias'/>

- Gensim
- HuggingFaces
- NLTK
- Pandas
- Python
- Spacy
- Streamlit


# Contribuciones
<div id='Contribuciones'/>
Si quieres contribuir en este proyecto no dudes en escribirme a mí o a cualquiera de nuestro equipo.

Mi mail es carnaghi.marco@gmail.com estoy a disposición por cualquier duda que tengas.
