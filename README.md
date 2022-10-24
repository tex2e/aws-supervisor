
# EC2停止スクリプト

### 事前設定

AWSコンソールで生成したアクセスキーをAWS CLIに設定する。
```bash
pip install awscli
aws configure
```

### 開発者向け

起動＆実行

```bash
docker-compose up -d
docker-compose exec -T aws-manager-python3-server python src/stop_ec2.py
```

ビルド（使用ライブラリの増加時のみ）

```bash
docker-compose build python3-server
docker-compose down
docker-compose up -d
```
