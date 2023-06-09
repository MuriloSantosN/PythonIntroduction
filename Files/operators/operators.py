# -*- coding: utf-8 -*-

def add(a, b):
  """ It add two numbers
  
      param a: First value
      type a: int, float
      param b: Second value
      type b: int, float
      
      return: int, float
  """
  if type(a) == str or type(b) == str:
    raise TypeError()
  return a + b


def subtraction(a, b):
  """ It subtraction two numbers
  
      param a: First value
      type a: int, float
      param b: Second value
      type b: int, float
      
      return: int, float
  """
  if type(a) == str or type(b) == str:
    raise TypeError()
  return a - b

def division(a, b):
  """ It divides two numbers
  
      param a: First value
      type a: int, float
      param b: Second value
      type b: int, float
      
      return: int, float
  """
  if type(a) == str or type(b) == str:
    raise TypeError()
  return a / b

def rest(a, b):
  """ It rest two numbers
  
      param a: First value
      type a: int, float
      param b: Second value
      type b: int, float
      
      return: int, float
  """
  if type(a) == str or type(b) == str:
    raise TypeError()
  return a % b