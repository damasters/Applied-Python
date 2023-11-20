import pandas as pd

# df = pd.DataFrame({"Name": ["Patrick", "Gary", "Sandy"], "Age": (33, 24, 29), "Height (cm)": pd.Series([23, 45, 17])})
# print(df)
# # print(df.iloc[1])
# print(df.loc[1])
#
# ser = np.random.rand(10)*10
# print(ser, '\n')
# ser = ser.astype('int')
# print(ser)
from matplotlib import pyplot as plt

df = pd.read_csv("penguins.csv")
# print(df.head())
# print("NaNs:", df.isnull())
# print("shape:", df.shape)
# df = df.dropna()
# print("shape after drop:", df.shape)
#
# df["body_mass_g"] = df["body_mass_g"].div(1000)
# df = df.rename(columns={"body_mass_g": "body_mass_kg"})
# print(df.head())
#
# five_kg_plus = df[df["body_mass_kg"] > 5]
# print(five_kg_plus.head())

# fig, ax = plt.subplots(1, 1)
# ax.scatter(x=df["flipper_length_mm"], y=df["bill_length_mm"])
# plt.show()
print(df["species"].unique())
adelie = df[df["species"] == "Adelie"]
chinstrap = df[df["species"] == "Chinstrap"]
gentoo = df[df["species"] == "Gentoo"]

fig, ax = plt.subplots(1, 1)
# ax.scatter(x=adelie["flipper_length_mm"], y=adelie["bill_length_mm"], color="blue", marker="*", label="Adelie")
# ax.scatter(x=chinstrap["flipper_length_mm"], y=chinstrap["bill_length_mm"], color="#FF00FF", marker="D", label="Chinstrap")
# ax.scatter(x=gentoo["flipper_length_mm"], y=gentoo["bill_length_mm"], color="green", marker="^", label="Gentoo")
species_list = df["species"].unique()
df_grouped = df.groupby("species")
color_list = ["blue", "#FF00FF", "green"]
marker_list = ["*", "D", "^"]
index = 0
for species in species_list:
    df_group = df_grouped.get_group(species)
    ax.scatter(x=df_group["flipper_length_mm"], y=df_group["bill_length_mm"], color=color_list[index], marker=marker_list[index], label=species)
    index += 1
ax.legend()

fig.tight_layout()
plt.show()



