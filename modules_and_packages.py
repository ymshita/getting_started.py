import package
from package import encoder
import package.decoder as dec0der
import sys

print('type package: ', type(package))
print('dir package: ', dir(package))
str = 'python'
base64 = encoder.str_to_base64(str)
print('encoder.str_to_base64(\'python\'): ', encoder.str_to_base64(str))
print('package.base64_to_str(base64): ', package.base64_to_str(base64))
print('dec0der.base64_to_str(base64): ', dec0der.base64_to_str(base64))

print('sys.path: ', sys.path)