# ChallengeCrimeData
 
Technical Test to evaluate my skills in Python with Pandas Library

## Solution Code
 - [Jupyter Solution](https://github.com/OMarcusCastro/ChallengeCrimeData/blob/main/teste.ipynb)
 - [Python Solution](https://github.com/OMarcusCastro/ChallengeCrimeData/blob/main/main.py)

## Steps

 - [x] Read Excel data in Victims.zip: Use zipfile.ZipFile
 - [x] Select crimes against propety without:
   - [x] totals: Remove column using  `df.drop('column_name',axis=1)` 
   - [x] index: Use `df.to_csv('file_name',index=False)`
   - [x] footer: Use `df.dropna()` removes rows with NaN values
      
