BOT_TOKEN = '902324374:AAGX2HlvYB0vXtQYHdwQ0RR_-WdBwW1dVCg'

Open_Weather_key = '4e855816a27b3c505f4349bc82c62b27'


def log(message):
    print('\n ------------')
    from datetime import datetime
    print(datetime.now())
    print('Сообщение от {0} {1} (username: {4}). (id = {2}) \nТекст = {3}'.format(message.from_user.first_name,
                                                                            message.from_user.last_name,
                                                                            str(message.from_user.id),
                                                                            message.text,
                                                                            message.from_user.username))