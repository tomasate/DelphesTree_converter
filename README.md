# DelphesTree_converter

Repository with python code to convert root files produced through Delphes into pandas DataFrame. 

The main code is stored in `dt_converter.py`. It has a class called `Converter` that can bu used as follows:

```
tree_test = Converter(fname)
    tree_test.generate({"Jet": ["PT", "Eta", "Phi", "Mass", "BTag", "TauTag"],
                        "Muon": ["PT", "Eta", "Phi", "Charge"],
                        "Electron": ["PT", "Eta", "Phi", "Charge"],
                        "MissingET": ["MET", "Phi"]})
    df = tree_test.df
```
You may include in the branches from the Delphes object that you're interested for your analysis as the example states.

Use the `split_events` from `ùtils.py` to store the dataframe split it into `.parquet/.coffea` files discriminating by the 
number of jets per event as follows:

```
split_events(df, label = 'Signal_37', path = '/store/atehort/', file_type = 'coffea')
```

Any question, please write to tatehort@cern.ch
