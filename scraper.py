import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    base_url = "http://quotes.toscrape.com"
    page = 1
    all_quotes = []
    
    while True:
        # Construir URL de la página actual
        url = f"{base_url}/page/{page}/"
        response = requests.get(url)
        
        # Verificar si la página existe
        if response.status_code != 200:
            break
            
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        
        if not quotes:
            break
            
        for quote in quotes:
            # Extraer texto de la cita
            text = quote.find('span', class_='text').text
            
            # Extraer autor
            author = quote.find('small', class_='author').text
            
            # Extraer etiquetas
            tags_div = quote.find('div', class_='tags')
            tags = [tag.text for tag in tags_div.find_all('a', class_='tag')]
            
            # Guardar en estructura de datos
            all_quotes.append({
                'text': text,
                'author': author,
                'tags': tags
            })
        
        print(f"Página {page} procesada - {len(quotes)} citas encontradas")
        page += 1
    
    return all_quotes

# Ejecutar el scraper
if __name__ == "__main__":
    quotes = scrape_quotes()
    
    print(f"\nTotal de citas extraídas: {len(quotes)}\n")
    
    # Mostrar algunas citas como ejemplo
    for i, quote in enumerate(quotes[:3], 1):
        print(f"Cita #{i}:")
        print(f"Texto: {quote['text']}")
        print(f"Autor: {quote['author']}")
        print(f"Etiquetas: {', '.join(quote['tags'])}")
        print("-" * 80)