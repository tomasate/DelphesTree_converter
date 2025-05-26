# DelphesTree_converter

Repository with python code to convert root files produced through Delphes into pandas DataFrame. 

It's recommended to use python 3.10.4 to run the scripts, and the required python modules. 

## Conda instalation
If your python version is not thisone, you can get it with a conda environment. Check if you have conda installed by doing:
```
conda --version
```
If you see anything different than `conda: command not found``, you have conda. Otherwise, download it by doing

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```
once downloaded, do 
```
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
```
to install it. Follow the instructions untill the end. Once installed activate conda if you didn't activated it by default in the instalation process doing:
```
source /home/atehort/miniconda3/bin/activate
```

Now you may want to create a virtual environment for this task by doing:

```
conda create -n <name_environment> python=3.10.4
```
And activate it by doing
```
conda activate <name_environment>
```

##Instalation of the requirements
When you create the environment you'll get a bunch of modules, the otherones needed you can get them by doing
```
pip install coffea==2025.3.0
```


##Running the code
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
