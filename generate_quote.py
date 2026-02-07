import random
import json
import textwrap

# 1. Carica le frasi
with open('quotes.json', 'r') as f:
    quotes = json.load(f)

quote = random.choice(quotes)

# 2. Gestione del testo (per evitare tagli e andare a capo)
# Dividiamo la frase in righe da circa 45 caratteri
lines = textwrap.wrap(quote['text'], width=45)

# Calcoliamo la posizione verticale per centrare il testo
text_tags = ""
y_start = 100 - (len(lines) * 12) # Centratura dinamica

for i, line in enumerate(lines):
    y_pos = y_start + (i * 25)
    text_tags += f'<text x="250" y="{y_pos}" fill="white" font-family="sans-serif" font-size="18" text-anchor="middle">"{line}"</text>\n'

# 3. Crea l'SVG con tag <text> standard (compatibili al 100% con GitHub)
svg_template = f'''
<svg width="500" height="200" viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="498" height="198" x="1" y="1" rx="15" fill="#0d1117" stroke="#f06292" stroke-width="2"/>
  {text_tags}
  <text x="250" y="{y_start + (len(lines) * 25) + 15}" fill="#a9d2ff" font-family="sans-serif" font-size="14" font-style="italic" text-anchor="middle">- {quote['author']}</text>
</svg>
'''

with open('quote.svg', 'w') as f:
    f.write(svg_template)
