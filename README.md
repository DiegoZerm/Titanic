# Análisis Exploratorio del Titanic

Proyecto de análisis exploratorio de datos utilizando el dataset **Titanic — Kaggle**.  
La práctica se enfoca exclusivamente en **limpieza, preprocesamiento, análisis exploratorio y visualización**.

> **Importante:** No se realiza ningún modelo de Machine Learning.

## Fuente de datos

Dataset Titanic — Kaggle:

- https://www.kaggle.com/c/titanic/data

Se utiliza principalmente el archivo `train.csv`.

En este repositorio el archivo se encuentra como:

```text
dataset.csv
```

## Objetivo

Analizar la información disponible de los pasajeros del Titanic para identificar características asociadas con la supervivencia.

El análisis considera variables como:

- Sexo
- Edad
- Clase del pasajero
- Tarifa
- Tamaño de la familia
- Si el pasajero viajaba solo o acompañado
- Puerto de embarque
- Disponibilidad de información de cabina

## Estructura del proyecto

```text
.
├── 01-analisis.ipynb
├── dataset.csv
├── requirements.txt
└── README.md
```

### Archivos

| Archivo | Descripción |
|---|---|
| `01-analisis.ipynb` | Notebook principal con todo el análisis |
| `dataset.csv` | Dataset Titanic utilizado por el notebook |
| `requirements.txt` | Dependencias necesarias para ejecutar el proyecto |
| `README.md` | Documentación del proyecto |

## Requisitos

Se recomienda utilizar:

- Python 3.11 o superior
- Git
- Jupyter Notebook o JupyterLab

El proyecto no requiere Anaconda.

## Clonar el repositorio

Desde una terminal:

```bash
git clone <URL-DE-TU-REPOSITORIO>
```

Después entra a la carpeta:

```bash
cd <NOMBRE-DEL-REPOSITORIO>
```

Por ejemplo:

```bash
git clone https://github.com/TU-USUARIO/titanic-analisis.git
cd titanic-analisis
```

## Crear el entorno virtual

Linux/macOS:

```bash
python3 -m venv .venv
```

Activar el entorno:

```bash
source .venv/bin/activate
```

En Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## Instalar dependencias

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

Las principales librerías utilizadas son:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `jupyter`
- `notebook`

## Ejecutar el notebook

Con el entorno virtual activado, ejecuta:

```bash
jupyter notebook
```

o:

```bash
jupyter lab
```

Después abre:

```text
01-analisis.ipynb
```

### Importante sobre el dataset

El notebook utiliza:

```python
pd.read_csv("dataset.csv")
```

Por lo tanto, `dataset.csv` debe encontrarse en la **misma carpeta que `01-analisis.ipynb`**.

Si el repositorio se clona completo, no es necesario modificar ninguna ruta.

## Contenido del análisis

### 1. Exploración inicial

Se revisa:

- Número de pasajeros
- Número de columnas
- Variables disponibles
- Tipos de datos
- Valores faltantes
- Registros duplicados
- Estadísticas descriptivas

### 2. Valores faltantes

Se analizan especialmente:

#### `Age`

Los valores faltantes se reemplazan utilizando la **mediana** de la variable.

La mediana se utiliza porque es menos sensible a valores extremos que el promedio.

#### `Cabin`

Debido a la gran cantidad de valores faltantes, no se intenta reconstruir una cabina específica.

Se crea:

```text
HasCabin
```

donde:

- `1` = existe información de cabina
- `0` = no existe información de cabina

Después se elimina `Cabin` del dataset utilizado para el análisis.

#### `Embarked`

Los valores faltantes se reemplazan utilizando la **moda** de la variable, debido a que es una variable categórica.

## Variables nuevas

El notebook crea cuatro variables nuevas.

### `FamilySize`

Se calcula mediante:

```text
FamilySize = SibSp + Parch + 1
```

El `+1` representa al propio pasajero.

### `IsAlone`

Indica si el pasajero viajaba solo:

```text
1 = Solo
0 = Acompañado
```

### `AgeGroup`

La edad se agrupa utilizando los siguientes criterios:

| Grupo | Rango |
|---|---|
| Niño | Menor de 13 años |
| Joven | 13 a 17 años |
| Adulto | 18 a 59 años |
| Adulto mayor | 60 años o más |

### `HasCabin`

Indica si el registro original contenía información de cabina:

```text
1 = Sí
0 = No
```

## Análisis realizados

El notebook realiza los siguientes análisis:

1. **Porcentaje de pasajeros que sobrevivió**
2. **Supervivencia según sexo**
3. **Supervivencia según clase del pasajero**
4. **Supervivencia según grupo de edad**
5. **Supervivencia según si el pasajero viajaba solo o acompañado**

## Visualizaciones

Se generan cuatro visualizaciones principales:

1. Supervivencia general
2. Tasa de supervivencia según sexo
3. Tasa de supervivencia según clase
4. Tasa de supervivencia según grupo de edad

Las gráficas se generan directamente desde el notebook utilizando `matplotlib` y `seaborn`.

## Reproducibilidad

Para reproducir el análisis desde cero:

```bash
git clone <URL-DE-TU-REPOSITORIO>
cd <NOMBRE-DEL-REPOSITORIO>

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

jupyter lab
```

Luego abre:

```text
01-analisis.ipynb
```

y ejecuta las celdas en orden.

El proyecto no requiere conexión a una base de datos ni servicios externos para ejecutar el análisis, siempre que `dataset.csv` esté incluido en el repositorio.

## Resultados y conclusiones

El análisis permite observar diferencias descriptivas en la supervivencia de los pasajeros según distintas características.

Entre las variables analizadas se encuentran:

- Sexo
- Clase
- Edad
- Tamaño de familia
- Viajar solo o acompañado

Los resultados corresponden específicamente al conjunto de datos utilizado y permiten realizar comparaciones entre grupos.

> Una diferencia observada entre grupos no implica por sí misma una relación causal.

## Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Machine Learning

Este proyecto **no implementa modelos de Machine Learning**.

El objetivo de la práctica es únicamente:

```text
Limpieza
   ↓
Preprocesamiento
   ↓
Análisis exploratorio
   ↓
Visualización
   ↓
Conclusiones
```
