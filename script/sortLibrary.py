import pandas as pd
import re
import glob
import sys
import os

# 引数からディレクトリを取得
if len(sys.argv) != 2:
    print("Usage: python sortLibrary.py <directory>")
    sys.exit(1)

directory = sys.argv[1]

# ディレクトリが存在するかチェック
if not os.path.isdir(directory):
    print(f"Error: Directory {directory} does not exist.")
    sys.exit(1)

# ディレクトリ内のファイルパスを作成
methods_file = os.path.join(directory, 'methods.csv')
dataids_file = os.path.join(directory, 'dataids.csv')

# ファイルの読み込み
methods_df = pd.read_csv(methods_file)
dataids_df = pd.read_csv(dataids_file)

# "log"で始まるすべてのファイルを読み込む
log_files = sorted(glob.glob(os.path.join(directory, 'log*.csv')))
log_df_list = [pd.read_csv(log_file, header=None) for log_file in log_files]

# リストの作成(MethodID, MethodName)
mid_mname_list = []
testmid_list = []

for index, row in methods_df.iterrows():
    method_name = row['MethodName']
    method_id = row['MethodID']
    
    # メソッド名がtestで始まるか
    if method_name.startswith('test'):
        testmid_list.append(method_id)
        work_list = []
        work_list.append(method_id)
        work_list.append(method_name)
        mid_mname_list.append(work_list)

print(mid_mname_list)

# リストの作成(methodID, Entry地点のdataID, Exit地点のdataID)
mid_start_end = []

for index, row in dataids_df.iterrows():
    if row['EventType'] == 'METHOD_NORMAL_EXIT':
        if row['MethodID'] in testmid_list:
            work_list.append(row['DataID'])
            mid_start_end.append(work_list)

    if row['EventType'] == 'METHOD_ENTRY':
        if row['MethodID'] in testmid_list:
            work_list = []
            work_list.append(row['MethodID'])
            work_list.append(row['DataID'])

print(mid_start_end)

# リストの作成(MethodID, [MethodID毎のDataIDリスト])
mid_did_list = []

for se in mid_start_end:
    work_list = []
    dataid_list = []
    mode = 0
    work_list.append(se[0])
    
    for log_df in log_df_list:
        for index in log_df[1]:
            if mode == 1:
                if index == se[2]:
                    work_list.append(dataid_list)
                    mid_did_list.append(work_list)
                    break
                dataid_list.append(index)
            if index == se[1]:
                mode = 1

print(mid_did_list)

# リストの作成(MethodID, [ライブラリのリスト])
filtered_dataids_df = dataids_df[dataids_df['EventType'] == 'CALL']

i = 0
mid_lname_list = []
for id in mid_did_list:
    work_list = []
    name_list = []
    work_list.append(id[0])
    for index, row in filtered_dataids_df.iterrows():
        if row['DataID'] in id[1]:
            match = re.search(r"owner=([\w/]+)", row['Attributes'])
            library_name = match.group(1)
            name_list.append(library_name)
    name_list = list(set(name_list))
    work_list.append(name_list)
    mid_lname_list.append(work_list)

print(mid_lname_list)
