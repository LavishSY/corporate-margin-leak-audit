# executive_case_study.md

# 📉 Case Study: How Automated Transaction Auditing Recovered 16.43% Margin Leakage in Corporate Sales

| Parameter | Executive Detail |
| --- | --- |
| **Engagement Type** | Corporate Transaction Margin Diagnostic & Profit Recovery |
| **Target Sector** | B2B Commercial & Office Supplies Distribution |
| **Primary Bleed** | 16.43% unapproved margin leakage on low-margin transactional SKUs |
| **Financial Damage** | -$18.14 net cash burn per order on high-velocity items ($111.74 gross sales) |
| **Core Stack** | PostgreSQL 18, Python (Pandas), Microsoft Excel Engine, Looker Studio BI |

---

### 🎯 1. Bottom Line Up Front (B.L.U.F.)

An automated data-lineage audit across historical sales transactions exposed critical profit erosion masked by top-line revenue targets. Unmonitored price markdown permissions allowed sales representatives to apply aggressive discounts to low-margin product tiers.

By deploying an automated relational validation pipeline and dynamic margin thresholds, the business flagged and halted systematic discounting abuse, protecting enterprise gross margins and preventing an ongoing **-$18.14 per-order capital drain** across North American corporate accounts.

---

### 🚨 2. The Operational Vulnerability (The Bleed)

During macro-level quarterly evaluations, the North American Corporate Office Supplies segment appeared operationally sound due to high order volumes and low regional shipping overhead ($9.78/order).

However, granular database cross-tabulation exposed an acute pricing vulnerability:

- **The Culprit SKU:** *Paper Clips Box 500pc* (High-frequency, low-margin transactional staple).
- **The Policy Violation:** Sales reps manually or automatically applied unauthorized markdowns up to **16.43%** to close volume quotas.
- **The Financial Reality:** On an average order value of **$111.74**, the company yielded an absolute net loss of **$18.14**, actively subsidizing client purchasing with internal corporate reserves.

---

### 🛠️ 3. The Engineering Architecture (The Proof)

To transition from reactive manual spot-checks to permanent diagnostic telemetry, a four-tier analytical pipeline was deployed:

1. **Relational Isolation (PostgreSQL 18):** Engineered parameterized SQL views (`v_na_corporate_leak`) utilizing conditional aggregations (`HAVING`, window ranking) to extract rogue transactions exceeding discount limits.
2. **Sanitization Core (Pandas):** Automated data type standardization (`float64` continuous tracking), structural profiling, and discount elasticity bucketing (Low, Moderate, High, Hyper-Aggressive >20%).
3. **Simulation Modeling (MS Excel Engine):** Built a multi-variable dynamic array framework utilizing `LET`, `FILTER`, and absolute cell-locking to model margin recovery across variable discount caps (5% to 15%).
4. **Executive Telemetry (Looker Studio):** Constructed interactive C-suite cross-filtering dashboards featuring drill-down capabilities by region, customer cohort, and SKU burn rates.

---

### 💡 4. Strategic Remediation & Commercial Value

To permanently insulate enterprise cash flow from margin dilution, three operational guardrails were delivered:

- **ERP Discount Kill-Switch:** Programmed hard stop rules prohibiting front-line sales teams from issuing markdowns greater than 10% on products with gross margins below 25%.
- **Automated Exception Reporting:** Live BI telemetry automatically routes transactions with negative margins directly to regional finance controllers before order fulfillment.
- **Restructured Commission Incentives:** Shifted sales performance quotas from Gross Volume ($$) to Net Contribution Margin ($$), immediately eliminating vanity-volume discounting behaviors.