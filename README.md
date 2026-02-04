# 📈Análisis Exploratorio y Predicción del Precio de las Acciones de Samsung

Este proyecto realiza un análisis exploratorio profundo (EDA) y un modelado predictivo sobre los precios históricos de las acciones de Samsung Electronics, combinando técnicas de visualización avanzada, análisis estadístico y Machine Learning.

# 🎯Objetivos del proyecto

- Analizar la evolución histórica del precio y volumen de Samsung.
- Explorar la distribución de variables financieras clave.
- Identificar relaciones y dependencias mediante matrices de correlación.
- Detectar tendencias utilizando escalas logarítmicas y medias móviles.
- Construir modelos predictivos para estimar el precio de cierre.
- Comparar el desempeño de distintos modelos de regresión.

# 📁Descripción del dataset

El dataset contiene información bursátil histórica de Samsung, incluyendo:
- Date: fecha de negociación
- Open: precio de apertura
- High: precio máximo
- Low: precio mínimo
- Close: precio de cierre
- Adj Close: precio de cierre ajustado
- Volume: volumen de operaciones

Además, se generan variables temporales:
- Año, mes y día
- Medias móviles y desviaciones móviles

# 📊Análisis exploratorio (EDA)

Visualización de datos:
  
  -- Gráficos lineales y de barras del precio de cierre.
  -- Histogramas y boxplots para detectar distribución y outliers.
  -- Visualización del precio y volumen en escala logarítmica.
  -- Análisis de tendencias con LOWESS smoothing.
  -- Gráficos de evolución temporal de máximos y volumen.
  -- Análisis estadístico
  -- Estadísticos descriptivos.
  -- Análisis de correlación entre variables financieras.
  -- Mapas de calor para identificar relaciones relevantes.

# 🔄Ingeniería y transformación de datos

- Conversión y validación de fechas.
- Extracción de componentes temporales (año, mes, día).
- Limpieza de valores faltantes.
- Renombrado y estandarización de variables.
- Creación de medias móviles y rolling statistics (30 días).

# 🤖Modelado predictivo

Se implementan y comparan modelos supervisados para predecir el precio de cierre:
- Modelos utilizados
- Regresión Lineal
- Random Forest Regressor
- Métricas de evaluación
- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- R² Score

Los resultados permiten comparar modelos lineales vs. no lineales en un contexto financiero real.

# 🛠️Tecnologías utilizadas

- Python
- pandas / numpy
- Matplotlib / Seaborn
- Plotly
- scikit-learn

# 📂Estructura del proyecto
├── Análisis de precios de acciones de Samsung.py
├── Samsung Dataset.csv
└── README.md


# 📌Resultados principales

- Tendencia alcista de largo plazo en el precio de Samsung.
- Disminución progresiva del volumen acompañando el aumento del precio.
- Alta correlación entre precios Open, High, Low y Close.
- El modelo Random Forest supera a la regresión lineal en precisión.
- El enfoque de ML captura relaciones no lineales del mercado.

# ⚠️Disclaimer

Este proyecto tiene fines educativos y analíticos.
No constituye asesoramiento financiero ni recomendaciones de inversión.

# 👤Autor

Flavia Hepp
Data Science en formación · Machine Learning · Análisis Financiero
