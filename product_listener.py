import os

def product_listener():

  URL="https://www.bestbuy.com/site/msi-gaming-x-nvidia-geforce-gtx-1660-super-6gb-gddr6-pci-express-3-0-graphics-card-black-gray/6389333.p?skuId=6389333"

  page = list(os.popen("curl -s --user-agent 'big-floppy-donkey-balls' --compressed " + URL))

  for junk in page:
    if(junk.find('Sold Out')):
      return 0
    elif(junk.find('Access Denied')):
      return -1
  
  return 1