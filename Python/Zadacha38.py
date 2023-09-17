
import telebot

# Создайте экземпляр бота, используя токен, полученный от BotFather
bot = telebot.TeleBot('6624070041:AAEdAHoV1A7FmZLxad9Y8eWpsSSfDE7db-E')

# Создайте экземпляр класса PhoneBook
class PhoneBook:
    def display_contacts(self):
        with open('Zadacha38.txt', 'r') as file:
            contacts = []
            for line in file:
                name, number = line.strip().split(',')
                contacts.append(f'Имя: {name}, Номер: {number}')
            return '\n'.join(contacts)

    def add_contact(self, name, number):
        with open('Zadacha38.txt', 'a') as file:
            file.write(f'{name},{number}\n')
        return f'Контакт {name} добавлен.'

    def search_contact(self, query):
        with open('Zadacha38.txt', 'r') as file:
            contacts = []
            for line in file:
                name, number = line.strip().split(',')
                if query in name:
                    contacts.append(f'Имя: {name}, Номер: {number}')
            return '\n'.join(contacts)

    def delete_contact(self, query):
        contacts = []
        deleted_contact = None
        with open('Zadacha38.txt', 'r') as file:
            for line in file:
                contact_name, contact_number = line.strip().split(',')
                if contact_name != query:
                    contacts.append(line)
                else:
                    deleted_contact = f'Контакт {contact_name} удален.'
        with open('Zadacha38.txt', 'w') as file:
            file.writelines(contacts)
        return deleted_contact

    def update_contact(self, name, new_number):
        contacts = []
        updated = False
        with open('Zadacha38.txt', 'r') as file:
            for line in file:
                contact_name, contact_number = line.strip().split(',')
                if contact_name == name:
                    line = f'{contact_name},{new_number}\n'
                    updated = True
                contacts.append(line)
        with open('Zadacha38.txt', 'w') as file:
            file.writelines(contacts)
        return f'Контакт {name} обновлен.' if updated else f'Контакт {name} не найден.'

phonebook = PhoneBook()

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Этот бот поможет вам управлять телефонным справочником. Введите /help для инструкций.")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Доступные команды:\n/add - Добавить контакт\n/search - Найти контакт\n/update - Обновить контакт\n/delete - Удалить контакт\n/view - Просмотреть все контакты")

# Обработчик команды /view
@bot.message_handler(commands=['view'])
def view_contacts(message):
    contacts = phonebook.display_contacts()
    bot.send_message(message.chat.id, contacts)

# Обработчик команды /add
@bot.message_handler(commands=['add'])
def add_contact(message):
    msg = bot.send_message(message.chat.id, "Введите имя контакта:")
    bot.register_next_step_handler(msg, process_name_step)

# Обработчик для ввода имени контакта
def process_name_step(message):
    chat_id = message.chat.id
    name = message.text
    msg = bot.send_message(chat_id, "Введите номер телефона:")
    bot.register_next_step_handler(msg, process_number_step, name)

# Обработчик для ввода номера телефона и добавления контакта
def process_number_step(message, name):
    chat_id = message.chat.id
    number = message.text
    response = phonebook.add_contact(name, number)
    bot.send_message(chat_id, response)

# Обработчик команды /search
@bot.message_handler(commands=['search'])
def search_contact(message):
    msg = bot.send_message(message.chat.id, "Введите имя для поиска:")
    bot.register_next_step_handler(msg, process_search)

# Обработчик для поиска контакта
def process_search(message):
    chat_id = message.chat.id
    query = message.text
    contacts = phonebook.search_contact(query)
    bot.send_message(chat_id, contacts)

# Обработчик команды /delete
@bot.message_handler(commands=['delete'])
def delete_contact(message):
    msg = bot.send_message(message.chat.id, "Введите имя контакта для удаления:")
    bot.register_next_step_handler(msg, process_delete)

# Обработчик для удаления контакта
def process_delete(message):
    chat_id = message.chat.id
    query = message.text
    response = phonebook.delete_contact(query)
    bot.send_message(chat_id, response)

# Обработчик команды /update
@bot.message_handler(commands=['update'])
def update_contact(message):
    msg = bot.send_message(message.chat.id, "Введите имя контакта для обновления:")
    bot.register_next_step_handler(msg, process_update_name)

# Обработчик для ввода имени контакта для обновления
def process_update_name(message):
    chat_id = message.chat.id
    name = message.text
    msg = bot.send_message(chat_id, "Введите новый номер телефона:")
    bot.register_next_step_handler(msg, process_update_number, name)

# Обработчик для ввода нового номера телефона и обновления контакта
def process_update_number(message, name):
    chat_id = message.chat.id
    new_number = message.text
    response = phonebook.update_contact(name, new_number)
    bot.send_message(chat_id, response)

# Запуск бота
bot.polling()
