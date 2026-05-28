<div align="center">

# 🎨 Servicio Social — Animaciones y Graficado Matemático

**Escuela Superior de Cómputo · Instituto Politécnico Nacional**

![IPN](https://img.shields.io/badge/IPN-ESCOM-darkred?style=flat-square)
![Periodo](https://img.shields.io/badge/Periodo-Abril--Octubre%202026-blue?style=flat-square)
![Estado](https://img.shields.io/badge/Estado-En%20progreso-green?style=flat-square)
![Horas](https://img.shields.io/badge/Horas%20acumuladas-76%2F480-orange?style=flat-square)

_Desarrollo de animaciones y visualizaciones matemáticas 2D/3D como material de apoyo educativo_

</div>

---

## 📌 Información general

| Campo                   | Detalle                                             |
| ----------------------- | --------------------------------------------------- |
| **Prestador**           | Daniel Tovar Abraham                                |
| **Boleta**              | 2018631321                                          |
| **Carrera**             | Ingeniería en Sistemas Computacionales              |
| **Correo**              | adanielt1700@alumno.ipn.mx                          |
| **Prestatario**         | Escuela Superior de Cómputo — IPN                   |
| **Programa**            | ESCOM-S.S. para Apoyo al Área Académica             |
| **Responsable directo** | M. en C. Jesús Ortuño Araujo · Profesor Asociado C. |
| **Periodo**             | 16 de abril de 2026 — 15 de octubre de 2026         |
| **Horas requeridas**    | 480 horas (4 hrs/día · lunes a viernes)             |

---

## 🎯 Objetivo del proyecto

Generar material visual educativo de alta calidad mediante animaciones y visualizaciones matemáticas programáticas, cubriendo temas de cálculo vectorial, álgebra lineal y análisis matemático. Cada herramienta del stack tiene un rol único y no reemplazable por las demás.

---

## 🛠️ Stack tecnológico

> Cada herramienta cubre un caso de uso que las demás **no pueden** resolver.

### 📄 Documentos y figuras estáticas

| Herramienta      | Versión              | Rol único                                                          |
| ---------------- | -------------------- | ------------------------------------------------------------------ |
| **MiKTeX**       | latest               | Distribución de LaTeX para Windows — motor de compilación          |
| **TeXnicCenter** | 2.02                 | Editor con autocompletado y compilación integrada                  |
| **TikZ**         | (incluida en MiKTeX) | Único que genera figuras de calidad editorial _dentro_ de un PDF   |
| **Ghostview**    | latest               | Visualización de archivos `.ps` y `.pdf` en proceso de compilación |
| **Sumatra PDF**  | latest               | Lector ligero con auto-refresh al recompilar LaTeX                 |

### 🎬 Animaciones y video

| Herramienta         | Versión | Rol único                                                                  |
| ------------------- | ------- | -------------------------------------------------------------------------- |
| **Python**          | 3.x     | Lenguaje base de todo el pipeline de animación                             |
| **Manim Community** | v0.20.1 | Único que renderiza **video animado** con fórmulas LaTeX programáticamente |
| **FFmpeg**          | latest  | Único procesador de video: cortar, unir y exportar clips de Manim          |

### 🌐 Visualizaciones interactivas

| Herramienta  | Versión      | Rol único                                                                   |
| ------------ | ------------ | --------------------------------------------------------------------------- |
| **GeoGebra** | web          | Único que permite al usuario **manipular en tiempo real** sin instalar nada |
| **Plotly**   | latest (pip) | Único optimizado para graficar **datos y superficies 3D** de forma rápida   |

### 🖼️ Edición de imágenes

| Herramienta | Versión | Rol único                                                                  |
| ----------- | ------- | -------------------------------------------------------------------------- |
| **GIMP**    | 3.0.4   | Único editor raster: thumbnails, capturas y edición de imágenes exportadas |

---

## 📅 Plan de actividades

### ✅ Mes 1 — Abril 2026 `76/76 hrs`

- Instalación y configuración del entorno completo (MiKTeX, TeXnicCenter, Ghostview, Sumatra PDF, GIMP 3.0.4)
- Introducción al lenguaje LaTeX: estructura básica, compilación de documentos, comandos esenciales
- Estudio de la librería TikZ: análisis de ejemplos de animaciones proporcionados por el profesor
- Ejercicios prácticos de graficado y primeras secuencias animadas

### 🔄 Mes 2 — Mayo 2026 `en progreso`

- Instalación de Manim Community v0.20.1 + configuración de entorno virtual Python
- Primeras animaciones propias en Manim: superficies paramétricas (Cinta de Möbius, toro, esfera)
- Profundización en TikZ: gráficas 2D y diagramas para documentos
- Instalación y primeros pasos con Plotly y GeoGebra

### ⏳ Mes 3 — Junio 2026

- Animaciones de Cálculo Vectorial: gradientes, campos vectoriales, curvas de nivel
- Renderizado de superficies 3D con rotación automática de cámara en Manim
- Integración de fórmulas LaTeX dentro de escenas de Manim
- Visualizaciones interactivas en GeoGebra para conceptos de límites y derivadas

### ⏳ Mes 4 — Julio 2026

- Álgebra Lineal animada: transformaciones lineales, eigenvalores y eigenvectores
- Graficado de datos y comparativas con Plotly (3D interactivo)
- Edición y composición de videos con FFmpeg
- Generación de material en alta calidad para uso del área académica

### ⏳ Mes 5 — Agosto 2026

- Series de Fourier y análisis matemático animado
- Escenas complejas en Manim: múltiples objetos, texto, cámaras y transiciones
- Documentación técnica de cada animación producida
- Revisión y ajustes con el responsable del proyecto

### ⏳ Mes 6 — Septiembre / Octubre 2026

- Organización y entrega del material visual generado durante el servicio
- Elaboración del reporte final de actividades
- Presentación de resultados al M. en C. Jesús Ortuño Araujo

---

## 📁 Estructura del repositorio

```
servicio-social/
├── mes1-configuracion/
│   ├── ejemplos-tikz/          # Animaciones analizadas del profesor
│   └── notas-latex/            # Primeros documentos compilados
├── mes2-manim-intro/
│   ├── superficies/
│   │   ├── mobius.py           # Cinta de Möbius 3D animada
│   │   ├── toro.py
│   │   └── esfera.py
│   └── plotly-intro/
├── mes3-calculo-vectorial/
│   ├── campos-vectoriales.py
│   ├── curvas-nivel.py
│   └── geogebra/
├── mes4-algebra-lineal/
│   ├── transformaciones.py
│   └── eigenvalores.py
├── mes5-fourier/
│   ├── series-fourier.py
│   └── analisis/
├── mes6-final/
│   └── reporte-final/
├── media/                      # Videos renderizados (generado por Manim)
└── README.md
```

---

## ⚡ Comandos rápidos

### Manim

```bash
# Activar entorno virtual (Windows)
venv\Scripts\activate

# Renderizar — prueba rápida (baja calidad)
manim -pql archivo.py NombreClase

# Renderizar — entrega final (alta calidad)
manim -pqh archivo.py NombreClase

# Renderizar con fondo transparente
manim -pqh --transparent archivo.py NombreClase
```

### Plotly

```bash
pip install plotly                  # instalar
python -c "import plotly; print(plotly.__version__)"  # verificar
```

### FFmpeg — edición de videos

```bash
# Unir dos clips
ffmpeg -i clip1.mp4 -i clip2.mp4 -filter_complex concat output.mp4

# Cambiar velocidad (x2)
ffmpeg -i input.mp4 -vf "setpts=0.5*PTS" output.mp4

# Exportar a GIF
ffmpeg -i input.mp4 -vf "fps=15,scale=640:-1" output.gif
```

### Git — flujo de trabajo

```bash
git checkout dev          # trabajar en rama dev
git add .
git commit -m "mes2: animacion mobius terminada"
git checkout main
git merge dev             # pasar a main cuando esté listo
git push
```

---

## 📊 Progreso general

| Mes | Periodo              | Horas        | Estado         |
| --- | -------------------- | ------------ | -------------- |
| 1   | 16 abr — 15 may 2026 | 76 / 76      | ✅ Completado  |
| 2   | 16 may — 15 jun 2026 | — / 80       | 🔄 En progreso |
| 3   | 16 jun — 15 jul 2026 | — / 80       | ⏳ Pendiente   |
| 4   | 16 jul — 15 ago 2026 | — / 80       | ⏳ Pendiente   |
| 5   | 16 ago — 15 sep 2026 | — / 84       | ⏳ Pendiente   |
| 6   | 16 sep — 15 oct 2026 | — / 80       | ⏳ Pendiente   |
|     | **Total**            | **76 / 480** | **15.8%**      |

---

<div align="center">

_ESCOM · IPN — Subdirección de Servicios Educativos e Integración Social_  
_Departamento de Extensión y Apoyos Educativos_

</div>
