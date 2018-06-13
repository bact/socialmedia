import csv
from wordcut import Wordcut

input_file = open('negative.txt', 'r')
csv_file = open('negative.csv', 'w', newline='')

writer = csv.writer(csv_file, dialect='excel', quoting=csv.QUOTE_ALL)

with open('bigthai.txt') as dict_file:
    word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
    word_list.sort()
    wordcut = Wordcut(word_list)

    for line in input_file:
        line = line.strip()
        space_count = line.count(' ')
        l = len(line)
        if (space_count*2.8) > l:
            line = line.replace(' ','')
        writer.writerow(wordcut.tokenize(line))

input_file.close()
csv_file.close()
