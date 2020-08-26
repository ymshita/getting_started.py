import package
from package import encoder
import package.decoder as dec0der
import sys
from package import counter as closure

print('type package: ', type(package))
print('dir package: ', dir(package))
str = 'python'
base64 = encoder.str_to_base64(str)
print('encoder.str_to_base64(\'python\'): ', encoder.str_to_base64(str))
print('package.base64_to_str(base64): ', package.base64_to_str(base64))
print('dec0der.base64_to_str(base64): ', dec0der.base64_to_str(base64))

print('sys.path: ', sys.path)
print('globals(): ', globals())
print('dir(__builtins__): ', dir(__builtins__))

counter1 = closure.counter()
print('counter1(): ', counter1())
print('counter1(): ', counter1())
print('counter1(): ', counter1())
counter2 = closure.counter()
print('counter2(): ', counter2())
print('counter2(): ', counter2())