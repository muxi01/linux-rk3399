
import os,sys,time
import subprocess


SKIP_GPIOS_SET1=[
    "gpio0_a3","gpio0_a5",
    "gpio1_a6",
    "gpio2_c4","gpio2_c5","gpio2_c6","gpio2_c7",
    "gpio2_d0","gpio2_d1","gpio2_d2","gpio2_d3","gpio2_d4",
]

SKIP_GPIOS=[
    "gpio0_a0","gpio0_a5",
    "gpio1_a6",
    "gpio2_c4","gpio2_c5","gpio2_c6","gpio2_c7",
    "gpio2_d0","gpio2_d1","gpio2_d2","gpio2_d3","gpio2_d4",
]


table=['a','b','c','d','e','f','g']

def scan_gpio():
    begin =int(sys.argv[1])
    end=int(sys.argv[2])
    for group in range(begin,end):
        for pin in range(0,32):
            nmb=int(pin % 8)
            idx=int(pin / 8)
            name ="gpio%d_%c%d" % (group,table[idx],nmb)
            if name in SKIP_GPIOS:
                print("skip this pin %s" % name)
                continue
            gpio_opt="gpioset %d %d=0" % (group,pin)
            print(gpio_opt)
            os.system(gpio_opt)
            time.sleep(1)
        
      
if __name__ == '__main__':   
    if len(sys.argv) < 2:
        print("%s <start> <end>" % sys.argv[0])
    else:
        scan_gpio()

