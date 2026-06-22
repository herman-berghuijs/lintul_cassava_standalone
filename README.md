# LINTUL Cassava NPK
This repository contains a Python implementation of the LINTUL Cassava NPK model. 

## Description
LINTUL Cassava NPK simulates the growth of cassava under potential growth conditions, water-limited growth conditions, and water-and-nutrient growth conditions. 

The first LINTUL Cassava was only capable of simulating the growth of cassava under potential and water-limited growth conditions (Ezui et al., 2018) and it was programmed in the programming language FST. Afterwards, the model was translated from FST to R and the model was extended with a soil nutrient (N, P, and K) model and the possibility to simulate N, P, and K limited growth (Adiele et al., 2022). Finally, the model was again translated in Python such that it could be made compatible with the Python Crop Simulation Engine (PCSE) modeling framework (https://github.com/ajwdewit/pcse). This repository contains the source code of LINTUL Cassava NPK, but the infrastructure to run the model is provided by PCSE.

## Example
Examples on how to run a LINTUL Cassava NPK simulation are provided in a form of a [Jupyter Notebook](example/example.ipynb) and a [Python script](example/example.py). Both examples run a single treatment (NfPfKf) of a cassava nutrient omission trial. In this trial, cassava was sown in 2016. This trial was part of a larger set of cassava nutrient trials in Nigeria (Adiele et al., 2020). Although only one treatment in one single experiment is simulated, the  input files to run all combinations of sowing year, treatment, and location that were used in this set of nutrient omission trials are provided.

## Software requirements
LINTUL Cassava NPK requires a Python interpreter to run. A Python Installation Manager can be dowloaded [here](https://www.python.org/downloads/). Click on the "Download Installation Manager" button to download the Python installation manager. Next, open the Python installation manager and follow the instructions to install or update Python. Follow the instructions to install Python.

Python can be run within PyCharm, an Integrated Development Environment (IDE) for Python. The newest version of PyCharm can be downloaded [here](https://www.jetbrains.com/pycharm/download/?section=windows). Click on the Download button to install an executable to install PyCharm. Note that you will get a free trial period that gives you access to the "Pro features" on top of the free features of PyCharm. After the trial period has finished, PyCharm will offer a paid subscription such that you can keep access to these Pro features. It is not necessary to accept this offer, as both using and further developing LINTUL Cassava can be done with the free features and does not require any of the Pro features.   

## User manual
This user manual assumes that LINTUL Cassava NPK is run within PyCharm. In order to run LINTUL Cassava NPK, follow these steps:
- Downlad the LINTUL Cassava NPK repository in a directory of your choice.
- Open PyCharm
- Click on the hamburger button (three lined equal sign in the left top corner)
- Click on File -> Open
- Browse to the  directory where the contents LINTUL Cassava NPK repository was stored.
- Click on "Select folder"

This will open all code in the repository. In order to run LINTUL Cassava NPK for the first time, a virtual environment needs to be installed. For this purpose, follow these steps:
- Click on the hamburger button.
- Click on Settings
- Click on Python -> Interpreter
- Click on Add Interpreter -> Add Local Interpreter...
- Either click on OK. Or, if you want to choose an alternative interpreter, pick another one and click "OK".
- Open a terminal by either clicking on the Terminal button in the bottom left corner of your screen or press Alt + F12
- Type "pip install -r requirements.txt" (without the quotes) and press Enter. 

The last step will install all packages that are required to run LINTUL Cassava NPK. The names of these packages are listed in .../requirements.txt.

In order to run the example Python script, double click on .../example/example.py in the file structure tree and click the run button (green triangle in the top bar)

In order to run the notebook, double click .../example/example.ipynb in the file structure tree. Double click on the double green triangle in the bar above the notebook content.

## References
Adiele, J. G., Schut, A. G. T., Ezui, K. S., & Giller, K. E. (2022) LINTUL-Cassava-NPK: A simulation model for nutrient-limited cassava growth. Field Crops Research, 281, Article 108488. https://doi.org/10.1016/j.fcr.2022.108488

Adiele, J. G., Schut, A. G. T., van den Beuken, R. P. M., Ezui, K. S., Pypers, P., Ano, A. O., Egesi, C. N., & Giller, K. E. (2020). Towards closing cassava yield gap in West Africa: Agronomic efficiency and storage root yield responses to NPK fertilizers. Field Crops Research, 253, Article 107820. https://doi.org/10.1016/j.fcr.2020.107820

Ezui K.S., Leffelaar P.A., Franke A.C., Mando A., Giller K.E. (2018) Simulating drought impact
and mitigation in cassava using the LINTUL model. Field Crops Research 219: 256-272.
https://doi.org/10.1016/j.fcr.2018.01.033

## Contact persons
Herman Berghuijs (herman.berghuijs@wur.nl)

Tom Schut (tom.schut@wur.nl)