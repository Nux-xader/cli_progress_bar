def progress_bar(progs, total):
	percent = 100*(progs/float(total))
	bar = '-'*int(percent)+' '*(100-int(percent))
	print(f"\r[{bar}] {percent:.2f}%", end="\r")


##########
# sample #
##########

import random, time
delay = [i/1000 for i in range(120)]
task = [i for i in range(random.randint(130, 270))]
for x, y in enumerate(task):
	time.sleep(random.choice(delay))
	progress_bar(x+1, len(task))