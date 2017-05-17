# tensorflow tutorial


### How to install in ubuntu
```
$ sudo apt-get update
$ sudo apt-get install python3-pip python3-dev python-virtualenv
$ virtualenv --system-site-packages -p python3 ~/tensorflow
$ source ~/tensorflow/bin/activate


# Ubuntu/Linux 64-bit, CPU only, Python 2.7
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.9.0-cp27-none-linux_x86_64.whl

# Ubuntu/Linux 64-bit, GPU enabled, Python 2.7 
# Requires CUDA toolkit 7.5 and CuDNN v4. For other versions, see "Install from sources" below.
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.9.0-cp27-none-linux_x86_64.whl

# Mac OS X, CPU only, Python 2.7:
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/tensorflow-0.9.0-py2-none-any.whl

# Ubuntu/Linux 64-bit, CPU only, Python 3.4
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.9.0-cp34-cp34m-linux_x86_64.whl

# Ubuntu/Linux 64-bit, GPU enabled, Python 3.4 
# Requires CUDA toolkit 7.5 and CuDNN v4. For other versions, see "Install from sources" below.
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.9.0-cp34-cp34m-linux_x86_64.whl

# Ubuntu/Linux 64-bit, CPU only, Python 3.5
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.9.0-cp35-cp35m-linux_x86_64.whl

# Ubuntu/Linux 64-bit, GPU enabled, Python 3.5 
# Requires CUDA toolkit 7.5 and CuDNN v4. For other versions, see "Install from sources" below.
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.9.0-cp35-cp35m-linux_x86_64.whl

# Mac OS X, CPU only, Python 3.4 or 3.5:
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/tensorflow-0.9.0-py3-none-any.whl


(tensorflow)$ pip3 install --upgrade $TF_BINARY_URL
(tensorflow)$ pip3 install jupyter
```


### How to run jupyter and tensorboard
```
jupyter notebook --ip=* --no-browser
tensorboard --logdir=/tmp/example
```