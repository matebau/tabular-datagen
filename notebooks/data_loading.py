from ucimlrepo import fetch_ucirepo
import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(dataset_id):
    dataset = fetch_ucirepo(id=dataset_id)

    X = dataset.data.features
    y = dataset.data.targets

    df = pd.concat([X, y], axis=1)
    return df

def preprocess_data(df, dataset_id):

    df = df.replace('?', pd.NA)
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()
        df[col] = df[col].fillna('Missing')

    if dataset_id == 2:
        df["income"] = df["income"].str.rstrip(".")

    return df

def split_data(df, target):
    train_df, test_df = train_test_split(
        df,
        test_size=0.2,
        random_state=42,
        stratify=df[target]
    )
    return train_df, test_df

def prepare_tabddpm_data():
    return
        