import Philipsamppython
import os
import pandas as pd
import pickle
# create server object
ex = Philipsamppython.AMP()

# intialize sparkContext, sqlContext
# ex.InitializeAMPConfig(conffile="../../../Release/MlServer/bin/bdamlconf.json")
ex.InitializeAMPConfig(conffile=os.path.join(os.environ.get('CONFIG_FILE_PATH'),"bdamlconf.json"))

data_path_str_validation_scikit = "/var/lib/dsp/dspvolume/data/BreastCancerTest_scikit.csv"

validation_df_scikit = pd.read_csv(data_path_str_validation_scikit)
feature_columns = []
for col in validation_df_scikit.columns:
    if col != 'Class' and col != 'Bare Nuclei':
        feature_columns.append(col)
        
print feature_columns
feature_data_validation = validation_df_scikit.as_matrix(columns=feature_columns)

# some time later...
 
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.predict(feature_data_validation)
df = pd.DataFrame(result)
print(df)
ex.AMPSetResult(dataframe=df)