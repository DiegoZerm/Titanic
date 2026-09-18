# Análisis exploratorio del dataset Titanic

Proyecto académico de análisis exploratorio de datos utilizando el dataset **Titanic**.

El proyecto se realiza exclusivamente con Python y análisis estadístico/descriptivo. **No se utiliza ningún modelo de Machine Learning.**

## Objetivo

Explorar las características de los pasajeros del Titanic e identificar patrones descriptivos relacionados con la supervivencia.

El análisis incluye:

- Exploración inicial del dataset.
- Número de registros y columnas.
- Tipos de variables.
- Valores faltantes.
- Registros duplicados.
- Estadísticas descriptivas.
- Tratamiento de valores faltantes.
- Transformación de variables.
- Creación de nuevas variables.
- Análisis de supervivencia.
- Visualizaciones.
- Conclusiones descriptivas.

## Estructura del proyecto

```text
Titanic/
├── data/
│   └── dataset.csv
├── resultados/
│   └── (gráficas generadas automáticamente)
├── analisis_titanic.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Dataset

El archivo utilizado es:

```text
data/dataset.csv
```

Debe conservar ese nombre y ubicación para que el script pueda encontrarlo automáticamente.

El dataset corresponde al conjunto de entrenamiento del Titanic utilizado habitualmente en Kaggle.

## Variables analizadas

Entre las variables originales se encuentran:

- `PassengerId`
- `Survived`
- `Pclass`
- `Name`
- `Sex`
- `Age`
- `SibSp`
- `Parch`
- `Ticket`
- `Fare`
- `Cabin`
- `Embarked`

Durante el análisis se crean las siguientes variables:

- `FamilySize`: tamaño de la familia del pasajero.
- `IsAlone`: indica si el pasajero viajaba solo.
- `AgeGroup`: categoría de edad.
- `HasCabin`: indica si existía información de cabina.

## Tratamiento de valores faltantes

### Age

Los valores faltantes de `Age` se reemplazan utilizando la **mediana** de la columna. La mediana permite realizar la imputación sin verse tan afectada por valores extremos.

### Cabin

La columna `Cabin` presenta una gran cantidad de valores faltantes. Para conservar la información disponible, se crea `HasCabin`, que indica si existe un registro de cabina, y posteriormente se elimina `Cabin`.

### Embarked

Los pocos valores faltantes de `Embarked` se reemplazan utilizando la **moda**, es decir, la categoría más frecuente.

## Nuevas variables

### FamilySize

```text
FamilySize = SibSp + Parch + 1
```

Representa el tamaño de la familia considerando al pasajero.

### IsAlone

Toma el valor:

- `1`: viajaba solo.
- `0`: viajaba acompañado.

### AgeGroup

Las edades se agrupan en:

- Niño: menor de 13 años.
- Joven: de 13 a 17 años.
- Adulto: de 18 a 59 años.
- Adulto mayor: 60 años o más.

### HasCabin

Indica:

- `1`: existe información de cabina.
- `0`: no existe información de cabina.

## Análisis realizados

El script realiza, entre otros, los siguientes análisis:

1. Tasa de supervivencia general.
2. Supervivencia por sexo.
3. Supervivencia por clase.
4. Supervivencia por grupo de edad.
5. Supervivencia según si viajaba solo o acompañado.
6. Comparación de tarifas promedio y medianas según supervivencia.

## Visualizaciones

Al ejecutar el programa se generan automáticamente cuatro gráficas:

```text
resultados/
├── 01_supervivencia_general.png
├── 02_supervivencia_por_sexo.png
├── 03_supervivencia_por_clase.png
└── 04_supervivencia_por_edad.png
```

Las gráficas se generan utilizando **Matplotlib**.

## Instalación

Se recomienda utilizar un entorno virtual de Python.

### 1. Crear el entorno virtual

```bash
python3 -m venv .venv
```

### 2. Activarlo

En Linux/macOS:

```bash
source .venv/bin/activate
```

En Windows:

```powershell
.venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecución

Desde la carpeta raíz del proyecto:

```bash
python analisis_titanic.py
```

El programa mostrará los resultados en la terminal y guardará las visualizaciones en la carpeta `resultados/`.

## Conclusiones

Las conclusiones se generan directamente a partir de los resultados obtenidos en el dataset.

El análisis permite observar diferencias en las tasas de supervivencia según variables como sexo, clase, grupo de edad y condición de viaje solo o acompañado.

Estas observaciones representan asociaciones descriptivas dentro del dataset y **no deben interpretarse como relaciones causales**.

## Nota

Este proyecto corresponde a un análisis exploratorio y descriptivo. **No contiene modelos de Machine Learning.**
