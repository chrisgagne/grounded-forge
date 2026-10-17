#!/bin/zsh
# Runs jsdiff before and after w12's commit ("Remove dead code", 4428de9c) on the input the reviewers named, and on
# three others. Usage: w12-check/run.sh PATH-TO-A-JSDIFF-CLONE
set -e
J=$1; H=${0:A:h}; W=$(mktemp -d)
for v in parent:7dbf2ea712aa7a6073ec9c0212b245b5273065ac child:4428de9c1c89c18804f9f6b23fba6d019abf556b; do
  n=${v%%:*}; mkdir -p $W/$n; git -C "$J" archive ${v#*:} src | tar -x -C $W/$n
  echo '{"type":"module"}' > $W/$n/package.json   # run the ES-module source as is, with explicit .js imports
  find $W/$n/src -name "*.js" -exec perl -pi -e "s#(from\s+'\.{1,2}/[^']+?)(?<!\.js)'#\$1.js'#g" {} \;
done
cp $H/check.mjs $W/; cd $W
for n in parent child; do node check.mjs $n 2>&1 | grep -v "^\s*at " | head -5; done
