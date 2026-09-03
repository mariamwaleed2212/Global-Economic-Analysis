import pandas as pd 
df=pd.read_csv("dataset/world_bank_data_2025.csv")
df_clean=df[df["year"]<=2023].copy()

columns_to_remove= [ "Interest Rate (Real, %)",
    "Government Expense (% of GDP)",
    "Government Revenue (% of GDP)",
    "Tax Revenue (% of GDP)",
    "Public Debt (% of GDP)"]

df_clean=df_clean.drop(columns=columns_to_remove)
print ("---data availablity---")

available=df_clean.notnull().sum()

print ("\n available values : ")
print (available)

print ("\n total raws :",len(df_clean))

print ("\n availability precentage:")
print ((df_clean.notnull().mean()*100).round(2))






df_clean.to_csv(
    "dataset/cleaned_economic_data.csv",
    index=False
)
print ("\n ----- clean dataset saved -----")
print ("file : dataset/cleaned_economic_data.csv" )




print ("\n ----- basic statics ----")
print (df_clean.describe())

financial_columns =["Inflation (CPI %)",
    "GDP (Current USD)",
    "GDP per Capita (Current USD)",
    "Unemployment Rate (%)",
    "GDP Growth (% Annual)",
    "Current Account Balance (% GDP)"
]


print("\n===== CLEAN DATASET COLUMNS =====")
print(df_clean.columns.tolist())

top_gdp = (
    df_clean.groupby("country_name")["GDP (Current USD)"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\n===== TOP 10 COUNTRIES BY AVERAGE GDP =====")
print(top_gdp)






import matplotlib.pyplot as plt

top_gdp.sort_values().plot(
    kind="barh",
    figsize=(10,6)
)
plt.title("top 10 countries by avarge GDP (2010-2023)")
plt.xlabel("avarge GDP (USD)")
plt.ylabel("country")

plt.tight_layout()
plt.show()



top_gdp_trillions = top_gdp / 1_000_000_000_000

top_gdp_trillions.sort_values().plot(
    kind="barh",
    figsize=(10, 6)
)

plt.title("Top 10 Countries by Average GDP (2010–2023)")
plt.xlabel("Average GDP (Trillion USD)")
plt.ylabel("Country")

plt.tight_layout()
plt.show()




top_growth = (
    df_clean.groupby("country_name")["GDP Growth (% Annual)"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\n===== TOP 10 COUNTRIES BY AVERAGE GDP GROWTH =====")
print(top_growth)




top_growth.sort_values().plot(
    kind="barh",
    figsize=(10, 6)
)

plt.title("Top 10 Countries by Average GDP Growth (2010-2023)")
plt.xlabel("Average GDP Growth (%)")
plt.ylabel("Country")

plt.tight_layout()
plt.show()




top_inflation = (
    df_clean.groupby("country_name")["Inflation (CPI %)"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\n===== TOP 10 COUNTRIES BY AVERAGE INFLATION =====")
print(top_inflation)


# ===== INFLATION CHART =====

top_inflation.sort_values().plot(
    kind="barh",
    figsize=(10, 6)
)

plt.title("Top 10 Countries by Average Inflation (2010-2023)")
plt.xlabel("Average Inflation (%)")
plt.ylabel("Country")

plt.tight_layout()
plt.show()


top_unemployment = (
    df_clean.groupby("country_name")["Unemployment Rate (%)"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\n===== TOP 10 COUNTRIES BY AVERAGE UNEMPLOYMENT =====")
print(top_unemployment)


top_unemployment.sort_values().plot(
    kind="barh",
    figsize=(10, 6)
)

plt.title("Top 10 Countries by Average Unemployment (2010-2023)")
plt.xlabel("Average Unemployment Rate (%)")
plt.ylabel("Country")

plt.tight_layout()
plt.show()



# ===== TOP 10 COUNTRIES BY AVERAGE CURRENT ACCOUNT BALANCE =====

top_current_account = (
    df_clean.groupby("country_name")["Current Account Balance (% GDP)"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\n===== TOP 10 COUNTRIES BY AVERAGE CURRENT ACCOUNT BALANCE =====")
print(top_current_account)



# ===== CURRENT ACCOUNT BALANCE CHART =====

top_current_account.sort_values().plot(
    kind="barh",
    figsize=(10, 6)
)

plt.title("Top 10 Countries by Average Current Account Balance (2010-2023)")
plt.xlabel("Average Current Account Balance (% GDP)")
plt.ylabel("Country")

plt.tight_layout()
plt.show()



