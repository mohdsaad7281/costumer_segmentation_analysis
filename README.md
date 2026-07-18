# Customer Segmentation & Retention Analytics
End-to-end customer segmentation project analyzing 1M+ retail transactions to identify 
behavioral customer segments, retention patterns, and revenue distribution across 37 
countries — extended with a simulated A/B test to validate a retention intervention.

## Dataset
- **Source:** UCI Online Retail Dataset (2009–2011)
- **Raw rows:** 1,048,575 transactions
- **Clean rows:** 800,000+ after removing nulls & returns
- **Customers:** 5,873 unique customers
- **Period:** December 2009 – December 2011
- **Countries:** 37

## Tools & Technologies
| Tools used |
| MySQL | Data cleaning, RFM scoring, cohort query, experiment tables |
| Excel | Cohort retention heatmap (25 months) |
| Power BI | Interactive dashboard (segmentation + experiment results) |
| Python | Statistical significance testing (chi-square) |

## Experiment 1: Customer Segmentation & Retention Analysis

Segmented customers using RFM (Recency, Frequency, Monetary) scoring and built a 
25-month cohort retention matrix to understand revenue concentration and churn patterns.

### Key Findings
- Champions (28% of customers) generate 60%+ of total revenue
- 2009-12 cohort retained 32–56% of customers after 12+ months
- United Kingdom accounts for majority of global revenue
- 1,692 at-risk/hibernating customers identified for win-back campaign

### Files
| File | Description |
|---|---|
| `sql_queries.txt` | RFM scoring & cohort SQL queries |
| `finaluploadretailprojectt.xlsx` | Cohort heatmap + RFM output |
| `customer_segmentation_project.pbix` | Power BI dashboard |

---

## Experiment 2: A/B Test — Simulated Win-Back Campaign

Extended Experiment 1 by designing a randomized experiment on the At-Risk/Hibernating 
segments to test a hypothetical reactivation campaign, applying random assignment 
and chi-square significance testing before recommending a rollout decision.

> **Note:** Campaign outcome is simulated (Control rate is real, derived from actual 
> customer behavior; Treatment rate uses an industry-grounded uplift assumption) since 
> the source dataset has no real campaign data. This experiment demonstrates 
> experimentation methodology and statistical testing — not actual observed business 
> results.


### Results
| Metric | Control | Treatment |
| Sample size | 447 | 450 |
| Reactivated | 138 | 179 |
| Reactivation rate | 30.87% | 39.78% |

### Files
| File | Description |
| `experiment2_sql.sql` | Full SQL: cutoff segmentation, baseline calculation, random assignment, and simulated outcomes |
| `experiment2_significance_test.py` | Chi-square significance testing and confidence interval (Python) |

## Author
**MOHD SAAD**
Aspiring Product/Data Analyst
LinkedIn: [linkedin.com/in/mohd-saad-5b052429b](https://www.linkedin.com/in/mohd-saad-5b052429b)
