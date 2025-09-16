import pandas as pd

# Load your CSV
df = pd.read_csv("source.csv")
df["revenue_nominal"] = pd.to_numeric(df["revenue_nominal"].astype(str).str.replace(r"[^\d.]", "", regex=True), errors="coerce")
df = df.dropna(subset=["revenue_nominal"])

# Compute metrics
total_revenue = df["revenue_nominal"].sum()
rev_by_country = df.groupby("country")["revenue_nominal"].sum().sort_values(ascending=False)
top5_revenue = rev_by_country.head(5)
num_companies = df.groupby("country")["company"].count().sort_values(ascending=False)
top5_companies = num_companies.head(5)
rev_share = (rev_by_country / total_revenue * 100).round(2)

# Helper to make Markdown table from Series
def to_md(s, col_name):
    return "| " + " | ".join([s.name, col_name]) + " |\n|---|---|\n" + \
           "\n".join(f"| {i} | {v:,} |" for i, v in s.items())

# Load template
with open("map.md", "r", encoding="utf-8") as f:
    md = f.read()

# Replace placeholders with actual data
md = md.replace("TOTAL_REVENUE_PLACEHOLDER", f"${total_revenue:,.0f}")
md = md.replace("REV_BY_COUNTRY_PLACEHOLDER", to_md(rev_by_country, "Revenue"))
md = md.replace("TOP5_REVENUE_PLACEHOLDER", to_md(top5_revenue, "Revenue"))
md = md.replace("NUM_COMPANIES_PLACEHOLDER", to_md(num_companies, "Companies"))
md = md.replace("TOP5_COMPANIES_PLACEHOLDER", to_md(top5_companies, "Companies"))
md = md.replace("REV_SHARE_PLACEHOLDER", to_md(rev_share, "Revenue Share (%)"))

# Save final Markdown
with open("report.md", "w", encoding="utf-8") as f:
    f.write(md)

print("✅ Markdown report generated: report.md")
