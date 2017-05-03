from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Functions to visualize data, plot graphs, and evaluate models go here.

def scatter_matrix(X, **kwargs):
	"""
	Plots a scatter matrix of the data.

	Parameters
	--------------------
		X -- numpy matrix of shape (n,d), features

	"""

	indexes = ['Example ' + str(i + 1) for i in xrange(X.shape[0])]
	if 'features' not in kwargs:
		features = ['Feature ' + str(i + 1) for i in xrange(X.shape[1])]
	else:
		features = kwargs.pop('features')
	d = {}
	X_arr = np.asarray(X.T)
	for feat, i in zip(X_arr, xrange(len(X_arr))):
		d[features[i]] = feat
	df = pd.DataFrame(d, index=indexes)
	pd.scatter_matrix(df)
	plt.show()

def correlation_matrix(X, y):
	"""
	Plots a correlation matrix of the data.

	Parameters
	--------------------
		X -- numpy matrix of shape (n,d), features
		y -- numpy matrix of shape (n,1), targets
	"""

	pass # TODO

def two_dimensional_slices(X, y, **kwargs):
	"""
	Plots 2-D slices of the data, with a specific attribute on the horizontal
	axis and the target on the vertical axis.

	Parameters
	--------------------
		X -- numpy matrix of shape (n,d), features
		y -- numpy matrix of shape (n,1), targets

	"""

	if 'color' not in kwargs:
		kwargs['color'] = 'b'

	instances = X.shape[1]
	if 'parameter_name' not in kwargs:
		y_label = 'Label Value'
	else:
		y_label = kwargs.pop('parameter_name') + ' Value'

	if 'x-label' not in kwargs:
		x_label = 'Feature Value'
	else:
		x_label = kwargs.pop('x-label')

	plt.ion()
	for i in xrange(instances):
		plt.scatter(X[:,i].A1, y.A1, **kwargs)
		plt.xlabel(x_label, fontsize=16)
		plt.ylabel(y_label, fontsize=16)
		plt.draw()
		plt.pause(0.001)
		cont = raw_input("Press [C] to see next scatter plot. ")
		if cont != "C" and cont != "c":
			break
		plt.clf()

def label_distribution(y, **kwargs):
	"""
	Plots a histogram displaying the distribution of the targets in the data.

	Parameters
	--------------------
		y -- numpy matrix of shape (n,1), targets

	"""

	if 'color' not in kwargs:
		kwargs['color'] = 'b'
	
	freqs = defaultdict(int)
	for val in y.A1:
		freqs[int(val)] += 1
	perf_values = freqs.keys()
	frequencies = freqs.values()

	if 'parameter_name' not in kwargs:
		label_name = 'Label Value'
	else:
		label_name = kwargs.pop('parameter_name') + ' Value'

	plt.bar(perf_values, frequencies, alpha=0.5, **kwargs)
	plt.xlabel(label_name, fontsize=16)
	plt.ylabel('Frequency', fontsize=16)
	plt.show()
	raw_input("Press any key to continue.")
	plt.clf()

def statistics(X, y, filename='stats.csv', **kwargs):
	"""
	Displays statistics relating to the data.

	Parameters
	--------------------
		X        -- numpy matrix of shape (n,d), features
		y        -- numpy matrix of shape (n,1), targets
		filename -- string, name of file to write to
	"""

	DISPLAY_MAX_ROWS = X.shape[0]
	pd.set_option("display.max_rows", DISPLAY_MAX_ROWS)
	if 'features' not in kwargs:
		digits = str(len(str(X.shape[1])))
		zeros_format = '0' + digits + 'd'
		features = ['Feature ' + format(i + 1, zeros_format) for i in
			xrange(X.shape[1])
		]
	else:
		features = kwargs.pop('features')
	d = {}
	X_arr = np.asarray(X.T)
	for feat, i in zip(X_arr, xrange(len(X_arr))):
		d[features[i]] = feat
	df = pd.DataFrame(d)

	dir = 'stats'
	if not os.path.exists(dir):
		os.makedirs(dir)
	file_path = os.path.join(dir, filename)

	avgs = df.apply(np.mean).values
	stds = df.apply(np.std).values
	d = { 'Mean' : avgs, 'Standard Deviation' : stds }
	df = pd.DataFrame(d, index=features)

	print ('Writing mean and standard deviation of each feature to ' +
		  file_path + '...'),
	df.to_csv(file_path, mode='w+')
	print 'Done.'
