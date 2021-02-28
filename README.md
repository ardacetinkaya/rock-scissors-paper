# rock-scissors-paper with Raspberry PI and Lobe 

This is a simple try and learn demonstration for some topics such as;
- Raspberry PI - Single-board small computer
- Raspberry PI Sense Hat - Add-on board for Raspberry PI to have some sensors and LED
- Machine Learning
    - Lobe - Machine Learning Tool to train and generate models - https://lobe.ai/
    - Tensorflow
- Python
- Lobe Python API - https://github.com/lobe/lobe-python

Basically the project is about very well-known game, Rock-Scissors-Paper game. Small Python script make some random choices between rock, scissors and paper. A set of images are trained with Lobe and exported as Tensorflow model. With a Python script, user's hand gestures are predicted within that model for rock,scissors and paper. So user tries to beat Raspberry PI. Very simple project but it opens lots of doors to learn new things. If you believe some fancy staff can be added, please free to add...


Lobe Python API required Tensorflow to be installed, so;
To install Tensorflow 2.0.0 for ARM based boards such as Rasberry PI, I have used this build
wget https://github.com/lhelontra/tensorflow-on-arm/releases/download/v2.0.0/tensorflow-2.0.0-cp37-none-linux_armv7l.whl

python3 -m pip install tensorflow-2.0.0-cp37-none-linux_armv7l.whl

- If you do not want to use Lobe Python API, just Tensorflow API's are also fine. Just check example *.py script when you exported your Lobe model as Tensorflow model
- A simple set of images that are trained with Lobe are also in model folder. Feel free to use it, but for best results, just download the Lobe and create your own model
