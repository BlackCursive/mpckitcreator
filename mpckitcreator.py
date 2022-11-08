import os
import shutil
from read_wav_files import sample_list
from read_wav_files import no_of_frames

directory_path = os.getcwd()
folder_name = os.path.basename(directory_path)

### Copy Blank Template File to New File With Folder Name
newFilename = folder_name + ".xpm"
shutil.copyfile("template.xml", newFilename)

### Write Program Name
with open(newFilename, "r") as templateFile:
  template = templateFile.read()
with open(newFilename, "w") as file:
    file.write(template.replace('__PROGRAMNAME__', folder_name))

### Write all Wav Files and Number of Samples to instruments
with open("instrument.xml", "r") as instrumentFile:
  instrument = instrumentFile.read()
for count, x, y in zip(range(len(sample_list)),sample_list, no_of_frames):
  with open('instrument_full.xml', "a") as file:
    file.write(instrument.replace('__SAMPLENAME__', x).replace('__SLICEEND__', str(y)).replace('__INSTNUMBER__', str(count+1)))
    file.write("\n")

### Write instruments to Program
with open(newFilename, "r") as newProgram:
  newProgramKit = newProgram.read()
with open('instrument_full.xml', "r") as testXML:
  testXMLFile = testXML.read()
with open(newFilename, "w") as newProgramKitFile:
  newProgramKitFile.write(newProgramKit.replace('__INSTRUMENTSANDLAYERS__', testXMLFile))
