# Guía de Interfaz Web Neo Labs

## 📋 Resumen Ejecutivo

La interfaz web de Neo Labs presenta un **diseño profesional y responsivo** que comunica autoridad técnica mientras mantiene accesibilidad total. Implementa la "Fusión Orgánica Premium" a través de:

1. ✅ **Paleta cromática estratégica** (Verde Bosque, Oro Metálico, Blanco, Gris)
2. ✅ **Tipografías premium** (IBM Plex Sans, Montserrat)
3. ✅ **Estructura narrativa optimizada** (Gancho → Descubrimiento → CTA)
4. ✅ **Experiencia de usuario moderna** (Drag-and-drop, animaciones, feedback real-time)

---

## 🚀 Inicio Rápido

### Requerimientos
- Python 3.10+
- FastAPI + Uvicorn
- Navegador moderno (Chrome, Firefox, Safari, Edge)

### Instalación

```bash
# 1. Navegar al directorio del proyecto
cd Auto_MultAgent_Cont_Comp-Engine_OPENROUTER

# 2. Crear entorno virtual
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/macOS

# 3. Instalar dependencias
pip install -r requirements.txt
pip install "uvicorn[standard]"

# 4. Configurar variables de entorno
copy .env.example .env
# Editar .env con tus credenciales (OPENROUTER_API_KEY, etc.)
```

### Ejecutar

```bash
uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
```

Acceder a: **http://127.0.0.1:8000/**

---

## 🎨 Flujo Visual y Narrativo

### 1. **Gancho (Hero Section)**

```
┌─────────────────────────────────────┐
│  Neo Labs                           │
│  Fusión Orgánica Premium            │
│                                     │
│  Análisis Inteligente de Contratos  │
│  Automatización de Auditoría Legal  │
│                                     │
│  "Descubre cambios críticos en      │
│   tus contratos al instante..."     │
└─────────────────────────────────────┘
```

**Objetivo**: Captar atención en los primeros 3 segundos.

**Colores**: 
- Fondo: Degradado Blanco → Verde Bosque suave
- Título: Verde Bosque (Montserrat 2.5rem bold)
- Texto: Gris Grafito (IBM Plex Sans)

---

### 2. **Descubrimiento (Discovery Cards)**

```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ 🔍           │  │ ⚡           │  │ 🛡️           │
│              │  │              │  │              │
│ Análisis     │  │ Velocidad    │  │ Precisión    │
│ Profundo     │  │ Extrema      │  │ Legal        │
│              │  │              │  │              │
│ Detección de │  │ Procesa en   │  │ Estructura   │
│ cambios en   │  │ segundos     │  │ validada por │
│ cláusulas... │  │ usando IA... │  │ profesionales│
└──────────────┘  └──────────────┘  └──────────────┘
```

**Objetivo**: Comunicar valor diferenciador.

**Comportamiento**:
- Hover: Elevación (+4px), sombra mejorada
- Borde izquierdo: 4px Oro Metálico
- Transición suave: 0.3s ease

---

### 3. **Llamado a la Acción (Form Section)**

```
┌─────────────────────────────────────┐
│  📋 Envía tus Contratos             │
│                                     │
│  Contrato Original                  │
│  ┌────────────────────────────────┐ │
│  │  Haz clic / Arrastra archivo   │ │
│  │         (JPG, PNG, PDF)        │ │
│  └────────────────────────────────┘ │
│                                     │
│  Documento de Enmienda              │
│  ┌────────────────────────────────┐ │
│  │  Haz clic / Arrastra archivo   │ │
│  │         (JPG, PNG, PDF)        │ │
│  └────────────────────────────────┘ │
│                                     │
│  [🚀 Analizar Ahora]  [↻ Limpiar]  │
└─────────────────────────────────────┘
```

**Objetivo**: Conversión de usuarios.

**Características**:
- ✅ Drag-and-drop soportado
- ✅ Validación de archivo en tiempo real
- ✅ Feedback visual con nombre del archivo
- ✅ Botones de alto contraste

**Botones**:
- Primario (Verde Bosque): Degradado, sombra, hover lift
- Secundario (Oro): Borde, color texto, hover background swap

---

### 4. **Resultados (Results Section)**

```
┌─────────────────────────────────────┐
│  📊 Resultados del Análisis        │
│         [Riesgo: ALTO]   ⚠️         │
│                                     │
│  Total de Cambios: 2                │
│  Evaluación de Riesgo: Alto         │
│                                     │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│                                     │
│  #1 - Cláusula 3.1 — Honorarios    │
│  Tipo: Modificación | Secciones: 3,3.1
│  🔴 Impacto Legal: Alto             │
│                                     │
│  📄 Original: "USD 5.000 mensuales" │
│  ✏️  Modificado: "USD 7.500..."     │
│                                     │
│  📌 Resumen: Se incrementa...       │
│  Temas: Honorarios, Obligaciones    │
│                                     │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│                                     │
│  [... más cambios ...]              │
└─────────────────────────────────────┘
```

