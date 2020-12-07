cat words.txt | grep -oP '\w+' | sort | uniq -c | sort -nr | awk '{print $2 " " $1}'
