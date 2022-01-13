def new_date(jam_baru, menit_baru):
	counter_x = int(menit_baru / 60)
	counter_z = 0
	for i in range(counter_x):
		if counter_z < 12:
			counter_z += 1
		else:
			counter_z = 0
			counter_z += 1
	counter_y = menit_baru

	if menit_baru >= 60:
		menit_baru = int(menit_baru % 60)
		if jam_baru == 12 and counter_y > 120 :
			jam_baru = counter_z
		elif jam_baru == 12 and counter_y < 120:
			jam_baru = 1
		elif counter_x > 1:
			jam_baru += counter_z
			if jam_baru >= 12:
				for i in range(counter_z):
					if jam_baru < 12:
						jam_baru += 1
					else:
						jam_baru = 0		
		else:
			jam_baru += 1 	 

	if jam_baru == 0 and menit_baru == 0:
		print('input salah') 
	elif jam_baru >= 10 and menit_baru >= 10:
		print("{0}:{1}".format(jam_baru,menit_baru))
	elif jam_baru >= 10 and  menit_baru <= 10:
		print("{0}:0{1}".format(jam_baru,menit_baru))
	elif jam_baru <= 10 and menit_baru >= 10:
		print("0{0}:{1}".format(jam_baru,menit_baru))
	elif jam_baru <= 10 and menit_baru <= 10:
		print('0{0}:0{1}'.format(jam_baru,menit_baru))
