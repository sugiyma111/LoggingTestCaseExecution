import pandas as pd

#CSVファイルのパス
csv_methods = 'methods.csv'
csv_dataids = 'dataids.csv'

#csvの読み込み
methods_df = pd.read_csv(csv_methods)
dataids_df = pd.read_csv(csv_dataids)

#ライブラリを読み込んでいる行を抜き出す
dataids_df['Library'] = dataids_df['Attributes'].str.extract(r'owner=([^,]+)')
dataids_df = dataids_df.dropna(subset=['Library'])

#必要なラベルを取り出す
library_usage_df = dataids_df[['ClassID', 'MethodID', 'Library']]

#メソッドとライブラリのdfを左結合
merged_df = pd.merge(methods_df, library_usage_df, on=['ClassID', 'MethodID'], how='left')

method_library_usage = merged_df[['ClassName', 'MethodName', 'Library']].drop_duplicates().reset_index(drop=True)

print(method_library_usage)

method_library_usage.to_csv('./method_library_usage.csv', index=False)  
