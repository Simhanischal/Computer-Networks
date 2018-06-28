#Stop and Wait Protocol
import random
import time
total_frames = 7
timeout = 4
rtt = 4 #Round Trip Time"
acknowledgement = True
wait_time = 0
i = 1
while(i<=total_frames):
    if acknowledgement == True and i!=1:
        print("\n SENDER : ACk for frame %d received " %(i-1))
    print("\n SENDER: Frame %d sent,waiting for ACK---" %(i))
    acknowledgement = False
    wait_time = random.random() % 4 + 1
    if(wait_time == timeout):
         print("SENDER:ACK not received for frame %d => timeout resending frame---- " %(i))
    else:
         time.sleep(rtt/2)
         print("\\n RECEIVER : Frame %d received, ACK sent\n" %(i))
         print("-------------------------------------")
         acknowledgement = True
         time.sleep(rtt/2)
         i = i + 1
	
	
	
#Sliding Window Protocol
import time
rtt = 5 #Round Trip Time"
frames = []
window_size = int(input("Enter the window size :"))
no_of_frames = int(input("Enter the number of frames to transmit:"))
for i in range(no_of_frames):
        inp = int(input("\nEnter frame %d :  " %(i)))
        frames.append(inp)
print("\nAfter sending %d frames at each stage , SENDER waits for ACK " %(window_size))
print("\nSending frames in the following manner ---------")
for i in range(no_of_frames):
    if i % window_size != 0:
         print("%d" %(frames[i]))
    else:
        print("\n%d" %(frames[i]))
        print("\nSENDER : Waiting for ACK-------")
        time.sleep(rtt/2) #stop the execution for specified time
        print("RECEIVER : Frames received ACk sent \n")
        print("---------------------------------------")
        time.sleep(rtt/2)
        print("SENDER : ACK received")