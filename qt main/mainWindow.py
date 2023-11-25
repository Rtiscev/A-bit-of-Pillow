import sys
import os
import cv2
import random
from PIL import Image, ImageQt, ImageFilter, ImageDraw, ImageOps, ImageChops
from PySide6.QtAsyncio import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

    # Greets the user
    def greetings(self):
        print(f"Hello {self.edit.text()}")


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class ImageBasicEdit(QHBoxLayout):
    imgPath = "./images/im1.jpg"
    originalImg = Image.open(imgPath)
    modifiedImg = originalImg

    def __init__(self):
        super().__init__()

        layout1 = QHBoxLayout()
        buttonsLayout = QVBoxLayout()
        layout3 = QVBoxLayout()

        # Change image button
        btn = QPushButton("Change image")
        btn.pressed.connect(self.changeImg)
        btn.setStyleSheet("background-color:orange;height:100%; font-size:40px;")

        # TRANSVERSE
        btnTRANSVERSE = QPushButton("Clockwise")
        btnTRANSVERSE.pressed.connect(self.Clockwise)
        btnTRANSVERSE.setStyleSheet(
            "background-color:yellow;height:100%; font-size:40px;"
        )

        # TRANSPOSE
        btnTRANSPOSE = QPushButton("Anti ClockWise")
        btnTRANSPOSE.pressed.connect(self.AntiClockWise)
        btnTRANSPOSE.setStyleSheet(
            "background-color:yellow;height:100%; font-size:40px;"
        )

        # FLIP_LEFT_RIGHT
        btnFLIP_LEFT_RIGHT = QPushButton("Horizontal flip")
        btnFLIP_LEFT_RIGHT.pressed.connect(self.HFlip)
        btnFLIP_LEFT_RIGHT.setStyleSheet(
            "background-color:yellow; height:100%; font-size:40px;"
        )

        # FLIP_TOP_BOTTOM
        btnFLIP_TOP_BOTTOM = QPushButton("Vertical flip")
        btnFLIP_TOP_BOTTOM.pressed.connect(self.VFlip)
        btnFLIP_TOP_BOTTOM.setStyleSheet(
            "background-color:yellow; height:100%; font-size:40px;"
        )

        # Combo box of blur filter effects
        self.cBox = QComboBox()
        self.cBox.addItems(
            [
                "BLUR",
                "CONTOUR",
                "DETAIL",
                "EDGE_ENHANCE",
                "EDGE_ENHANCE_MORE",
                "EMBOSS",
                "FIND_EDGES",
                "SHARPEN",
                "SMOOTH",
                "SMOOTH_MORE",
            ]
        )
        self.cBox.setStyleSheet("background-color:red; font-size:40px;")

        # BLUR
        btnBlur = QPushButton("Blur")
        btnBlur.pressed.connect(self.Blur)
        btnBlur.setStyleSheet("background-color:yellow; height:100%; font-size:40px;")

        # INVERT
        btnInvert = QPushButton("Invert")
        btnInvert.pressed.connect(self.Invert)
        btnInvert.setStyleSheet("background-color:yellow; height:100%; font-size:40px;")

        # RESET
        btnReset = QPushButton("Reset")
        btnReset.pressed.connect(self.Reset)
        btnReset.setStyleSheet("background-color:yellow; height:100%; font-size:40px;")

        # SLIDER
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 360)
        self.slider.setValue(0)
        self.slider.setSingleStep(1)
        self.slider.setTickPosition(QSlider.TickPosition.NoTicks)
        self.slider.valueChanged.connect(self.rotate)

        # insert image
        self.label = QLabel()
        image = QPixmap(self.imgPath)
        self.label.setPixmap(image)

        # manage layout
        buttonsLayout.addWidget(btnTRANSVERSE)
        buttonsLayout.addWidget(btnTRANSPOSE)
        buttonsLayout.addWidget(btnFLIP_LEFT_RIGHT)
        buttonsLayout.addWidget(btnInvert)
        buttonsLayout.addWidget(btnFLIP_TOP_BOTTOM)
        buttonsLayout.addWidget(btn)

        buttonsLayout.addWidget(self.cBox)
        buttonsLayout.addWidget(btnBlur)
        buttonsLayout.addWidget(btnReset)

        buttonsLayout.addWidget(self.slider)
        layout3.addWidget(Color("red"))
        layout3.addWidget(Color("purple"))

        layout1.addWidget(self.label)
        layout1.addLayout(buttonsLayout)
        layout1.addLayout(layout3)

        # add styles

        self.addLayout(layout1)

    def changeImg(self):
        curDir = os.path.curdir
        filename, _ = QFileDialog.getOpenFileName(
            QWidget(), "select image", curDir, "Images(*.png *.jpg *.jpeg)"
        )
        if filename:
            self.imgPath = filename
            self.slider.setValue(0)

            self.modifiedImg = self.originalImg = Image.open(filename)
            qimage = ImageQt.ImageQt(self.originalImg)
            pixmap = QPixmap.fromImage(qimage)

            self.label.setPixmap(pixmap)

    def Blur(self):
        choice = self.cBox.currentText()
        _filter = ImageFilter.BLUR
        if choice == "BLUR":
            _filter = ImageFilter.BLUR
        elif choice == "CONTOUR":
            _filter = ImageFilter.CONTOUR
        elif choice == "DETAIL":
            _filter = ImageFilter.DETAIL
        elif choice == "EDGE_ENHANCE":
            _filter = ImageFilter.EDGE_ENHANCE
        elif choice == "EDGE_ENHANCE_MORE":
            _filter = ImageFilter.EDGE_ENHANCE_MORE
        elif choice == "EMBOSS":
            _filter = ImageFilter.EMBOSS
        elif choice == "FIND_EDGES":
            _filter = ImageFilter.FIND_EDGES
        elif choice == "SHARPEN":
            _filter = ImageFilter.SHARPEN
        elif choice == "SMOOTH":
            _filter = ImageFilter.SMOOTH
        elif choice == "SMOOTH_MORE":
            _filter = ImageFilter.SMOOTH_MORE

        self.modifiedImg = im_blurred = self.modifiedImg.filter(_filter)
        self.abridgedSet(im_blurred)

    def Reset(self):
        self.modifiedImg = self.originalImg
        self.abridgedSet(self.originalImg)

    def Invert(self):
        print("here")
        self.modifiedImg = ImageOps.invert(self.modifiedImg)
        self.abridgedSet(self.modifiedImg)

    def Clockwise(self):
        self.modifiedImg = temp = self.modifiedImg.transpose(Image.ROTATE_270)
        self.abridgedSet(temp)

    def AntiClockWise(self):
        self.modifiedImg = temp = self.modifiedImg.transpose(Image.ROTATE_90)
        self.abridgedSet(temp)

    def HFlip(self):
        self.modifiedImg = temp = self.modifiedImg.transpose(Image.FLIP_LEFT_RIGHT)
        self.abridgedSet(temp)

    def VFlip(self):
        self.modifiedImg = temp = self.modifiedImg.transpose(Image.FLIP_TOP_BOTTOM)
        self.abridgedSet(temp)

    def abridgedSet(self, param):
        qimage = ImageQt.ImageQt(param)
        pixmap = QPixmap.fromImage(qimage)
        self.label.setPixmap(pixmap)

    def rotate(self, value):
        pil_Image = Image.open(self.imgPath)
        rotatedImg = pil_Image.rotate(value)
        self.abridgedSet(rotatedImg)


