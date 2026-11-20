import re, sys

path = sys.argv[1] if len(sys.argv) > 1 else "index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

new_block = """const PRICE_IDS = {
    pro:    { monthly: 'price_1Tw2gzF6K4YHMTtacoJh9S8f',  annual: 'price_1Tw2gzF6K4YHMTtahI75WYBJ'  },
    team:   { monthly: 'price_1Tw2k5F6K4YHMTtaEkdDnpnX', annual: 'price_1Tw2k5F6K4YHMTta2UXJNeg5' },
  };"""

pattern = re.compile(r"const PRICE_IDS = \{.*?\};", re.DOTALL)

if not pattern.search(content):
    print("AVISO: bloco PRICE_IDS não encontrado. Nada foi alterado.")
else:
    content = pattern.sub(new_block, content, count=1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("OK: price_id atualizados.")
