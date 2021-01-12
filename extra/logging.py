# LOGGING(more convenient than print)
import os
import platform
from logging import logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(
        os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log'
    )
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')

logging.basicConfig(
    level=logging.DEBUG,  # (CRITICAL,ERROR,WARNING,INFO,DEBUG)
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)
logging.debug("Начало программы")
logging.info("Какие-то действия")
logging.warning("Программа умирает")

# Вывод:
# Сохраняем лог в C:\Users\swaroop\test.log
# Если открыть файл test.log , он будет выглядеть примерно так:
# 2012-10-26 16:52:41,457 : DEBUG : Начало программы
# 2012-10-26 16:52:41,474 : INFO : Какие-то действия
# 2012-10-26 16:52:41,475 : WARNING : Программа умирает
