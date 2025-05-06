import argparse
from utils import split_events
from dt_converter import Converter

parser = argparse.ArgumentParser(description="Run the converter with given path to the .root file.")
parser.add_argument("--path", 
                    type=str, 
                    help="Path to the .root file.")
parser.add_argument("--label", 
                    type=str, 
                    help="Label to save the output file.")
parser.add_argument("--output_path", 
                    type=str, 
                    help="Path to the output file.")
parser.add_argument("--file_type", 
                    type=str, 
                    default="parquet",
                    help="Type of the output file.")
args = parser.parse_args()

root_path = args.path
label = args.label
output_path = args.output_path
file_type = args.file_type

tree_test = Converter(root_path)
tree_test.generate({"Jet": ["PT", "Eta", "Phi", "Mass"],
                    "Muon": ["PT", "Eta", "Phi", "Charge"],
                    "Electron": ["PT", "Eta", "Phi", "Charge"],
                    "MissingET": ["MET", "Phi"]})
df = tree_test.df

split_events(df, label, output_path, file_type)










