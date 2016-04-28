import redis

r_server = redis.Redis('localhost') #this line creates a new Redis object and
                                    #connects to our redis server

f = open("mobile.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line.strip('\r\n'))
    if line.strip('\r\n')!='':
        r_server.rpush('mobile', line.strip('\r\n')) #we use list1 as a list and push element1 as its element
