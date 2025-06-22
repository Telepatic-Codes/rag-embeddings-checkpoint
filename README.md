# 🧠 RAG System V1 - Aprendiendo Embeddings y Similitud Semántica

Un proyecto educativo para aprender los fundamentos de los sistemas RAG (Retrieval-Augmented Generation) a través de embeddings y similitud semántica.

## 🎯 Objetivo del Proyecto

Este proyecto te guía paso a paso para entender:
- **Embeddings**: Representaciones numéricas del texto
- **Similitud Semántica**: Cómo medir qué tan parecidos son dos textos
- **Sistemas RAG**: Base para construir sistemas de IA que recuperan información relevante

## 📁 Estructura del Proyecto

```
RAG System V1/
├── embeddings_simple.py      # Script principal con embeddings reales de OpenAI
├── test_embeddings.py        # Versión de prueba sin API key
├── scratch_embeddings.py     # Versión con langchain (experimental)
├── requirements.txt          # Dependencias del proyecto
├── .env                      # Configuración de API key (no subido a Git)
└── README.md                 # Este archivo
```

## 🚀 Configuración Rápida

### 1. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 2. Configurar API Key de OpenAI
1. Crea un archivo `.env` en la raíz del proyecto
2. Agrega tu API key:
```
OPENAI_API_KEY=sk-tu_clave_aqui
```
3. Obtén una API key gratuita en: https://platform.openai.com/api-keys

### 3. Ejecutar el Script
```bash
python embeddings_simple.py
```

## 📊 Ejemplo de Salida

```
🧠 GENERANDO EMBEDDINGS REALES CON OPENAI
==================================================
Textos a procesar: ['hola mundo', 'perro feliz', 'limón verde', 'gato contento', 'casa grande']

Generando embeddings...
✅ Texto 1: 'hola mundo' -> Vector de 1536 dimensiones
✅ Texto 2: 'perro feliz' -> Vector de 1536 dimensiones
✅ Texto 3: 'limón verde' -> Vector de 1536 dimensiones
✅ Texto 4: 'gato contento' -> Vector de 1536 dimensiones
✅ Texto 5: 'casa grande' -> Vector de 1536 dimensiones

🔍 CALCULANDO SIMILITUD SEMÁNTICA
========================================
Matriz de similitud (coseno):
            hola mundo perro feliz limón verdegato contento casa grande
  hola mundo       1.000       0.367       0.256       0.359       0.264
 perro feliz       0.367       1.000       0.237       0.572       0.242
 limón verde       0.256       0.237       1.000       0.291       0.233
gato contento       0.359       0.572       0.291       1.000       0.308
 casa grande       0.264       0.242       0.233       0.308       1.000

🎯 PARES MÁS SIMILARES:
   'perro feliz' y 'gato contento' (0.572)
```

## 🧠 Conceptos Clave Aprendidos

### ¿Qué son los Embeddings?
Los embeddings son **vectores numéricos** que representan el significado del texto. Cada palabra o frase se convierte en un punto en un espacio multidimensional donde textos similares están cerca entre sí.

**Ejemplo:**
- "gato" → [0.2, -0.1, 0.8, ...] (vector de 1536 números)
- "felino" → [0.19, -0.12, 0.79, ...] (vector muy similar)
- "casa" → [-0.5, 0.3, -0.2, ...] (vector muy diferente)

### ¿Qué es la Similitud Semántica?
Mide qué tan parecidos son dos textos en **significado**, no solo en palabras exactas.

**Ejemplos:**
- "El gato está feliz" vs "El felino está contento" → **Alta similitud** (mismo significado)
- "El gato está feliz" vs "La casa es grande" → **Baja similitud** (significados diferentes)

### ¿Qué es la Similitud Coseno?
Una **métrica matemática** que mide qué tan parecidos son dos vectores:
- **1.000**: Vectores idénticos
- **0.000**: Vectores completamente diferentes
- **0.500**: Vectores moderadamente similares

## 🔧 Scripts Disponibles

### `embeddings_simple.py` (Recomendado)
- ✅ Usa embeddings reales de OpenAI
- ✅ 1536 dimensiones de precisión
- ✅ Captura significado semántico profundo
- ✅ Requiere API key de OpenAI

### `test_embeddings.py` (Para Pruebas)
- ✅ No requiere API key
- ✅ Simulación de embeddings
- ✅ Perfecto para entender conceptos
- ✅ 5 dimensiones simplificadas

### `scratch_embeddings.py` (Experimental)
- ⚠️ Usa langchain (puede tener problemas de compatibilidad)
- ✅ Más funcionalidades avanzadas
- ⚠️ Requiere configuración adicional

## 🎯 Ejercicios de Práctica

1. **Modifica los textos**: Cambia las frases en la lista `texts` y observa cómo cambia la similitud
2. **Agrega más frases**: Experimenta con diferentes tipos de texto
3. **Compara resultados**: Prueba frases similares vs diferentes
4. **Analiza patrones**: ¿Por qué algunos textos son más similares que otros?

## 🔒 Seguridad y Buenas Prácticas

- ✅ El archivo `.env` está en `.gitignore` (no se sube a GitHub)
- ✅ Nunca compartas tu API key públicamente
- ✅ Usa variables de entorno para configuraciones sensibles
- ✅ Revisa siempre qué archivos vas a commitear

## 🚀 Próximos Pasos

### Ejercicio 2: Vector Store con Chroma
- Almacenar embeddings en una base de datos vectorial
- Buscar textos similares rápidamente
- Construir un sistema RAG básico

### Ejercicio 3: Sistema RAG Completo
- Integrar embeddings con un modelo de lenguaje
- Crear respuestas basadas en documentos
- Optimizar la recuperación de información

## 🤝 Contribuciones

Este es un proyecto educativo. Si encuentras errores o tienes sugerencias:
1. Abre un Issue en GitHub
2. Propón mejoras en el código
3. Comparte ejemplos interesantes

## 📚 Recursos Adicionales

- [OpenAI Embeddings Documentation](https://platform.openai.com/docs/guides/embeddings)
- [Similitud Coseno - Wikipedia](https://es.wikipedia.org/wiki/Similitud_coseno)
- [Sistemas RAG - Conceptos](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)

---

**¡Disfruta aprendiendo sobre embeddings y sistemas RAG! 🎉**

*Proyecto creado para aprender los fundamentos de IA y procesamiento de lenguaje natural.* 