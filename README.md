# Flet Images Carousels 
Images Carousles for [Flet](https://github.com/flet-dev/flet), python framework
1) Automatic image carousel (UserControl) + example
2) Basic image carousel (UserControl) + example

## Automatic image carousel 
### Usage
The class takes in:
- **image_list**:*list[tuples]* : list of tuples, each tuple is made of image and image description or only the image
- **perseverace_time**:*float* : seconds of each image perseverance on screen
- **animations**:*list*: list made of 2 animations, IN and OUT
- **descriptive**:*bool*: specify if the carousel needs to show the images description. 
    - default: **True**
    - **[**NOTE**]**: if the images_list's tuples do not contain the image description is needs to be set to **False**

### Demo

descriptive: False |  descriptive: True
:-: | :-:
<video src="https://user-images.githubusercontent.com/81587335/218256446-d8d1be25-7bdf-476a-9dd3-85588b4ba829.mov"> | <video src="https://user-images.githubusercontent.com/81587335/218256505-f1ef25c9-6d95-402f-af00-ecbb99e9c623.mov">

## Basic image carousel 
### Usage
The class takes in:
- **image_list**:*list[tuples]* : list of tuples, each tuple is made of image and image description or only the image
- **animations**:*list*: list made of 2 animations, IN and OUT
- **descriptive**:*bool*: specify if the carousel needs to show the images description. 
    - default: **True**
    - **[**NOTE**]**: if the images_list's tuples do not contain the image description is needs to be set to **False**

### Demo

descriptive: False |  descriptive: True
:-: | :-:
<video src="https://user-images.githubusercontent.com/81587335/218309667-6deb3d16-3468-4e50-bb3c-04763cad58b5.mov"> | <video src="https://user-images.githubusercontent.com/81587335/218309606-84b01e40-976e-460b-95f2-3f4a5ffd0496.mov">
