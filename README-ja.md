## 概要
このツールはjmeterを使用した性能検証半自動化ツールです。  
jmeterのテストプランのパラメータの設定パターンを変えて何度も検証したい場合に非常に有効なツールです。  
このツールで提供しているデフォルトの機能は以下の通りです。
- パラメータ設定の組み合わせによるjmeterの自動実行
- 各組み合わせの実行間隔の設定
- 各組合せに対するイテレーションの設定
- 各実行結果の出力先を自動設定
- それらの結果を１つにまとめる

また、シンプルな設計のため、前処理、後処理をjmeter実行前後に仕込んで任意に拡張することが容易です。

## 環境
java 11.0.18 2023-01-17 LTS  
jmeter 5.5（5.6はCLIにバグがあり正しく動きません）  
python 3.11.1  

## 性能検証
### jmeterの設定
1. テストプラン作成
2. 変更したいパラメータを変数化
    - ユーザー定義で以下のように設定  
    `parameter_name | ${__P(parameter_name)} | description`
    - 設定した変数を該当箇所に設定
### directory構成
- jmeter: jmeterのjmxなどの置き場所
    - performanceTest.jmx: 性能検証内容設定ファイル（編集はGUIで、実行は下記コード群で行うのが望ましい）
- modules: performance_test.pyで使用するモジュール
    - run_jmeter.py: jmeterの実行を行うモジュール。
- results: 検証結果を出力する場所
    - combined_statistics.py: 指定したdirectoryの配下にあるstatistics.jsonの内容を一覧にまとめてcsv出力する。エクセルに検証結果をまとめたいときに使う
- performance_test.py: ツールの本体
- setting.json: 性能検証用設定ファイル

### setting.jsonの設定
- property_sets
    - jmeterのテストプランに渡すプロパティの指定ができます。
    - プロパティの内容はjmeterのユーザー定義変数で変更することができます。
- loop_count_per_set
    - property_setsで設定したsetをそれぞれ何回繰り返して実行するかを設定します。
    - 例えば、3を設定した場合、一つのsetにつき3回同じ設定でjmeterを起動します。その後次のsetに移ります。
- wait_time
    - jmeterを連続で動かす際に、どれくらい時間を空けてから実行するかを設定します。単位は秒です。
    - cpuクレジットなどを考慮する場合に利用する設定しておくと回復を期待できます。
- result_base_folder
    - 結果を出力するフォルダを設定できます。
- test_plan
    - jmeterのテストプランのファイルを指定します。

### 実行
1. `python performance_test.py`を実行
2. 実行後、結果出力先を指定する入力を受け付けるので、任意の名前を入力   
（ディレクトリを作っておく必要はない）

## 結果を見る
1. results（結果出力ディレクトリ）に移動
2. `python -m http.server`
3. http://localhost:8000 に移動

## 一覧でcsv出力する（エクセル挿入時など）
1. results（結果出力ディレクトリ）に移動
2. combined_statistics.pyのroot_dir（5行目）を結果を一覧化したいディレクトリに変更
3. `python combined_statistics.py`を実行
4. combined_statics.csvをエクセルへ読み込み