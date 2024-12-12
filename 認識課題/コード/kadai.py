import cv2
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact

# 二値化処理
image_path = "Lenna.jpg"  # 任意の画像ファイルを指定
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# 二値化処理を行う関数
def binarize(threshold):
    """
    二値化処理を行なう
    閾値は threshold で指定

    Parameters
    ----------
    threshold : int
        二値化の閾値
    
    Returns
    -------
    None
    """
    _, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    plt.imshow(binary_image, cmap='gray')
    plt.title("Binarized Image")
    plt.axis("off")
    plt.show()

# スライドバー+二値化画像表示
interact(binarize, threshold=(0, 255, 1))

"""
説明：
thresholdの値よりも大きい画素値を255に、それ以外を0に変換することで二値化処理を行っています。
"""



