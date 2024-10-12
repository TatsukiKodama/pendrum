## 使用技術

## 目次

## プロジェクト名
N重振り子のシミュレーション

## 環境

## ディレクトリ構成

## 開発環境構築

下記で仮想環境を立ち上げる：  
python3 -m venv venv  
source venv/bin/activate  



pip install -r requirements.txt



## 実行方法
python -m pendrum


## ヘルプ
### 誤ってプロジェクトに関係のないファイル・フォルダをプッシュした場合

以下のように入力する：
* ファイル
git rm --cashed [ファイル名]

--cashedを付ける場合、localのファイルは削除されない。

* フォルダ
 git rm -r --cached [フォルダ名]/

 例）仮想環境venvをプッシュしてしまった場合
 git rm -r --cached venv/


