"""Figuere gerena la figura
    output_file genera el archivo de salido
    show para mostrar la figura
"""
from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('simple_graph.html')
    fig = figure()

    total_vals = int(input('how many years do you want to graph? '))
    x_vals = []
    for i in range(total_vals):
        x_vals.append(int(input(f'year of netflix? - ')))
    y_vals = []

    for x in x_vals:
        val = int(input(f'Subcribes who were {x} - '))
        y_vals.append(val)
    
    fig.line(x_vals, y_vals, line_width=3)
    show(fig)