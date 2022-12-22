
import pandas as pd
pd.set_option("display.max_rows", None)
df = pd.read_csv('dataset/persona.csv')
df.head()
df.isnull().sum()
df.shape
df.info()

df["SOURCE"].nunique()
df["SOURCE"].value_counts()
df["PRICE"].value_counts()
df["COUNTRY"].value_counts()
df.groupby("COUNTRY")["PRICE"].count()
df.pivot_table(values="PRICE",index="COUNTRY",aggfunc="sum")
df["SOURCE"].value_counts()
df.groupby('COUNTRY').agg({"PRICE": "mean"})
df.groupby('SOURCE').agg({"PRICE": "mean"})
df.groupby(["COUNTRY", 'SOURCE']).agg({"PRICE": "mean"})

df.groupby(["COUNTRY", 'SOURCE', "SEX", "AGE"]).agg({"PRICE": "mean"}

sub_df = df.groupby(["COUNTRY", 'SOURCE', "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
sub_df.head()

sub_df.reset_index(inplace=True)

divide_points = [0, 18, 24, 32, 40, sub_df["AGE"].max()]

age_cat_labels = ["0_18", "19_24", "25_32", "33_40", "41_" + str(sub_df["AGE"].max())]

sub_df["age_cat"] = pd.cut(sub_df["AGE"], divide_points, labels=age_cat_labels)
sub_df.head()

sub_df['customers_level_based'] = sub_df[['COUNTRY', 'SOURCE', 'SEX', 'age_cat']].agg(lambda x: '_'.join(x).upper(), axis=1)

sub_df = sub_df[["customers_level_based", "PRICE"]]

sub_df = sub_df.groupby("customers_level_based").agg({"PRICE": "mean"})

sub_df = sub_df.reset_index()

sub_df["SEGMENT"] = pd.qcut(sub_df["PRICE"], 4, labels=["D", "C", "B", "A"])
sub_df.head(30)
sub_df.groupby("SEGMENT").agg({"PRICE": "mean"})

new_user1 = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]

new_user2 = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]






