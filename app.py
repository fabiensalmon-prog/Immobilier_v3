import streamlit as st
from pathlib import Path
st.set_page_config(page_title='Ultimate Invest v5 – Immobilier locatif', layout='wide')
st.title('🏠 Ultimate Invest v5 – Chasseur d\'opportunités (multi‑villes)')
st.caption('Scraping (LBC/SeLoger) • Négociation auto • TF/Comptable • DVF (opt.) • Financement • After‑tax • Alertes.')
st.markdown("""**Workflow :**
1) **Paramètres** → stratégie, encadrement, charges, fiscalité & amortissements.
2) **Dashboard** → annonces, cash‑flow, after‑tax, top à visiter.
3) **Financement** → mensualités & amortissement.
4) **Alertes** → règles + scan à la demande.
""")
st.info('⚠️ Respecte les CGU. Anti‑bot possible.')
example_dir = Path('data/examples')
for fn in ['rents_example.csv','dvf_medians_example.csv','rates_2025-08.csv']:
    p = example_dir / fn
    if p.exists(): st.download_button(f'⬇️ {fn}', data=p.read_bytes(), file_name=fn)