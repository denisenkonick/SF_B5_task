import time

NUM_RUNS = 10

def time_this(num_runs=1):
	def decorator(func):
		def avg_time_func():
			avg_time = 0
			for _ in range(num_runs):
			    t0 = time.time()

			    ### <<полезный>> код
			    func()

			    t1 = time.time()
			    avg_time += (t1 - t0)
			avg_time /= NUM_RUNS
			print("Выполнение заняло %.5f секунд" % avg_time)
		return avg_time_func
	return decorator



@time_this(num_runs=10)
def f():
    for j in range(1000000):
        pass

f()