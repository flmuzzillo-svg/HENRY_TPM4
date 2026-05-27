# 🚀 Quick Start - Neo Labs Web Interface

## 60 segundos para tener la interfaz funcionando

### Paso 1: Clonar y Configurar (20 seg)

```bash
cd Auto_MultAgent_Cont_Comp-Engine_OPENROUTER
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install "uvicorn[standard]"
```

### Paso 2: Configurar Variables de Entorno (20 seg)

```bash
copy .env.example .env
```

Editar `.env` y agregar:
```
OPENROUTER_API_KEY=tu_clave_aqui
LANGFUSE_PUBLIC_KEY=tu_clave_aqui
LANGFUSE_SECRET_KEY=tu_clave_aqui
LLM_MODEL=openai/gpt-4o-mini
VISION_MODEL=openai/gpt-4o
```

### Paso 3: Ejecutar (20 seg)

```bash
uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
```

### Paso 4: Abrir en Navegador

```
http://127.0.0.1:8000/
```

---

## 👀 Qué Verás

```
┌─────────────────────────────────────────────────────┐
│  ◆ Neo Labs | Fusión Orgánica Premium              │  ← Header Verde
├─────────────────────────────────────────────────────┤
│                                                     │
│  🎯 Análisis Inteligente de Contratos              │  ← Gancho
│  Automatización de Auditoría Legal con IA          │
│                                                     │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐   │
│  │ 🔍 Análisis│  │ ⚡ Velocidad│  │ 🛡️ Precisión│   │  ← Descubrimiento
│  │ Profundo   │  │ Extrema    │  │ Legal      │   │
│  └────────────┘  └────────────┘  └────────────┘   │
│                                                     │
│  ◆ Envía tus Contratos                            │  ← Formulario (CTA)
│  📄 Original: [Haz clic / Arrastra]               │
│  📄 Enmienda: [Haz clic / Arrastra]               │
│  [🚀 Analizar Ahora]  [↻ Limpiar]                │
│                                                     │
│  (Los resultados aparecen aquí abajo con          │
│   detalles, riesgos y cambios detectados)         │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 🎨 Paleta Visual

| Elemento | Color | Código |
|----------|-------|--------|
| Headers, botones | Verde Bosque | #2D5016 |
| Acentos, bordes | Oro Metálico | #D4AF37 |
| Fondos | Blanco Nieve | #F8F9FA |
| Texto | Gris Grafito | #2C3E50 |

---

## 📁 Archivos Importantes

```
Auto_MultAgent_Cont_Comp-Engine_OPENROUTER/
├── src/api/templates/upload.html      ← Interfaz (HTML+CSS+JS)
├── src/api/main.py                    ← Backend FastAPI
├── DESIGN_SYSTEM.md                   ← Guía de diseño completa
├── WEB_UI_GUIDE.md                    ← Documentación de interfaz
├── COLOR_PALETTE_REFERENCE.md         ← Paleta de colores
└── README.md                          ← Documentación general
```

---

## 🎯 Características Principales

✅ **Interfaz Profesional**: Diseño moderno con paleta estratégica  
✅ **Drag-and-Drop**: Sube archivos de forma intuitiva  
✅ **Análisis en Vivo**: Resultados procesados por IA  
✅ **Visualización Clara**: Cambios organizados con badges de riesgo  
✅ **Responsive**: Funciona en desktop, tablet y mobile  
✅ **Accesible**: WCAG AA compliance  

---

## 🔧 Troubleshooting

| Problema | Solución |
|----------|----------|
| Página en blanco | `Ctrl+F5` o revisar console (F12) |
| 404 Not Found | Puerto 8000 ocupado, usar `--port 8001` |
| Estilos rotos | Limpiar cache del navegador |
| Upload lento | Archivos grandes, máximo 10MB recomendado |
| Error de API | Verificar OPENROUTER_API_KEY en .env |

---

## 📚 Documentación Completa

Para entender la arquitectura, componentes, y personalización:

1. **DESIGN_SYSTEM.md** - Sistema de diseño completo
2. **WEB_UI_GUIDE.md** - Guía técnica de la interfaz
3. **COLOR_PALETTE_REFERENCE.md** - Referencia de colores
4. **README.md** - Documentación del proyecto

---

**¿Necesitas ayuda?** Revisa los archivos `*.md` en la raíz del proyecto.

**Última actualización**: 2026-05-27  
**Versión**: 1.0 ✅
