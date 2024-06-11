import os
import sys

sys.path.append(os.path.dirname("../../"))

from Latex_Extractor.main import Image2Text
from Calculator.main import Cal
import cv2
from Controls.main import save_bode_plot

def process_image(img_location):
    I2T = Image2Text()
    img = cv2.imread(img_location)
    cv2.imshow("img",img)
    cv2.waitKey(0)
    return(I2T.run_for_std_scenario(img))

def process_image_for_whiteboard(img_location):
    I2T = Image2Text()
    img = cv2.imread(img_location)
    cv2.imshow("img",img)
    cv2.waitKey(0)
    return(I2T.run_for_training_scenario(img))

def calculate_expression(expression):
    if not expression:
        return []
    cal = Cal()
    ans = []
    for exp in expression:
        ans.append(cal.do_nothing(exp))

    return ans

def save_bode_plot_from_image(numerator,denominator):
    path = save_bode_plot(numerator,denominator)
    return path
