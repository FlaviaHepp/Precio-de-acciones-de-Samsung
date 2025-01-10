

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
from plotly import express
from datetime import datetime
sns.set_style('darkgrid')
plt.style.use('dark_background')
warnings.filterwarnings("ignore", category=DeprecationWarning)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


df = 'Samsung Dataset.csv'

df = pd.read_csv(filepath_or_buffer=df, parse_dates=['Date'])
df['year'] = df['Date'].dt.year
print(df)

df['Date']=pd.to_datetime(df['Date'])
df.describe().T

df.describe().T.plot()

df.columns.to_list()

corr_matrix = df.corr()

plt.figure(figsize=(10,6))
sns.heatmap(corr_matrix, annot=True, cmap='cool')
plt.title('Matriz de correlación\n', fontsize = '16', fontweight = 'bold')
plt.show()

#Se convierte la columna 'Fecha' al formato de fecha y hora si es necesario
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])

#Gráfico lineal
fig, ax = plt.subplots(figsize=(20, 8))
ax.plot(df['Date'], df['Close'], color='green')
ax.xaxis.set_major_locator(plt.MaxNLocator(15))
ax.tick_params(axis='x', rotation=45)  
ax.set_xlabel('Fecha\n', fontsize=14)
ax.set_ylabel('Precio en USD\n', fontsize=14)
plt.title('Precio de las acciones de Samsung\n', fontsize = '16', fontweight = 'bold')
plt.grid()
plt.show()

#Gráfico de barras
fig2, ax = plt.subplots(figsize=(20, 8))
ax.bar(df['Date'], df['Close'], color='green', edgecolor = "blue")
ax.xaxis.set_major_locator(plt.MaxNLocator(15))
ax.tick_params(axis='x', rotation=45)  
ax.set_xlabel('Fecha\n', fontsize=14)
ax.set_ylabel('Precio en USD', fontsize=14)
plt.title('Precio de las acciones de Samsung\n', fontsize = '16', fontweight = 'bold')
plt.show()

df.hist(bins = 20, figsize = (20,20), color = 'fuchsia', edgecolor = "gold")
plt.show()

for column in ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']:
    express.histogram(data_frame=df, x=column, template = "plotly_dark").show()
    
#Veamos primero el historial de precios; Como se trata de una empresa exitosa y tenemos una serie larga, probablemente necesitemos observar los 
#datos en una escala logarítmica.
express.line(data_frame=df, x='Date', y=['Open', 'High', 'Low', 'Close'], log_y=True, template = "plotly_dark").show()
express.line(data_frame=df, x='Date', y=['Close', 'Adj Close'], log_y=True, template = "plotly_dark").show()
express.line(data_frame=df, x='Date', y='Volume', log_y=True, template = "plotly_dark").show()

#Nuestros datos de volumen parecen bastante sólidos, pero tenemos algunos días con un volumen anormalmente bajo..
express.scatter(data_frame=df, x='Date', y='Volume', trendline='lowess', log_y=True, color='year', title = "Análisis del volumen en función del tiempo\n", template = "plotly_dark")

#El volumen ha disminuido ligeramente con el tiempo a pesar de que el precio ha aumentado sustancialmente.
express.scatter(data_frame=df, x='Date', y='Adj Close', trendline='lowess', color='year', log_y=True, title = "Análisis del volumen en función del tiempo y el precio\n", template = "plotly_dark")

#Nuestra línea de tendencia de precios es muy suave incluso cuando utilizamos valores de cierre ajustados diariamente.

express.scatter(data_frame=df[df['Volume'] > 2000000], x='Volume', y='Adj Close', color='year', log_x=True, log_y=True, title = "Análisis de la tendencia de precios y valores de cierre ajustados diariamente\n", template = "plotly_dark")

#Aquí hemos filtrado los valores atípicos de volumen y obtenemos casi una torta anual de precios de cierre por año, ya que el precio 
# de las acciones de Samsung ha subido cada vez más incluso cuando el volumen de operaciones ha disminuido.

