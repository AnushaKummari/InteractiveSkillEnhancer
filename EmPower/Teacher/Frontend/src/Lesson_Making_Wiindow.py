from Frontend.src.Document_Formatter import *
from Backend.Database.lesson_db import lesson_data as ld
import os
import json
import shutil


class Lesson_Making_Window(QMainWindow):  # Home extends QMainWindow

    def __init__(self, ui_object):
        super(QMainWindow, self).__init__()

        # window
        self.lesson_making_window = ui_object
        self.form = None

        self.populate_module_data()

    def getFolderDetails(self):

        moduleNames = []
        moduleDescriptsions = []
        table_data = []

        # read the folders
        modules_dir = 'Lessons/modules'
        if os.path.exists(modules_dir):
            moduleNames = os.listdir(modules_dir)

            for folder in moduleNames:
                if 'module' in folder.lower() or 'মডিউল' in folder:
                    items = os.listdir(os.path.join(modules_dir, folder))

                    for item in items:
                        if item == 'content.json':
                            with open(os.path.join(modules_dir, folder, item), encoding='utf-8') as f:
                                data = json.load(f)
                                moduleDescriptsions.append(data.get('module_topic', ''))
                                break

        for col1, col2 in zip(moduleNames, moduleDescriptsions):
            table_data.append([col1, col2])

        return table_data

    def populate_module_data(self):

        tableRowContent = self.getFolderDetails()

        rows = len(tableRowContent)
        columns = self.lesson_making_window.lsn_module_table_widget.columnCount()
        self.lesson_making_window.lsn_module_table_widget.setRowCount(rows)

        # store the reloaded value into the PyQt_UI
        for row in range(rows):
            for col in range(columns):
                self.lesson_making_window.lsn_module_table_widget.setItem(
                    row, col, QTableWidgetItem(str(tableRowContent[row][col])))

    def remove_list_item(self):

        selected_indexes = self.lesson_making_window.lsn_new_module_list_view.selectedIndexes()
        if selected_indexes:
            selected_index = selected_indexes[0]
            model = self.lesson_making_window.lsn_new_module_list_view.model()
            model.removeRow(selected_index.row())

    def make_lesson(self):
          
        # count the number of lesson_* folders in the 'Lessons' folder
        sub_folders = []
        if os.path.exists('Lessons'):
            sub_folders = os.listdir('Lessons')

        if len(sub_folders) == 0:
            lesson_serial_no = 0
        else:
            lesson_serial_no = 0
            tmp_serial = []

            for folder in sub_folders:
                parts = folder.split('_')
                if len(parts) > 1 and parts[0].lower().startswith('lesson'):
                    try:
                        serial = int(parts[1])
                        tmp_serial.append(serial)
                    except:
                        continue

            lesson_serial_no = int(max(tmp_serial)) if tmp_serial else 0

        # create a new folder for the lesson
        folder_path = os.path.join('Lessons', 'lesson_' + str(lesson_serial_no + 1))
        os.path.exists(folder_path) or os.mkdir(folder_path)

        # copy the selected modules into the new lesson folder
        model = self.lesson_making_window.lsn_new_module_list_view.model()
        for row in range(model.rowCount()):
            index = model.index(row, 0)
            item = model.data(index)
            if item and ('module' in item.lower() or 'মডিউল' in item):
                sub_folder_name = os.path.join(folder_path, item)

                # handle duplicate names
                try:
                    os.mkdir(sub_folder_name)
                except:
                    pass
                shutil.copytree(os.path.join('Lessons', 'modules', item), sub_folder_name, dirs_exist_ok=True)

        print('Lesson created successfully')

        data = [str(lesson_serial_no + 1), folder_path]
        print("LESSON: ", data)
        # add the lesson to the database
        ld().add_entry(data)

        self.lesson_making_window.lsn_new_module_list_view.model().clear()
        show_success_message('Lesson Created', 'Lesson has been created. Open the Lessons folder to view it.')
     
    def show_lessons(self):
        
        # open lesson folder  
        os.startfile('Lessons')
                     
        
