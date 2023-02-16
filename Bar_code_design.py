from barcode import EAN13
from barcode. writer import Imagewriter
number : '5901234123457
my_code = EAN13(number, writer=Imagewriter())
my_code. save("new_ code 1")