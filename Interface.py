import Note
import Functions
def run():
    input_from_user = ''
    while input_from_user != '6':
        print("Главное меню:\n\n1 - вывод всех заметок из файла\n2 - добавление заметки\n3 - удаление заметки\n4 - редактирование заметки\n5 - выборка заметок по дате\n6 - показать заметку по id\nВведите номер функции: ")
        input_from_user = input().strip()
        if input_from_user == '1':
            Functions.show('all')
        if input_from_user == '2':
            Functions.add_to_file()
        if input_from_user == '3':
            Functions.show('all')
            Functions.id_edit_delete_show('del')
        if input_from_user == '4':
            Functions.show('all')
            Functions.id_edit_delete_show('edit')
        if input_from_user == '5':
            Functions.show('date')
        if input_from_user == '6':
            Functions.show('id')
            Functions.id_edit_delete_show('show')
            break
