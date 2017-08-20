c = 0;
def QSort(left, right):
  global c;
  key = a[(left + right) // 2];
  i = left;
  j = right;
  while True:
     while a[i] < key:
        i += 1;
        c += 1;
     while a[j] > key:
        j -= 1;
        c += 1;
     if i <= j:
       a[i], a[j] = a[j], a[i];
       i += 1;
       j -= 1;
     if i > j:
       break;
  if left < j:
      QSort(left, j);
  if i < right:
      QSort(i, right);

a = [5, 2, 6, 3, 4, 1]
QSort(0, 5);
print(a);

  
  
  
    
   
