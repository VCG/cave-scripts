## About

This repository contains scripts for programmatic access to Lichtman Lab datasets hosted by [CAVE](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10402030/) (Connectome Annotation and Versioning Engine). The scripts are written in Python and use the [CAVEClient](https://caveclient.readthedocs.io/en/latest/?badge=latest). 

## Supported Datasets

* [H01](https://h01-release.storage.googleapis.com/proofreading.html) - (Shapson-Coe at al. 2021) - [Latest Proofread Version](https://ngl.brain-wire.org/#!middleauth+https://global.brain-wire-test.org/nglstate/api/v1/5737328739876864)
* Fish 1.0 (coming soon)

Interactive proofreading can be done through [this link](https://ngl.brain-wire.org) - also check out the [proofreading tutorial](https://h01-release.storage.googleapis.com/proofreading.html). 

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

* Creating Custom Annotation Tables - [notebook](https://github.com/VCG/cave-scripts/blob/master/notebooks/Create_Tables.ipynb)
* Visualizing CAVE annotation tables in Neuroglancer - [notebook](https://github.com/VCG/cave-scripts/blob/master/notebooks/Display_Annotations.ipynb)
* Downloading Meshes of Proofread Neurons - [notebook](https://github.com/VCG/cave-scripts/blob/master/notebooks/Mesh_Download.ipynb)
* Query Materialized Annotation Tables - [notebook](https://github.com/VCG/cave-scripts/blob/master/notebooks/Query_Materialization.ipynb)
* Uploading Custom Annotations to CAVE - [notebook](https://github.com/VCG/cave-scripts/blob/master/notebooks/Upload_Data.ipynb)
* View Segment Proofreading Changelog - [website_service](https://local.brain-wire-test.org/progress/api/v1/query?rootid=864691132406661507&dataset=&submit=true)
* Count Edits over Time (Admins only) - [notebook](https://github.com/VCG/cave-scripts/blob/master/notebooks/count_edits.ipynb)
* Query Synapses - [notebook](https://github.com/VCG/cave-scripts/blob/master/notebooks/Query_Synapses.ipynb)

## Limitations / Known Issues

Programmatic access to H01 through CAVE is fairly new. So expect improvements, and please report bugs by opening an issue in the repository.

## Acknowledgements

We thank Akhilesh Halageri, Sven Dorkenwald, Forrest Collman, Casey Schneider-Mizell, Chris Jordan, Nico Kemnitz, Derrick Brittain, and Will Silversmith for their efforts in making CAVE open-source. 

## Cite
Please consider citing the following articles, when using code from this repository. 

```bibtex
@article{dorkenwald2023cave,
  title={CAVE: Connectome annotation versioning engine},
  author={Dorkenwald, Sven and Schneider-Mizell, Casey M and Brittain, Derrick and Halageri, Akhilesh and Jordan, Chris and Kemnitz, Nico and Castro, Manual A and Silversmith, William and Maitin-Shephard, Jeremy and Troidl,    Jakob and others},
  journal={bioRxiv},
  year={2023},
  publisher={Cold Spring Harbor Laboratory Preprints}
}
```

```bibtex
@article{shapson2024petavoxel,
  title={A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution},
  author={Shapson-Coe, Alexander and Januszewski, Micha{\l} and Berger, Daniel R and Pope, Art and Wu, Yuelong and Blakely, Tim and Schalek, Richard L and Li, Peter H and Wang, Shuohong and Maitin-Shepard, Jeremy and others},
  journal={Science},
  volume={384},
  number={6696},
  pages={eadk4858},
  year={2024},
  publisher={American Association for the Advancement of Science}
}
```
