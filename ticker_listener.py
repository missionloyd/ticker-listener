import requests
import json
import logger
import time
import datetime
import progressBar

sleepTime = 10
recoverTime = 30
response_API = None
previousTickers = None
log = logger.configLogger()
status = False

def timeAgo():
  return str(datetime.timedelta(seconds=sleepTime))

def diff(curr, prev):
  dec = str(round(curr - prev, 2))
  perc = str(round((((abs(prev - curr))/((prev + curr) / 2)) * 100), 2))
  return dec, perc

def sleep(time):
  print("")
  progressBar.sleepProgress(50, time)
  print("")
  return

while(True):

  count = 0

  tickers = json.load(open('manifest.json', 'r'))
  #logger.display('info', log, 'ENTRY START')

  # load prices
  for ticker in tickers:
    while(True):
      try:
        response_API = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=' + ticker['ticker'])
      except:
        logger.display('error', log, "API error -> attempting to fix")

      if(str(response_API) != "<Response [200]>"):
        sleep(recoverTime)
      else:
        data = json.loads(response_API.text)
        tickers[count].update({ 'price': data['price'], "index": count })
        count += 1
        time.sleep(0.1)
        break

  # print results
  for ticker in tickers:
    curr = float(ticker['price'])
    price_clean = str(round(curr, 2))

    if(previousTickers != None):
      prev = float(previousTickers[ticker['index']]['price'])
      dec, perc = diff(curr, prev)
      
      if(curr < prev):
        logger.display('decrease', log, (ticker['symbol'] + ": $" + price_clean + " ▼ " + dec + " (" + perc + "%" + ") " + timeAgo()))
      else:
        logger.display('increase', log, (ticker['symbol'] + ": $" + price_clean + " ▲ " + dec + " (" + perc + "%" + ") " + timeAgo()))
    else:
      logger.display('info', log, (ticker['symbol'] + ": $" + price_clean))

  #logger.display('info', log, 'ENTRY END')

  previousTickers = tickers
  sleep(sleepTime)