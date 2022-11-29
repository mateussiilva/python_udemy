from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap
from designer.designer import *
# from utilidades import redimensionarImage
import sys



# NÃO USAR A CAIXAR DO SISTEMA POR PADRÃO : options=QFileDialog.DontUseNativeDialog

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnChooseFile.clicked.connect(self.open_image)
        self.btnRedimensionar.clicked.connect(self.redimensionar)
        self.btnSalvar.clicked.connect(self.salvar)
        
        
    def open_image(self):
        image, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Open Image',
            r'c:\Users\mateus\Pictures',    
        )
        self.inputOpenFile.setText(image)
        self.original_img = QPixmap(image)
        self.labelImage.setPixmap(self.original_img)
        
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))
        
    
    def redimensionar(self):
        largura = int(self.inputLargura.text())
        self.nova_image = self.original_img.scaledToWidth(largura)
        
        self.labelImage.setPixmap(self.nova_image)
        self.inputLargura.setText(str(self.nova_image.width()))
        self.inputAltura.setText(str(self.nova_image.height()))
        
    def salvar(self):
        image, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Open Image',
            r'c:\Users\mateus\Desktop',    
        )
        self.nova_image.save(image, 'PNG')
        
        
        
        
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    window = Window()
    
    window.show()
    qt.exec_()