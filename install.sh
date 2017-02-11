pip3 install numpy scipy scikit-learn pillow h5py
pip3 install --upgrade --no-deps git+git://github.com/Theano/Theano.git
#pip3 install keras
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0-cp35-cp35m-linux_x86_64.whl
#export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0-cp27-none-linux_x86_64.whl
pip3 install --upgrade $TF_BINARY_URL
