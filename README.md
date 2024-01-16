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

Submit [this form](https://forms.gle/tpbndoL1J6xB47KQ9) to request access. We will respond within 24h. If you don't hear back, please email us (jinhanchoi@g.harvard.edu).

### CAVE credentials

Use [this script](https://github.com/VCG/cave-scripts/blob/master/notebooks/CAVEsetup.ipynb) to get your CAVE credentials. This assumes you have been approved in the previous step already.

## Notebooks

In the notebooks folder, there are several working scripts to interact with CaveClient.

## Data

### Examples

`example_data.h5` and `dash_example_data.h5` are from [NeuroglancerAnnotationUI](https://github.com/seung-lab/NeuroglancerAnnotationUI/tree/master/examples).

### Nucleus

`h01_cell_body_nucleus_matrix_may16_2023.csv` is an original table that contains nucleus id, volume, position and bounding box's position. Daniel Berger compiled on May 16, 2023.

`h01_nucleus_table_data.h5` is a table ingested into CAVE.

About Columns:

* id: ID in the VAST segmentation file (for neurons/glia this should be consistent with the 'dbid' value in other tables)
* volume: volume estimate of cell body or nucleus in cubic micrometers, at _very low resolution_ (mip6 every 128th section for neurons/glia, mip7 every 16th section for bv nuclei, manually painted)
* pt_position: X, Y, Z anchor point within cell body or nucleus, in pixels at 8x8x33 nm
* bb_start_position: Xmin, Ymin, Zmin of bounding box of cell body or nucleus, in pixels at 8x8x33 nm
* bb_end_position: Xmax, Ymax, Zmax of bounding box of cell body or nucleus, in pixels at 8x8x33 nm

### Annotations

`dbcells-dump.csv` contains annotations previously done for H01.

`dbcells_dump_table_data.h5` is a table ingested into CAVE.

About Columns:

* pt_position: X, Y, Z anchor point within cell body or nucleus, in pixels at 8x8x33 nm
* classification_system: comma-seperated string joined from 'dbsubcelltype', 'dbsubcelltype2', and 'dbsubcelltype3'
* cell_type: cell type (manually classified)
  + 0: [U] unknown
  + 1: [P] pyramidal
  + 2: [I] interneuron
  + 3: [N] unclassified neuron
  + 4: [A] astrocyte
  + 5: [O] oligodendrocyte
  + 6: [G] mg/opc
  + 7: [C] 'c-shaped' cell (also mg/opc)
  + 8: [B] blood vessel cell (does not occur in this list)
  + 9: [S] Spiny stellate
  + 10: [E] Excitatory/spiny with atypical tree\n% Evelinas blood vessel nucleus types are
  + 11: 'Pericytes'
  + 12: 'vSMC'
  + 13: 'fibroblast'
  + 14: 'perivascular lymphocytes'
  + 15: 'perivascular macrophages'
  + 16: 'undecided' (unspecified blood vessel cell)
  + 17: 'Endothelial cells'
  + 18: 'circulating imm'

### SNEMI

You can download SNEMI data in [here](http://rhoana.rc.fas.harvard.edu/dataset/snemi.zip)
