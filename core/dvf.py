import pandas as pd

def load_dvf_medians(dvf_df):
    if dvf_df is None or dvf_df.empty: return None
    cols = {c.lower(): c for c in dvf_df.columns}; required = cols.get('city'), cols.get('median_price_sqm')
    if any(c is None for c in required): raise ValueError('DVF medians CSV doit contenir: city, median_price_sqm')
    return dvf_df
def price_gap_vs_dvf(price, surface_m2, city, dvf_df):
    if dvf_df is None or dvf_df.empty or surface_m2 is None or surface_m2 <= 0: return None
    cols = {c.lower(): c for c in dvf_df.columns}; city_col = cols.get('city'); med_col = cols.get('median_price_sqm')
    sub = dvf_df[dvf_df[city_col].str.lower() == str(city).lower()]; 
    if sub.empty: return None
    med = float(sub.iloc[0][med_col]); 
    if med <= 0: return None
    listing_ppm2 = price / surface_m2; return (listing_ppm2 - med) / med * 100.0
