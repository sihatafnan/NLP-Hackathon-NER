import pandas as pd

file = './data/train_generic_small.csv'
df = pd.read_csv(file, encoding='utf-8')
print(df.head(10))

# plot the label frequency of a dataframe
# df: dataframe
# label: label column name
# title: title of the plot
# save: save the plot to a file
def plot_label_frequency(df, label, title, save=False):
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.figure(figsize=(16, 5))
    ax = sns.countplot(x=label, data=df)
    plt.title(title)
    # plt.show()
    if save: plt.savefig("eda/" + title + '.png')

plot_label_frequency(df, 'tag', 'Label Frequency', True)


# extract and plot the top-15 word frequency of a dataframe
# df: dataframe
# label: label column name
# title: title of the plot
# save: save the plot to a file
def plot_top_15_word_frequency(df, label, title, save=False):
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.figure(figsize=(16, 5))
    ax = sns.countplot(x=label, data=df)
    plt.title(title)
    # plt.show()
    if save: plt.savefig("eda/" + title + '.png')
    

