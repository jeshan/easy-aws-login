#!/usr/bin/env sh
set -e

python setup.py sdist bdist_wheel
cp -r dist /custom

twine upload --skip-existing --username ${TWINE_USERNAME} --password ${TWINE_PASSWORD} dist/*

python ../post-release-data.py > data.json

curl --header "Content-Type: application/json" \
  -u jeshan:${GITHUB_TOKEN} \
  --request POST \
  --data @data.json \
  https://api.github.com/repos/jeshan/easy-aws-login/releases
