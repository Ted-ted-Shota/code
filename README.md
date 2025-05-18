# 初めてのGitHub連携

このリポジトリにはサンプルの FastAPI アプリケーションが含まれます。

## サーバーの起動方法

```bash
source ~/.venvs/openagents-env/bin/activate
uvicorn backend.main:app --host 127.0.0.1 --port 8002 --reload
```

### サーバー再起動

```bash
pkill -f uvicorn
source ~/.venvs/openagents-env/bin/activate
uvicorn backend.main:app --host 127.0.0.1 --port 8002 --reload
```

### ポート確認

```bash
lsof -iTCP:8002 -sTCP:LISTEN
```

### API ドキュメント確認

ブラウザや curl で次の URL にアクセスし、ドキュメントが表示されることを確認します。

```
http://127.0.0.1:8002/docs
```

```bash
curl http://127.0.0.1:8002/docs
```
