def is_balance(s):
  def setEqual(a, b):
    for ele in a:
      if ele not in b:
        return False
    for ele in b:
      if ele not in a:
        return False
    return True
  i = 1
  while i < len(s):
    j = 0
    while j <= i:
      upper = set()
      lower = set()
      for ele in s[j:i+1]:
        if ele.isupper():
          upper.add(ele.lower())
        else:
          lower.add(ele)
      if setEqual(upper, lower):
        return i - j + 1
      j += 1
    i += 1
  return -1

print(is_balance("azABaabza"))
print(is_balance("TacoCat"))
print(is_balance("AcZCbaBz"))
