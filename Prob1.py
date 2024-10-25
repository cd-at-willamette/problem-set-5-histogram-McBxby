##################################################
# Name: Myles Crandall
# Collaborators: n/a
# Estimate of time spent (hr): 2.0
##################################################

from pgl import *

#1a
def create_histogram_array(data:list[int])->list[int]:
    hist = [0] * (max(data) + 1)
    for value in data:
        hist[value] += 1
    return hist
#1b
def print_histogram(hist:list[int]) -> None:
    [print(str(i) + ": " + hist[i] * "*") for i in range(len(hist))]
#1c
def graph_histogram(hist:list[int], width:int, height:int) -> None:
    gw = GWindow(width, height)
    
    def my_rect(x,y,w,h,color):
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)
    
    col_width = width / len(hist)
    max_val = max(hist)
    scale = height / max_val
    
    for i in range(len(hist)):
        x = i * col_width
        h = hist[i] * scale
        y = height - h
        my_rect(x, y, col_width, h, "red")

# Some testing printouts for your use!
PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]
hist = create_histogram_array(PI_DIGITS)
print(hist)
print_histogram(hist) # uncomment to test
graph_histogram(hist, 400, 400) # uncomment to test
