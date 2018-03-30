# api

Compiler API for [vyper](https://github.com/ethereum/vyper) online editor


## Installation

Clone repository and install deps via:

```
pip install -r requirements.txt
pip install -r requirements_dev.txt # DEV requirements
```

Project is using ``Python 3.6`` and [Flask](http://flask.pocoo.org/)
for API setup.

Vyper is added as submodule, initialize and update submodule with:

```
git submodule init
git submodule update
```

Follow the instruction from the [vyper docs](https://vyper.readthedocs.io/en/latest/installing-vyper.html) for 
installing vyper into your virtualenv.

The dev server on http://127.0.0.1:5000 can be started with:

```
python app.py
```

## API Usage

Endpoint: ``compile/``
Methods: ``GET``, ``POST`` (recommended)

Params:

| Name          | Description           | Mandatory  |
| ------------- |:---------------------:| ----------:|
| source        | Vyper source code     | yes        |

Example request (with [HTTPie](https://httpie.org/)):

```
http --form POST http://127.0.0.1:5000/compile/ source='Some viper source code'
```

Request from file:

```
http --form POST http://127.0.0.1:5000/compile/ source=@viper/examples/crowdfund.v.py
```
