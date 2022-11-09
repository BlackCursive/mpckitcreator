[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
# MPC Kit Creator

Tool to create an Akai MPC program with wave files - MPC Live 1/2, MPC X or MPC one

### Requirements
-- Python 3.6 or higher

-- SoundFile

-- BeautifulSoup

-------------
### Installation 
#### Check your version of Python and upgrade if necessary
```bash
python3 --version
```

#### Clone repository
```bash
git clone https://github.com/BlackCursive/mpckitcreator.git
cd mpckitcreator
```
____
#### Create MPC Program from the wav files in the current directory
```shell
python3 mpckitcreator.py
```
____
#### Display wav file in the current directory and number of samples ( sample length )
```shell
python3 read_wav_files.py
```
____
#### Display wav file in the MPC Program
```shell
python3 read_smpl_mpckit.py FILENAME
```
