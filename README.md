# speee_technicalproblem
speeeの技術課題提出用repo [リンク](https://www.dropbox.com/scl/fi/44rqxeog3bivmiekc23kw/25-_-Speee-new10.pdf?rlkey=wzulssselcwk3caaj3p34bxm4&dl=0)

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
