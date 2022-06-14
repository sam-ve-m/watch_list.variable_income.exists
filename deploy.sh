#!/bin/bash
fission spec init
fission env create --spec --name watch-list-exists-env --image nexus.sigame.com.br/fission-async:0.1.6 --builder nexus.sigame.com.br/fission-builder-3.8:0.0.1
fission fn create --spec --name watch-list-exists-fn --env watch-list-exists-env --src "./func/*" --entrypoint main.symbol_exists  --rpp 100000
fission route create --spec --method GET --url /watch_list/exists --function watch-list-exists-fn
