
import streamlit as st, pandas as pd
st.header("⚙️ Paramètres & hypothèses")
if "params" not in st.session_state: st.session_state["params"] = {}
p = st.session_state["params"]
p["strategy"] = st.selectbox("Stratégie", ["meuble","nu","colocation"], 0)
p["tmi"] = st.slider("TMI (tranche marginale)", 0.0, 0.45, 0.30, 0.01)
p["ps"] = st.slider("Prélèvements sociaux", 0.0, 0.20, 0.172, 0.001)
p["building_share"] = st.slider("Part du bâti amortissable (%)", 50, 95, 80, 1) / 100.0
p["amortization_rate_building"] = st.slider("Taux d'amortissement bâti (%/an)", 1.5, 4.0, 2.5, 0.1) / 100.0
p["apply_cap"] = st.checkbox("Appliquer un plafond €/m²", True)
p["cap_per_m2"] = st.number_input("Plafond €/m² (si applicable)", 0.0, value=0.0, step=0.5)
p["rent_control_cities"] = {c.lower() for c in ["Paris","Lille","Lyon","Villeurbanne","Montpellier","Bordeaux"]}
p["taux"] = st.slider("Taux nominal annuel (%)", 1.0, 6.0, 3.05, 0.01)/100.0
p["assurance"] = st.slider("Assurance annuelle (% capital)", 0.0, 1.0, 0.30, 0.01)/100.0
p["duree_annees"] = st.slider("Durée (années)", 10, 30, 25, 1)
p["frais_notaires"] = st.slider("Frais de notaire (% du prix)", 6.0, 9.0, 7.5, 0.1)/100.0
p["travaux"] = st.number_input("Travaux (€)", 0, value=0, step=1000)
p["apport"] = st.number_input("Apport (€)", 0, value=0, step=1000)
p["vacancy_rate"] = st.slider("Vacance (% loyer)", 0.0, 15.0, 8.0, 0.5)/100.0
p["mgmt_rate"] = st.slider("Gestion (% loyer)", 0.0, 12.0, 7.0, 0.5)/100.0
p["nonrecup_rate"] = st.slider("Non récup. (% loyer)", 0.0, 12.0, 5.0, 0.5)/100.0
p["capex_rate"] = st.slider("Capex/Entretien (% loyer)", 0.0, 12.0, 5.0, 0.5)/100.0
p["gli_rate"] = st.slider("GLI (% loyer)", 0.0, 5.0, 2.5, 0.1)/100.0
p["pno_monthly"] = st.number_input("PNO (€/mois)", 0.0, value=12.0, step=1.0)
p["taxe_fonciere_monthly"] = st.number_input("TF (fallback, €/mois)", 0.0, value=60.0, step=10.0)
p["compta_monthly"] = st.number_input("Comptable LMNP (€/mois)", 0.0, value=40.0, step=5.0)
if "city_presets" not in p:
    p["city_presets"] = pd.DataFrame({"city":["Brest","Paris"],"rent_per_m2":[9.5,30.0],"tf_per_m2_month":[0.6,0.9]})
presets = st.data_editor(p["city_presets"], num_rows="dynamic", use_container_width=True)
p["rpm2_fallback"] = {"default": float(presets["rent_per_m2"].mean() if not presets.empty else 20.0)}
p["tf_per_city"] = {}
for _, r in presets.iterrows():
    p["rpm2_fallback"][str(r["city"]).lower()] = float(r["rent_per_m2"])
    p["tf_per_city"][str(r["city"]).lower()] = float(r["tf_per_m2_month"])
p["base_neg"] = st.slider("Base négo (% prix affiché)", 0.0, 15.0, 3.0, 0.5)/100.0
p["extra_per_30d"] = st.slider("Bonus / 30j (%)", 0.0, 5.0, 1.5, 0.1)/100.0
p["neg_max"] = st.slider("Négo max (%)", 0.0, 25.0, 12.0, 0.5)/100.0
up = st.file_uploader("CSV: city, property_type, rent_per_m2", type=["csv"])
p["rent_bench_df"] = pd.read_csv(up) if up is not None else None
st.success("✅ Paramètres enregistrés — ouvrez **Dashboard**.")
