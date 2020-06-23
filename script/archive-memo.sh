#!/usr/bin/env bash
#
# Archive a/memo/YYYYMMDD.md into a/memo/YYYY/ directory.
#
# SYNOPSIS:
#     archive-memo.sh YYYYMMDD
#

set -euo pipefail

base_dir=$(cd $(dirname $0)/.. && pwd)
CONTENT_DIR="${base_dir}/content/ja"
MEMO_DIR="${CONTENT_DIR}/a/memo"

yyyymmdd=$1

cd $CONTENT_DIR

if [[ ! -f "${MEMO_DIR}/${yyyymmdd}.md" ]]; then
  echo "Error! Not exist: ${MEMO_DIR}/${yyyymmdd}.md" >&2
  exit 1
fi

if [[ "${yyyymmdd}" =~ ^([0-9]{4}) ]]; then
  year=${BASH_REMATCH[1]}
else
  echo "Error! Does not match to year: ${yyyymmdd}" >&2
  exit 1
fi


pushd $MEMO_DIR
mkdir -p $year
git mv $yyyymmdd.md $year/
echo "[ok] Archive $yyyymmdd.md into $year/"
popd

if git grep "memo/${yyyymmdd}.md"; then
  git grep -l "memo/${yyyymmdd}.md" | xargs perl -pi -e "s#memo/${yyyymmdd}\.md#memo/${year}/${yyyymmdd}.md#g"
  echo "[notice] Some text substitution occured"
fi

pushd $MEMO_DIR/$year
grep -Hn '\bref\b' $MEMO_DIR/$year/$yyyymmdd.md || true

exit
