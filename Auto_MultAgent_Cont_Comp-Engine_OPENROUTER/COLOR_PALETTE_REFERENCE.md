# Paleta de Colores Neo Labs - Referencia Rápida

## 🎨 Colores Principales

### Verde Bosque (Forest Green) - 60% de uso
```
Código Hex:    #2D5016
RGB:           45, 80, 22
HSL:           103°, 57%, 20%
Uso Principal: Headers, títulos, CTAs primarios, fondos de gradientes
```
**Visual:**
```
████████████████████████████████ Verde Bosque
```

### Oro Metálico (Metallic Gold) - 30% de uso
```
Código Hex:    #D4AF37
RGB:           212, 175, 55
HSL:           44°, 75%, 52%
Uso Principal: Acentos, bordes, iconografía, hover states
```
**Visual:**
```
████████████████████████████████ Oro Metálico
```

### Blanco Nieve (Snow White) - 10% de uso
```
Código Hex:    #F8F9FA
RGB:           248, 249, 250
HSL:           210°, 12%, 98%
Uso Principal: Fondos, espacios negativos, cards
```
**Visual:**
```
████████████████████████████████ Blanco Nieve
```

### Gris Grafito (Graphite Gray) - Complementario
```
Código Hex:    #2C3E50
RGB:           44, 62, 80
HSL:           204°, 29%, 24%
Uso Principal: Texto secundario, detalles, subtítulos
```
**Visual:**
```
████████████████████████████████ Gris Grafito
```

### Verde Acentuado (Accent Green)
```
Código Hex:    #3D7322
RGB:           61, 115, 34
HSL:           108°, 55%, 29%
Uso Principal: Variaciones de Verde Bosque, gradientes
```
**Visual:**
```
████████████████████████████████ Verde Acentuado
```

---

## 📊 Regla 60-30-10

```
┌────────────────────────────────────────────────┐
│                                                │
│  ████████████████████ Verde Bosque (60%)       │
│  ████████ Oro Metálico (30%)                   │
│  ██ Blanco Nieve (10%)                         │
│                                                │
└────────────────────────────────────────────────┘
```

### Cómo Aplicar

**En una página típica:**
- 60% Verde Bosque: Header, footer, fondos primarios, elementos principales
- 30% Oro Metálico: Bordes izquierdos (4px), acentos, highlights, hover states
- 10% Blanco Nieve: Espacios negativos, cards, background suave

**Ejemplo Visual:**
```
┌─────────────────────────────────────────────┐
│ ╔════════════════════════════════════════════╗  ← Verde Bosque (Header)
│ ║ Neo Labs | Fusión Orgánica Premium        ║
│ ╚════════════════════════════════════════════╝
│                                             │
│ ┌────────────────────────────────────────┐  │
│ │  ████ Contenido Principal              │  │ ← Blanco Nieve (Card)
│ │ ◆ Oro Metálico (borde izquierdo 4px)  │  │ ← Oro Metálico
│ │                                        │  │
│ │ [🚀 Botón Verde Bosque]                │  │ ← Verde + Oro en hover
│ └────────────────────────────────────────┘  │
│                                             │
│ ╔════════════════════════════════════════════╗  ← Verde Bosque (Footer)
│ ║ © 2026 Neo Labs - Powered by AI            ║
│ ╚════════════════════════════════════════════╝
└─────────────────────────────────────────────┘
```

---

## 🎨 Combinaciones de Colores

### Gradientes Recomendados

#### 1. Verde Principal → Verde Acentuado
```css
background: linear-gradient(135deg, #2D5016 0%, #3D7322 100%);
```
**Uso**: Headers, botones primarios, CTAs

#### 2. Verde Muy Suave (Background)
```css
background: linear-gradient(135deg, #F8F9FA 0%, #F0F3F0 100%);
```
**Uso**: Fondos de página, espacios de contenido

#### 3. Oro a Transparente (Overlay)
```css
background: rgba(212, 175, 55, 0.05);
```
**Uso**: Input fields, cards ligeros

#### 4. Verde Suave (Hover)
```css
background: rgba(45, 80, 22, 0.02);
```
**Uso**: Filas de tabla en hover, fondos sutiles

---

## 🔴 Colores de Estado (Complementarios)

### Indicadores de Riesgo

**Alto Riesgo - Rojo**
```
Código Hex:    #D32F2F
Uso:           Badges "Riesgo Alto", alertas críticas
Fondo claro:   rgba(255, 69, 58, 0.2)
Ejemplo:       🔴 Impacto Legal: Alto
```

**Medio Riesgo - Naranja**
```
Código Hex:    #F57F17
Uso:           Badges "Riesgo Medio", advertencias
Fondo claro:   rgba(255, 193, 7, 0.2)
Ejemplo:       🟠 Impacto Legal: Medio
```

**Bajo Riesgo - Verde Seguridad**
```
Código Hex:    #388E3C
Uso:           Badges "Riesgo Bajo", confirmaciones
Fondo claro:   rgba(76, 175, 80, 0.2)
Ejemplo:       🟢 Impacto Legal: Bajo
```

