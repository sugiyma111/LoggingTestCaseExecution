#!/bin/bash

# カレントディレクトリのパスを取得
current_dir=$(pwd)

# ログファイルのコピー先を保存するディレクトリを作成
timestamp=$(date +"%Y%m%d%H%M%S")
new_dir="$current_dir/$timestamp"
mkdir $new_dir

# 引数で選択したディレクトリ(dir2)に移動する
if [ -z "$1" ]; then
  echo "エラー: ディレクトリパスを引数として指定してください。"
  exit 1
fi

dir2=$1
if [ ! -d "$dir2" ]; then
  echo "エラー: 指定されたディレクトリが存在しません。"
  exit 1
fi

cd $dir2

# 選択したディレクトリでテスト実行
mvn -DargLine="-Xmx4g -Xms1024m -javaagent:../selogger-0.5.1.jar=format=omni,weaverlog=log.txt,output={time},weave=EXEC+CALL,e=org/junit,e=org/apache/maven,e=org/opentest4j" test

# 降順にした際に一番最初のディレクトリ(dir3)に移動する
echo "Available directories:"
ls -d */
dir3=$(ls -d */ | grep -E '^[0-9]{8}-[0-9]{9}/$' | sort -r | head -n 1)
if [ -z "$dir3" ]; then
  echo "エラー: 該当するディレクトリが見つかりません。"
  exit 1
fi

echo "Navigating to directory: $dir3"
cd $dir3

# dir3のtxtファイルをcsvに変換して保存
echo "Copying .txt files to $new_dir as .csv files"
for file in *.txt; do
  if [[ ! "$file" =~ ^'.*' ]]; then
    cp "$file" "$new_dir/${file%.txt}.csv"
    echo "Copied $file to $new_dir/${file%.txt}.csv"
  else
    echo "Skipping $file"
  fi
done

# ライブラリ抽出のプログラムを実行
cd $new_dir
python3 ../sortLibrary.py $new_dir
