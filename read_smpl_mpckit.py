import os
import sys
from bs4 import BeautifulSoup
from subprocess import call

xpm = sys.argv[1]

with open(xpm, 'r') as f:
    data = f.read()

soup = BeautifulSoup(data, "xml")

def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name == 'posix' else 'cls')
clear()

### Function to get Filename and Number of Samples from a Program kit
def read_smpl_list(xpm):
  count=0
  for tag in soup.find_all('SampleName'):
    if len(tag.get_text(strip=True)) != 0:
        # print(f"i+1} Sample Name : {tag.text} / Slice End : {slcEnd}")
        count +=1
        print(f"{count} - {tag.text}")
read_smpl_list(xpm)
