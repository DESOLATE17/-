from enum import Enum

# Токент бота
TOKEN = '5597125983:AAFcvSuyrWoSHXnNoJTntzYY3kNUd62ucvs'

# Файл базы данных Vedis
db_file = "db.vdb"

# Ключ записи в БД для текущего состояния
CURRENT_STATE = "CURRENT_STATE"

# Состояния автомата
class States(Enum):
    STATE_START = "STATE_START"  # Начало нового диалога
    STATE_GROUP = "STATE_GROUP"
    STATE_DAY = "STATE_DAY"
    #STATE_OPERATION = "STATE_"