#!/bin/bash
if [ $# -lt 1  -o  $# -gt 2 ] ; then
	echo "Provide one or two integers"
	exit 1
fi

start=$1
end=$2

if [ $# -eq 1 ] ; then
	end=$start
fi

if [ "$(echo ${start} | grep -P '^\d+$' -c)" -ne 1 ] ; then
	echo "Arguments must be numbers"
	exit 1
fi

if [ "$(echo ${end} | grep -P '^\d+$' -c)" -ne 1 ] ; then
	echo "Arguments must be numbers"
	exit 1
fi

for i in $(seq ${start} ${end}) ; do
	mkdir "daily${i}" 2>/dev/null
	if [ ! -f "src/daily${i}/Task${i}.md" ] ; then
		echo -en "# Daily Coding Problem ${i}\n" > "src/daily${i}/Task${i}.md"
	fi
	if [ ! -f "src/daily${i}/Daily${i}.java" ] ; then
		echo -en "package daily${i};\n\nclass Daily${i} {\n\n}\n" > "src/daily${i}/Daily${i}.java"
	fi
done
