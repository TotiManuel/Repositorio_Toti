ifconfig | grep "inet" >> IP.txt
echo ------------------------------------- >> IP.txt
ifconfig >> IP.txt
echo ------------------------------------- >> IP.txt
nmap 10.20.83.214 >> IP.txt
echo ------------------------------------- >> IP.txt
nmap -vv www.totimanuel.com.ar >> IP.txt // muestra los puertos disponibles en esa direccion
