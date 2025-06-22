# scratch_embeddings.py
# Este archivo te ayudará a aprender sobre embeddings y similitud semántica
# Los embeddings son representaciones numéricas de texto que capturan su significado

import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Carga tu API key desde el archivo .env
# Esto es una buena práctica de seguridad para no exponer claves en el código
load_dotenv()

# Inicializa el modelo de embeddings de OpenAI
# Los embeddings convierten texto en vectores numéricos
emb = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

# Frases de prueba para comparar
# Estas frases nos ayudarán a entender cómo funcionan los embeddings
texts = [
    "hola mundo",      # Saludo básico
    "perro feliz",     # Animal con emoción
    "limón verde",     # Fruta con color
]

print("=== GENERANDO EMBEDDINGS ===")
print(f"Textos a procesar: {texts}")
print()

# Genera embeddings para cada texto
# embed_query convierte cada frase en un vector de números
print("Generando embeddings...")
vectors = []
for i, text in enumerate(texts):
    vector = emb.embed_query(text)
    vectors.append(vector)
    print(f"Texto {i+1}: '{text}' -> Vector de {len(vector)} dimensiones")

print()

# Calcula la matriz de similitud usando similitud coseno
# La similitud coseno mide qué tan parecidos son dos vectores (0-1)
print("=== CALCULANDO SIMILITUD ===")
sim_matrix = cosine_similarity(np.array(vectors))

# Imprime resultados de forma clara
print("Matriz de similitud (coseno):")
print("Valores cercanos a 1 = muy similares")
print("Valores cercanos a 0 = muy diferentes")
print()
print("          ", end="")
for text in texts:
    print(f"{text:>10}", end="")
print()

for i, text in enumerate(texts):
    print(f"{text:>10}", end="")
    for j in range(len(texts)):
        similarity = sim_matrix[i][j]
        print(f"{similarity:>10.3f}", end="")
    print()

print()
print("=== EXPLICACIÓN ===")
print("• La diagonal siempre es 1.000 (cada texto es idéntico a sí mismo)")
print("• Valores más altos indican textos más similares semánticamente")
print("• Los embeddings capturan el significado, no solo palabras exactas") 