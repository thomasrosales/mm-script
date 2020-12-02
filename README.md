python .\app\image_converter.py --filename input.jpg --output tt --ext png --gray_scale bw1bp --rotate 90 --gray_scale bw8bp --overlay python.png --rotate 15 --verbose --show
## Folder Structure

```
.
├── app
|    ├── __init__.py
|    └── image_converter.py  # script python
├── output                   # file output
├── source                   # soruce files provide to media monks
|    ├── input.jpg
|    ├── python.png
|    └── README.md
├── temp                     # temp file
├── requirements.txt         # python requirements.txt to install dependecies
├── test.py                  # python test file
├── .gitignore
└── README.md
```

## How to use

1. In the source folder must be the files that you want to transform. Also the image that you will use to overlay the base image.
2. It's necessary to have installed python >= 3.7
3. In the root of the folder is the requirements.txt file. Go to there through the terminal and execute the following command:
  ```pip install -r requirements.txt```
4. To run the script you must be execute the following code:
  ```python
  python app/image_converter.py --filename input.jpg --output tt --ext png  --rotate 90 --gray_scale bw8bp --overlay python.png --rotate 15  --verbose --show
  ```
5. To run the test you could execute the following code:
  ```python test.py```
  
 ### Options
 
 | Command Option 	| Description                                                                                                                                             	| Required 	|
|----------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------	|----------	|
| --filename     	| The filename of the base image. It's necessary to expecify the extension. For example: --filename input_file.png                                        	| Yes      	|
| --output       	| The output filename. Only the name without the extension. For example: --output output_file                                                             	| Yes      	|
| --ext          	| The output filename extension. The possible values are ['png', 'jpg']. For example: --ext png                                                           	| Yes      	|
| --rotate       	| It's a number of degrees that it's used to rotate the image. For example: --rotate 15                                                                   	| No       	|
| --gray_scale   	| It's an string that it's used to transform the image in black and white. Optional values are ['bw1bp', 'bw8bp']. For example: --gray_scale bw8bp        	| No       	|
| --overlay      	| It's the name of the image thant you want to overlay with the --filename image. It's necessary write the entire name. For example: --overlay python.png 	| No       	|
| --verbose      	| Show on the command line different messages to indicate which process is running.                                                                       	| No       	|
| --show         	| Show the output image file.                                                                                                                             	| No       	|
