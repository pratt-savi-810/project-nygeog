a = {"1": 10, "2": 20, "3": 10, "4": 40, "5": 50, "6": 60}
b = {"1": 15, "2": 3, "3": 10, "4": 45, "5": 1, "6": 2477}

import json

def read_json_file(json_file):
	with open(json_file) as json_data:
		d = json.load(json_data)
		return d

def select_time_threshold(j, time_threshold=25):
	d_valid = {}
	for key, val in j.items():
		if val < time_threshold:
			d_valid[key] = val
	return d_valid

def find_od_matches(o_a, d_a, o_b, d_b): # origin A., Dict. destinations A., origin B., Dict. destination B. 
	matches = {}
	for d_a_key,d_a_val in d_a.items():
		for d_b_key, d_b_val in d_b.items():
			
			if d_a_key == d_b_key:
				#print d_a_key, d_a_val, d_b_key, d_b_val
				matches[d_a_key] = {} # shared destination id's match under max time threshold
				matches[d_a_key][o_a + '-' + d_a_key] = d_a_val #origin a - dest a = origin a -> destination a time
				matches[d_a_key][o_b + '-' + d_b_key] = d_b_val #origin b - dest b = origin b -> destination b time
				# remove values from a and b, maybe would save time 
	return matches 
	# compare dicts and find destination hexagons that match
	
def main(a, b):
	a = 'data/input/json/%s.json' % a
	b = 'data/input/json/%s.json' % b

	d_a = select_time_threshold(read_json_file(w))
	d_b = select_time_threshold(read_json_file(v))
	return find_od_matches('300', d_a, '303', d_b)

main(300,303)
