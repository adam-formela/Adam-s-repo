# Zadanie 5. Porównaj zachowanie discard() vs remove() dla typu set.

days_discard = {'Sunday', 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'}
days_remove = {'Sunday', 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'}

days_discard.discard('Tuesday')
days_remove.remove('Tuesday')

print(days_discard)
print(days_remove)

print('-------------------')
days_discard.discard('Sunnight')
try:
    days_remove.remove('Sunnight')
except:
    print('Remove method unlike discard will raise an errors if the specified item does not exist in set')

print(days_discard)
print(days_remove)