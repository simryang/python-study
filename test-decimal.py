import decimal
import sys

print(sys.getsizeof(decimal.Decimal('1.1')))
print(sys.getsizeof(1.1))
print(sys.getsizeof(1))
print(sys.getsizeof('a'))