class TwoImagesEdit(QHBoxLayout):
    def __init__(self):
        super().__init__()

        # left side
        image = QPixmap("./images/im1.jpg")
        self.label1 = QLabel()
        self.label1.setPixmap(image)
        self.label1.setScaledContents(True)

        image = QPixmap("./images/im2.jpg")
        self.label2 = QLabel()
        self.label2.setPixmap(image)
        self.label2.setScaledContents(True)

        vHolder = QVBoxLayout()
        vHolder.addWidget(self.label1)
        vHolder.addWidget(self.label2)

        # right side
        vHolder2 = QVBoxLayout()

        image = QPixmap("./images/im3.jpg")
        self.label3 = QLabel()
        self.label3.setPixmap(image)
        self.label3.setScaledContents(True)

        # btnComposite = QPushButton()
        # btnComposite.text = "asdkasdjaskl"
        # btnComposite.pressed.connect(lambda: self.Composite(0, False))

        sliderDiv = QHBoxLayout()

        self.checkbox.pressed.connect(lambda: self.Composite(0))

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 1000)
        self.slider.setValue(0)
        self.slider.setSingleStep(10)
        self.slider.setTickPosition(QSlider.TickPosition.NoTicks)
        self.slider.valueChanged.connect(self.Update)

        sliderDiv.addWidget(self.checkbox)
        sliderDiv.addWidget(self.slider)

        vHolder2.addWidget(self.label3)
        # vHolder2.addWidget(btnComposite)
        vHolder2.addLayout(sliderDiv)

        self.addLayout(vHolder)
        self.addLayout(vHolder2)

    def Update(self, value):
        self.Composite(value)

    def Composite(self, value):
        pilIm1 = Image.open("./images/im1.jpg")
        pilIm2 = Image.open("./images/im2.jpg").resize(pilIm1.size)

        mask = Image.new("L", pilIm1.size, 0)
        draw = ImageDraw.Draw(mask)

        # get W,H center
        WCenter, HCenter = mask.width / 2, mask.height / 2
        radius = value

        draw.ellipse(
            (WCenter - radius, HCenter - radius, WCenter + radius, HCenter + radius),
            fill=255,
        )
        if self.checkbox.isChecked:
            im = Image.composite(pilIm1, pilIm2, mask)
        else:
            im = Image.composite(pilIm2, pilIm1, mask)

        self.abridgedSet(im)

    def abridgedSet(self, param):
        qimage = ImageQt.ImageQt(param)
        pixmap = QPixmap.fromImage(qimage)
        self.label3.setPixmap(pixmap)


