#include <fcntl.h>
#include <linux/i2c-dev.h>
#include <stdio.h>
#include <unistd.h>

int main(int args,char **argv) {

    char name[128];
    int bus_number=0;
    int dev_address=0;
    int reg_address=0;
    int addr_width=0;
    int result;

    if(args < 5) {
        printf("%s [bus.number] [device.addr] [reg.addr] [addr.width]\n",argv[0]);
        printf("example: %s 0x03 0x10 0x3000 2\n",argv[0]);
        return 0;
    }

    sscanf(argv[1], "%x", &bus_number);
    sscanf(argv[2], "%x", &dev_address);
    sscanf(argv[3], "%x", &reg_address);
    sscanf(argv[4], "%d", &addr_width);

    sprintf(name,"/dev/i2c-%d",bus_number);

    int fd = open(name, O_RDWR);
    if(fd <= 0) {
        printf("%s is not exsit",name);
        return 0;
    }

    result =ioctl(fd, I2C_SLAVE, dev_address & 0xff);  // 设置设备地址
    if(result < 0) {
        printf("%s failed to set dev_addr\n",name);
        return 0;
    }

    char reg_addr[16];
    char data[16]={0};
    if(addr_width == 1) {
        reg_addr[0] =reg_address & 0xff;
        result =write(fd, reg_addr, 1);
        if(result < 0) {
            printf("%s failed to write reg addr\n",name);
            return 0;
        }

        result=read(fd, data, 1);
        if(result < 0) {
            printf("%s failed to write reg addr\n",name);
            return 0;
        }
        printf("Read: 0x%02X\n", data[0]);
    }
    else {
        reg_addr[0] =(reg_address >>8) & 0xff;
        reg_addr[1] =(reg_address) & 0xff;
        result =write(fd, reg_addr, 2);
        if(result < 0) {
            printf("%s failed to write reg addr\n",name);
            return 0;
        }

        result=read(fd, data, 2);
        if(result < 0) {
            printf("%s failed to write reg addr\n",name);
            return 0;
        }
        printf("Read: 0x%02X%02X\n", data[0], data[1]);
    }
    
    close(fd);
    return 0;
}
