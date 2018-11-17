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

def home(request):
    np.random.seed(19680801)

    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Example data
    people = ('*4 Semana', '3 Semana', '2 Semana', '1 Semana')
    y_pos = np.arange(len(people))
    performance = 3 + 100 * np.random.rand(len(people))
    error = np.random.rand(len(people))

    ax.bar(y_pos, performance, xerr=error, align='center',
    color='#730000', ecolor='red')
    ax.set_xticks(y_pos)
    ax.set_xticklabels(people)
    ax.invert_xaxis()  # labels read top-to-bottom
    ax.set_ylabel('Ofertas estimadas')
    ax.set_title('Ofertas laborales x semana')

		#Despues de crear la img llamamos esto para convertirla a base64 y poder renderizarla en el html
    buffer = io.BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    graphIMG = PIL.Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb())
    graphIMG.save(buffer, "PNG")
    
    g = base64.b64encode(buffer.getvalue())
    g = g.decode('ascii')
		
    t = get_template('current_datetime.html')
    html = t.render({'graphic': g})
    return HttpResponse(html)
		
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

    t = get_template('result-company.html')
    html = t.render({'graph1': g1, 'graph2': g2})
    return HttpResponse(html)

		
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
		
