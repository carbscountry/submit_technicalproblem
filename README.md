# technicalproblem
技術課題提出用repo 

##  Dockerコンテナの作成&起動
```
docker-compose up -d app
```

## Dockerコンテナにアクセス
```
docker-compose exec app bash
```

## REST APIのテスト
```
root@094d1915df3c:/workspace# python app.py
# 別のターミナルでコンテナにアクセスして
root@094d1915df3c:/workspace#　python unit_test.py
# curlで実行
root@094d1915df3c:/workspace#　curl -X GET "http://127.0.0.1:5000/fib?n=5"
```

## 工夫した点
- dockerを利用してコードの共有が簡単にできるようにした
- ユニットテストが実行できるようにした
- ログが残るようにした


