##################################################
# Name: Myles Crandall
# Collaborators: n/a
# Estimate of time spent (hr): 2.0
##################################################

from pgl import *

#1a
def create_histogram_array(data:list[int])->list[int]:
    hist = [0] * 10  # Create list of 10 zeros for digits 0-9
    for num in data:
        hist[num] += 1  # Increment count for each digit
    return hist

#1b
def print_histogram(hist:list[int]) -> None:
    for i in range(len(hist)):
        if hist[i] > 0:
            print(f"{i}: {'*' * hist[i]}")

#1c
def graph_histogram(hist:list[int], width:int, height:int) -> None:
    gw = GWindow(width, height)
    max_value = max(hist)
    bar_width = width / len(hist)
    scale = height / max_value

    def my_rect(x,y,w,h,color):
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)

    for i in range(len(hist)):
        if hist[i] > 0:
            bar_height = hist[i] * scale
            my_rect(i * bar_width, height - bar_height, bar_width, bar_height, "red")

# Some testing printouts for your use!
PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]
hist = create_histogram_array(PI_DIGITS)
print(hist)
print_histogram(hist) # uncomment to test
graph_histogram(hist, 400, 400) # uncomment to test
