# Name: Daniel Masters
# Spring 2022
# Section: 31883
# ITP 216 Lab 13

import matplotlib.pyplot as plt
import pandas as pd


def main():
    # import data and set up figure params
    df = pd.read_csv("penguins.csv")
    fig, ax = plt.subplots(2, 1)

    # clean data, group by species, and set up colors list
    df = df.dropna()
    species_list = df["species"].unique()
    df_grouped = df.groupby("species")
    colors = ["orange", "magenta", "cyan"]

    # bar plot
    df.round({"flipper_length_mm": 0})
    count = []
    for species in species_list:
        count.append(df_grouped.get_group(species)["flipper_length_mm"].value_counts())
    for i, species in enumerate(species_list):
        ax[0].bar(count[i].index, count[i].values,
                  width=1, label=species, alpha=0.4, color=colors[i])
    ax[0].set(title="Penguin flipper lengths (BAR)",
              xlabel="Flipper length (mm)", ylabel="Frequency")
    ax[1].grid(which='major', color='#999999', alpha=0.2)
    ax[0].legend()

    # histogram
    for i, species in enumerate(species_list):
        ax[1].hist(df_grouped.get_group(species)["flipper_length_mm"],
                   bins=36, alpha=0.4, color=colors[i], label=species)
    ax[1].set(title="Penguin flipper lengths (HIST)",
              xlabel="Flipper length (mm)", ylabel="Frequency")
    ax[1].grid(which='major', color='#999999', alpha=0.2)
    ax[1].legend()

    # format and show
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()


def main2():
    df = pd.read_csv("penguins.csv")
    df = df.dropna()

    fig, ax = plt.subplots(2, 1)

    # do the things with new dataframes
    adelie = df[df["species"] == "Adelie"]
    chinstrap = df[df["species"] == "Chinstrap"]
    gentoo = df[df["species"] == "Gentoo"]

    ax[0].scatter(x=adelie["flipper_length_mm"], y=adelie["bill_length_mm"], color="blue", marker="*",
                  label="Adelie")
    ax[0].scatter(x=chinstrap["flipper_length_mm"], y=chinstrap["bill_length_mm"], color="#FF00FF", marker="D",
                  label="Chinstrap")
    ax[0].scatter(x=gentoo["flipper_length_mm"], y=gentoo["bill_length_mm"], color="green", marker="^",
                  label="Gentoo")
    ax[0].set(title="individual species")
    ax[0].legend()

    # do the things with groups (slightly longer, but more abstracted!
    species_list = list(df["species"].unique())
    df_grouped = df.groupby("species")
    color_list = ["blue", "#FF00FF", "green"]
    marker_list = ["*", "D", "^"]
    index = 0
    for species in species_list:
        df_group = df_grouped.get_group(species)
        ax[1].scatter(x=df_group["flipper_length_mm"], y=df_group["bill_length_mm"], color=color_list[index],
                      marker=marker_list[index], label=species)
        index += 1
        print(species, end=": ")
        print(df_group["flipper_length_mm"].mean())
    ax[1].set(title="with groups")
    ax[1].legend()

    plt.tight_layout()
    plt.show()
