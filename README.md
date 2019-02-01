# Precision Health Initiative (φ)

Main repository for the Machine Learning and Analytics side of the Precision Health Initiative (PHI).

## Getting Started

Data should not be stored here.

This section describes how to organize this work and how to get the code running. Currently this assumes familiarity with Python projects, UNIX systems, and Git.

#### Getting Organized

The running assumption is that `Data/` contains the .csv files representing the data set, and this `PHI/` repository contains the code and documentation.

Each may be stored as follows (though this may be tweaked through config files):

```bash
Precision-Health-Initiative/
├── Data/
│   ├── pregnancy_outcomes.csv
│   ├── Screening.csv
│   └── Visit1.csv
└── PHI/
    └── README.md
```

#### Getting Running

Clone the repository from GitHub:

```bash
git clone git@github.com:batflyer/PHI.git
```

If you're using Anaconda, this would be a good time to create an environment:

```bash
conda create -n PHI python=3.6
```

... and install dependencies.

```bash
pip install -r phi/requirements.txt
```