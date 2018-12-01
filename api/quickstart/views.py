from django.http import HttpResponse
from django.template.loader import get_template
from matplotlib import pylab
from pylab import *
from io import *
from io import StringIO 
from PIL import *
import PIL
import PIL.Image
import io
import base64
import matplotlib.pyplot as plt
import numpy as np

from django.shortcuts import render, render_to_response

from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components

def index(request):
    t = get_template('home-company.html')
    html = t.render()
    return HttpResponse(html)
		
def login(request):
    t = get_template('login.html')
    html = t.render()
    return HttpResponse(html)
		
def homeCompany(request):
    t = get_template('home-company.html')
    html = t.render()
    return HttpResponse(html)
		
def homePerson(request):
    t = get_template('home-person.html')
    html = t.render()
    return HttpResponse(html)
		
def resultCompany(request):
    x= ['San Francisco', 'Virginia', 'New York', 'Washington']
    y= [77,73,72,60]
    title = 'Offers x city'

    plot = figure(
				title= title , 
        x_axis_label= 'City', 
				x_range = x,
        y_axis_label= 'Offer amount', 
        plot_width =950,
        plot_height =400)

    plot.line(x, y, legend= 'Amount', line_width = 2)
    script, div = components(plot)

    x= ['Week 1', 'Week 2', 'Week 3', 'Week 4']
    y= [175,230,235,234]

    y2= [100,200,205,204]
    title = 'Offers x city'

    plot2 = figure(
				title= title , 
        x_axis_label= 'Week', 
				x_range= x,
        y_axis_label= 'Offer amount', 
        plot_width =950,
        plot_height =400)

    plot2.vbar(x,top=y, legend= 'Amount', width = 2)
    plot2.vbar(x, top=y2, legend= 'Amount', width = 2, line_color='red')
    script2, div2 = components(plot2)

    x= ['Interno', 'Externo']
    y= [2800,1600]

    plot3 = figure(
				title= title , 
				x_range=x,
        plot_width =400,
        plot_height =400)

    plot3.vbar(x,top=y, legend= 'Amount', width = 0.9)
    script3, div3 = components(plot3)



    return render_to_response(
               'result-company.html',
               {'script1' : script , 'fig1' : div,
               'script2' : script2 , 'fig2' : div2,
               'script3' : script3 , 'fig3' : div3}
    )
		
def resultPerson(request):
    np.random.seed(19680801)

    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Example data
    people = ('New York', 'San Francisco', 'Virginia', 'Washington')
    y_pos = np.arange(len(people))
    performance = 3 + 100 * np.random.rand(len(people))
    error = np.random.rand(len(people))

    ax.bar(y_pos, performance, xerr=error, align='center',
    color='#730000', ecolor='red')
    ax.set_xticks(y_pos)
    ax.set_xticklabels(people)
    ax.invert_xaxis()  # labels read top-to-bottom
    ax.set_ylabel('Offer amount')
    ax.set_title('Offer amount by city')

		#Despues de crear la img llamamos esto para convertirla a base64 y poder renderizarla en el html
    buffer = io.BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    graphIMG = PIL.Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb())
    graphIMG.save(buffer, "PNG")
    
    g1 = base64.b64encode(buffer.getvalue())
    g1 = g1.decode('ascii')
	
    np.random.seed(19680801)

    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Example data
    people = ('Next Week', '2 Week', '3 Week', '4 Week')
    y_pos = np.arange(len(people))
    performance = 3 + 300 * np.random.rand(len(people))
    error = np.random.rand(len(people))

    ax.bar(y_pos, performance, xerr=error, align='center',
    color='#730000', ecolor='red')
    ax.set_xticks(y_pos)
    ax.set_xticklabels(people)
    ax.invert_xaxis()  # labels read top-to-bottom
    ax.set_ylabel('Offer amount')
    ax.set_title('Offer amount by week')

		#Despues de crear la img llamamos esto para convertirla a base64 y poder renderizarla en el html
    buffer = io.BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    graphIMG = PIL.Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb())
    graphIMG.save(buffer, "PNG")
    
    g2 = base64.b64encode(buffer.getvalue())
    g2 = g2.decode('ascii')

    t = get_template('result-person.html')
    html = t.render({'graph1': g1, 'graph2': g2})
    return HttpResponse(html)
		
