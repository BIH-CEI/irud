# Data Model of the Initiative on Rare and Undiagnosed Diseases (IRUD) for Phenopackets

This repository provides the LinkML data model for the Japanese Initiative on Rare and Undiagnosed Diseases (IRUD), along with preprocessing scripts from the IRUD Tracker to enable export to Phenopackets using RareLink.

[![Python CI](https://github.com/BIH-CEI/irud/actions/workflows/python_ci.yml/badge.svg)](https://github.com/BIH-CEI/irud/actions/workflows/python_ci.yml)
[![Python 3.10-3.12](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/downloads/)
[![License: Apache v2.0](https://img.shields.io/badge/License-Apache2.0-yellow.svg)](https://opensource.org/licenses/MIT)
[![Phenopackets](https://img.shields.io/badge/Phenopackets-2.0-purple.svg)](https://phenopacket-schema.readthedocs.io/en/latest/)
[![LinkML](https://img.shields.io/badge/LinkML-1.8.0+-green.svg)](https://linkml.io/)
[![RareLink](https://img.shields.io/badge/RareLink-v2.0.0-blue.svg)](https://github.com/BIH-CEI/RareLink)

> **Note:** This repository does not contain any real patient data but only represents its data model definitions for subsequent local export to Phenopackets.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
- [Usage](#usage)
   - [Importing from RareLink](#importing-from-rarelink)
   - [Generating Phenopackets](#generating-phenopackets)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Description

The IRUD ... 
<!-- TODO -->

You can find more information on the IRUD here: https://www.amed.go.jp/en/program/IRUD/. 

## Features

* **LinkML Data Model:** Defines the structure of the IRUD Tracker data ready for Phenopacket export.
* **Preprocessing:** Includes a preprocessing module to prepare the data from IRUD Tracker for Phenopackets.
* **RareLink Integration:** Enables the export of the processed LinkML-IRUD data to Phenopackets, and via REDCap to HL7 FHIR Genomics Reporting and International Patient Summary resources.

## Getting Started 

### Prerequisites

### Installation

1. Clone the repository with submodules:
   ```bash
   git clone https://github.com/BIH-CEI/irud.git
   cd irud
   git submodule update --init --recursive
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
   ```

3. Install the package in development mode:
   ```bash
   pip install -e .
   ```

   This will install IRUD and its dependencies, including RareLink from the submodule.

## License

Specify the license under which your project is distributed.

## Acknowledgements

tba.