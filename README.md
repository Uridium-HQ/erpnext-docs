# ERP / Frappe Docs Mirror

CLI alat za skidanje i lokalno mirror-ovanje dokumentacije sa `docs.frappe.io`, uz očuvanje:

- hijerarhije i strukture stranica
- internih linkova i anchor linkova (`#sekcija`)
- slika i animiranih GIF-ova
- izlaza u Markdown wiki formatu
- pomoćnih fajlova: `index.json`, `linkmap.json`, `nav.json`, `SUMMARY.md`, `mkdocs.yml`
- opcionalnog prevoda na srpski uz očuvanje linkova

Alat je pravljen tako da radi i za ERPNext i za Frappe Framework dokumentaciju, ali je dovoljno generički da može da se prilagodi i drugim docs sajtovima sa sličnom strukturom.

## 1. Šta je verifikovano na aktuelnom sajtu

Na aktuelnoj stranici `https://docs.frappe.io/framework/user/en/introduction` vidi se da dokumentacija trenutno ima:

- levi docs navigation tree sa sekcijama kao što su **Getting Started**, **Tutorial**, **Basics**, **Python API**, **JS API** i druge
- glavni sadržaj stranice sa naslovom **Introduction**
- akcije **Copy page as Markdown for LLMs**, **Open in ChatGPT** i slične
- internu navigaciju tipa **Next Page** i **On this page**

Zbog toga je u projektu podešen extractor tako da prioritet daje užem content selektoru (`main article`, `article`) umesto celom `main` regionu, kako levi sidebar i pomoćne akcije ne bi nepotrebno ulazile u sadržaj za eksport i prevod.

## 2. Glavne mogućnosti

- Crawl od jedne ili više početnih (`--seed`) stranica
- Ograničavanje crawl-a na određeni domen i prefikse
- Parsiranje sadržaja iz glavnog dela stranice
- Skidanje asset-a (`img`, uključujući GIF)
- Konverzija HTML sadržaja u Markdown
- Rewrite lokalnih linkova tako da upućuju na lokalne `.md` fajlove
- Generisanje lokalne navigacije i summary fajla
- Validacija internih linkova nakon generisanja
- Resume preko `state.json`
- Dedup asset-a preko SHA256 hash-a
- Konfigurisanje CSS selektora bez promene koda
- Prevod mirror-a na srpski latinicu uz očuvanje link target-a, fajl putanja, anchor-a i code blokova

## 3. Preporučeno okruženje

- Python 3.11+
- Linux / macOS
- Radi i na Windows-u, ali su primeri komandi dati za Bash

## 4. Instalacija

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Ako želiš da pokrećeš paket preko `python -m erp_docs_mirror.cli`, koristi:

```bash
export PYTHONPATH=src
```

## 5. Najbrži start

### ERPNext + Frappe Framework

```bash
export PYTHONPATH=src
python -m erp_docs_mirror.cli crawl \
  --seed https://docs.frappe.io/erpnext/introduction \
  --seed https://docs.frappe.io/framework/user/en/introduction \
  --output ./output/full \
  --max-pages 200
```

### Samo ERPNext

```bash
export PYTHONPATH=src
python -m erp_docs_mirror.cli crawl \
  --seed https://docs.frappe.io/erpnext/introduction \
  --output ./output/erpnext \
  --max-pages 300 \
  --allowed-prefix /erpnext/
```

### Samo Frappe Framework

```bash
export PYTHONPATH=src
python -m erp_docs_mirror.cli crawl \
  --seed https://docs.frappe.io/framework/user/en/introduction \
  --output ./output/framework \
  --max-pages 300 \
  --allowed-prefix /framework/
```

## 6. Prevod na srpski sa očuvanjem linkova

Postoje dva načina.

### Varijanta A — prvo crawl, pa poseban prevod

1. Napravi mirror:

```bash
export PYTHONPATH=src
python -m erp_docs_mirror.cli crawl \
  --seed https://docs.frappe.io/framework/user/en/introduction \
  --output ./output/framework \
  --allowed-prefix /framework/ \
  --max-pages 300
```

2. Postavi OpenAI kompatibilan API ključ:

```bash
export OPENAI_API_KEY="tvoj_kljuc"
```

3. Prevedi mirror u srpsku latinicu:

```bash
export PYTHONPATH=src
python -m erp_docs_mirror.cli translate \
  --input ./output/framework \
  --output ./output/framework_sr \
  --language sr-Latn \
  --model gpt-4o-mini
```

### Varijanta B — crawl i odmah prevedi

```bash
export OPENAI_API_KEY="tvoj_kljuc"
export PYTHONPATH=src
python -m erp_docs_mirror.cli crawl \
  --seed https://docs.frappe.io/framework/user/en/introduction \
  --output ./output/framework \
  --allowed-prefix /framework/ \
  --translate-to sr-Latn
```

Ako ne zadaš `--translated-output`, alat će napraviti prevedeni izlaz u folderu kao što je:

```text
./output/framework__sr-Latn
```

### Šta prevod čuva netaknuto

Prevodni modul maskira i čuva:

- markdown link target-e, npr. `(../../api/document.md#example)`
- image target-e
- code blokove
- inline code
- URL-ove i anchor fragmente
- HTML komentare

