# ChallengeCrimeData
 
Technical Test to evaluate my skills in Python with Pandas Library

Run scrapping.py. Results in path './dowlaods' that will be created.
## Steps

 - [x] Scrapping with selenium:  headless mode, untrack driver automations
 - [x] Read Excel data in Victims.zip: Use zipfile.ZipFile
 - [x] Select crimes against propety without:
   - [x] totals: Remove column using  `df.drop('column_name',axis=1)` 
   - [x] index: Use `df.to_csv('file_name',index=False)`
   - [x] footer: Use `df.dropna()` removes rows with NaN values
