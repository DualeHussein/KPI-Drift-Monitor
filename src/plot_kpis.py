import os, pandas as pd, matplotlib.pyplot as plt
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(ROOT,"data","weekly_attribute_kpis.csv"))
df["pct_negative"] = df["negative_mentions"]/df["total_attr_mentions"]
os.makedirs(os.path.join(ROOT,"charts"), exist_ok=True)
for (brand, attr), grp in df.groupby(["brand","attribute"]):
    grp = grp.sort_values("week_start")
    plt.figure(); plt.plot(grp["week_start"], grp["pct_negative"]); plt.xticks(rotation=45, ha="right")
    plt.title(f"{brand} – {attr} – % negative mentions (weekly)"); plt.tight_layout()
    plt.savefig(os.path.join(ROOT,"charts",f"{brand}_{attr}_pct_negative.png"), dpi=160); plt.close()
    plt.figure(); plt.plot(grp["week_start"], grp["avg_stars"]); plt.xticks(rotation=45, ha="right")
    plt.title(f"{brand} – {attr} – average stars (weekly)"); plt.tight_layout()
    plt.savefig(os.path.join(ROOT,"charts",f"{brand}_{attr}_avg_stars.png"), dpi=160); plt.close()
print("Saved charts to charts/")
