## Define churn  -> churn = churn_flag in subscriptions 
# churn_label = 1 if account exists in churn_events OR churn_flag == True
# else 0

# ---- Useful Github actions ---- #
# git status
# git add .
# git commit -m ""
# git push origin main

import pandas as pd
import numpy as np

# Load data - Pull raw SaaS data from CSV files
subscriptions = pd.read_csv("ravenstack_subscriptions.csv") # Subscription details - start date, end date, churn flag
churn_events = pd.read_csv("ravenstack_churn_events.csv") # When customer left and why
accounts = pd.read_csv("ravenstack_accounts.csv")  # Account details
