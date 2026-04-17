## Define churn  -> churn = churn_flag in subscriptions 
# churn_label = 1 if account exists in churn_events OR churn_flag == True
# else 0

# ---- Github actions ---- #
# git status
# git add .
# git commit -m ""
# git push origin main

import pandas as pd
import numpy as np

# Load data - Pull raw SaaS data from CSV files

subscriptions = pd.read_csv("subscriptions.csv") # Subscription details - start date, end date, churn flag
churn_events = pd.read_csv("churn_events.csv") # When customer left and why
accounts = pd.read_csv("accounts.csv")  # Account details

# Build churn label
churned_from_events = churn_events["account_id"].unique() # Creates a list of all accounts that ever churned according to the churn events table.
subscriptions["churn_label"] = subscriptions["churn_flag"].astype(int) # Convert churn_flag to integer (1 for True, 0 for False)

subscriptions["churn_label"] = np.where(
    subscriptions["account_id"].isin(churned_from_events),
    1,
    subscriptions["churn_label"]
)