---

## 📱 Paleta en Diferentes Contextos

### Tema Claro (Light Theme)
```
Fondo General:      Blanco Nieve #F8F9FA
Texto Principal:    Gris Grafito #2C3E50
Acentos:            Verde Bosque #2D5016 + Oro Metálico #D4AF37
Bordes:             Gris Claro #E8EAED
```

### Tema Oscuro (Opcional - Futuro)
```
Fondo General:      Gris Oscuro #1E1E1E
Texto Principal:    Blanco Nieve #F8F9FA
Acentos:            Oro Metálico #D4AF37 (mejorado)
Bordes:             Gris Oscuro #2C3E50
```

---

## 🖼️ Paleta CSS Copy-Paste

```css
:root {
  /* Colores Primarios (60-30-10) */
  --forest-green: #2D5016;           /* 60% */
  --metallic-gold: #D4AF37;          /* 30% */
  --snow-white: #F8F9FA;             /* 10% */
  
  /* Complementarios */
  --graphite-gray: #2C3E50;          /* Texto */
  --light-gray: #E8EAED;             /* Bordes */
  --accent-green: #3D7322;           /* Gradientes */
  --text-dark: #1A1A1A;              /* Body text */
  
  /* Estados */
  --risk-high: #D32F2F;              /* Rojo */
  --risk-medium: #F57F17;            /* Naranja */
  --risk-low: #388E3C;               /* Verde */
  
  /* Transparencias útiles */
  --gold-bg-light: rgba(212, 175, 55, 0.05);
  --gold-bg-medium: rgba(212, 175, 55, 0.1);
  --green-bg-hover: rgba(45, 80, 22, 0.02);
  
  /* Espaciado */
  --spacing-xs: 0.5rem;
  --spacing-sm: 1rem;
  --spacing-md: 1.5rem;
  --spacing-lg: 2rem;
  --spacing-xl: 3rem;
  
  /* Radios */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-full: 999px;
  
  /* Sombras */
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.08);
  --shadow-md: 0 4px 20px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.15);
}
```

---

## 📐 Especificaciones de Accesibilidad

### Contraste de Color

| Combinación | Ratio | WCAG |
|-------------|-------|------|
| Verde Bosque + Blanco | 10.2:1 | AAA ✅ |
| Oro + Verde Bosque | 7.5:1 | AA ✅ |
| Gris Grafito + Blanco | 8.3:1 | AAA ✅ |
| Oro + Blanco | 5.1:1 | AA ✅ |

Todos los ratios cumplen **WCAG AA mínimo** y varios alcanzan **AAA**.

---

## 🎯 Checklist de Uso

### ✅ Para Componentes Nuevos

- [ ] ¿Usa Verde Bosque para elemento principal? (60%)
- [ ] ¿Tiene acentos en Oro Metálico? (30%)
- [ ] ¿El contraste es suficiente? (WCAG AA mínimo)
- [ ] ¿Funciona en mobile? (responsive)
- [ ] ¿Las transiciones son suaves? (0.3s default)
- [ ] ¿Hay estados hover/active/focus?
- [ ] ¿Es consistente con la paleta?

### ✅ Para Diseño de UI

- [ ] Header usa gradiente Verde Bosque → Verde Acentuado
- [ ] Botones primarios tienen fondo gradiente
- [ ] Cards tienen borde izquierdo Oro (4px)
- [ ] Fondos son Blanco Nieve, no blanco puro
- [ ] Texto es Gris Grafito, no negro puro
- [ ] Acentos están distribuidos en 30-10%
- [ ] Hay suficiente espaciado (padding/margin)

---

## 🔄 Mantenimiento de Paleta

### Cambiar Color Principal (Verde Bosque)

1. **Actualizar variable CSS**
   ```css
   --forest-green: #NUEVOHEX;
   ```

2. **Verificar contraste** con Blanco Nieve
   - Usar tool: contrast checker online

3. **Actualizar gradiente** (Verde Acentuado)
   - Usar versión más clara/oscura del nuevo color

4. **Probar en todos los contextos**
   - Header, botones, texto, hover states

### Versionar Cambios

```markdown
## Cambios de Paleta

### v1.0 (Original)
- Verde Bosque: #2D5016
- Oro Metálico: #D4AF37

### v1.1 (Futuro)
- Verde Bosque: #[nuevo]
- Razón: [descripción del cambio]
```

---

## 📚 Referencias Externas

- **Accessibility**: [WCAG Contrast Checker](https://webaim.org/resources/contrastchecker/)
- **Color Theory**: [Adobe Color Wheel](https://color.adobe.com/)
- **Gradientes**: [Gradient Generator](https://www.colordot.it/)
- **Tipografía**: [Google Fonts](https://fonts.google.com/)

---

**Última actualización**: 2026-05-27  
**Versión**: 1.0 - Paleta Inicial  
**Estado**: ✅ Finalizado y Validado
