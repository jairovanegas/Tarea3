import numpy
import logging
import sys
import random
#Configuracion de librerias
numpy.set_printoptions(threshold = sys.maxsize)
logging.basicConfig(level=logging.DEBUG, filename='knapsack.log', filemode='w', format='%(message)s')

class Item:
  name = ''
  weigth = 0
  value = 0
  def __init__(self, name, weigth, value):
    self.name = name
    self.weigth = weigth
    self.value = value
  def __str__(self):
    return 'name: ' + self.name + ' weigth: ' + str(self.weigth) + ' value: ' + str(self.value)

def knapsack(a, w):
  c = numpy.matrix(numpy.zeros([a.size, w]))
  for i in range(1, a.size):
    item = a[i-1]
    for j in range(1, w):
      if(item.weigth > j):
        c[i,j] = c[i-1, j]
      else:
        c[i, j] = max(c[i-1, j], item.value + c[i-1, j-item.weigth])
    logging.info('{}: {}'.format(i, c[i]));
  logging.info('Cache: {}'.format(c))
  return c[a.size-1, w-1]

def generateRoom(x, minW, maxW, minV, maxV):
  a = []
  for i in range(x):
    a.append(Item('Item{}'.format(i), random.randint(minW, maxW), random.randint(minV, maxV)))
  return numpy.array(a)

#a = numpy.array([Item('Lingote', 5, 2000), Item('Nintendo Switch', 1, 230), Item('Diario', 2, 40), Item('Caja fuerte', 300, 4500), Item('Laptop', 3, 900)])
x = 5
a = generateRoom(x, 1, 16, 200, 1600)
w = 20;
logging.info('w: {}'.format(w))
for i in range(x):
  logging.info(a[i])
logging.info('Best knapsack for an avaliable weigth of {} is worth: {}'.format(w, knapsack(a, w)))
print('Finished')