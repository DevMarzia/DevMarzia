import random
import json

# Carica le frasi
with open('quotes.json', 'r') as f:
    quotes = json.load(f)

quote = random.choice(quotes)

# Crea l'SVG personalizzato (niente più tagli!)
svg_template = f"""
<svg width="500" height="200" viewBox="0 0 500 200" fill="none" xmlns="http://www.w3.org/2000/center">
  <rect width="498" height="198" x="1" y="1" rx="15" fill="#0d1117" stroke="#f06292" stroke-width="2"/>
  <foreignObject x="20" y="20" width="460" height="160">
    <div xmlns="http://www.w3.org/1999/xhtml" style="color: white; font-family: sans-serif; text-align: center; display: flex; flex-direction: column; justify-content: center; height: 100%;">
      <p style="font-size: 18px; margin: 0;">"{quote['text']}"</p>
      <p style="font-size: 14px; color: #a9d2ff; margin-top: 10px;">- {quote['author']}</p>
    </div>
  </foreignObject>
</svg>
"""

with open('quote.svg', 'w') as f:
    f.write(svg_template)
