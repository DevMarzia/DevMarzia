import random
import json
import textwrap

# 1. Carica le frasi dal file JSON
with open('quotes.json', 'r') as f:
    quotes = json.load(f)

quote = random.choice(quotes)

# 2. Gestione del testo: lo dividiamo per non farlo uscire dai bordi
# Creiamo righe da circa 45 caratteri
lines = textwrap.wrap(quote['text'], width=45)

# Prepariamo i tag del testo (citazione)
text_tags = ""
y_start = 80 - (len(lines) * 5) # Calcola l'altezza iniziale per centrare

for i, line in enumerate(lines):
    y_pos = y_start + (i * 25)
    text_tags += f'<text x="250" y="{y_pos}" fill="white" font-family="Arial, sans-serif" font-size="18" text-anchor="middle">"{line}"</text>\n'

# Posizione dell'autore (sotto l'ultima riga)
y_author = y_start + (len(lines) * 25) + 10

# 3. Costruiamo l'SVG (Sfondo scuro + Bordo rosa + Testo)
svg_template = f'''<svg width="500" height="200" viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="490" height="190" x="5" y="5" rx="15" fill="#0d1117" stroke="#f06292" stroke-width="3"/>
  
  {text_tags}
  
  <text x="250" y="{y_author}" fill="#a9d2ff" font-family="Arial, sans-serif" font-size="14" font-style="italic" text-anchor="middle">- {quote['author']}</text>
</svg>'''

with open('quote.svg', 'w') as f:
    f.write(svg_template)
