# LocoTOML

LocoTOMLは、Pythonで最も軽量なPythonプログラムの多言語対応のための全く新しいライブラリです。
標準ライブラリのみを使用し、外部依存は全くありません。

ただしLocoTOMLは、[LocoCore](https://github.com/drago-suzuki58/LocoCore)というコアライブラリに依存しています。LocoCoreは、共通の多言語対応機能を提供し、LocoTOMLはその上にTOML形式の翻訳機能を追加します。

English README
[English](README.md)

## 機能

- **簡単な呼び出し**:

  `loc.key1.key2.key3()`のように記述するだけで簡単に翻訳を呼び出せて、コードの可読性も向上します。詳細については、ドキュメントをご覧ください。

- **柔軟な呼び出し**:

  今このときだけ英語で出力したい！というときにもloc.key1("en")のようにするだけで言語を一時的に変えることができます。

- **TOML形式でわかりやすい翻訳**:

  翻訳はTOML形式で、各言語に対応したファイルを簡単に読み込むことができます。

- **翻訳の階層構造**:

  複数のキーを階層的に扱えて、key1.key2.key3のように取得でき、データが多くなった場合にも快適に使用できます。

- **ログの詳細出力**:

  翻訳キーが不完全だった場合やエラーが発生した際に、該当箇所のファイル名と行数を含む詳細なログが出力され、トラブルシューティングが簡単に行えます。

- **フォールバック**:

  言語に対応する翻訳が見つからない場合、設定したデフォルト言語に自動でフォールバックします。また、翻訳が全くない場合は、翻訳IDをそのまま出力し、開発者に明確に通知します。

## インストール方法

PyPIからインストール

```sh
pip install locotoml
```

または、GitHubリポジトリよりインストールが可能です

```sh
python -m pip install git+https://github.com/drago-suzuki58/LocoTOML
```

## サンプルコード

基本的な使用

`main.py`
```python
from locotoml import LocoTOML

# 出力する基本の言語が日本語で、フォールバック言語が英語
loc = LocoTOML(locale="ja", fallback_locale="en", locale_dir="loc")

# こんにちは
print(loc.greeting.hello())

# こんにちは！太郎さん
print(loc.greeting.hello_to_user(user="太郎"))
```

一時的に言語を指定して翻訳を取得

`main.py`
```python
# Hello
print(loc.greeting.hello("en"))

# Hello! John
print(loc.greeting.hello_to_user("en", user="John"))
```

フォールバックが起きる場合
その呼び出された該当行と該当のファイル名を通知して開発をサポートします

`main.py`
```python
# Log: 2024-11-17 20:23:03 | WARNING    | main.py:18 - Missing translation: greeting.hello in: fr, return key name
# Hello
print(loc.greeting.hello("fr")) # 存在しない翻訳言語

# Log: 2024-11-17 20:23:03 | WARNING    | main.py:23 - Missing translation: greeting.goodbye in: ja, falling back to en
# Log: 2024-11-17 20:23:03 | WARNING    | main.py:25 - Missing translation: greeting.goodbye in: en, return key name
# greeting.goodbye
print(loc.greeting.goodbye())
```

不要な引数が渡された場合
ログでフォールバック同様に該当行と該当のファイル名を通知します

`main.py`
```python
# Log: 2024-11-17 20:23:03 | WARNING    | main.py:29 - Unused keys: {'message': 'hogehoge'}
# こんにちは
print(loc.greeting.hello(message="hogehoge"))
```

以下は`main.py`で使用した翻訳ファイルのサンプルです。

`loc/ja.toml`
```toml
sample = "サンプル"

[greeting]
hello = "こんにちは"
hello_to_user = "こんにちは！{user}さん"
```

`loc/en.toml`
```toml
sample = "Sample"

[greeting]
hello = "Hello"
hello_to_user = "Hello! {user}"
```

以上のサンプルコード以外にも、実用的なサンプルを[example](https://github.com/drago-suzuki58/LocoTOML/tree/main/examples)フォルダに作りました。ぜひご覧ください。

## Q&A

### 翻訳言語の言語コードは何を使えばいい？

基本的には自由で、TOMLのファイル名と合っていれば問題ありません。(`UwU.toml`でも正常に認識されます！)
ただし、可読性からISO 639-1(`en`など)や、ISO-3166(`US`)などの標準的な形式を使用することを推奨します。

### デフォルト言語やフォールバック言語は設定必須ですか？

デフォルト言語に関しては必須ですが、フォールバック言語に関しては必須ではありません。
設定しなかった場合は`en`が自動で設定されます。

### TOMLファイル以外のフォーマット（例: YAML）は使えますか？

いいえ、現在のところTOMLのみの対応になっています。需要が高いようであればLocoYAMLのような別ライブラリを開発するかもしれません。

## 貢献

LocoTOMLはオープンソースプロジェクトです！バグ報告や機能提案を歓迎します。

## 更新情報

<details>
<summary>クリックして更新情報を表示</summary>

### v0.2.0

- 初回リリース

</details>
