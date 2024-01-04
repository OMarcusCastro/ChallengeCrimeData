import pandas as pd
import zipfile

ZIP = 'victims.zip'
FILENAME = 'Victims_Age_by_Offense_Category_2022.xlsx'


archive = zipfile.ZipFile(ZIP, 'r')
xlfile = archive.open(FILENAME)

victims_df = pd.read_excel(xlfile)

victims_df.columns = ['Offense Category', 'Total Victims', '10 and Under', '11-15',
                      '16-20', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51-55',
                      '56-60', '61-65', '66 and orver', 'Unknown age']

category_index = victims_df.loc[(victims_df['Offense Category'] ==
                                 'Crimes Against Property')].index.values[0]

start_category_index = category_index + 1

categories_df = victims_df.iloc[start_category_index::].drop(
    'Total Victims', axis=1).dropna().reset_index(drop=True)


categories_df.to_csv('victims.csv', index=False)
