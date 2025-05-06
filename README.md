# DelphesTree_converter

Repository with python code to convert root files produced through Delphes into pandas DataFrame. 

It's recommended to use python 3.10.4 to run the scripts, and the required libraries are stored in `requirements_coffea_env.txt`,
and can be installed doing on your terminal:
```
pip install requirements_coffea_env.txt
```

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

Use the `runner` via terminal as:

```
python3 runner --path <Path_To_The_Root> --label <label_for_the_output_file> --output_path <path_to_the_output_dir> --file_type <desired_output_type>
```

Supported output types are `parquet`, `coffea` or `csv`

Any question, please write to tatehort@cern.ch
