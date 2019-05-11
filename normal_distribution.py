import numpy as np 
import matplotlib.pyplot as plt 


def bin_range(min_x, max_x, bin_size):
	result = []
	current = min_x

	while current <= max_x:
		result.append(current)
		current += bin_size

	return result	

mean = 5.0
std = 0.5
grain = 100


random_samples = sorted(np.random.normal(mean, std, 100))

min_sample = min(random_samples)
max_sample = max(random_samples)
bin_size = abs(min_sample - max_sample)/grain


bins = bin_range(min_sample, max_sample, bin_size)
bin_dict = {}

sample_index = 0
current_bin_index = 0
while (sample_index < len(random_samples)):
	current_bin = bins[current_bin_index]
	sample = random_samples[sample_index]
	if sample <= current_bin + bin_size:
		if current_bin not in bin_dict:
			bin_dict[current_bin] = []
		bin_dict[current_bin].append(sample)
		sample_index += 1
	else:
		current_bin_index += 1

x_values = [k for k, v in bin_dict.items()]
y_values = [len(v) for k, v in bin_dict.items()]

plt.plot(x_values, y_values)
plt.show()

