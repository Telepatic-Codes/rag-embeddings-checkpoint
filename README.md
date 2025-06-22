# 🧠 Aprendiendo Embeddings y Similitud Semántica

Este proyecto te ayudará a entender los conceptos fundamentales de embeddings y similitud semántica en el contexto de sistemas RAG (Retrieval-Augmented Generation).

## 📋 Conceptos que Aprenderás

### ¿Qué son los Embeddings?
Los **embeddings** son representaciones numéricas de texto que capturan su significado semántico. Imagina que cada palabra o frase se convierte en un punto en un espacio multidimensional donde textos similares están cerca entre sí.

### ¿Qué es la Similitud Semántica?
La **similitud semántica** mide qué tan parecidos son dos textos en términos de significado, no solo de palabras exactas. Por ejemplo, "gato feliz" y "felino contento" son semánticamente similares aunque usen palabras diferentes.

## 🚀 Configuración Inicial

### 1. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 2. Configurar API Key
1. Crea un archivo llamado `.env` en la raíz del proyecto
2. Agrega tu API key de OpenAI:
```
OPENAI_API_KEY=tu_api_key_aqui
```
3. Puedes obtener una API key gratuita en: https://platform.openai.com/api-keys

### 3. Ejecutar el Script
```bash
python scratch_embeddings.py
```

## 📊 ¿Qué Verás?

El script generará:
- **Embeddings**: Vectores numéricos para cada texto
- **Matriz de Similitud**: Una tabla que muestra qué tan parecidos son los textos entre sí
- **Explicaciones**: Comentarios que te ayudan a entender cada paso

## 🎯 Ejercicios de Práctica

1. **Modifica los textos**: Cambia las frases en la lista `texts` y observa cómo cambia la similitud
2. **Agrega más frases**: Experimenta con diferentes tipos de texto
3. **Compara resultados**: Prueba frases similares vs diferentes

## 🔍 Conceptos Clave

- **`embed_query()`**: Función que convierte texto en vectores numéricos
- **`cosine_similarity()`**: Función que calcula la similitud entre vectores (0-1)
- **Vector**: Lista de números que representa el significado del texto
- **Semántica**: El significado de las palabras, no solo su forma

¡Disfruta aprendiendo sobre embeddings! 🎉 