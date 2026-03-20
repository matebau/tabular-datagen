# Exploratory Data Analysis (EDA)

This folder contains initial exploratory data analyses for three benchmark tabular datasets from the UCI Machine Learning Repository:

- **Adult**: predicts whether a person’s annual income exceeds \$50K based on census-related attributes. The dataset has **48,842 instances**, **14 input features**, and includes some missing values. :contentReference[oaicite:0]{index=0}
- **Default of Credit Card Clients**: predicts default payment for Taiwanese credit card clients. The dataset has **30,000 instances**, **23 input features**, and no missing values are reported in the original source. :contentReference[oaicite:1]{index=1}
- **Bank Marketing**: predicts whether a client subscribes to a term deposit after direct marketing calls by a Portuguese banking institution. The dataset has **45,211 instances**, **16 input features**, and no missing values are reported in the original source. :contentReference[oaicite:2]{index=2}

Official dataset pages:
- Adult: https://archive.ics.uci.edu/dataset/2/adult
- Default of Credit Card Clients: https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients
- Bank Marketing: https://archive.ics.uci.edu/dataset/222/bank+marketing

The notebooks in this folder examine dataset structure, variable types, missing values, duplicates, distributions, category balance, correlations, and initial preprocessing considerations. The goal is to understand the main characteristics of each dataset before applying baseline models or synthetic tabular data generation methods.
