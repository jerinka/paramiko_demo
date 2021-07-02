'''
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('tensorflow==2.4.0')
'''
def gpu_check():
    import tensorflow as tf

    gpus = tf.config.list_physical_devices('GPU')

    print(gpus)

    print('server test done!')
    return gpus

if __name__=='__main__':
    gpu_check()
