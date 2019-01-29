import logzero

def log(msg, STYLE = "INFO"):
    log_format = '%(color)s%(message)s%(end_color)s'
    formatter = logzero.LogFormatter(fmt=log_format)
    logzero.setup_default_logger(formatter=formatter)

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

    