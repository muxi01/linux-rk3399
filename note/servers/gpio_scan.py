
import os,sys,time
import subprocess


SKIP_GPIOS=[
    "gpio1_b2","gpio1_b0","gpio0_a5","gpio1_a1","gpio1_c7","gpio1_c2",

    "gpio1_b5","gpio3_a4","gpio3_b4","gpio3_b5","gpio4_d4","gpio1_c5","gpio1_c1","gpio1_b6",

    "gpio0_b2","gpio0_a3","gpio4_d1","gpio1_c3",

    "gpio1_b7","gpio1_c0","gpio4_a1","gpio4_a2","gpio3_b2","gpio3_b3",

    "gpio4_a3","gpio4_a4","gpio4_a5","gpio4_a6","gpio4_a7",

    "gpio2_c4","gpio2_c5","gpio2_c6","gpio2_c7","gpio2_d0","gpio2_d1","gpio2_d3","gpio2_a4",

    "gpio4_c2"
]

table=['a','b','c','d','e','f','g']

def scan_gpio():
    for group in range(0,5):
        for pin in range(0,32):
            nmb=int(pin % 8)
            idx=int(pin / 8)
            name ="gpio%d_%c%d" % (group,table[idx],nmb)
            if name in SKIP_GPIOS:
                print("skip this pin %s" % name)
                continue
            gpio_opt="gpioset %d %d=1" % (group,pin)
            print(gpio_opt)
            os.system(gpio_opt)
            time.sleep(1)
            os.system("echo '1' > /dev/watchdog")
    while True:
        os.system("echo '1' > /dev/watchdog")
        time.sleep(1)
        
      
if __name__ == '__main__':   
    scan_gpio()

