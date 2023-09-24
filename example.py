from logger import Logger, set_custom_handler_levels
import time


def run_example():
    # Доступные уровни логирования:
    # 10: 'DEBUG'
    # 20: 'INFO'
    # 30: 'WARNING'
    # 40: 'ERROR'
    # 50: 'CRITICAL'
    # 60: 'SYSTEM'
    # 70: 'INIT'
    # 80: 'DIAGNOST'

    # Пример создания логера с уровнем логирования в консоли 10, в файле 30, т.е. в консоль будут выводиться сообщения
    # с уровнем DEBUG и выше, а в файл WARNING и выше
    log = Logger(name='log_example', console_level=10, file_level=30)

    sample_msg = 'Пример использования универсальной функции для всех уровней логирования'
    log.logger(level_index=10, msg=sample_msg, is_error=False) # параметры переданы явно для наглядности. Последний
    # параметр по умолчанию имеет значение False, так что можно не передавать, если не нужно, чтобы он был True

    time.sleep(0.01)
    sample_msg = 'Пример использования универсальной функции с уровнем логирования INIT и ошибой'
    log.logger(30, sample_msg, True)

    time.sleep(0.01)
    sample_msg = 'Пример использования функции логирования для уровня DEBUG'
    log.debug(msg=sample_msg)

    time.sleep(0.01)
    sample_msg = 'Пример использования функции логирования для уровня INFO'
    log.info(sample_msg)

    time.sleep(0.01)
    sample_msg = 'Пример использования функции логирования для уровня WARNING'
    log.warning(sample_msg, True) # второй параметр отвечает за наличие ошибки

    time.sleep(0.01)
    sample_msg = 'Пример использования функции логирования для уровня ERROR'
    log.error(sample_msg) # для данной функции флаг is_error недоступен, т.к. сообщение об ошибке не может быть
    # без ошибки

    time.sleep(0.01)
    sample_msg = 'Пример использования функции логирования для уровня CRITICAL'
    log.critical(sample_msg, True) # тут флаг ошибки доступен для упрощения поиска ошибок в логах (ctrl f ERROR)
    # По умолчанию в данной функции is_error = True, т.е. можно не передавать второй параметр

    time.sleep(0.01)
    sample_msg = 'Пример использования функции логирования для уровня SYSTEM'
    log.system(sample_msg)

    time.sleep(0.01)
    sample_msg = 'Пример использования функции логирования для уровня INIT'
    log.init(sample_msg)

    time.sleep(0.01)
    sample_msg = 'Пример использования функции логирования для уровня DIAGNOST'
    log.diagnost(sample_msg)

    time.sleep(0.01)

    # Пример использования кастомной настройки уровней логирования.
    # Используем функцию, задающую желаемые нам уровни для консоли и файла
    set_custom_handler_levels(console_levels=[10, 20, 70], file_levels=[20, 60, 70, 80])
    # для консоли установлены следующие уровни: DEBUG, INFO, INIT
    # для файла установлены следующие уровни: INFO, SYSTEM, INIT, DIAGNOST
    log = Logger('custom_lvl_example') # Если не передать в параметрах уровень для консоли и файла,
    # то будет использоваться кастомная настройка

    sample_msg = 'DEBUG msg'
    log.debug(sample_msg)
    time.sleep(0.01)

    sample_msg = 'INFO msg'
    log.info(sample_msg)
    time.sleep(0.01)

    sample_msg = 'WARNING msg'
    log.warning(sample_msg)
    time.sleep(0.01)

    sample_msg = 'ERROR msg'
    log.error(sample_msg)
    time.sleep(0.01)

    sample_msg = 'CRITICAL msg'
    log.critical(sample_msg)
    time.sleep(0.01)

    sample_msg = 'SYSTEM msg'
    log.system(sample_msg)
    time.sleep(0.01)

    sample_msg = 'INIT msg'
    log.init(sample_msg)
    time.sleep(0.01)

    sample_msg = 'DIAGNOST msg'
    log.diagnost(sample_msg)
    time.sleep(0.01)
