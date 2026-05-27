# Neo Labs - Design System
## Concepto Visual: Fusión Orgánica Premium

---

## 📐 Paleta Cromática (Regla 60-30-10)

### Colores Estratégicos

| Nombre | Código | Uso | Proporción |
|--------|--------|-----|-----------|
| **Verde Bosque** | `#2D5016` | Primario - Headers, CTAs, títulos | 60% |
| **Oro Metálico** | `#D4AF37` | Acentos - Bordes, iconografía, énfasis | 30% |
| **Blanco Nieve** | `#F8F9FA` | Fondo - Espacios negativos | 10% |
| **Gris Grafito** | `#2C3E50` | Texto secundario, detalles |  |
| **Verde Acentuado** | `#3D7322` | Variación de Verde Bosque (gradientes) |  |

### Aplicación en Interfaz

- **Backgrounds**: Blanco Nieve con gradientes suaves de Verde Bosque
- **Headers**: Gradiente Verde Bosque → Verde Acentuado
- **Botones Primarios**: Gradiente Verde Bosque → Verde Acentuado
- **Bordes de Énfasis**: Oro Metálico (4px left borders)
- **Texto Principal**: Gris Grafito (#1A1A1A)
- **Hover States**: Tonos más claros de Verde Bosque con sombras

---

## 🔤 Tipografías de Autoridad

### Familias Tipográficas

```
Logo & Títulos:    Montserrat
Descripción:       Montserrat (600-800)
Cuerpo de Texto:   IBM Plex Sans
Interfaz:          IBM Plex Sans
```

### Jerarquía Tipográfica

| Elemento | Familia | Tamaño | Peso | Color |
|----------|---------|--------|------|-------|
| Logo | Montserrat | 1.5rem | 700 | Blanco |
| H1 (Hero) | Montserrat | 2.5rem | 800 | Verde Bosque |
| H2 (Secciones) | Montserrat | 1.8rem | 700 | Verde Bosque |
| H3 (Subtítulos) | Montserrat | 1.3rem | 600 | Verde Bosque |
| Body | IBM Plex Sans | 1rem | 400 | Gris Grafito |
| Label (Botones) | Montserrat | 1rem | 600 | Blanco / Verde |
| Caption | IBM Plex Sans | 0.9rem | 400 | #666 |

---

## 🎯 Estructura de Contenido

### 1. **Gancho (Hook)**
- **Ubicación**: Hero Section (top)
- **Elemento**: Título impactante + Subtítulo + Descripción corta
- **Objetivo**: Captar atención inmediata
- **Visual**: Verde Bosque dominante, tipografía Montserrat extra-bold

```
"Análisis Inteligente de Contratos"
"Automatización de Auditoría Legal con IA"
"Descubre cambios críticos en tus contratos al instante..."
```

### 2. **Descubrimiento (Discovery)**
- **Ubicación**: Cards debajo del Hero
- **Elementos**: 3 tarjetas con iconos, títulos y descripciones
- **Objetivo**: Comunicar valor y capacidades
- **Visual**: Bordes Oro Metálico, fondo blanco, hover lift effect

```
🔍 Análisis Profundo
⚡ Velocidad Extrema
🛡️ Precisión Legal
```

### 3. **Llamado a la Acción (CTA)**
- **Ubicación**: Formulario interactivo
- **Elementos**: Inputs estilizados, botones prominentes
- **Objetivo**: Generar conversión (upload de archivos)
- **Visual**: Botón primario Verde Bosque con gradiente, botón secundario con borde Oro Metálico

```
Botón Principal:   "🚀 Analizar Ahora" (Verde Bosque)
Botón Secundario:  "↻ Limpiar" (Borde Oro Metálico)
```

### 4. **Resultados (Results)**
- **Ubicación**: Sección que aparece post-análisis
- **Elementos**: Resumen, tabla de cambios, badges de riesgo
- **Objetivo**: Presentar información compleja de forma visual
- **Visual**: Cards anidados, badges de riesgo (Alto/Medio/Bajo), animación slide-up

---

## 🎨 Componentes Principales

### Header
- **Altura**: 4rem (con padding)
- **Fondo**: Gradiente Verde Bosque → Verde Acentuado
- **Logo**: Icono Oro Metálico (círculo ◆) + Texto "Neo Labs"
- **Tagline**: "Fusión Orgánica Premium"
- **Posición**: Sticky (fixed al scroll)
- **Sombra**: `0 4px 20px rgba(45, 80, 22, 0.15)`

### Cards (Discovery)
- **Radio de esquinas**: 12px
- **Borde izquierdo**: 4px Oro Metálico
- **Sombra**: `0 2px 12px rgba(0, 0, 0, 0.08)`
- **Hover**: Elevación (-4px) + Sombra mejorada
- **Contenido**: Icono (2.5rem) + Título + Descripción

### Botones

#### Primario (CTA Principal)
```css
Background:   Gradiente Verde Bosque → Verde Acentuado
Color:        Blanco
Padding:      1rem 2rem
Radius:       8px
Hover:        Elevación + Mayor sombra
Transform:    translateY(-2px)
```

#### Secundario
```css
Background:   Transparente
Border:       2px Oro Metálico
Color:        Oro Metálico
Padding:      1rem 2rem
Radius:       8px
Hover:        Fondo Oro Metálico, Texto Verde Bosque
```

### Inputs de Archivo
- **Borde**: 2px dashed Oro Metálico
- **Fondo**: `rgba(212, 175, 55, 0.05)` (Oro muy ligero)
- **Radio**: 8px
- **Hover**: Fondo más intenso + Borde Verde Bosque
- **Feedback**: Label actualizado con nombre del archivo + checkmark ✓

### Results Cards
- **Borde izquierdo**: 4px Oro Metálico
- **Fondo**: Blanco con sección de resumen en gradiente suave
- **Badges**: Alto (Rojo), Medio (Naranja), Bajo (Verde)
- **Animación**: Aparición smooth `slideUp` 0.5s

---

## ✨ Efectos y Transiciones

### Animaciones
```css
Default Transition:  all 0.3s ease
Card Hover:          translateY(-4px)
Button Press:        translateY(0)
Result Appear:       slideUp 0.5s ease (opacity + translate)
Loading:             Spinner con rotación spin 0.8s linear infinite
```

### Estados Interactivos
- **Focus**: Borde Oro Metálico + Sombra interna
- **Hover**: Cambios de elevación y color
- **Active**: Presión visual (transform scale o translateY)
- **Loading**: Spinner animado + Texto descriptivo
- **Error**: Fondo rojo claro + Borde rojo + Icono ❌

---

## 📱 Responsive Design

### Breakpoints
- **Desktop**: 1200px (max-width container)
- **Tablet**: 768px (ajustes de grid)
- **Mobile**: < 480px (stack vertical)

### Cambios por Dispositivo
- **Header**: Flex column en mobile (logo centrado)
- **Hero H1**: 2.5rem → 2rem
- **Discovery Grid**: 3 columnas → 1 columna
- **Change Details**: 2 columnas → 1 columna
- **Botones**: Horizontal → Stack vertical (flex-direction: column)

---

## 🎬 Guía de Contenido para Videos

### Estructura Narrativa por Sección

#### 1️⃣ Gancho (5-8 seg)
- **Apertura**: Problema (auditoría manual lenta)
- **Visual**: Montaje rápido de documentos siendo revisados
- **Audio**: Música energética, problema enunciado

#### 2️⃣ Descubrimiento (10-15 seg)
- **Demostración**: Cómo Neo Labs resuelve el problema
- **Visual**: Animaciones de UI, cambios detectados, badges de riesgo
- **Audio**: Explicación de capacidades (análisis, velocidad, precisión)

#### 3️⃣ Llamado a la Acción (5-8 seg)
- **CTA Explícita**: "Prueba Neo Labs Hoy"
- **Visual**: Botón animado, interfaz responsiva
- **Audio**: Cierre inspirador, tono de autoridad

### Paleta Visual para Videos
- **Fondo**: Blanco Nieve con overlays Verde Bosque suave
- **Acentos**: Oro Metálico para resaltar elementos clave
- **Tipografía**: Montserrat para títulos (bold), IBM Plex Sans para subtítulos
- **Efectos**: Transiciones suaves, zoom in/out en cambios detectados
- **Color Grading**: Contraste cálido (Verde + Oro)

---

## 🚀 Casos de Uso de Color

### Indicadores de Estado

| Estado | Color | Significado |
|--------|-------|-------------|
| **Riesgo Alto** | Rojo (#D32F2F) | Cambio crítico requiere acción inmediata |
| **Riesgo Medio** | Naranja (#F57F17) | Cambio significativo, revisar con atención |
| **Riesgo Bajo** | Verde (#388E3C) | Cambio menor, impacto limitado |
| **Procesando** | Oro Metálico | Loading/en progreso |
| **Completado** | Verde Bosque | Análisis exitoso |
| **Error** | Rojo | Problema detectado |

---

## 📐 Espaciado y Layout

### Escala de Padding/Margin
```
xs:   0.5rem
sm:   1rem
md:   1.5rem
lg:   2rem
xl:   3rem
```

### Container
```css
max-width: 1200px
padding:   3rem 2rem (desktop)
padding:   1.5rem (mobile)
```

### Grid
```css
Discovery Cards: 3 columnas (desktop)
Change Details:  2 columnas (desktop)
Form:            1 columna
```

---

## 🎯 Métricas de Diseño

- **Consistencia**: Todos los bordes izquierdos 4px, esquinas 8-12px
- **Alineación**: Múltiplos de 8px
- **Sombras**: Valores consistentes (0 2px, 0 4px, 0 8px)
- **Transiciones**: 0.3s default, 0.5s para animaciones principales
- **Z-index**: Header 100, overlays 50

---

## 💾 Implementación Técnica

### CSS Variables (Raíz)
```css
--forest-green: #2D5016;
--metallic-gold: #D4AF37;
--snow-white: #F8F9FA;
--graphite-gray: #2C3E50;
--light-gray: #E8EAED;
--accent-green: #3D7322;
--text-dark: #1A1A1A;
```

### Fuentes (Google Fonts)
```html
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=Montserrat:wght@600;700;800&display=swap" rel="stylesheet">
```

### Estructura HTML
```
header (sticky)
  └─ .logo, .tagline

.container
  ├─ .hero (Gancho)
  ├─ .discovery (Descubrimiento - 3 cards)
  ├─ .form-section (CTA Principal)
  │  └─ file inputs + botones
  ├─ .results-section (Dinámico, post-análisis)
  └─ .footer-cta (CTA Secundaria)
```

---

## 📝 Notas de Marca

- **Nombre**: Neo Labs (con subtítulo "Fusión Orgánica Premium")
- **Propuesta**: Moderno + Profesional + Precisión Legal
- **Tono**: Autoridad técnica + Accesibilidad
- **Emocional**: Confianza, eficiencia, innovación

---

**Última actualización**: 2026-05-27  
**Versión**: 1.0 - Design System Inicial
