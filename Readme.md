# How to Use

By This you can easily convert 
- Labelme json file to Pngs (To preview)
- Labelme json file to Masked Images ( To Use in the Image Segmentation Unet Model)


## Labelme Json file to Voc Dataset (Png File & Segment Class) 

1. Output Path should not exist
2. Made a ```.Txt``` file containing all labels (each in new line) present in Json file
3. Go to Directory where ```labelme2voc.py``` file is present

``` python labelme2voc.py path\to\json path\to\output  --labels path\to\labels.txt ```

## Labelme Json file to Masked PNGs (PNG can be used  in Image Segmentation Unet Model) 
1. Open ```labelme2masked.py``` file
2. Change the ```output_dir``` and ```json_dir``` accordingly 
3. Define all labels that are present in the JSON file in the ```Labels``` array

Email Us @ bilal.ahsan7705@gmail.com

1. Visit the application homepage: [https://www.utuexample.com](https://www.example.com).
