fission spec init
fission env create --spec --name wtc-list-exists-env --image nexus.sigame.com.br/fission-wacth-list-exists:0.2.0-0 --poolsize 0 --version 3 --imagepullsecret "nexus-v3" --spec
fission fn create --spec --name wtc-list-exists-fn --env wtc-list-exists-env --code fission.py --targetcpu 80 --executortype newdeploy --maxscale 3 --requestsperpod 10000 --spec
fission route create --spec --name wtc-list-exists-rt --method GET --url /watch_list/variable_income/exists --function wtc-list-exists-fn
