"""
Análisis exploratorio del dataset Titanic.

Requisitos:
    pip install -r requirements.txt

Ejecución:
    python analisis_titanic.py

El script no utiliza modelos de Machine Learning.
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# -------------------------------------------------------------------
# Configuración
# -------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "dataset.csv"
OUTPUT_DIR = BASE_DIR / "resultados"

OUTPUT_DIR.mkdir(exist_ok=True)


# -------------------------------------------------------------------
# Funciones auxiliares
# -------------------------------------------------------------------

def encabezado(texto):
    print("\n" + "=" * 70)
    print(texto)
    print("=" * 70)


def porcentaje(valor):
    return f"{valor:.2f}%"


# -------------------------------------------------------------------
# Carga de datos
# -------------------------------------------------------------------

encabezado("1. CARGA DEL DATASET")

if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"No se encontró el archivo: {DATA_PATH}\n"
        "Coloca dataset.csv dentro de la carpeta data/."
    )

df = pd.read_csv(DATA_PATH)

print(f"Filas: {df.shape[0]}")
print(f"Columnas: {df.shape[1]}")


# -------------------------------------------------------------------
# Exploración inicial
# -------------------------------------------------------------------

encabezado("2. EXPLORACIÓN INICIAL")

print("\nColumnas:")
print(df.columns.tolist())

print("\nTipos de datos:")
print(df.dtypes)

print("\nValores faltantes:")
print(df.isnull().sum())

print(f"\nRegistros duplicados: {df.duplicated().sum()}")

print("\nEstadísticas descriptivas:")
print(df.describe(include="all").transpose())


# -------------------------------------------------------------------
# Tratamiento de valores faltantes
# -------------------------------------------------------------------

encabezado("3. TRATAMIENTO DE VALORES FALTANTES")

print("Valores faltantes antes del tratamiento:")
print(df.isnull().sum())

# Age:
# Se utiliza la mediana porque es una medida robusta ante valores extremos.
age_median = df["Age"].median()
df["Age"] = df["Age"].fillna(age_median)

# Cabin:
# La columna tiene una gran cantidad de valores faltantes.
# En lugar de eliminar información completamente, se conserva la
# indicación de si el pasajero tenía una cabina registrada.
df["HasCabin"] = df["Cabin"].notna().astype(int)
df = df.drop(columns=["Cabin"])

# Embarked:
# Solo existen dos valores faltantes, por lo que se utiliza la moda.
embarked_mode = df["Embarked"].mode()[0]
df["Embarked"] = df["Embarked"].fillna(embarked_mode)

print("\nValores utilizados:")
print(f"Mediana de Age: {age_median}")
print(f"Moda de Embarked: {embarked_mode}")

print("\nValores faltantes después del tratamiento:")
print(df.isnull().sum())


# -------------------------------------------------------------------
# Transformaciones y nuevas variables
# -------------------------------------------------------------------

encabezado("4. TRANSFORMACIONES Y NUEVAS VARIABLES")

# Tamaño de la familia: pasajero + hermanos/cónyuges + padres/hijos.
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# Indicador de si viajaba solo.
df["IsAlone"] = np.where(df["FamilySize"] == 1, 1, 0)

# Categorías de edad.
def clasificar_edad(edad):
    if edad < 13:
        return "Niño"
    elif edad < 18:
        return "Joven"
    elif edad < 60:
        return "Adulto"
    return "Adulto mayor"


df["AgeGroup"] = df["Age"].apply(clasificar_edad)

print("\nNuevas variables:")
print("- FamilySize")
print("- IsAlone")
print("- AgeGroup")
print("- HasCabin")

print("\nPrimeros registros transformados:")
print(df.head())


# -------------------------------------------------------------------
# Análisis 1: supervivencia general
# -------------------------------------------------------------------

encabezado("5. ANÁLISIS DE SUPERVIVENCIA GENERAL")

survival_rate = df["Survived"].mean() * 100

print(f"Pasajeros analizados: {len(df)}")
print(f"Sobrevivientes: {df['Survived'].sum()}")
print(f"Tasa de supervivencia: {porcentaje(survival_rate)}")


# -------------------------------------------------------------------
# Análisis 2: supervivencia por sexo
# -------------------------------------------------------------------

encabezado("6. SUPERVIVENCIA POR SEXO")

survival_by_sex = (
    df.groupby("Sex")["Survived"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

print(survival_by_sex.map(porcentaje))


# -------------------------------------------------------------------
# Análisis 3: supervivencia por clase
# -------------------------------------------------------------------

encabezado("7. SUPERVIVENCIA POR CLASE")

survival_by_class = (
    df.groupby("Pclass")["Survived"]
    .mean()
    .mul(100)
)

print(survival_by_class.map(porcentaje))


# -------------------------------------------------------------------
# Análisis 4: supervivencia por grupo de edad
# -------------------------------------------------------------------

encabezado("8. SUPERVIVENCIA POR GRUPO DE EDAD")

age_order = ["Niño", "Joven", "Adulto", "Adulto mayor"]

survival_by_age = (
    df.groupby("AgeGroup", observed=False)["Survived"]
    .mean()
    .mul(100)
    .reindex(age_order)
)

print(survival_by_age.map(porcentaje))


# -------------------------------------------------------------------
# Análisis adicional: solo vs acompañado
# -------------------------------------------------------------------

encabezado("9. SUPERVIVENCIA SEGÚN SI VIAJABA SOLO O ACOMPAÑADO")

alone_labels = {0: "Acompañado", 1: "Solo"}

survival_by_alone = (
    df.groupby("IsAlone")["Survived"]
    .mean()
    .mul(100)
)

survival_by_alone.index = survival_by_alone.index.map(alone_labels)

print(survival_by_alone.map(porcentaje))


# -------------------------------------------------------------------
# Análisis adicional: tarifa
# -------------------------------------------------------------------

encabezado("10. ANÁLISIS DE TARIFA")

print("Tarifa promedio por supervivencia:")
print(df.groupby("Survived")["Fare"].mean())

print("\nTarifa mediana por supervivencia:")
print(df.groupby("Survived")["Fare"].median())


# -------------------------------------------------------------------
# Visualizaciones
# -------------------------------------------------------------------

encabezado("11. GENERACIÓN DE VISUALIZACIONES")

# 1. Supervivencia general
counts = df["Survived"].value_counts().reindex([0, 1], fill_value=0)

plt.figure(figsize=(7, 5))
plt.bar(["No sobrevivió", "Sobrevivió"], counts.values)
plt.title("Supervivencia general")
plt.ylabel("Número de pasajeros")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "01_supervivencia_general.png", dpi=150)
plt.close()

# 2. Supervivencia por sexo
plt.figure(figsize=(7, 5))
plt.bar(survival_by_sex.index, survival_by_sex.values)
plt.title("Tasa de supervivencia por sexo")
plt.ylabel("Supervivencia (%)")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "02_supervivencia_por_sexo.png", dpi=150)
plt.close()

# 3. Supervivencia por clase
plt.figure(figsize=(7, 5))
plt.bar(survival_by_class.index.astype(str), survival_by_class.values)
plt.title("Tasa de supervivencia por clase")
plt.xlabel("Clase")
plt.ylabel("Supervivencia (%)")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "03_supervivencia_por_clase.png", dpi=150)
plt.close()

# 4. Supervivencia por grupo de edad
valid_age = survival_by_age.dropna()

plt.figure(figsize=(8, 5))
plt.bar(valid_age.index, valid_age.values)
plt.title("Tasa de supervivencia por grupo de edad")
plt.ylabel("Supervivencia (%)")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "04_supervivencia_por_edad.png", dpi=150)
plt.close()

print(f"Visualizaciones guardadas en: {OUTPUT_DIR}")


# -------------------------------------------------------------------
# Conclusiones
# -------------------------------------------------------------------

encabezado("12. CONCLUSIONES")

highest_sex = survival_by_sex.idxmax()
highest_class = survival_by_class.idxmax()
highest_age = valid_age.idxmax()

print(
    f"1. La tasa de supervivencia general fue de "
    f"{survival_rate:.2f}%."
)

print(
    f"2. En este dataset, la categoría de sexo con mayor tasa de "
    f"supervivencia fue {highest_sex}."
)

print(
    f"3. La clase con mayor tasa de supervivencia fue la clase "
    f"{highest_class}."
)

print(
    f"4. Entre los grupos de edad definidos, {highest_age} presentó "
    f"la mayor tasa de supervivencia."
)

print(
    "5. Los pasajeros que viajaban solos y acompañados presentaron "
    "diferencias en sus tasas de supervivencia."
)

print(
    "\nEstas conclusiones describen asociaciones observadas en el "
    "dataset y no implican causalidad. No se utilizó ningún modelo "
    "de Machine Learning."
)

print("\nAnálisis terminado correctamente.")
