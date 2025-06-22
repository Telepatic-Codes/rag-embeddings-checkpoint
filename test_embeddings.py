# test_embeddings.py
# Versión de prueba que no requiere API key
# Te muestra cómo funcionan los embeddings y la similitud semántica

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

print("🧠 APRENDIENDO SOBRE EMBEDDINGS Y SIMILITUD SEMÁNTICA")
print("=" * 60)
print()

# Simulamos embeddings para diferentes textos
# En la realidad, estos vectores serían generados por el modelo de OpenAI
print("📊 SIMULACIÓN DE EMBEDDINGS")
print("Los embeddings son vectores numéricos que representan el significado del texto")
print()

# Textos de ejemplo
texts = [
    "hola mundo",      # Saludo básico
    "perro feliz",     # Animal con emoción  
    "limón verde",     # Fruta con color
    "gato contento",   # Animal con emoción (similar a perro feliz)
    "casa grande",     # Objeto con tamaño (diferente a los anteriores)
]

# Simulamos embeddings (vectores de 5 dimensiones para simplificar)
# En la realidad, los embeddings de OpenAI tienen 1536 dimensiones
mock_embeddings = [
    [0.1, 0.2, 0.3, 0.1, 0.1],  # hola mundo
    [0.8, 0.9, 0.1, 0.2, 0.1],  # perro feliz
    [0.1, 0.1, 0.8, 0.9, 0.2],  # limón verde
    [0.7, 0.8, 0.2, 0.3, 0.1],  # gato contento (similar a perro feliz)
    [0.2, 0.1, 0.1, 0.1, 0.9],  # casa grande (diferente)
]

print("Textos procesados:")
for i, text in enumerate(texts):
    print(f"  {i+1}. '{text}' -> Vector: {mock_embeddings[i]}")
print()

# Calculamos la matriz de similitud
print("🔍 CALCULANDO SIMILITUD SEMÁNTICA")
print("La similitud coseno mide qué tan parecidos son dos vectores (0-1)")
print()

sim_matrix = cosine_similarity(np.array(mock_embeddings))

# Mostramos la matriz de forma clara
print("Matriz de similitud (coseno):")
print("Valores cercanos a 1 = muy similares")
print("Valores cercanos a 0 = muy diferentes")
print()

# Encabezado
print("          ", end="")
for text in texts:
    print(f"{text:>12}", end="")
print()

# Filas de la matriz
for i, text in enumerate(texts):
    print(f"{text:>12}", end="")
    for j in range(len(texts)):
        similarity = sim_matrix[i][j]
        print(f"{similarity:>12.3f}", end="")
    print()

print()
print("📈 ANÁLISIS DE RESULTADOS")
print("=" * 40)

# Encontramos las similitudes más altas (excluyendo la diagonal)
max_similarity = 0
most_similar_pair = None

for i in range(len(texts)):
    for j in range(i+1, len(texts)):  # Solo comparamos pares diferentes
        similarity = sim_matrix[i][j]
        print(f"• '{texts[i]}' vs '{texts[j]}': {similarity:.3f}")
        
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_pair = (texts[i], texts[j])

print()
print(f"🎯 PARES MÁS SIMILARES:")
print(f"   '{most_similar_pair[0]}' y '{most_similar_pair[1]}' ({max_similarity:.3f})")
print()

print("💡 CONCEPTOS CLAVE:")
print("• Los embeddings capturan el significado, no solo palabras exactas")
print("• Textos con significado similar tienen embeddings similares")
print("• La similitud coseno mide el ángulo entre vectores")
print("• Valores cercanos a 1 = muy similares, cercanos a 0 = muy diferentes")
print()

print("🚀 PRÓXIMO PASO:")
print("Para usar embeddings reales, necesitas:")
print("1. Una API key de OpenAI")
print("2. Configurar el archivo .env")
print("3. Ejecutar scratch_embeddings.py") 