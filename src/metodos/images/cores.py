def getColor(img, x, y):
  return img.item(y, x, 0), img.item(y, x, 1), img.item(y, x, 2)

def setColor(img, x, y, b, g, r):
  img.itemset((y, x, 0), b)
  img.itemset((y, x, 1), g)
  img.itemset((y, x, 2), r)
  return img