# Docking Streamlit - Molecular Simulation Autodock Vina on the Web

First you need to install ADFSuite at the link bellow: 
https://ccsb.scripps.edu/adfr/downloads/

$ tar zxvf ADFRsuite_x86_64Linux_1.0.tar.gz
$ cd ADFRsuite_x86_64Linux_1.0
$ mkdir /home/iwatobipen/src/ADFRSuite1.0
$ ./install.sh -d /home/iwatobipen/src/ADFRSuite1.0 -c 0
$ export PATH=/home/iwatobipen/src/ADFR1.0/bin

$ pip install vina==1.2.2 

$ alias prepare_receptor="/home/iwatobipen/src/ADFR1.0/bin/prepare_receptor"
$ alias prepare_ligand="/home/iwatobipen/src/ADFR1.0/bin/prepare_ligand"

$ prepare_receptor -r name.pdb -o nameout.pdqt
$ prepare_ligand -l name.pdb -o nameout.pdqt

Test the vina code, to see if everything is right:

$ python dockvina.py

Then you will have the simulation done and the files generated from the code.  After this code version I will code an application ont he web using streamlit. 
