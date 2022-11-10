from os import remove
import threading
import time
import random
from colorama import Fore, Style

# Creará una lista en la memoria con la cantidad
# dada y lo rellenará con números aleatorios 
def ram_thread(size):
	l = []
	for x in range(size):
		l.append(999999999999)



# Creara archivos
def file_thread(filename, size):
	filename = "tmp/" + filename
	fd = open(filename, "w")
	
	for x in range(size):
		fd.write("12345678901234567890123456789012345678901234567890")

	fd.close()
	remove(filename)



def run(n):
	times = [] 							# Lista de tiempos de cada ejecucion
	n_threads = 10					# Num of threads
	s_ram_thread = 10**7	 	# Item nums in each thread list
	s_file_thread = 10**6 	# Lines nums in each block of file
	men_thrd_list = []			# Lista de hilos de memoeria ram
	file_thrd_list = []			# Lista de hilos de archivo

	print(f"Runs: {n}. Threads: {n_threads}. size(m): {s_ram_thread}. size(f): {s_file_thread}")
	for i in range(n):
		print(f"Run {i+1}/{n}.")
		t_start = time.time()

		for i in range(n_threads):
			men_thrd_list.append(threading.Thread(target=ram_thread, args=(s_ram_thread,)))
			men_thrd_list[i].start()
			file_thrd_list.append(threading.Thread(target=file_thread, args=(str(i), s_file_thread,)))
			file_thrd_list[i].start()

		# Eliminar de la lista todos los hilos de memoeria que hayan terminado
		while len(men_thrd_list) > 0:
			print("                                          \r" +
				f"Ram threads for ends: {len(men_thrd_list)}\r", end="")
			for thrd in men_thrd_list:
				if not thrd.is_alive():
					men_thrd_list.remove(thrd)

		# Eliminar de la lista todos los hilos de archivos que hayan terminado
		while len(file_thrd_list) > 0:
			print("                                          \r" +
				f"File threads for ends: {len(file_thrd_list)}\r", end="")
			for thrd in file_thrd_list:
				if not thrd.is_alive():
					file_thrd_list.remove(thrd)

		t_end = time.time()
		times.append(t_end - t_start)
		print("                                          \r" +
			f"Time: {round((t_end - t_start)*1000)} ms")

	return sum(times) / n



def main():
	mean = run(5)
	print(f"{Fore.YELLOW}Average: {round(mean * 1000)} ms. {Fore.RESET}")



if __name__ == '__main__':
	main()