df.describe()

#Comprobación de valor faltante
df.isnull().sum()

#Transformación de datos
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d') 
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df = df.rename(columns = {'Adj Close': 'Adj'})
df['Adj'] = pd.to_numeric(df['Adj'], errors='coerce')

#Verificación de datos
df.head(3)

#Visualización de datos
num_col = df.select_dtypes(include = ['int64','float64']).columns

#Histograma
f, ax = plt.subplots(3,2, figsize=(15, 15))
ax = ax.flatten()

for index, cols in enumerate(num_col):
    sns.histplot(data= df, x= cols, ax = ax[index],kde=True)
    ax[index].set_title(cols)
    
plt.tight_layout()
plt.show()

f, ax = plt.subplots(3,2, figsize=(20, 20))
ax = ax.flatten()

for index, cols in enumerate(num_col):
    sns.boxplot(data= df, y = cols, ax = ax[index])
    ax[index].set_title(cols)
    
plt.tight_layout()
plt.show() 

#Cambios en el precio más alto
plt.plot(df['Date'], df['High'], label = 'Cambios en el precio más alto de Samsung Electronics', color = 'red')
plt.title('Cambios en el precio más alto de Samsung Electronics\n')
plt.yscale('log')
plt.legend()
plt.show()

#muestran un aumento constante

#Cambios en el volumen
plt.plot(df['Date'], df['Volume'], label = 'Cambios en el volumen de Samsung Electronics',color = 'skyblue')
plt.title('Cambios en el volumen de Samsung Electronics\n')
plt.yscale('log')
plt.legend()
plt.show()

#Cambios en el Rolling del precio más alto (30 días)
df2 = df.copy() 

if 'Date' in df2.columns:
    df2['Date'] = pd.to_datetime(df2['Date'])
    df2.set_index('Date', inplace=True)

df2['Rolling Mean Dev of High'] = df2['High'].rolling(window=30).mean()

plt.plot(df2['Rolling Mean Dev of High'], label='Desviación media móvil de 30 días del máximo', color = 'red')
plt.yscale('log')
plt.title('Desviación media móvil de alto\n')
plt.ylabel('Volumen\n')
plt.show()

#Cambios en el número total de acciones negociadas (30 días)
df2 = df.copy() 

if 'Date' in df2.columns:
    df2['Date'] = pd.to_datetime(df2['Date'])
    df2.set_index('Date', inplace=True)

df2['Rolling Mean Dev of Volume'] = df2['Volume'].rolling(window=30).mean()

plt.plot(df2['Rolling Mean Dev of Volume'], label='Desviación media móvil de 30 días del volumen',color = 'royalblue')
plt.yscale('log')
plt.title('Desviación media móvil del volumen\n')
plt.ylabel('Volumen\n')
plt.show()

#Cambio de volumen por año
df_year = df.groupby('Year').mean()
df_year.plot(kind='bar', y=['Volume'], rot=45, title='Volumen por año\n')
plt.yscale('log')
plt.show()

#Mapa de calor de correlación
sns.heatmap(df[num_col].corr(),annot=True,cmap='spring')
plt.show()

#Modelado
#Utilizamos la regresión para predecir
df = df.dropna()
X = df[['Open', 'High', 'Low', 'Adj','Volume']]
Y = df['Close']
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

RF = RandomForestRegressor(random_state=42)
RF.fit(X_train,Y_train)

pred_RF = RF.predict(X_test)
print(f'MAE : {mean_absolute_error(Y_test,pred_RF)}')
print(f'MSE : {mean_squared_error(Y_test,pred_RF)}')
print(f'Puntuación r2 : {r2_score(Y_test,pred_RF)}')

LR = LinearRegression()
LR.fit(X_train,Y_train)

pred_LR = LR.predict(X_test)
print(f'MAE : {mean_absolute_error(Y_test,pred_LR)}')
print(f'MSE : {mean_squared_error(Y_test,pred_LR)}')
print(f'Puntuación r2 : {r2_score(Y_test,pred_LR)}')
