import pandas as pd

#ファイルの読み込み
methods_df = pd.read_csv('methods.csv')
dataids_df = pd.read_csv('dataids.csv')
log_df = pd.read_csv('log-00001.csv', header=None)

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

#リストの作成(methodID, Entry地点のdataID, Exit地点のdataID)
methodIdLibrary_list = []

dataids_df = dataids_df.dropna(subset=['Attributes'])
for index, row in dataids_df.iterrows():
    index = 0
    if row['EventType'] == 'METHOD_ENTRY':
        idList = []
        method_id = row['MethodID']
        idList.append(method_id)
        idList.append(row['DataID'])
        methodIdLibrary_list.append(idList)
    if row['EventType'] == 'METHOD_EXCEPTIONAL_EXIT':
        methodIdLibrary_list[method_id].append(row['DataID'])
print(methodIdLibrary_list)

midDid_list = []
method_id = 0
mode = 0
for row in log_df[1]:
    if mode == 0:
        if row == methodIdLibrary_list[method_id][1]:
            idList = []
            idList.append(row)
            mode = 1
    if mode == 1:
        if row == methodIdLibrary_list[method_id][2]:
            method_id = method_id + 1
            mode = 0
            print(idList)
            midDid_list.append(idList)
        else:
            idList.append(row)
print(midDid_list)
        


