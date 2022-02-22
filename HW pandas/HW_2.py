import pandas as pd
# import matplotlib.pyplot as plt
import seaborn as sns

# 1
reads_inf = pd.read_csv('https://raw.githubusercontent.com/Serfentum/bf_course/master/14.pandas/train.csv')
reads_inf_nucl = reads_inf.drop(["reads_all", "matches", "mismatches", "deletions", "insertions", "A_fraction",
                                "T_fraction", "G_fraction", "C_fraction"], axis=1)
sns.set_palette("Set2")
reads_inf_nucl.plot(x="pos", y=["A", "C", "G", "T"],  kind='bar')
reads_inf_nucl_in = reads_inf_nucl.set_index("pos")
sns.displot(reads_inf_nucl_in)
reads_inf_nucl.iloc[:, 1:] = reads_inf_nucl.iloc[:, 1:].div(reads_inf_nucl.iloc[:, 1:].sum(1), axis=0).mul(100)
reads_inf_nucl.plot(x="pos", y=["A", "C", "G", "T"], kind='bar')

# 2
mean_matches = reads_inf["matches"].mean()
train_part = reads_inf.loc[reads_inf["matches"] > mean_matches]
train_part = train_part.filter(items=["pos", "reads_all", "mismatches", "deletions", "insertions"])
train_part.to_csv('train_part', sep='\t', index=False)

# 3
data_path = 'Mall_Customers.csv'
customers_data = pd.read_csv(data_path)
customers_data.describe()
# customers_data.dtypes
sns.set_palette("crest")
sns.pairplot(customers_data)
sns.set_palette("Set2")
sns.lmplot(y='Annual Income (k$)', x='Spending Score (1-100)', hue='Gender')
sns.set_palette("icefire")
sns.displot(customers_data, x="Spending Score (1-100)", hue="Gender", multiple="dodge")
