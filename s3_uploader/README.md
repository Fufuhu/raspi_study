# s3_uploader

ファイルの作成を検知してS3にアップロードするスクリプトです。
ファイルの作成の検知に`watchdog`、アップロードに`boto3`を用いています。

## 環境変数

基本的には、`AWS.*`はk8sのSecretリソースで定義し、
`TARGET_DIR`はConfigMapで定義するとよろし。

|環境変数名|内容|デフォルト値|
|---|---|---|
|AWS_ACCESS_KEY_ID|AWSのアクセスキーID|dummy|
|AWS_SECRET_ACCESS_KEY|AWSのシークレットアクセスキー|dummy|
|TARGET_DIR|ファイル作成を監視するディレクトリ|/tmp|

