import logging
from copy import copy
MAPPING = {
    'DEBUG': 36,  # white
    'INFO': 32,  # green
    'WARNING': 33,  # yellow
    'ERROR': 31,  # red
    'CRITICAL': 41,  # white on red bg
}

PREFIX = '\033['
SUFFIX = '\033[0m'
BOLD_PREFIX = '\033[1'


class ColorFormatter(logging.Formatter):
    def format(self, record):
        colored_record = copy(record)

        levelname = colored_record.levelname
        lineno = colored_record.lineno
        msg = colored_record.msg
        name = colored_record.name
        filename = colored_record.filename
        seq = MAPPING.get(levelname, 37)  # default white

        colored_levelname = ('{0}{1}m [ {2} ] {3}').format(PREFIX, seq, levelname, SUFFIX)
        colored_msg = ('{0}{1}m [ {2} ]{3}').format(PREFIX, seq, msg, SUFFIX)
        colored_lineno = ('{0}{1}m [ {2} ]{3}').format(PREFIX, 36, lineno, SUFFIX)
        colored_name = ('{0}{1}m [ {2} ]{3}').format(PREFIX, 36, name, SUFFIX)
        colored_filename = ('{0}{1}m [ {2} ]{3}').format(PREFIX, seq, filename, SUFFIX)
        # colored_created = ('{0}{1}m [ {:d} ]{3}').format(PREFIX, seq, created, SUFFIX)

        colored_record.levelname = colored_levelname
        colored_record.msg = colored_msg
        colored_record.name = colored_name
        colored_record.filename = colored_filename
        colored_record.lineno = colored_lineno

        return super(ColorFormatter, self).format(colored_record)


def Logger(loggerName):
    LOG_NAME = loggerName
    LOG_FILE_INFO = loggerName
    LOG_FILE_ERROR = loggerName
    # stream_handler.setFormatter(ColorFormatter('%(asctime)s : %(name)s : %(levelname)s -> %(message)s'))
    log = logging.getLogger(LOG_NAME)
    log_formatter = logging.Formatter('[ %(asctime)s ] [ %(name)s ] [ %(lineno)s) ] [ %(levelname)s ] -> %(message)s')

    # comment this to suppress console output
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(ColorFormatter('\033[0;36m[ %(asctime)s ]\033[0m%(name)s%(lineno)s%(levelname)s%(message)s'))
    log.addHandler(stream_handler)

    file_handler_info = logging.FileHandler("{0}/{1}.log".format("logs", LOG_FILE_INFO))
    file_handler_info.setFormatter(log_formatter)
    file_handler_info.setLevel(logging.INFO)
    log.addHandler(file_handler_info)

    file_handler_error = logging.FileHandler("{0}/{1}.err".format("logs", LOG_FILE_ERROR))
    file_handler_error.setFormatter(log_formatter)
    file_handler_error.setLevel(logging.INFO)
    log.addHandler(file_handler_error)

    return log


def removeStreamHandlerFromLogger(logger):
    for handler in logger.handlers:
        if handler.stream.name == "<stderr>":
            logger.removeHandler(handler)


def setLogTypeFile(logger, level):
	if level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
		return False
	else:
		for handler in logger.handlers:
        		if ".err" in str(handler.stream):
                		handler.setLevel("CRITICAL")
	return logger
