# fedi_challenge

Fedi engineering challenge

## Prerequisites

![python](https://img.shields.io/badge/python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

The code is run and tested with Python 3.12.4 on macOS 14.5.

### Access the data

Download the database from https://fedi-public-snapshots.s3.amazonaws.com/fedimint-observer.db.gz.

Decompress the .gz file:

```bash
unzip fedimint-observer.db.gz
```

### Environment

Clone the repo to your local machine.
Create a virtual environment for Python 3 with:

```
virtualenv -p python3 env
```

Activate the virtual environment with:

```
source env/bin/activate
```

Install the required Python packages with:

```
pip install -r requirements.txt
```

Register the environment as a jupyter kernel::

```
python -m ipykernel install --user --name env
```

Start jupyter notebook (make sure to use the env kernel):

```
python -m jupyter notebook
```
