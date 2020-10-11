## Using Optical Character Recognition to read text on aerial imagery
This repository showcases my attempt to use optical character recognition to read text on an image and use this text to rename the file.  
This repository can also be used as a tutorial for basic use of optical character recognition.  
For those not wanting to download this repository or run the notebook you can view the notebook as a pdf.  
The PDF is in this repository and is called *ImageOCR.pdf*

## Getting Started
Before you can use this repository locally you must first install tesseract a stand alone application.  
The notebook in this repository uses tesseract 5.0.0 Alpha version. Using other versions will likely result in different and  
poorer text predictions that those presented here notebook.
For [Windows](https://github.com/UB-Mannheim/tesseract/wiki) installation of tesseract for [Linx/Ubuntu](https://github.com/tesseract-ocr/tesseract/wiki#ubuntu-ppa) and [Mac](https://github.com/tesseract-ocr/tesseract/wiki#macos)
 
Once tesseract is installled if you have Anaconda installation you can use the Anconda Prompt to install all of the python libraries  
and their dependencies. In the Anaconda Prompt change directories so that you are in the local copy of this repository. In the prompt then enter:

*conda env create*  
once the environment is created enter:  
*conda activate imageOCR*  
then enter:  
*jupyter notebook*

From here open the notebook entitled *ImageOCR.ipynb*

## Example:
This image after it was scanned was given the filename *0F6185_0001_2.tif*, my employer wanted to rename the file so that it used the information in the top right of this image.  
Renaming the files in the manner would ultimately make them more searchable and useable for future use.  
So rather than manually open each image and to see view this text I proposed using optical character recognition  
to change the file name from *0F6185_0001_2.tif* to *DWW-A-5-1.tif* in this example. Open the notebook and follow  
along with the steps I used to be able to read these text from the image.

![Historic Scanned Forest Service Imagery](images/singleImage/0F6185_0001_2.png?raw=true)

