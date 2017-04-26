# read file into a @table
#
# @file_name: string
# @table: list of lists of strings
def get_table_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table


# write a @table into a file
#
# @file_name: string
# @table: list of lists of strings
def write_table_to_file(file_name, table):
    with open(file_name, "w") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row.replace("\r\n", " ") + "\n")

def add_item_to_table(list_table, request):
    max_id = max(int(i[0]) for i in list_table)
    list_table.append([str(max_id+1),
                      request.form['story_title'],
                      request.form['user_story'],
                      request.form['acceptance_criteria'],
                      request.form['business_value'],
                      request.form['estimation'],
                      request.form['status']])
    return list_table


def update_by_id(list_table, request):
    line_to_update_index = None
    new_entry = [request.form['id_to_update'],
                 request.form['story_title'],
                 request.form['user_story'],
                 request.form['acceptance_criteria'],
                 request.form['business_value'],
                 request.form['estimation'],
                 request.form['status']]
    for index, line in enumerate(list_table):
        if line[0] == request.form['id_to_update']:
            #line_to_update_index = list_table[index]
            list_table[index] = new_entry
    return list_table

def delete_by_id(list_table, delete_id):
    for index, line in enumerate(list_table):
        if line[0] == delete_id:
            del(list_table[index])
            break
    return list_table
