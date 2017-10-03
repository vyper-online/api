# api

Compiler API for [viper](https://github.com/ethereum/viper) online editor


## Installation

Clone repository and install deps via:

```
pip install -r requirements.txt
pip install -r requirements_dev.txt # DEV requirements
```

Project is using ``Python 3.6`` and [Flask](http://flask.pocoo.org/)
for API setup.

Viper is added as submodule, initialize and update submodule with:

```
git submodule init
git submodule update
```

Follow the instruction from the [viper docs](https://eth-viper.readthedocs.io/en/latest/installing-viper.html) for 
installing viper into your virtualenv.
