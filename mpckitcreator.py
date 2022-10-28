import os
from soundfile import SoundFile
import xml.etree.ElementTree as ET

directory = '/content/drive/MyDrive/Colab Notebooks/wav_converter/'
os.chdir(directory)

# directory = os.getcwd()

print("Return a dictionary of available formats.\n")
sf.available_formats()

print("Return a dictionary of available subtypes.\n")
sf.available_subtypes('WAV')

print("Return the default subtype for a given format.\n")
sf.default_subtype('WAV')

### List files from directory with Resolution, Channel, Sample Rate and Number of Sample ### 

for filename in os.listdir(directory):
  if filename.endswith(".WAV") or filename.endswith(".wav"):
    with SoundFile(filename, 'r') as myfile:
      print(f"Filename = {myfile.name}")
      print(f"Number of Samples = {myfile.frames-1}")
      print(f"Sample Rate = {myfile.samplerate} Hz")
      if myfile.subtype == 'PCM_16':
        print(f"Resolution = 16 bits")
      if myfile.subtype == 'PCM_24':
        print(f"Resolution = 24 bits")
      if myfile.subtype == 'PCM_32' or  myfile.subtype == 'FLOAT':
        print(f"Resolution = 32 bits")
      if myfile.channels == 2:
        print(f"Channels = Stereo \n")
      else:
        print(f"Channels = Mono \n")
        
### Import MPC *.xpm file and figure out XML Structure ### 

tree = ET.parse('mpc.xpm')
root = tree.getroot()

print(root)
print(root[0])
print(root[1])

for i in root[1]:
  print(i.tag, i.attrib)

for i in root[0][1]:
  print(i.text)
  
print(f"Root - {root}\n")
print(f"File Version - {root[0][0].text}\n")
print(f"Application_Version - {root[0][1].text}\n")
print(f"Program Name - {root[1][0].text}\n")
print(f"Element - {root[1][22].tag}\n")
print(f"Instrument - {root[1][22][0].tag}\n")
print(f"Insrument Number - {root[1][22][0].attrib}\n")
print(f"Layers - {root[1][22][0][66].tag}\n")
print(f"Layer - {root[1][22][0][66][0].tag}\n")
print(f"Layer Number - {root[1][22][0][66][0].attrib}\n")
print(f"Layer Number - {root[1][22][0][66][1].attrib}\n")
print(f"SampleName - {root[1][22][0][66][0][18].tag}\n")
print(f"SampleName Text- {root[1][22][0][66][0][18].text}\n")
print(f"SliceEnd - {root[1][22][0][66][0][24].tag}\n")
print(f"SlicEnd Text- {root[1][22][0][66][0][24].text}\n")

# Loop through tags inside Layers
for i in range(0,28):
  print(f"{i} : {root[1][22][0][66][0][i]}")
  
#  Loop through all the Sample Names in the program - 16 Pads - 8 Pad Banks A-D and E-H
for i in range(0,127):
  smpltxt = root[1][22][i][66][0][18].text
  if smpltxt != None:
    print(f"{i} : {smpltxt}")
  else:
    pass
