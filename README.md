# pipman

🧪 Automatický instalátor Python knihoven s offline fallbackem.

##
## 🔧 Funkce

### ✅ Základ:

Načte requirements.txt nebo jiný seznam balíčků

Pomocí subprocess spustí pip install

Zaznamená chyby

### 💾 Offline fallback (pokud třeba není internet k dispozici nebo PyPI down):

Knihovny jako .whl v adresáři offline_libs/

Pokud pip install <lib> selže, zkusí to z lokálního souboru

### 📁 Podpora i pro:

requirements.txt

## Použití
Zapiš jména požadovaných balíčků do requirements.txt,
pokud není dostupný internet nebo pip, vlož .wheel soubory do offline_libs,
spusť v operativní složce:
```bash
python autoinstall.py
