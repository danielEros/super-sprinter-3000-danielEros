from flask import render_template, request
from app import app
from app import data_manager
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))


@app.route('/story')
def story():
    return render_template('form.html',
                           title=' - Add new Story',
                           story_title='',
                           user_story='',
                           acceptance_criteria='',
                           business_value='',
                           estimation='',
                           status=1, # to select the rigtht status its number should be passed to the function
                           submit_title='Create',
                           action_target='list')


@app.route('/', methods=['GET', 'POST'])
@app.route('/list', methods=['GET', 'POST'])
def list_():
    file_name = current_file_path + "/sp3000_data.csv"
    list_table = data_manager.get_table_from_file(file_name)
    if 'POST' in str(request):
        if 'id_to_update' in request.form:
            list_table = data_manager.update_by_id(list_table, request)
        else:
            list_table = data_manager.add_item_to_table(list_table, request)
        data_manager.write_table_to_file(file_name, list_table)
    if 'GET' in str(request) and 'delete_id=' in str(request):
        delete_id = str(request)[str(request).index("=")+1:str(request).index("[GET]")-2]
        list_table = data_manager.delete_by_id(list_table, delete_id)
        data_manager.write_table_to_file(file_name, list_table)
    return render_template('list.html', list_table=list_table)


@app.route('/story/<item_id>')
def item_(item_id):
    file_name = current_file_path + "/sp3000_data.csv"
    list_table = data_manager.get_table_from_file(file_name)
    select_options = {'Planning': 1, 'TODO': 2, 'In Progress': 3, 'Review': 4, 'Done': 5}
    list_to_show = []
    for i in list_table:
        if i[0] == item_id:
            list_to_show = i
    return render_template('form.html',
                           title=' - Edit Story',
                           id_to_update=list_to_show[0],
                           story_title=list_to_show[1],
                           user_story=list_to_show[2],
                           acceptance_criteria=list_to_show[3],
                           business_value=list_to_show[4],
                           estimation=list_to_show[5],
                           status=select_options[list_to_show[6]], # to select the rigtht status its number should be passed to the function
                           submit_title='Update',
                           action_target='../list')
