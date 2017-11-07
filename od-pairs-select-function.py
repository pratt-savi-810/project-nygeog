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
				matches[d_a_key] = {} # shared destination id's match under max time threshold
				matches[d_a_key][o_a + '-' + d_a_key] = d_a_val #origin a - dest a = origin a -> destination a time
				matches[d_a_key][o_b + '-' + d_b_key] = d_b_val #origin b - dest b = origin b -> destination b time
				# remove values from a and b, maybe would save time 
	return matches # compare dicts and find destination hexagons that match

def main(a=300, b=303, a_time_threshold=25, b_time_threshold=55):
	a_json = 'data/input/json/%s.json' % a
	b_json = 'data/input/json/%s.json' % b
	d_a = select_time_threshold(read_json_file(a_json), a_time_threshold)
	d_b = select_time_threshold(read_json_file(b_json), b_time_threshold)
	return find_od_matches(str(a), d_a, str(b), d_b)

main(300, 303, 25, 55)

# def main():	
# 	return od_matches_dictionary(300, 303, 25, 55) #test

if __name__ == '__main__':
    main(300, 303, 25, 55)

# do this w/ sys args https://www.saltycrane.com/blog/2007/12/how-to-pass-command-line-arguments-to/