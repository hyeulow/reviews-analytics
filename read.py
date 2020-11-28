data = []
count = 0
total_data_len = 2
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count +=1
		if count % 1000 == 0:
			print(len(data))
	for len_per_data in f:
		print(len(len_per_data))

print(len(data))

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print(sum_len/len(data))
