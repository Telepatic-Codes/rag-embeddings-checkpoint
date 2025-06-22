# embeddings_simple.py
# Versión simplificada que usa OpenAI directamente
# Te muestra embeddings reales de OpenAI

import os
from dotenv import load_dotenv
import openai
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Carga tu API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print(f"🔑 API Key encontrada: {api_key[:20]}..." if api_key else "❌ No se encontró API key")

if not api_key:
    print("❌ Error: No se encontró la API key en el archivo .env")
    print("Asegúrate de que el archivo .env contenga: OPENAI_API_KEY=tu_clave_aqui")
    exit(1)

openai.api_key = api_key

# Frases de prueba
texts = [
    "hola mundo",      # Saludo básico
    "perro feliz",     # Animal con emoción
    "limón verde",     # Fruta con color
    "gato contento",   # Animal con emoción (similar a perro feliz)
    "casa grande",     # Objeto con tamaño (diferente)
]

print("🧠 GENERANDO EMBEDDINGS REALES CON OPENAI")
print("=" * 50)
print(f"Textos a procesar: {texts}")
print()

# Genera embeddings usando OpenAI directamente
print("Generando embeddings...")
vectors = []

for i, text in enumerate(texts):
    try:
        print(f"Procesando: '{text}'...")
        # Usa el modelo text-embedding-3-small de OpenAI
        response = openai.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        vector = response.data[0].embedding
        vectors.append(vector)
        print(f"✅ Texto {i+1}: '{text}' -> Vector de {len(vector)} dimensiones")
    except Exception as e:
        print(f"❌ Error con '{text}': {e}")
        print(f"Tipo de error: {type(e).__name__}")
        break

if vectors:
    print()
    print("🔍 CALCULANDO SIMILITUD SEMÁNTICA")
    print("=" * 40)
    
    # Calcula matriz de similitud
    sim_matrix = cosine_similarity(np.array(vectors))
    
    # Muestra resultados
    print("Matriz de similitud (coseno):")
    print("Valores cercanos a 1 = muy similares")
    print("Valores cercanos a 0 = muy diferentes")
    print()
    
    # Encabezado
    print("          ", end="")
    for text in texts[:len(vectors)]:
        print(f"{text:>12}", end="")
    print()
    
    # Filas de la matriz
    for i, text in enumerate(texts[:len(vectors)]):
        print(f"{text:>12}", end="")
        for j in range(len(vectors)):
            similarity = sim_matrix[i][j]
            print(f"{similarity:>12.3f}", end="")
        print()
    
    print()
    print("📈 ANÁLISIS DE RESULTADOS")
    print("=" * 30)
    
    # Encuentra las similitudes más altas
    max_similarity = 0
    most_similar_pair = None
    
    for i in range(len(vectors)):
        for j in range(i+1, len(vectors)):
            similarity = sim_matrix[i][j]
            print(f"• '{texts[i]}' vs '{texts[j]}': {similarity:.3f}")
            
            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_pair = (texts[i], texts[j])
    
    print()
    if most_similar_pair:
        print(f"🎯 PARES MÁS SIMILARES:")
        print(f"   '{most_similar_pair[0]}' y '{most_similar_pair[1]}' ({max_similarity:.3f})")
    
    print()
    print("💡 CONCEPTOS CLAVE:")
    print("• Los embeddings reales de OpenAI tienen 1536 dimensiones")
    print("• Capturan significado semántico profundo")
    print("• Textos similares tienen vectores similares")
    print("• La similitud coseno mide qué tan parecidos son los vectores")

else:
    print("❌ No se pudieron generar embeddings. Verifica tu API key.") 