class VisualEffectsGen(QGridLayout):
    x0 = 0.1
    y0 = 0.1
    x1 = 0.1
    y1 = 0.1
    tempImg = None
    arr = [(0, 0, 0), (0, 0, 0), (0, 0, 0)]
    qualityV = 100
    rangeMin, rangeMax = -3000, 3000

    def __init__(self):
        super().__init__()

        leftFrame = QVBoxLayout()
        horizontalLayout = QHBoxLayout()

        # x0
        x0Layout = QVBoxLayout()
        self.x0Slider = QSlider(Qt.Orientation.Vertical)
        self.x0Slider.setRange(self.rangeMin, self.rangeMax)
        self.x0Slider.setValue(0)
        self.x0Slider.setSingleStep(1)
        self.x0Slider.setTickPosition(QSlider.TickPosition.NoTicks)
        self.x0Slider.valueChanged.connect(self.modifyX0)
        x0Layout.addWidget(QLabel("x0"))
        x0Layout.addWidget(self.x0Slider)

        # y0
        y0Layout = QVBoxLayout()
        self.y0Slider = QSlider(Qt.Orientation.Vertical)
        self.y0Slider.setRange(self.rangeMin, self.rangeMax)
        self.y0Slider.setValue(0)
        self.y0Slider.setSingleStep(1)
        self.y0Slider.setTickPosition(QSlider.TickPosition.NoTicks)
        self.y0Slider.valueChanged.connect(self.modifyY0)
        y0Layout.addWidget(QLabel("y0"))
        y0Layout.addWidget(self.y0Slider)

        # x1
        x1Layout = QVBoxLayout()
        self.x1Slider = QSlider(Qt.Orientation.Vertical)
        self.x1Slider.setRange(self.rangeMin, self.rangeMax)
        self.x1Slider.setValue(0)
        self.x1Slider.setSingleStep(1)
        self.x1Slider.setTickPosition(QSlider.TickPosition.NoTicks)
        self.x1Slider.valueChanged.connect(self.modifyX1)
        x1Layout.addWidget(QLabel("x1"))
        x1Layout.addWidget(self.x1Slider)

        # y1
        y1Layout = QVBoxLayout()
        self.y1Slider = QSlider(Qt.Orientation.Vertical)
        self.y1Slider.setRange(self.rangeMin, self.rangeMax)
        self.y1Slider.setValue(0)
        self.y1Slider.setSingleStep(1)
        self.y1Slider.setTickPosition(QSlider.TickPosition.NoTicks)
        self.y1Slider.valueChanged.connect(self.modifyY1)
        y1Layout.addWidget(QLabel("y1"))
        y1Layout.addWidget(self.y1Slider)

        horizontalLayout.addLayout(x0Layout)
        horizontalLayout.addLayout(y0Layout)
        horizontalLayout.addLayout(x1Layout)
        horizontalLayout.addLayout(y1Layout)

        # reset button and slider for quality
        qualityVLayout = QVBoxLayout()

        self.qualitySlider = QSlider(Qt.Orientation.Horizontal)
        self.qualitySlider.setRange(0, 1000)
        self.qualitySlider.setValue(100)
        self.qualitySlider.setSingleStep(10)
        self.qualitySlider.setTickPosition(QSlider.TickPosition.NoTicks)
        self.qualitySlider.valueChanged.connect(self.vChanged)

        qualityVLayout.addWidget(QLabel("Quality"))
        qualityVLayout.addWidget(self.qualitySlider)
        btnReset = QPushButton("Reset")
        btnReset.pressed.connect(self.Reset)
        qualityVLayout.addWidget(btnReset)

        # x,y values:
        X0Frame = QHBoxLayout()
        Y0Frame = QHBoxLayout()
        X1Frame = QHBoxLayout()
        Y1Frame = QHBoxLayout()

        self.x0L = QLabel()
        self.y0L = QLabel()
        self.x1L = QLabel()
        self.y1L = QLabel()
        self.x0L.text = self.x0
        self.y0L.text = self.y0
        self.x1L.text = self.x1
        self.y1L.text = self.y1

        X0Frame.addWidget(QLabel("X0"))
        X0Frame.addWidget(self.x0L)
        Y0Frame.addWidget(QLabel("Y0"))
        Y0Frame.addWidget(self.y0L)
        X1Frame.addWidget(QLabel("X1"))
        X1Frame.addWidget(self.x1L)
        Y1Frame.addWidget(QLabel("Y1"))
        Y1Frame.addWidget(self.y1L)

        self.colorize = QPushButton("Colorize image")
        self.colorize.pressed.connect(self.fnColorize)
        self.createMandra = QPushButton("Create M image")
        self.createMandra.pressed.connect(self.modify)
        self.saveImg = QPushButton("Save image")
        self.saveImg.pressed.connect(self.fnSaveImg)

        leftFrame.addLayout(X0Frame)
        leftFrame.addLayout(Y0Frame)
        leftFrame.addLayout(X1Frame)
        leftFrame.addLayout(Y1Frame)
        leftFrame.addLayout(horizontalLayout)
        leftFrame.addLayout(qualityVLayout)
        leftFrame.addWidget(self.colorize)
        leftFrame.addWidget(self.createMandra)
        leftFrame.addWidget(self.saveImg)

        # right side
        image = QPixmap()
        self.label1 = QLabel()
        self.label1.setPixmap(image)

        # self.label1.setScaledContents(True)

        self.setColumnStretch(0, 3)
        self.setColumnStretch(1, 7)
        self.addLayout(leftFrame, 0, 0)
        self.addWidget(self.label1, 0, 1, Qt.AlignmentFlag.AlignCenter)

    def modifyX0(self, value):
        self.x0 = value / 1000
        # self.x0 = math.sin(math.pi * value) * 2.5
        self.x0L.setText(str(self.x0))
        # self.modify()

    def modifyY0(self, value):
        self.y0 = value / 1000
        # self.y0 = math.cos(math.pi * value) * 1.5
        self.y0L.setText(str(self.y0))
        # self.modify()

    def modifyX1(self, value):
        self.x1 = value / 1000
        # self.x1 = math.sin(math.pi * value) * 2.5
        self.x1L.setText(str(self.x1))
        # self.modify()

    def modifyY1(self, value):
        self.y1 = value / 1000
        # self.y1 = math.cos(math.pi * value) * 1.5
        self.y1L.setText(str(self.y1))
        # self.modify()

    def vChanged(self, value):
        self.qualityV = value
        # self.modify()

    def fnSaveImg(self):
        a = random.randint(0, 9000)
        self.tempImg.save(f"{a}.jpeg")

    def fnColorize(self):
        self.arr = []
        for cc in range(3):
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            rgb_color = (red, green, blue)
            self.arr.append(rgb_color)
        self.modify()

    def modify(self):
        manderbrot_img = Image.effect_mandelbrot(
            (1000, 800),
            # -0.114, 0.352, 0.616, 0.863
            # (-0.7436, 0.1306, -0.7426, 0.1316),
            # (-0.000125, -0.00000125, 0.000125, 0.000125),
            # (-0.7208, 0.1319, -0.7185, 0.1332),
            (self.x0, self.y0, self.x1, self.y1),
            self.qualityV,
        )

        if self.arr == [(0, 0, 0), (0, 0, 0), (0, 0, 0)]:
            print("yes")
            img2 = manderbrot_img
        else:
            img2 = ImageOps.colorize(
                manderbrot_img,
                black=self.arr[0],
                white=self.arr[1],
                mid=self.arr[2],
            )
        self.abridgedSet(img2)

    def abridgedSet(self, param):
        self.tempImg = param
        qimage = ImageQt.ImageQt(param)
        pixmap = QPixmap.fromImage(qimage)
        self.label1.setPixmap(pixmap)

    def Reset(self):
        self.qualitySlider = self.x0 = self.y0 = self.x1 = self.y1 = 0
        self.x0Slider.setValue(0)
        self.x1Slider.setValue(0)
        self.y0Slider.setValue(0)
        self.y1Slider.setValue(0)
        self.qualitySlider.setvalue(0)


