# <p align="center">Proxy Tester</p>

<p align="center">A simple Python program used for testing proxy servers to see if they are active. </p>

## <p align="center">Requirements</p>
<p align="center"> pip install arsenic </p>

# <p align="center">How to Use</p>

<p align="center"> In the program folder there are two txt files. Put your list of proxy servers in the one named "proxies.txt". When the program is ran, the proxies that are able to make a connection are written to "goodproxies.txt"

# <p align="center">Setup/Config</p>

 <p align="center">In ProxyTester.py, on line 11 you will find the variable max_concurrent = x (the default is 10). Change this number to how many concurrent driver instances you would like checking the proxies. Be warned, a high number will use a lot of RAM and CPU and potentially crash. Set to 30, it uses ~4GB RAM.