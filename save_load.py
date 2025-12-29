import csv

def load_file(file: str, book_manage: dict, log_manage: dict, borrow_manage: dict):
    with open(file, mode='r', newline='') as file_reader:
        file_load = csv.reader(file_reader, delimiter=',')
        temp_dict = {}
        turn = 0
        for line in file_load:
            if line:
                if line[0] == "START_BOOK":
                    turn = 1
                    continue
                elif line[0] == "END_BOOK":
                    turn = 0
                    continue
                elif line[0] == "START_LOG":
                    turn = 2
                    continue
                elif line[0] == "END_LOG":
                    turn = 0
                    continue
                elif line[0] == "START_BORROW":
                    turn = 3
                    continue
                elif line[0] == "END_BORROW":
                    turn = 0
                    continue
                
                if turn == 0:
                    continue
                elif turn == 1:
                    book_id = str(line[0])
                    title = line[1]
                    author = line[2]
                    date_published = line[3]
                    status = line[4]
                    list_of_borrowers = []
                    if line[5]:
                        for i in range(5,len(line)):
                            borrower = line[i]
                            list_of_borrowers.append(borrower)
                    book_manage[book_id] = {
                        'title': title,
                        'author': author,
                        'date_published': date_published,
                        'status': status,
                        'list_of_borrowers': list_of_borrowers
                    }
                elif turn == 2:
                    log_id = line[0]
                    name = line[1]
                    date_of_log = line[2]
                    time_of_log = line[3]
                    purpose = line[4]
                    log_manage[log_id] = {
                        'name': name,
                        'date_of_log': date_of_log,
                        'time_of_log': time_of_log,
                        'purpose':purpose
                    }
                elif turn == 3:
                    borrow_id = line[0]
                    book_id = line[1]
                    log_id = line[2]
                    date_return = line[3]
                    borrow_manage[borrow_id] = {
                        'book_id': book_id,
                        'log_id': log_id,
                        'date_return': date_return
                    }
            else:
                continue 

def save_file(file: str, book_manage:dict, log_manage:dict, borrow_manage: dict):
    with open(file, mode='w', newline='') as file_writer:
        if book_manage:
            start = "START_BOOK\n"
            file_writer.write(start)
            for key, value in book_manage.items():
                file_writer.write(key)
                file_writer.write(',')
                file_writer.write(value['title'])
                file_writer.write(',')
                file_writer.write(value['author'])
                file_writer.write(',')
                file_writer.write(value['date_published'])
                file_writer.write(',')
                file_writer.write(value['status'])
                list_of_borrowers = value['list_of_borrowers']
                if len(list_of_borrowers)>0:
                    for i in range(0, len(list_of_borrowers)):
                        file_writer.write(',')
                        file_writer.write(list_of_borrowers[i])
                        #if i != (len(list_of_borrowers)-1):
                            #file_writer.write(',')
                file_writer.write('\n')
            end = "END_BOOK\n"
            file_writer.write(end)
        file_writer.write('\n')
        if log_manage:
            start = "START_LOG\n"
            file_writer.write(start)
            for key, value in log_manage.items():
                file_writer.write(key)
                file_writer.write(',')
                file_writer.write(value['name'])
                file_writer.write(',')
                file_writer.write(value['date_of_log'])
                file_writer.write(',')
                file_writer.write(value['time_of_log'])
                file_writer.write(',')
                file_writer.write(value['purpose'])
                file_writer.write('\n')
            end = "END_LOG\n"
            file_writer.write(end)
        file_writer.write('\n')
        if borrow_manage:
            start = "START_BORROW\n"
            file_writer.write(start)
            for key, value in borrow_manage.items():
                file_writer.write(key)
                file_writer.write(',')
                file_writer.write(value['book_id'])
                file_writer.write(',')
                file_writer.write(value['log_id'])
                file_writer.write(',')
                file_writer.write(value['date_return'])
                file_writer.write('\n')
            end = "END_BORROW\n"
            file_writer.write(end)