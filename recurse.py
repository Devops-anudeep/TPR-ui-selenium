import os, threading

def seq():
	for i in range(1,300):
		j = "%03d" % i;
		name = "user"+str(j)
		print(name)
		command = "python TPR_Login_Selenium2.py " + name
		print(command)
	
def exec_cmd(name):	
	print(name + "\n")
	command = "python TPR_Login_Selenium2.py " + name
	print(command + "\n")
	os.system(command)
	
t1=threading.Thread(target=exec_cmd, args=("user001",) )
t2=threading.Thread(target=exec_cmd, args=("user002",) )
t3=threading.Thread(target=exec_cmd, args=("user003",) )
t4=threading.Thread(target=exec_cmd, args=("user004",) )
t5=threading.Thread(target=exec_cmd, args=("user005",) )
t6=threading.Thread(target=exec_cmd, args=("user006",) )
t7=threading.Thread(target=exec_cmd, args=("user007",) )
t8=threading.Thread(target=exec_cmd, args=("user008",) )
t9=threading.Thread(target=exec_cmd, args=("user009",) )
t0=threading.Thread(target=exec_cmd, args=("user010",) )
	
t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()
# t7.start()
# t8.start()
# t9.start()
# t0.start()

t1.join()
print("Verified User1")
# t2.join()
# print("Verified User2")
# t3.join()
# print("Verified User3")
# t4.join()
# print("Verified User4")
# t5.join()
# print("Verified User5")
# t6.join()
# print("Verified User1")
# t7.join()
# print("Verified User2")
# t8.join()
# print("Verified User3")
# t9.join()
# print("Verified User4")
# t0.join()
# print("Verified User5")
