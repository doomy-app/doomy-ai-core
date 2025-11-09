# 🏠 DOOMY AI CORE

<p align="center">
  <img src="https://raw.githubusercontent.com/iadoomy/assets/main/doomy_logo.png" alt="Doomy Logo" width="220"/>
</p>

### 💡 Núcleo Inteligente del Asistente Inmobiliario Doomy  
**Versión:** 1.0.0  
**Autor:** [@iadoomy](https://github.com/iadoomy)  
**Modelo:** GPT-5 Mini (OpenAI API)  

---

## 🚀 Descripción
**Doomy AI Core** es la base del ecosistema **Doomy**, un asistente de inteligencia artificial diseñado para automatizar todo el proceso de compra, venta y verificación de vivienda social (INFONAVIT, FOVISSSTE, etc.) sin intervención humana.

El sistema permite:
- Asesoría inmobiliaria automática  
- Simuladores de crédito  
- Verificación documental (IA)  
- Edición inteligente de imágenes  
- Generación de contratos y documentos legales  

---

## ⚙️ Instalación rápida  

```bash
git clone https://github.com/iadoomy/doomy-ai-core.git
cd doomy-ai-core
pip install -r requirements.txt
cp .env.example .env
```

Agrega tu clave OpenAI:  
```
OPENAI_API_KEY=tu_clave
OPENAI_MODEL=gpt-5-mini
```

Ejecuta el asistente:  
```bash
python main.py
```

---

## ☁️ Conexión con Oracle Cloud (Visual Builder + Autonomous DB)

1. **Conéctate a Visual Builder Studio**  
   - Crea un proyecto “Doomy”  
   - Conecta tu repo GitHub `https://github.com/iadoomy/doomy-ai-core`  

2. **Agrega un pipeline básico**  
   - Fase 1: Build → Python 3.11  
   - Fase 2: Deploy → Oracle Function / Container Instance  
   - Variables de entorno:  
     ```
     OPENAI_API_KEY=...
     OPENAI_MODEL=gpt-5
     ```

3. **Base de datos**  
   - Usa *Autonomous JSON DB* (free tier)  
   - Crea tabla `properties` y `users`  
   - Conecta vía REST o SDK Python  

---

## 🧩 Arquitectura Modular

| Módulo | Descripción |
|--------|--------------|
| `agent_core.py` | Orquesta todos los roles del agente |
| `property_assistant.py` | Busca y filtra propiedades |
| `document_checker.py` | Revisa documentos con IA |
| `image_editor.py` | Mejora imágenes de casas |
| `legal_helper.py` | Genera contratos y cartas |
| `credit_simulator.py` | Calcula créditos INFONAVIT/FOVISSSTE |

---

## 🧠 Ejemplo de conversación

```
👤 Usuario: Busco casa en Tamazunchale con crédito Infonavit  
🏠 Doomy: Encontré 2 opciones disponibles con rango entre 600 y 800 mil pesos. ¿Deseas que te muestre los detalles?
```

---

## 🔮 Próximos pasos
- Integrar frontend web con Oracle Visual Builder  
- Desarrollar Doomy Chat (React + API REST)  
- Entrenar IA personalizada con datos inmobiliarios  

---

## 🧾 Licencia
MIT © 2025 [iadoomy](https://github.com/iadoomy)
