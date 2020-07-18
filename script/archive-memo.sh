#!/usr/bin/env bash
#
# Archive a/memo/YYYYMMDD.md into a/memo/YYYY/ directory.
#
# SYNOPSIS:
#     archive-memo.sh           # auto mode
#     archive-memo.sh YYYYMMDD
#

set -euo pipefail

base_dir=$(cd $(dirname $0)/.. && pwd)
CONTENT_DIR="${base_dir}/content/ja"
MEMO_DIR="${CONTENT_DIR}/a/memo"
KEEP_NUM=7

archive_one_ymd() {
  local yyyymmdd=$1

  pushd $CONTENT_DIR &>/dev/null

  if [[ ! -f "${MEMO_DIR}/${yyyymmdd}.md" ]]; then
    echo "Error! Not exist: ${MEMO_DIR}/${yyyymmdd}.md" >&2
    exit 1
  fi

  if [[ "${yyyymmdd}" =~ ^([0-9]{4}) ]]; then
    local year=${BASH_REMATCH[1]}
  else
    echo "Error! Does not match to year: ${yyyymmdd}" >&2
    exit 1
  fi

  pushd $MEMO_DIR &>/dev/null
  mkdir -p $year
  git mv $yyyymmdd.md $year/
  echo "[ok] Archive $yyyymmdd.md into $year/"
  popd &>/dev/null

  if git grep "memo/${yyyymmdd}.md"; then
    git grep -l "memo/${yyyymmdd}.md" | xargs perl -pi -e "s#memo/${yyyymmdd}\.md#memo/${year}/${yyyymmdd}.md#g"
    echo "[notice] Some text substitution occured"
  fi

  pushd $MEMO_DIR/$year &>/dev/null
  grep -Hn '\bref\b' $MEMO_DIR/$year/$yyyymmdd.md || true
  popd &>/dev/null

  popd &>/dev/null
}

archive_one_file() {
  local memo=$1
  local base=$(basename $1)
  local ymd=${base%.*}
  archive_one_ymd $ymd
}

if [[ -n "${1:-}" ]]; then
  archive_one_ymd $1
else
  for memo in $(ls -1 ${MEMO_DIR}/2*.md | sort -r | awk -v n=$KEEP_NUM 'NR>n'); do
    echo "archive $(basename $memo)"
    archive_one_file $memo
  done
fi

exit
