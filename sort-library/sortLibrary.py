import pandas as pd

#ファイルの読み込み
methods_df = pd.read_csv('methods.csv')
dataids_df = pd.read_csv('dataids.csv')
log_df = pd.read_csv('log-00001.csv')

#辞書の作成(key:メソッド名 value:メソッドIDのリスト)
methodNameID_dict = {}
current_method = None

for index, row in methods_df.iterrows():
    method_name = row['MethodName']
    method_id = row['MethodID']
    
    #メソッド名がtestで始まるか
    if method_name.startswith('test'):
        #新しいtestメソッドのときにMethodIDのリストを初期化
        current_method = method_name
        methodNameID_dict[current_method] = [method_id]
    else:
        #testメソッドでないときMethodIDを現在のメソッドのリストに追加
        if current_method:
            methodNameID_dict[current_method].append(method_id)

print(methodNameID_dict)

#辞書の作成(key:メソッド名 value:ライブラリのリスト)
methodNameLibrary_dict = {}

dataids_df = dataids_df.dropna(subset=['Attributes'])
