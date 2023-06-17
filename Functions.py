import Note


# Создаем функцию записи заметок в файл.
def write_file(array, mode):
    file = open("notes.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Note.Note.to_string(notes))
        file.write('\n')
    file.close

# Создаем функция чтения файла с заметками.
def read_file():
    try:
        array = []
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Note.Note(
                id = split_n[0], title = split_n[1], body = split_n[2], date = split_n[3])
            array.append(note)
    except Exception:
        print('Нет сохраненных заметок...')
    finally:
        return array 
    
number = 1    
# Функция создания заметки
def add_note(number):
    title = is_len_correct(
        input('Введите заголовок: '), number)
    body = is_len_correct(
        input('Введите тело заметки: '), number)
    return Note.Note(title=title, body=body)

# Функция проверки кол-ва символов
def is_len_correct(text, n):
    while len(text) <= n:
        print(f'Текст должен содержать минимум {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text
    
# Добавление заметки в файл
def add_to_file():
    note = add_note(number)
    array = read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    write_file(array, 'a')
    print('Заметка добавлена')


def show(text):
    logic = True
    array = read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Заметок нет')

# Функция поиска. редактирования. удаления. показа всех заметок.
def id_edit_delete_show(text):
    id = input('Введите id необходимой заметки: ')
    array = read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = add_note(number)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('Заметка успешно изменена')
            if text == 'delete':
                array.remove(notes)
                print('Заметка успешно удалена')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Такой заметки не найдено, проверьте id')
    write_file(array, 'a')
