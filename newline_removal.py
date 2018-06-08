import csv

def newPost(path, path1):
    h = 0
    input = open(path, 'r', encoding='utf_8')
    output = open(path1, 'w', newline='', encoding='utf_8')
    writer = csv.writer(output)
    for row in csv.reader(input):
        if row:
            writer.writerow(row)
    input.close()
    output.close()