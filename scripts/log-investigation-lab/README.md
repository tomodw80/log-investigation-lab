# Log Investigation Lab – BrightLane Bikes Incident

This project is a self-contained **security investigation lab** designed to demonstrate core SOC / blue team skills:

- Log analysis and incident reconstruction  
- Identification of indicators of compromise (IOCs)  
- Writing clear incident documentation  
- Basic automation using Python for log parsing  

The scenario is fictional but modelled on realistic attack behaviour against a small e-commerce company hosted in the cloud.

---

## 🧩 Scenario Overview

**Company:** BrightLane Bikes – an online retailer selling high-end bicycles.  
**Environment:** Web application front-end, Linux web server, and cloud storage for customer reports.  

The monitoring system has raised an alert:

> “Multiple unusual requests to `/admin` and a spike in S3 object downloads from a single IP address.”

You have been tasked with investigating the activity using the provided logs and documenting your findings as if you were working as a junior Security Analyst.

---

## 📂 Repository Structure

```text
log-investigation-lab/
├── logs/
│   ├── webserver-access.log     		# Simulated web server access logs
│   ├── auth.log                             		# SSH authentication events
│   └── cloudtrail.json                   		# Simplified cloud audit logs
│
├── scripts/
│   └── parse_logs.py                     		# Python helper script for basic log analysis
│
├── reports/
│   ├── incident-summary.md      		 # High-level incident report
│   └── timeline.md                        		 # Detailed timeline of key events
│
├── findings/
│   └── indicators-of-compromise.md  # IPs, artefacts, and notable patterns
│
├── images/                       			  # Diagrams / screenshots (optional)
│
└── README.md
