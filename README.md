# Python code for creating a calculator android application.

https://github.com/Raj-Kamal-CSE-IITD/CalculatorApp/blob/main/TKinterCalculator.py

https://github.com/Raj-Kamal-CSE-IITD/CalculatorApp/blob/main/KivyCalculator.py

## Packaging for Android
### Install Kivy and Buildozer (Linux/macOS):
```
sudo apt install python3-pip git zip unzip openjdk-17-jdk
pip install kivy
pip install buildozer
```

### Create your build environment:
```
buildozer init
```

### Edit buildozer.spec:

Set your app title, package name, version.

Add required permissions if needed.

Add math library in requirements:

```
requirements = python3,kivy
```
