# Template

This repository is a template for CARES projects on GitHub

<p align="center">
<img src="./media/robots.png" alt="Pepper and NAO" style="width: 80%;"/>
</p>
<p align="center">
Pepper (Left) and NAO (Right)
</p>


## Description

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac condimentum tellus. Quisque dignissim ante sapien. Duis ac nunc viverra, semper massa ut, sagittis nunc. Pellentesque tellus sem, tristique eget nibh sit amet, rhoncus varius quam. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Morbi venenatis nec magna ac fermentum. Pellentesque consequat interdum eros, at vulputate mi iaculis et. Duis ornare quis libero interdum ornare. Pellentesque tristique quis nulla et aliquet. Sed ultricies tristique felis, quis pretium ligula tincidunt quis. Maecenas et suscipit arcu, et finibus risus. Aliquam consequat blandit turpis ut molestie. Donec porta eros et finibus molestie. Vestibulum cursus gravida suscipit. Phasellus ac ipsum felis.

## Getting Started
### Dependencies

![Python](https://img.shields.io/badge/python-3.10-blue.svg) ![GCC](https://img.shields.io/badge/GCC-15.2+-red.svg) ![Java](https://img.shields.io/badge/Java-21+-brown.svg) ![JavaScript](https://img.shields.io/badge/JavaScript-ES2024-olive.svg) ![ROS](https://img.shields.io/badge/ROS-Jazzy-indigo.svg)
* Ubuntu 24.04 or Newer
* Conda
* Docker

### Installing
#### SDK
Clone the GitHub repo and install the requirements
```
git clone git@github.com:UoA-CARES/template.git
cd template
pip install -r requirements.txt
```
Download the SDK from the [Aldebaran](https://aldebaran.com/en/support/kb/nao6/downloads/nao6-software-downloads/) website (Alternatively from the [United Robotics Group](https://support.old.unitedrobotics.group/en/support/solutions/articles/80001024221-pepper-2-5-downloads) website). Once the SDK has downloaded, copy and paste it into the sdk folder and extract it.


## Executing Python program
It is highly recommended to create a separate Python 2.7 environment using Conda and set the Python path to the SDK
```
conda create -n naoqi27 python=2.7 -y
conda activate naoqi27
cd sdk/<NAME OF NAOQI SDK>/
conda env config vars set PYTHONPATH=${PYTHONPATH}:{$PWD}/lib/python2.7/site-packages
``` 

If you do not set the Conda environment variable, then you can alternatively set it every time you activate the naoqi27 environment:
```
export PYTHONPATH=${PYTHONPATH}:<PATH TO PYTHON SDK>/lib/python2.7/site-packages
```


To check if the SDK works, you can run either of these checks
```
conda deactivate
conda activate naoqi27
python -c "import qi"
```

# Package Structure

```text
template/
├─ src/
│  ├─ test.py
│  ├─ test.cpp
│  ├─ test.java
│  ├─ test.js
```

`src`: contains the source files for testing

## Notes

* Lorem ipsum dolor sit amet, consectetur adipiscing elit.


## Author

[Finn Tracey](finn.tracey@auckland.ac.nz)

## Version History
* 1.0
    * Initial Release
