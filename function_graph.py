from math import sin, cos, pi, floor, ceil, sqrt
from time import sleep, time
import os

draw_canvas = {}
canvas_view = ""
draw_symbol = "@"
empty_symbol = "."
vertical_symbol = "│"
arrow_up_symbol = "↑"
horizontal_symbol = "─"
arrow_right_symbol = "🠖"
canvas_size = 60
canvas_size = canvas_size + 1 if canvas_size % 2 == 1 else canvas_size

def plot_function_graph():
    global draw_canvas, canvas_view
    for y in range(canvas_size//2, -canvas_size//2-1, -1): # These cycles make the function graph logic.
        for x in range(-canvas_size//2*2, canvas_size//2*2+1):
            draw_canvas[x,y] = (empty_symbol if x != 0 else (vertical_symbol if y != canvas_size//2 else arrow_up_symbol)) if y != 0 else (horizontal_symbol if x != canvas_size//2*2 else arrow_right_symbol)

            draw_canvas[x, round(sin((x+t)*(sin(t*0.3)*0.1))*5)] = draw_symbol # here you can put your function.
            
    for yV in range(canvas_size//2, -canvas_size//2-1, -1): # These cycles make the function graph visible.
        for xV in range(-canvas_size//2*2, canvas_size//2*2+1):
            canvas_view += draw_canvas[xV,yV]
        canvas_view += "\n"

    print(canvas_view, end=" ")
    draw_canvas = {}
    canvas_view = ""

print(canvas_view)
start_time = time()

while True:
    t = (time() - start_time) * 5

    plot_function_graph()
    sleep(0.02)