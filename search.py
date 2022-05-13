import csv 

right_entries = []

def search_helper(dictionary):
    row_num = [1,4,5,6,7,8]
    check_dict = {}
    for i, key in enumerate(dictionary.keys()):
        if dictionary[key] != '0':
            check_dict[row_num[i]] = dictionary[key]
    return check_dict

def search(dictionary, csvs):
    text_boxes = search_helper(dictionary)
    csv_file = csv.reader(open(csvs, "r", encoding='UTF8'), delimiter=",")
    next(csv_file)
    retRows = []
    for row in csv_file:
        Good_row = True
    #if current rows 2nd value is equal to input, print that row
        for row_num in text_boxes.keys():
            if text_boxes[row_num].lower() not in row[row_num].lower():
                Good_row = False
        if Good_row:
            retRows.append(row)
    return retRows

def download(path):
    headers = ['OrderNumber',"Pet Names", "SKU", "Color", "Line1", "line2", "line3", "line4", "line5"]
    with open(path + '.csv', 'w', newline ='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for i in right_entries:
            writer.writerows(i)

