import argparse
from utils import split_events
from dt_converter import Converter

parser = argparse.ArgumentParser(description="Run the converter with given path to the .root file.")
parser.add_argument("-p",
                    "--path", 
                    type=str, 
                    help="Path to the .root file.")
parser.add_argument("-l",
                    "--label", 
                    type=str, 
                    help="Label to save the output file.")
parser.add_argument("-o",
                    "--output_path", 
                    type=str, 
                    help="Path to the output file.")
parser.add_argument("-f",
                    "--file_type", 
                    type=str, 
                    default="parquet",
                    help="Type of the output file.")
parser.add_argument("-jn",
                    "--jet_multiplicity", 
                    type=int, 
                    default=4,
                    help="Number of jets to keep.")
parser.add_argument("-en",
                    "--e_mu_multiplicity", 
                    type=int, 
                    default=2,
                    help="Number of electrons and muons to keep.")
args = parser.parse_args()

root_path = args.path
label = args.label
output_path = args.output_path
file_type = args.file_type
jet_multiplicity = args.jet_multiplicity
e_mu_multiplicity = args.e_mu_multiplicity

tree_test = Converter(root_path)
tree_test.generate({"Jet": ["PT", "Eta", "Phi", "Mass"],
                    "Muon": ["PT", "Eta", "Phi", "Charge"],
                    "Electron": ["PT", "Eta", "Phi", "Charge"],
                    "MissingET": ["MET", "Phi"]}, 
                    jet_elements = jet_multiplicity, e_mu_elements = e_mu_multiplicity)
df = tree_test.df
df = df.loc[~ df[f"muon_pt{e_mu_multiplicity - 1}"].isna()]
df.reset_index(drop = True, inplace = True)
df

split_events(df, label, output_path, file_type)