class Deformer:
    choice = 1

    def __init__(self, choice):
        # print("hi")

        self.choice = choice

    def getmesh(self, img):
        w, h = img.size

        # right mirror
        if self.choice == 1:
            left = ((0, 0, w // 2, h), (0, 0, 0, h, w // 2, h, w // 2, 0))
            right = ((w // 2, 0, w, h), (w // 2, 0, w // 2, h, 0, h, 0, 0))
            return [left, right]

        # left mirror
        if self.choice == 2:
            left = ((0, 0, w // 2, h), (w, 0, w, h, w // 2, h, w // 2, 0))
            right = ((w // 2, 0, w, h), (w // 2, 0, w // 2, h, w, h, w, 0))
            return [left, right]

        # top mirror
        if self.choice == 3:
            top = ((0, 0, w, h // 2), (0, 0, 0, h // 2, w, h // 2, w, 0))
            down = ((0, h // 2, w, h), (0, h // 2, 0, 0, w, 0, w, h // 2))
            return [top, down]

        # bottom mirror
        if self.choice == 4:
            top = ((0, 0, w, h // 2), (0, h, 0, h // 2, w, h // 2, w, h))
            down = ((0, h // 2, w, h), (0, h // 2, 0, h, w, h, w, h // 2))
            return [top, down]

        # quad mirror
        if self.choice == 5:
            LeftTop = ((0, 0, w // 2, h // 2), (0, h, 0, 0, w, 0, w, h))
            RightTop = ((w // 2, 0, w, h // 2), (w, h, w, 0, 0, 0, 0, h))
            LeftDown = ((0, h // 2, w // 2, h), (0, 0, 0, h, w, h, w, 0))
            RightDown = ((w // 2, h // 2, w, h), (w, 0, w, h, 0, h, 0, 0))
            return [LeftTop, LeftDown, RightTop, RightDown]


class Thread(QThread):
    choice = 5
    changePixmap = Signal(QPixmap)

    @Slot(int)
    def changeEffect(self, choice):
        self.choice = choice

    def run(self):
        cap = cv2.VideoCapture(0)
        while True:
            check, frame = cap.read()
            if check:
                resized_image = cv2.resize(
                    frame, (1000, 800), interpolation=cv2.INTER_LINEAR
                )
                color_converted = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

                pilIMG = Image.fromarray(color_converted)

                deformed = ImageOps.deform(pilIMG, Deformer(self.choice))

                qimage = ImageQt.ImageQt(deformed)
                pixmap = QPixmap.fromImage(qimage)
                self.changePixmap.emit(pixmap)


class Camera(QHBoxLayout):
    changeMode = Signal(int)
    th = Thread()

    def __init__(self):
        super().__init__()

        # insert image
        self.label3 = QLabel()
        self.label3.setFixedSize(1000, 800)
        # self.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.button1 = QPushButton("right mirror")
        self.button2 = QPushButton("left mirror")
        self.button3 = QPushButton("top mirror")
        self.button4 = QPushButton("bottom mirror")
        self.button5 = QPushButton("quad mirror")

        self.button1.setStyleSheet(
            "border:5px solid red;border-radius:40px;background-color:orange;height:100%; font-size:40px;"
        )
        self.button2.setStyleSheet(
            "border:5px solid red;border-radius:40px;background-color:orange;height:100%; font-size:40px;"
        )
        self.button3.setStyleSheet(
            "border:5px solid red;border-radius:40px;background-color:orange;height:100%; font-size:40px;"
        )
        self.button4.setStyleSheet(
            "border:5px solid red;border-radius:40px;background-color:orange;height:100%; font-size:40px;"
        )
        self.button5.setStyleSheet(
            "border:5px solid red;border-radius:40px;background-color:orange;height:100%; font-size:40px;"
        )

        self.button1.clicked.connect(lambda: self.Switch(1))
        self.button2.clicked.connect(lambda: self.Switch(2))
        self.button3.clicked.connect(lambda: self.Switch(3))
        self.button4.clicked.connect(lambda: self.Switch(4))
        self.button5.clicked.connect(lambda: self.Switch(5))

        self.th = Thread(self)
        self.th.changePixmap.connect(self.setImage)
        self.th.start()

        self.newVertical = QVBoxLayout()
        self.newVertical.addWidget(self.button1)
        self.newVertical.addWidget(self.button2)
        self.newVertical.addWidget(self.button3)
        self.newVertical.addWidget(self.button4)
        self.newVertical.addWidget(self.button5)

        self.addLayout(self.newVertical)
        self.addWidget(self.label3)

    def Switch(self, choice):
        print(self.th.choice)
        self.th.choice = choice

    @Slot(QPixmap)
    def setImage(self, image):
        self.label3.setPixmap(image)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        main_layout = QHBoxLayout(self)
        self.setLayout(main_layout)

        # create a tab widget
        tab = QTabWidget(self)

        # 1 tab
        first_page = QWidget(self)
        first_page.setLayout(ImageBasicEdit())
        # 2 tab
        # second_page = QWidget(self)
        # second_page.setLayout(TwoImagesEdit())
        # 3 tab
        third_page = QWidget(self)
        third_page.setLayout(VisualEffectsGen())
        # 4 tab
        fourth_page = QWidget(self)
        fourth_page.setLayout(Camera())

        tab.addTab(first_page, "AHHH")
        # tab.addTab(second_page, "gggg")
        tab.addTab(third_page, "rtttt")
        tab.addTab(fourth_page, "rtttt")

        main_layout.addWidget(tab)

        self.showMaximized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.setStyleSheet("background-color:red;")
    sys.exit(app.exec())
