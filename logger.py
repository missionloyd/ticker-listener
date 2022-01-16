import coloredlogs, logging

def configLogger():
  logger = logging.getLogger(__name__)
  coloredlogs.install(fmt='%(asctime)s,%(msecs)03d %(hostname)s %(message)s')

  _logger = logging.getLogger(__name__)

  coloredlogs.install(
      logger=_logger, fmt='%(asctime)s,%(msecs)03d %(hostname)s %(message)s', use_chroot=False,
      field_styles={
        'asctime': {'color': 'cyan'},
        'hostname': {'color': 'magenta'},
        'levelname': {'color': 242, 'bold': True},  
      }
      , datefmt='%d-%m-%Y %H:%M:%S',
      level_styles={
          'info': {'color': 'cyan', 'bold': True},
          'warn': {'color': 'green', 'bold': False},
          'error': {'color': 'red', 'bold': False},
          'critical': {'background': 'red', 'bold': True}
      },
      isatty=True
  )

  return _logger

def display(op, logger, text):

  if(op == 'info'):
    logger.info(text)
  elif(op == 'increase'):
    logger.warning(text)
  elif(op == 'decrease'):
    logger.error(text)
  elif(op == 'error'):
    logger.critical(text)

  return
