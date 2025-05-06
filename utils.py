import numpy as np
import pandas as pd
from coffea.util import load
from coffea.util import save

def split_events_in_parquets(df:pd.DataFrame, label:str, path:str = "./")->None:
    """
    Split the events in the dataframe into different parquets based on the number of jets.
    Args:
        df: pd.DataFrame
            The dataframe to split.
        label: str
            The label of the dataframe.
        path: str
            The path to save the parquets.
    Returns:
        None
    """
    split_crit_df = df.loc[:,['jet_pt0', 'jet_pt1', 'jet_pt2', 'jet_pt3']].isna().sum(axis = 1)*-1 + 4
    index_2 = split_crit_df[split_crit_df ==2].index.tolist()
    index_3 = split_crit_df[split_crit_df ==3].index.tolist()
    index_4 = split_crit_df[split_crit_df ==4].index.tolist()
    df2 = df.copy().loc[index_2]
    df3 = df.copy().loc[index_3]
    df4 = df.copy().loc[index_4]
    

    save(df2, f"{path}/{label}_2jets.parquet")
    save(df3, f"{path}/{label}_3jets.parquet")
    save(df4, f"{path}/{label}_4jets.parquet")

    
    