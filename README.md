## About

This repository contains scripts for programmatic access to Lichtman Lab datasets hosted by [CAVE](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10402030/) (Connectome Annotation and Versioning Engine). The scripts are written in Python and use the [CaveClient](https://caveclient.readthedocs.io/en/latest/?badge=latest). 

## Supported Datasets

* [H01](https://h01-release.storage.googleapis.com/proofreading.html) - (Shapson-Coe at al. 2021)
* Fish 2.0 (coming soon)

## Getting Started

### Local Environment

Setup a virtual environment using [virtualenv](https://virtualenv.pypa.io/en/latest/).

```bash
git clone https://github.com/VCG/cave-scripts.git
cd cave-scripts
virtualenv -p python3.9 venv
source venv/bin/activate
pip install -r requirements.txt
```

### Request CAVE permission

Submit [this form](https://forms.gle/tpbndoL1J6xB47KQ9) to request access. We will respond within 24h. If you don't hear back, please [email us](mailto:jinhanchoi@g.harvard.edu).

### CAVE credentials

Use [this script](https://github.com/VCG/cave-scripts/blob/master/notebooks/CAVEsetup.ipynb) to get your CAVE credentials. This assumes you have been approved in the previous step already.

## Tutorials
Tutorials on how to use scripts in this repo are available in our [wiki](https://github.com/VCG/cave-scripts/wiki).
