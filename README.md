
# CD Creator

The script for burn data from file to CD.


## Description

 - Skrip get data from the .txt file.
 - Take row from txt file and look for file in path wich contain the row in filename.
 - Burn the files into CD.




## Environment Variables

To run this project, you will need to add the following environment variables to `Utils\Utls.py`

`ACD_LETTER` - The letter of CD ROM

`FILE` - Path of data file. Default is `C:\\CD_Creator\\sn.txt`

`DSC_PATH` - Path to serch area for burn files



## Deployment

To deploy this project run `start.bat` or `main.py`