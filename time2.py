str_time = int(input("What time is it now?: "))
str_wait_time = int(input("What is the number of hours to wait?: "))
time = str_time
wait_time = str_wait_time

time_when_alarm_go_off = time + wait_time
print("You will wait",wait_time,"hours until it is",time_when_alarm_go_off)
