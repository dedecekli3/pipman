# pipman

🧪 Automatický instalátor Python knihoven s offline fallbackem.

## Funkce
- ✅ Načte `requirements.txt`
- 🌐 Pokusí se o online instalaci
- 📦 Pokud selže, použije `.whl` soubory z `offline_libs/`

## Použití
Zapiš jména požadovaných balíčků do requirements.txt,
pokud není dostupný internet nebo pip, vlož .wheel soubory do offline_libs/ ,
spusť:
```bash
python autoinstall.py
