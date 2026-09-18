# Análisis Exploratorio: Pasajeros del Titanic

## Objetivo
Realizar un análisis exploratorio y preprocesamiento del dataset del Titanic para identificar
características asociadas con la supervivencia, cumpliendo con los requisitos de la práctica.

## Dataset
- **Archivo:** `data/dataset.csv`
- **Pasajeros:** 891 del RMS Titanic
- **Fuente:** Kaggle Titanic Competition
- **Variables:** 12 columnas (PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked)

## Estructura de la Práctica
Este notebook sigue la estructura de celdas alternadas: Markdown - Código - Markdown - Código, etc.

## Outputs y Explicaciones

### Celda 2: Carga y Exploración
**Output:**
- Número de pasajeros: 891
- Columnas del dataset: 12
- Variables disponibles: PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked

**Explicación:** Se carga el dataset y se muestra la información básica para comprender la estructura de los datos.

### Celda 4: Preprocesamiento
**Output:**
- FamilySize promedio: 1.9

**Explicación:** Se creó la variable `FamilySize` sumando SibSp (hermanos/esposos) + Parch (padres/hijos) + 1. El promedio de 1.9 indica que la mayoría de los pasajeros viajaban con 1-2 familiares.

### Celda 5: Results & Outputs
**Outputs explicados:**
- **Output de la celda 2:** Estructura básica del dataset (891 pasajeros, 12 variables)
- **Output de la celda 4:** FamilySize promedio calculado (1.9), variable creada exitosamente

**Explicación:** Estos outputs demuestran que el preprocesamiento fue exitoso y las nuevas variables están listas para el análisis.

## Visualizaciones Generadas

Se guardaron 3 gráficas en la carpeta `outputs/resultados/`:

1. **`supervivencia_genero.png`** - Supervivencia por género
   - **Resultado:** Mujeres tuvieron 74% de supervivencia vs 19% de hombres

2. **`supervivencia_clase.png`** - Supervivencia por clase
   - **Resultado:** Clase 1: 63%, Clase 2: 47%, Clase 3: 24%

3. **`supervivencia_edad.png`** - Supervivencia por edad
   - **Resultado:** Categorías Niño/Joven/Adulto/Adulto mayor

## Requisitos
- Python 3.x
- Bibliotecas: pandas, numpy, matplotlib, seaborn (ver `requirements.txt`)

## Instalación
1. Clonar repositorio: `git clone https://github.com/DiegoZerm/Titanic`
2. Entorno virtual: `python -m venv .venv`
3. Activar e instalar: `source .venv/bin/activate` y `pip install -r requirements.txt`

## Ejecución
Abrir notebook: `jupyter lab` y ejecutar las celdas en orden.