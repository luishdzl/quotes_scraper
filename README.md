# Quotes Scraper

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Un web scraper en Python que extrae citas inspiradoras de [Quotes to Scrape](http://quotes.toscrape.com), incluyendo texto, autor y etiquetas.

## Características principales

- **Extracción completa**: Obtiene todas las citas disponibles en el sitio
- **Datos estructurados**: Procesa cada cita con:
  - Texto de la cita
  - Autor
  - Lista de etiquetas
- **Paginación automática**: Recorre todas las páginas sin configuración adicional
- **Salida formateada**: Muestra resultados en formato legible
- **Exportación a JSON**: Opción para guardar los datos en formato JSON

## Requisitos

- Python 3.7+
- Bibliotecas:
  - `requests`
  - `beautifulsoup4`

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/quotes-scraper.git
cd quotes-scraper
