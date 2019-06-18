import Philipsamppython
import os
import pandas as pd
import pickle
import argparse
import json
import base64
from StringIO import StringIO

# create server object
ex = Philipsamppython.AMP()

# intialize sparkContext, sqlContext
# ex.InitializeAMPConfig(conffile="../../../Release/MlServer/bin/bdamlconf.json")
ex.InitializeAMPConfig(conffile=os.path.join(os.environ.get('CONFIG_FILE_PATH'),"bdamlconf.json"))

# parse the input arguments
parser = argparse.ArgumentParser()
parser.add_argument('inputdata', type=str, help="base64 of CSV file content")
args = parser.parse_args()
# Get 'AdditionalParams' argument
input_data = json.loads(args.inputdata)['additionalParams']
sample_data = base64.standard_b64decode(input_data)
validation_df_scikit = pd.read_csv(StringIO(sample_data), delimiter=',')

feature_columns = []
for col in validation_df_scikit.columns:
    if col != 'Class' and col != 'Bare Nuclei':
        feature_columns.append(col)
        
print feature_columns
feature_data_validation = validation_df_scikit.as_matrix(columns=feature_columns)

# some time later...
 
# load the model from disk
loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
result = loaded_model.predict(feature_data_validation)
df = pd.DataFrame(result)
print(df)
ex.AMPSetResult(dataframe=df)