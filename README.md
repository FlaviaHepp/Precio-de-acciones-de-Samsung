# Precio-de-acciones-de-Samsung
Esta información es necesaria para realizar análisis históricos, pronosticar el desempeño futuro de las acciones y comprender las tendencias del mercado a largo plazo relacionadas con las acciones de Samsung Electronics.

**Desarrollo:** 
Desarrollo de un análisis exhaustivo de los datos históricos de precios de acciones de Samsung, evaluando tendencias de mercado, cambios en volumen y precios, y su relación con factores clave. Se utilizaron técnicas avanzadas de modelado para predecir valores futuros del precio de cierre.
*Herramientas y tecnologías utilizadas:* Python, pandas, numpy, matplotlib, seaborn, plotly (gráficos dinámicos y líneas de tendencia), scikit-learn, RandomForestRegressor y LinearRegression.
*Métricas de evaluación:* MAE, MSE, R².
**Resultados clave:**
Identificación de una tendencia de aumento constante en los precios ajustados y una disminución gradual en el volumen de operaciones.
Implementación de modelos predictivos con un R2R^2R2 para regresión lineal y para el modelo Random Forest.
Creación de visualizaciones interactivas para explorar desviaciones móviles y correlaciones clave en los datos.
*Habilidades aplicadas:* Análisis exploratorio de datos (EDA), preprocesamiento de datos, modelado y evaluación de regresión, creación de visualizaciones avanzadas.


📈 Análisis Exploratorio y Predicción del Precio de las Acciones de Samsung

Este proyecto realiza un análisis exploratorio profundo (EDA) y un modelado predictivo sobre los precios históricos de las acciones de Samsung Electronics, combinando técnicas de visualización avanzada, análisis estadístico y Machine Learning.

🎯 Objetivos del proyecto

Analizar la evolución histórica del precio y volumen de Samsung.

Explorar la distribución de variables financieras clave.

Identificar relaciones y dependencias mediante matrices de correlación.

Detectar tendencias utilizando escalas logarítmicas y medias móviles.

Construir modelos predictivos para estimar el precio de cierre.

Comparar el desempeño de distintos modelos de regresión.

📁 Descripción del dataset

El dataset contiene información bursátil histórica de Samsung, incluyendo:

Date: fecha de negociación

Open: precio de apertura

High: precio máximo

Low: precio mínimo

Close: precio de cierre

Adj Close: precio de cierre ajustado

Volume: volumen de operaciones

Además, se generan variables temporales:

Año, mes y día

Medias móviles y desviaciones móviles

📊 Análisis exploratorio (EDA)
Visualización de datos

Gráficos lineales y de barras del precio de cierre.

Histogramas y boxplots para detectar distribución y outliers.

Visualización del precio y volumen en escala logarítmica.

Análisis de tendencias con LOWESS smoothing.

Gráficos de evolución temporal de máximos y volumen.

Análisis estadístico

Estadísticos descriptivos.

Análisis de correlación entre variables financieras.

Mapas de calor para identificar relaciones relevantes.

🔄 Ingeniería y transformación de datos

Conversión y validación de fechas.

Extracción de componentes temporales (año, mes, día).

Limpieza de valores faltantes.

Renombrado y estandarización de variables.

Creación de medias móviles y rolling statistics (30 días).

🤖 Modelado predictivo

Se implementan y comparan modelos supervisados para predecir el precio de cierre:

Modelos utilizados

Regresión Lineal

Random Forest Regressor

Métricas de evaluación

MAE (Mean Absolute Error)

MSE (Mean Squared Error)

R² Score

Los resultados permiten comparar modelos lineales vs. no lineales en un contexto financiero real.

🛠️ Tecnologías utilizadas

Python

pandas / numpy

Matplotlib / Seaborn

Plotly

scikit-learn

📂 Estructura del proyecto
├── Análisis de precios de acciones de Samsung.py
├── Samsung Dataset.csv
└── README.md

▶️ Cómo ejecutar el proyecto

Clonar el repositorio

git clone https://github.com/tu_usuario/nombre_del_repo.git


Instalar dependencias

pip install pandas numpy matplotlib seaborn plotly scikit-learn


Ejecutar el script

python "Análisis de precios de acciones de Samsung.py"

📌 Resultados principales

Tendencia alcista de largo plazo en el precio de Samsung.

Disminución progresiva del volumen acompañando el aumento del precio.

Alta correlación entre precios Open, High, Low y Close.

El modelo Random Forest supera a la regresión lineal en precisión.

El enfoque de ML captura relaciones no lineales del mercado.

⚠️ Disclaimer

Este proyecto tiene fines educativos y analíticos.
No constituye asesoramiento financiero ni recomendaciones de inversión.

👤 Autor

Flavia Hepp
Data Science · Machine Learning · Análisis Financiero
