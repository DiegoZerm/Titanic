# Análisis de Pasajeros del Titanic

## Nombre del Proyecto
Análisis exploratorio y preprocesamiento del dataset del Titanic para identificar características asociadas con la supervivencia.

## Explica brevemente de qué trata
Este proyecto realiza un análisis exploratorio y preprocesamiento del dataset del Titanic, que contiene información de pasajeros del trágico accidente del RMS Titanic. El objetivo es identificar patrones y características asociadas con la supervivencia, realizando limpieza de datos, creación de nuevas variables y análisis estadístico descriptivo.

## Dataset
- **Nombre:** Titanic - Machine Learning from Disaster
- **Fuente:** Kaggle (https://www.kaggle.com/c/titanic)
- **Descripción:** Dataset que contiene información de 892 pasajeros del Titanic, incluyendo datos demográficos, clase del pasaje, información de familia y si sobrevivieron o no el desastre.

## Objetivo
Realizar un análisis exploratorio del dataset Titanic para identificar características asociadas con la supervivencia, realizando el necesario preprocesamiento y limpieza de datos, y presentando conclusiones a partir de los análisis realizados.

## Requisitos
- Python 3.x
- Bibliotecas incluidas en requirements.txt

## Instalación
1. Clonar el repositorio:
   ```
   git clone URL_DEL_REPOSITORIO
   ```
2. Entrar al proyecto:
   ```
   cd titanic-project
   ```
3. Crear el entorno virtual:
   ```
   python -m venv .venv
   ```
4. Activarlo e instalar dependencias:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
   - Luego: `pip install -r requirements.txt`

## Ejecución
python src/analysis.py

## Análisis realizados
- Análisis de valores faltantes en Age, Cabin, Embarked
- Creación de variable FamilySize = SibSp + Parch + 1
- Categorización de edad (Niño, Joven, Adulto, Adulto mayor)
- Análisis de supervivencia por género, clase y edad

## Resultados y conclusiones
[Por completar después del análisis exploratorio]