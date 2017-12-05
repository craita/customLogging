import logger as LOGGER
logger = LOGGER.Logger("MAINLOGGER")
"""Remove streamhandler 
"""
#removeStreamHandlerFromLogger(logger)

"""Set level of log that will pe written in fille  
""" 
LOGGER.setLogTypeFile(logger, "CRITICAL")

if __name__ == "__main__":
	logger.debug("DEBUG LOG")
	logger.info("INFO LOG")
	logger.warning("WAWRNING LOG")
	logger.error("ERROR LOG")
	logger.critical("CRITICAL LOG")
