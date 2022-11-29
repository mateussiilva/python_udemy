from PIL import Image

def redimensionarImage():
    ...
    
path_img = r'C:/Users/mateus/Pictures/Screenshots/Captura de tela_20221125_201725.png'
img = Image.open(path_img)
img_pequena = img.resize((20,20))
img_pequena.save("print.png")
img_pequena.show()