
#!/bin/bash
#定义了要读取文件的路径
c0=0
c1=0
c2=0
c3=0
c4=0
sen=0
sen1=0

while true              
  do


MY_FILE=/www/pages/a.txt  
asensor0=/sys/bus/iio/devices/iio:device0/in_voltage0_raw
asensor1=/sys/bus/iio/devices/iio:device0/in_voltage1_raw
asensor2=/sys/bus/iio/devices/iio:device0/in_voltage2_raw
asensor3=/sys/bus/iio/devices/iio:device0/in_voltage3_raw

#while read MY_LINE
#do
#输出读到的每一行的结果
#echo $MY_LINE
#done < $MY_FILE

MY_LINE=`cat $MY_FILE`
sensor0=`cat $asensor0`
sensor1=`cat $asensor1`
sensor2=`cat $asensor2`
sensor3=`cat $asensor3`
dsensor=`cat /sys/class/gpio/gpio39/value`
#echo $sensor0.$sensor1.$sensor2.$sensor3
#echo $MY_LINE


pid=`pgrep mp3blaster`
#echo $pid

if [ -n "$pid" ]; then

if [ $MY_LINE -ne 000 ]; then
kill -9 $pid
fi

if [ $MY_LINE  = stop ]; then
kill -9 $pid
fi

else
##########################################################
if  [ $sensor2 -lt  100 ]; then
if [ $c0 -eq 0 ]; then
mp3blaster /mp3/005.mp3 </dev/null> /dev/null 2>1&
sleep 5s
#echo "waring"
c0=1
fi
else
c0=0
fi

if  [ $sensor3 -gt  100 ]; then
if [ $c1 -eq 0 ]; then
kill -9 $pid
sleep 0.1s
mp3blaster /mp3/005.mp3 </dev/null> /dev/null 2>1&
sleep 5s
#echo "waring1"
c1=1
fi
else
c1=0
fi

if  [ $sensor0 -gt  1500 ]; then
if [ $c2 -eq 0 ]; then
echo 0 > /sys/class/gpio/gpio26/value
mp3blaster /mp3/005.mp3 </dev/null> /dev/null 2>1&
sleep 5s

#echo "waring2"
fi
c2=1
else
c2=0
echo 1 > /sys/class/gpio/gpio26/value
fi


#echo $sensor1
if  [ $sensor1 -gt  800 ]; then
if [ $c3 -eq 0 ]; then
#mp3blaster /mp3/005.mp3 </dev/null> /dev/null 2>1&
#sleep 5s
if [ $dsensor -eq 1 ]; then
#echo "waring3"
echo -n "0" > /sys/class/gpio/gpio24/value
sleep 0.8s
echo -n "1" > /sys/class/gpio/gpio24/value
echo -n "0" > /sys/class/gpio/gpio39/value

fi
c3=1
fi
else
c3=0
fi


if  [ $sensor1 -lt  700 ]; then
if [ $c4 -eq 0 ]; then
#mp3blaster /mp3/005.mp3 </dev/null> /dev/null 2>1&
#sleep 5s
if [ $dsensor -eq 0 ]; then
echo -n "0" > /sys/class/gpio/gpio27/value
sleep 0.8s
echo -n "1" > /sys/class/gpio/gpio27/value
echo -n "1" > /sys/class/gpio/gpio39/value
fi
c4=1
fi
else
c4=0
fi














###################################################
if [ $MY_LINE = 001 ]; then
#mp3blaster /mp3/001.mp3 </dev/null> /dev/null 2>1&
echo 000 > $MY_FILE 
elif [ $MY_LINE = 004 ]; then
#mp3blaster /mp3/004.mp3 </dev/null> /dev/null 2>1&
echo 000 > $MY_FILE 
fi

fi
sleep 0.5s
done


