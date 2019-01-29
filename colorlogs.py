import logzero

DEF_STYLE = "SUCCESS"

def log(*msgs,STYLE = DEF_STYLE):

    log_format = '%(color)s%(message)s%(end_color)s'
    formatter = logzero.LogFormatter(fmt=log_format)
    logzero.setup_default_logger(formatter=formatter)

    for msg in msgs:
        if (STYLE == "GREEN" or STYLE == "SUCCESS"):
            logzero.logger.info(str(msg))
        elif (STYLE == "BLUE" or STYLE == "INFO"):
            logzero.logger.debug(str(msg))
        elif (STYLE == "YELLOW" or STYLE == "WARNING"):
            logzero.logger.warning(str(msg))
        elif (STYLE == "RED" or STYLE == "ERROR"):
            logzero.logger.error(str(msg))
        else:
            logzero.logger.error(str("INVALID TYPE"))

def setDefaultStyle(STYLE = "SUCCESS"):
    if (STYLE == "GREEN" or STYLE == "SUCCESS"):
        DEF_STYLE = "SUCCESS"
    elif (STYLE == "BLUE" or STYLE == "INFO"):
        DEF_STYLE = "INFO"
    elif (STYLE == "YELLOW" or STYLE == "WARNING"):
        DEF_STYLE = "WARNING"
    elif (STYLE == "RED" or STYLE == "ERROR"):
        DEF_STYLE = "ERROR"
    else:
        pass

def test():
    log("THIS IS A TEST MSG!", STYLE = "YELLOW")
