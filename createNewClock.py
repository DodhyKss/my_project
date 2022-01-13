def newClock(new_clock, new_minute):
	counter_x = int(new_minute / 60)
	counter_z = 0
	for i in range(counter_x):
		if counter_z < 12:
			counter_z += 1
		else:
			counter_z = 0
			counter_z += 1
	counter_y = new_minute

	if new_minute >= 60:
		new_minute = int(new_minute % 60)
		if new_clock == 12 and counter_y > 120 :
			new_clock = counter_z
		elif new_clock == 12 and counter_y < 120:
			new_clock = 1
		elif counter_x > 1:
			new_clock += counter_z
			if new_clock >= 12:
				for i in range(counter_z):
					if new_clock < 12:
						new_clock += 1
					else:
						new_clock = 0		
		else:
			new_clock += 1 	 

	if new_minute == 0 and new_minute == 0:
		print('input salah') 
	elif new_clock >= 10 and new_minute >= 10:
		print("{0}:{1}".format(new_clock,new_minute))
	elif new_clock >= 10 and  new_minute <= 10:
		print("{0}:0{1}".format(new_clock,new_minute))
	elif new_clock <= 10 and new_minute >= 10:
		print("0{0}:{1}".format(new_clock,new_minute))
	elif new_clock <= 10 and new_minute <= 10:
		print('0{0}:0{1}'.format(new_clock,new_minute))
