from django.shortcuts import render
from pylab import *
import matplotlib
matplotlib.use('Agg')

# Create your views here.

def index(request):
	return render(request, 'mandelapp/index.html')
	
def generate(request):
	breite = int(request.GET.get('breite',''))
	hohe = int(request.GET.get('hohe',''))
	iterationen = int(request.GET.get('iterationen',''))
	path_save = createMandelBrot(breite, hohe, iterationen)
	
	return render(request, 'mandelapp/index.html', {'code':5, 'path': path_save})

def createMandelBrot(breite, hohe, iter):
	path = 'C:\\Users\\carole\\Desktop\\Django-1.9.11\\django\\bin\\mandelbrot\\assets\\mandelbrot.png'
	iterations = iter
	density = 1000
	x_min, x_max = -2, 1
	y_min, y_max = -1.5, 1.5
	x, y = meshgrid(linspace(x_min, x_max, density),
	linspace(y_min, y_max, density))
	c = x + 1j*y
	z = c.copy()
	m = zeros((density, density))
	for n in xrange(iterations):
		#print "Completed %d %%" % (100 * float(n)/iterations)
		indices = (abs(z) <= 10)
		z[indices] = z[indices]**2 + c[indices]
		m[indices] = n
	imshow(log(m), cmap=cm.hot, extent=(x_min, x_max, y_min, y_max))
	savefig(path);
	title('Mandelbrot Set')
	xlabel('Re(z)')
	ylabel('Im(z)')
	return path
	#show()
