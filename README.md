# my-full-16type-app

Pythonで作成した100問構成の16タイプ性格診断プログラムです。

## 特徴
- 質問100問をJSONファイルで管理
- スコアリング方式による性格タイプ判定
- CLI（コマンドラインインターフェース）での提供

## セットアップと実行

1. リポジトリをクローンします：
   ```bash
   git clone https://github.com/pikapika-hikaru/my-full-16type-app.git
   cd my-full-16type-app
   ```

2. プログラムを実行します：
   ```bash
   python type16_app.py
   ```

## 使い方
画面に表示される100個の質問に対して、1（全く当てはまらない）から5（非常に当てはまる）の数字で回答してください。すべての回答が終わると、性格タイプが表示されます。

## ファイル構成
- `type16_app.py`: メインのプログラムロジック
- `questions.json`: 診断用の質問データ
