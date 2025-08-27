import os, pandas as pd, numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(ROOT,"data","weekly_attribute_kpis.csv"))
df["pct_negative"] = df["negative_mentions"]/df["total_attr_mentions"]
baseline_weeks = 8
alerts = []
for (brand, attr), grp in df.groupby(["brand","attribute"]):
    grp = grp.sort_values("week_start").copy()
    base = grp.head(baseline_weeks)
    m_neg, s_neg = base["pct_negative"].mean(), base["pct_negative"].std(ddof=1)
    m_star, s_star = base["avg_stars"].mean(), base["avg_stars"].std(ddof=1)
    for _, row in grp.iterrows():
        neg_dev = 0 if s_neg==0 else (row["pct_negative"]-m_neg)/s_neg
        star_dev = 0 if s_star==0 else (row["avg_stars"]-m_star)/s_star
        if abs(neg_dev)>1 or abs(star_dev)>1:
            alerts.append({"week_start":row["week_start"],"brand":brand,"attribute":attr,
                           "pct_negative":round(row["pct_negative"],3),"avg_stars":row["avg_stars"],
                           "neg_sigma":round(float(neg_dev),2),"star_sigma":round(float(star_dev),2)})
out = os.path.join(ROOT,"reports","alerts.csv"); os.makedirs(os.path.dirname(out), exist_ok=True)
pd.DataFrame(alerts).sort_values(["week_start","brand","attribute"]).to_csv(out, index=False)
print(f"Wrote alerts to {out}")
