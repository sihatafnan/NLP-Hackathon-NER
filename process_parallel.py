import pandas as pd
from joblib import Parallel, delayed
# Read train_generic.csv
import pandas as pd

from sklearn_crfsuite import CRF
from sklearn_crfsuite import metrics


df = pd.read_csv('data/train_generic.csv')
print(df.head(10))



from bnlp import POS
bn_pos = POS()
model_path = "model/bn_pos.pkl"

def isPPR(text): 
  if(bn_pos.tag(model_path, text) == "PPR"): 
    # print("Yes PPR")
    return True
  return False 

def isStopWord(text):
  global stopwords
  return text in stopwords

def extract_sentence_features(df):
    sentence_length = len(df)

    for i in range(sentence_length):
        token = df.iloc[i]['word']

        features = {
            'bias': 1.0,
            'token.lower()': token.lower(),
            # 'isPPR(token)': isPPR(token),
            'isStopWord(token)': isStopWord(token),
            'token.isupper()': token.isupper(),
            'token.istitle()': token.istitle(),
            'token.isdigit()': token.isdigit()
        }

        if i > 0:
            previous_token = df.iloc[i-1]['word']
            features.update({
                'previous_token.lower()': previous_token.lower(),
                # 'isPPR(previous_token)': isPPR(previous_token),
                'isStopWord(previous_token)': isStopWord(previous_token),
                'previous_token.isupper()': previous_token.isupper(),
                'previous_token.istitle()': previous_token.istitle(),
                'previous_token.isdigit()': previous_token.isdigit()
            })
        else:
            features['BOS'] = True

        if i < sentence_length - 1:
            posterior_token = df.iloc[i+1]['word']
            features.update({
                'posterior_token.lower()': posterior_token.lower(),
                # 'isPPR(posterior_token)': isPPR(posterior_token),
                'isStopWord(posterior_token)': isStopWord(posterior_token),
                'posterior_token.isupper()': posterior_token.isupper(),
                'posterior_token.istitle()': posterior_token.istitle(),
                'posterior_token.isdigit()': posterior_token.isdigit()
            })
        else:
            features['EOS'] = True

        yield features

from tqdm import tqdm
def prepare(df, include_y=False):
    X, y = [], []
    for _, group_df in tqdm(df.groupby(['sentence_id'])):
        X.append(list(extract_sentence_features(group_df)))
        if include_y:
            y.append(group_df['tag'])
    if include_y:
        return X, y
    return X

def process_subset(df_subset):
    # Perform some computation on df_subset
    return df_subset



# Split the DataFrame into subsets
df_subsets = [df.iloc[i:i+1000] for i in range(0,len(df),1000)]

# Perform the computation in parallel on each subset
results = Parallel(n_jobs=-1)(delayed(process_subset)(df_subset) for df_subset in df_subsets)

# Concatenate the results
df_result = pd.concat(results)