To znači da će tekst linka biti preveden, ali će sama putanja ostati ista.

Primer:

```markdown
[Next Page](../prerequisites.md)
```

postaje nešto kao:

```markdown
[Sledeća strana](../prerequisites.md)
```

## 7. Validacija linkova

Posle crawl-a ili prevoda:

```bash
export PYTHONPATH=src
python -m erp_docs_mirror.cli validate --output ./output/full
```

Ako želiš JSON izveštaj:

```bash
export PYTHONPATH=src
python -m erp_docs_mirror.cli validate --output ./output/full --json
```

Isto možeš pokrenuti i nad prevedenim folderom:

```bash
export PYTHONPATH=src
python -m erp_docs_mirror.cli validate --output ./output/framework_sr
```

## 8. Generisani izlaz

Primer strukture:

```text
output/full/
  assets/
    12ab34cd56ef-example.gif
    98fa10bc22dd-image.png
  pages/
    erpnext/
      introduction.md
      accounting/
        chart-of-accounts.md
    framework/
      user/
        en/
          introduction.md
          api/
            document.md
  meta/
    index.json
    linkmap.json
    nav.json
    state.json
  SUMMARY.md
  mkdocs.yml
```

### Šta je šta

- `pages/` — lokalni Markdown fajlovi
- `assets/` — skinute slike/GIF-ovi
- `meta/index.json` — lista obrađenih stranica sa metapodacima
- `meta/linkmap.json` — mapa `remote_url -> local_path`
- `meta/nav.json` — pronađena hijerarhija među stranicama
- `meta/state.json` — stanje crawler-a za resume
- `SUMMARY.md` — wiki summary stil
- `mkdocs.yml` — osnovna MkDocs konfiguracija

## 9. Resume rada

Ako prekineš proces, samo ponovo pokreni isti crawl nad istim output folderom. Alat koristi `meta/state.json` i preskočiće već obrađene stranice kada je moguće.

## 10. Kako alat odlučuje gde snima fajlove

URL:

```text
https://docs.frappe.io/framework/user/en/api/document
```

postaje:

```text
pages/framework/user/en/api/document.md
```

URL sa završnim slash-om ili `index` scenarijem se normalizuje u smislen lokalni `.md` path.

## 11. Asset deduplikacija

Ako se ista slika ili isti GIF pojavljuju više puta, alat računa SHA256 i čuva samo jednu lokalnu kopiju kada je sadržaj identičan.

## 12. Podešavanje selektora

Ako docs sajt promeni HTML strukturu, selektore možeš promeniti u fajlu:

```text
src/erp_docs_mirror/default_config.json
```

Bitna polja:

- `content_selectors`
- `nav_selectors`
- `title_selectors`
- `remove_selectors`

Alat pokušava selektore redom dok ne pronađe odgovarajući element.

## 13. Primeri korisnih opcija

### Sporiji i sigurniji crawl

```bash
export PYTHONPATH=src
python -m erp_docs_mirror.cli crawl \
  --seed https://docs.frappe.io/erpnext/introduction \
  --output ./output/slow \
  --max-pages 100 \
  --delay 0.5 \
  --timeout 30
```

### Samo isti host + samo određeni prefiksi

```bash
export PYTHONPATH=src
python -m erp_docs_mirror.cli crawl \
  --seed https://docs.frappe.io/erpnext/introduction \
  --seed https://docs.frappe.io/framework/user/en/introduction \
  --output ./output/scoped \
  --allowed-prefix /erpnext/ \
  --allowed-prefix /framework/
```

### Bez skidanja asset-a

```bash
export PYTHONPATH=src
python -m erp_docs_mirror.cli crawl \
  --seed https://docs.frappe.io/erpnext/introduction \
  --output ./output/no-assets \
  --no-assets
```

## 14. Korišćenje sa MkDocs

Ako želiš lokalni docs portal:

```bash
pip install mkdocs
mkdocs serve -f output/full/mkdocs.yml
```

Napomena: prevedena verzija po default-u kopira originalni `mkdocs.yml`. Ako želiš da i naziv navigacije u MkDocs-u bude preveden, najbezbednije je da to uradiš kontrolisano posle prevoda, jer YAML struktura mora ostati ispravna.

## 15. Ograničenja i preporuke

- Trenutna opcija za prevod koristi **OpenAI kompatibilan Chat Completions API**.
- Ako želiš drugi provider, najlakše je da koristiš kompatibilan `--api-base` endpoint.
- Kod veoma velikih stranica prevod ide u chunk-ovima da bi se smanjio rizik od pucanja request-a.
- Ako sajt promeni DOM strukturu, prvo prilagodi `default_config.json`.
- Za potpuno pouzdano zadržavanje svih heading anchor-a, preporuka je da radiš validaciju posle prevoda.

## 16. Sledeći logičan korak

Ako budeš želeo, sledeća dorada ovog projekta može da bude:

- direktno korišćenje opcije **Copy page as Markdown for LLMs** kada je dostupna
- eksport baš za Wiki.js import tok
- prevod po terminološkom glosaru za ERP/Frappe pojmove
- keširanje prevoda da ne plaćaš isti tekst više puta
