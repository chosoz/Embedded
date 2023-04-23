$ make
$ aarch64-linux-gnu-gcc app.c
$ cp a.out led.ko /nfs/rootfs	
# setenv bootargs  root=/dev/nfs rw nfsroot=192.168.9.119:/nfs/rootfs,v3 console=ttyS0,115200 init=/linuxrc ip=192.168.9.9
# setenv nfsboot ext4load mmc 1:1 0x84000000 /boot/Image \; ext4load mmc 1:1 83100000 /boot/tegra210-p3448-0002-p3449-0000-b00.dtb \; booti 0x84000000 - 83100000
# run nfsboot //成功 可看到 read buf is  let's go ，即读出的数据和写入的一致