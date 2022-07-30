# TilemapGenerator
Creates tilemaps with two textures and a template. 

Usage:
Load all the scripts in a python3 venv and install the dependencies (cv2, numpy).
Create two folders: Images and Tilemaps. Place the textures to combine in the images folder. The final tilemaps will be placed in the Tilemaps-folder. In the main folder, place the mask. Run the TextureMaker script to combine the textures. <br> The CreateTilemapTemplate creates a template of your tilemap mask to use with Vinark117's script to automate rule tiles in Unity (https://github.com/Vinark117/Tutorials/blob/main/RuleTileGenerator/). This script needs a copy of your mask with a 4x4 grid. 
<br>
I've included a mask example for the TextureMaker script and the mask_temp for the CreateTilemapTemplate script.
