
import pandas as pd
def soft_dedup(df):
    if df.empty: return df
    df = df.drop_duplicates(subset=[c for c in df.columns if c.lower()=='url']).copy()
    if 'price' in df.columns and 'surface_m2' in df.columns:
        df['_price_r'] = (df['price'].round(-3)).astype('Int64'); df['_surf_r'] = (df['surface_m2'].round(0)).astype('Int64')
        df = df.sort_values(['_price_r','_surf_r']).drop_duplicates(['_price_r','_surf_r','city'], keep='first').drop(columns=['_price_r','_surf_r'], errors='ignore')
    return df