**Objetivo**: Presentación clara y profesional de análisis.

**Características**:
- ✅ Resumen executivo con stats
- ✅ Badges de riesgo (Alto/Medio/Bajo)
- ✅ Cards anidados por cambio
- ✅ Animación de aparición suave (slideUp)
- ✅ Código de colores para nivel de riesgo

**Badges de Riesgo**:
| Nivel | Color | Significado |
|-------|-------|-------------|
| Alto | Rojo (#D32F2F) | Requiere revisión urgente |
| Medio | Naranja (#F57F17) | Revisar con atención |
| Bajo | Verde (#388E3C) | Cambio menor |

---

## 🎯 Experiencia Interactiva

### Estados UI

#### 1. **Estado Inicial**
- Formulario vacío
- Sección de resultados oculta
- Sin mensajes de error

#### 2. **Archivo Seleccionado**
- Label actualizado: "✓ [nombre_archivo.jpg]"
- Validación en tiempo real
- Hover feedback en inputs

#### 3. **Procesando**
- Spinner animado
- Texto: "Analizando tus contratos con IA..."
- Botón deshabilitado (visual)
- Mensaje: "Este proceso puede tomar unos segundos"

#### 4. **Éxito**
- Animación slideUp de resultados
- Scroll automático a sección de resultados
- Presentación de hallazgos

#### 5. **Error**
- Mensaje rojo con icono ❌
- Descripción del problema
- Opción de reintentar

### Transiciones y Animaciones

```css
/* Hover Cards */
transform: translateY(-4px);
transition: all 0.3s ease;

/* Buttons */
transition: all 0.3s ease;
hover: transform translateY(-2px)
active: transform translateY(0)

/* Results Appear */
@keyframes slideUp {
  from: opacity 0, translateY(20px)
  to:   opacity 1, translateY(0)
}
duration: 0.5s ease

/* Loading Spinner */
@keyframes spin {
  0%:   rotate(0deg)
  100%: rotate(360deg)
}
duration: 0.8s linear infinite
```

---

## 📱 Responsive Design

### Breakpoints

| Dispositivo | Ancho | Cambios |
|-------------|-------|---------|
| **Desktop** | > 768px | Layout normal (3 cols) |
| **Tablet** | 480-768px | Ajustes de padding |
| **Mobile** | < 480px | Stack vertical, 1 columna |

### Adaptaciones

**Desktop (1200px)**
```
Header: Flex horizontal
Hero H1: 2.5rem
Discovery: 3 columnas
Change Details: 2 columnas
Botones: Horizontal
```

**Mobile (< 480px)**
```
Header: Flex vertical, centrado
Hero H1: 2rem
Discovery: 1 columna
Change Details: 1 columna
Botones: Stack vertical
Padding: 1.5rem (reducido)
```

---

## 🔧 Estructura Técnica

### Arquitectura HTML

```
header (sticky)
  └─ .header-content
     ├─ .logo-icon (◆ Oro)
     └─ .logo-text + .tagline

.container
  ├─ .hero (gancho visual)
  ├─ .discovery (3 cards)
  ├─ .form-section
  │  ├─ #uploadForm
  │  ├─ .form-group (original)
  │  ├─ .form-group (amendment)
  │  ├─ #loading (oculto inicialmente)
  │  └─ .button-group
  ├─ .results-section (oculto hasta análisis)
  │  ├─ .analysis-summary
  │  └─ #changesList
  └─ .footer-cta
```

### CSS Variables Principales

```css
:root {
  --forest-green: #2D5016;         /* 60% */
  --metallic-gold: #D4AF37;        /* 30% */
  --snow-white: #F8F9FA;           /* 10% */
  --graphite-gray: #2C3E50;        /* Text */
  --light-gray: #E8EAED;           /* Borders */
  --accent-green: #3D7322;         /* Gradients */
  --text-dark: #1A1A1A;            /* Body text */
}
```

### JavaScript Funcionalidad

```javascript
// 1. File input handlers
document.getElementById('original').addEventListener('change', ...)
document.getElementById('amendment').addEventListener('change', ...)

// 2. Drag and drop setup
setupDragDrop('original', 'original-label')
setupDragDrop('amendment', 'amendment-label')

// 3. Form submission
#uploadForm.addEventListener('submit', async (e) => {
  // Mostrar loading
  // Hacer POST a /process
  // Mostrar resultados o error
})

// 4. Display results
displayResults(data) => {
  // Renderizar summary stats
  // Renderizar cada cambio
  // Mostrar section con animación
  // Scroll a resultados
}
```

---

## 🎬 Guía de Contenido para Videos

### Video 1: "Intro a Neo Labs" (30 seg)

**Gancho (5 seg)**
- Problema: "¿Horas revisando contratos?"
- Visual: Montaje rápido de documentos
- Audio: Música energética

**Solución (15 seg)**
- Demostración de interfaz
- Upload de archivos
- Presentación de resultados
- Badges de riesgo

**CTA (10 seg)**
- "Neo Labs: Automatización Legal"
- Botón "Analizar Ahora"
- Call to action: "Prueba Gratis"

### Paleta Visual para Video
- **Fondo**: Blanco Nieve con overlays suaves de Verde Bosque
- **Acentos**: Oro Metálico para highlights
- **Tipografía**: Montserrat Bold para títulos
- **Color Grading**: Contraste cálido (Verde + Oro)
- **Transiciones**: Fade, zoom in/out suave
- **Música**: Tono profesional + moderno

---

## 📊 Métricas de Éxito

### KPIs de Interfaz

| Métrica | Meta | Medida |
|---------|------|--------|
| **Time to Interaction** | < 3 seg | Hasta poder subir archivo |
| **Error Rate** | < 2% | % de uploads fallidos |
| **Results Load** | < 2 seg | Tiempo de respuesta API |
| **Mobile Usability** | 95%+ | Score de Google PageSpeed |
| **Accessibility** | WCAG AA | Contraste, navegación, textos |

---

## 🛠️ Personalización y Extensión

### Agregar Nuevas Secciones

1. **Crear HTML**
```html
<section class="custom-section">
  <h2>Mi Sección</h2>
  <!-- contenido -->
</section>
```

2. **Estilos** (respetar variables CSS)
```css
.custom-section {
  color: var(--forest-green);
  border-left: 4px solid var(--metallic-gold);
  padding: var(--spacing-lg);
}
```

3. **JS** (si aplica)
```javascript
document.querySelector('.custom-section').addEventListener('click', ...)
```

### Cambiar Colores

Editar `:root` en `<style>`:
```css
:root {
  --forest-green: #2D5016;    /* ← Cambiar aquí */
  --metallic-gold: #D4AF37;   /* ← Cambiar aquí */
  /* ... resto */
}
```

Todos los elementos automáticamente se actualizarán.

### Agregar Fuentes Personalizadas

Reemplazar `<link>` de Google Fonts:
```html
<link href="https://fonts.googleapis.com/css2?family=TuaFuente1&family=TuaFuente2&display=swap" rel="stylesheet">
```

Actualizar en CSS:
```css
body { font-family: 'TuaFuente1', sans-serif; }
h1 { font-family: 'TuaFuente2', sans-serif; }
```

---

## 🐛 Troubleshooting

### Problema: Página en blanco

**Solución**:
```bash
# 1. Verificar que uvicorn está corriendo
# 2. Verificar puerto 8000 disponible
# 3. Revisar console del navegador (F12) para errores
# 4. Limpiar cache (Ctrl+Shift+Del)
```

### Problema: Estilos no se aplican

**Solución**:
```bash
# 1. Forzar refresh: Ctrl+F5 (Windows) o Cmd+Shift+R (Mac)
# 2. Verificar sintaxis CSS en DevTools
# 3. Comprobar que fonts de Google están disponibles
```

### Problema: Drag-and-drop no funciona

**Solución**:
```bash
# 1. Verificar que el navegador soporta HTML5 Drag-and-Drop
# 2. Comprobar que preventDefault() está siendo llamado
# 3. Revisar archivos en console del navegador
```

### Problema: Upload lento

**Solución**:
```bash
# 1. Verificar tamaño de archivos (máx 10MB recomendado)
# 2. Revisar latencia de red (F12 → Network)
# 3. Confirmar que el servidor API está respondiendo
# 4. Aumentar timeout si es necesario en JS
```

---

## 📚 Referencias y Recursos

### Documentación
- `DESIGN_SYSTEM.md` - Guía completa de componentes y colores
- `README.md` - Documentación del proyecto completo
- Backend: `src/api/main.py` - Servidor FastAPI

### Herramientas Útiles
- **DevTools**: F12 en navegador (inspeccionar elementos)
- **Responsive Design**: Ctrl+Shift+M en Chrome/Firefox
- **Color Picker**: DevTools → Picker Tool
- **Performance**: DevTools → Lighthouse

### Google Fonts
- [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans)
- [Montserrat](https://fonts.google.com/specimen/Montserrat)

---

## 📝 Changelog

### v1.0 (2026-05-27)
- ✅ Interfaz profesional "Neo Labs"
- ✅ Paleta cromática estratégica
- ✅ Tipografías premium (IBM Plex + Montserrat)
- ✅ Estructura narrativa (Gancho → Descubrimiento → CTA)
- ✅ Drag-and-drop file upload
- ✅ Validación en tiempo real
- ✅ Resultados con badges de riesgo
- ✅ Responsive design (Desktop, Tablet, Mobile)
- ✅ Animaciones suaves
- ✅ Accesibilidad WCAG AA

---

**Última actualización**: 2026-05-27  
**Versión**: 1.0 - Web UI Inicial
