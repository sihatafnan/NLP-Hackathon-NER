file = './data/train_generic_small.csv'
import pandas as pd

# group by first column sentence_id and create pair of 2nd and 3rd column (word , tag)
# group by sentence_id and create list of words and list of tags

# split by newline
cnt = 0
with open(file) as f:
    # read csv file as pandas dataframe
    df = pd.read_csv(f, sep=',', header=None, names=['Sentence_id', 'Word', 'Tag'])
    # group by sentence_id and create list of words and list of tags
    df = df.groupby('Sentence_id').agg({'Word': lambda x: list(x), 'Tag': lambda x: list(x)})
    # create pair of 2nd and 3rd column (word , tag)
    df['word_tag'] = df.apply(lambda x: list(zip(x['Word'], x['Tag'])), axis=1)
    # create list of pair of 2nd and 3rd column (word , tag)
    word_tag_list = df['word_tag'].tolist()
    
    #print(word_tag_list)


samples = word_tag_list
# divide samples into train and test and validation
# 80% train, 10% test, 10% validation

