import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
file_path = '/Users/daniellethompson/Desktop/CNP Project/IDEA_Public_Schools.csv'
data = pd.read_csv(file_path)


# 1. Participation Analysis
participation_stats = data.groupby('SiteName')[['BreakfastADP', 'LunchADP', 'SnackADP']].mean().reset_index()
print("Participation Statistics:")
print(participation_stats)

# Schools with highest and lowest lunch participation
top_participation = data.groupby('SiteName')['LunchADP'].mean().nlargest(5).reset_index()
bottom_participation = data.groupby('SiteName')['LunchADP'].mean().nsmallest(5).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='LunchADP', y='SiteName', data=top_participation)
plt.title('Top 5 Schools by Average Daily Lunch Participation')
plt.xlabel('Average Daily Lunch Participation')
plt.ylabel('School Name')
plt.tight_layout()
plt.savefig('/Users/daniellethompson/Desktop/CNP Project/highest_reimbursements_trend.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='LunchADP', y='SiteName', data=bottom_participation)
plt.title('Bottom 5 Schools by Average Daily Lunch Participation')
plt.xlabel('Average Daily Lunch Participation')
plt.ylabel('School Name')
plt.tight_layout()
plt.savefig('/Users/daniellethompson/Desktop/CNP Project/lowest_reimbursements_trend.png')
plt.show()

# 2. Reimbursement Analysis
top_reimbursements = data.groupby('SiteName')['TotalReimbursement'].sum().nlargest(5).reset_index()
bottom_reimbursements = data.groupby('SiteName')['TotalReimbursement'].sum().nsmallest(5).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='TotalReimbursement', y='SiteName', data=top_reimbursements)
plt.title('Top 5 Schools by Total Reimbursement')
plt.xlabel('Total Reimbursement')
plt.ylabel('School Name')
plt.tight_layout()
plt.savefig('/Users/daniellethompson/Desktop/CNP Project/total_reimbursements_trend.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='TotalReimbursement', y='SiteName', data=bottom_reimbursements)
plt.title('Bottom 5 Schools by Total Reimbursement')
plt.xlabel('Total Reimbursement')
plt.ylabel('School Name')
plt.tight_layout()
plt.savefig('/Users/daniellethompson/Desktop/CNP Project/bottom_reimbursements_trend.png')
plt.show()

# Correlation between meals served and reimbursements
meal_reimbursement_corr = data[['BreakfastTotal', 'LunchTotal', 'SnackTotal', 'TotalReimbursement']].corr()
print("Correlation between Meals Served and Reimbursements:")
print(meal_reimbursement_corr)

# 3. Equity Analysis
hidalgo_data = data[data['SiteCounty'] == 'Hidalgo']
meal_eligibility_distribution = data.groupby('SiteName')[['FreeEligibleQty', 'ReducedEligibleQty', 'PaidEligibleQty']].sum().reset_index()
print("Meal Eligibility Distribution 2017-2018:")
print(meal_eligibility_distribution)

plt.figure(figsize=(10, 6))
meal_eligibility_distribution.set_index('SiteName').plot(kind='bar', stacked=True)
plt.title('Distribution of Meal Eligibility by School 2017-2018')
plt.xlabel('School Name')
plt.ylabel('Number of Students')
plt.legend(title='Eligibility Type')
plt.tight_layout()
plt.savefig('/Users/daniellethompson/Desktop/CNP Project/eligibility.png')
plt.show()
