import time
import io
#===========================================
# io_examples/string_io.py
start_time = time.time()
for i in range(10):
    stream = io.StringIO()
    stream.write('Learning Python Programming.\n')
    #print('Become a Python ninja!', file=stream)
    stream.write('Become a Python ninja!')
    contents = stream.getvalue()
    print(contents)
    stream.close()
print(f'{time.time() - start_time} is elapsed')
#===========================================
start_time = time.time()
for i in range(10):
    stream = io.BytesIO()
    stream.write('Learning Python Programming.\n'.encode('utf-8'))
    #print('Become a Python ninja!'.encode('utf-8'), file=stream)
    stream.write('Become a Python ninja!'.encode('utf-8'))
    contents = stream.getvalue()
    print(contents)
    stream.close()
print(f'{time.time() - start_time} is elapsed')
#===========================================