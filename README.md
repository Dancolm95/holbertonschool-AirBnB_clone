
# AirBnB Clone

This project is the first part of a total of four that comprises the entirety to clone Airbnb. In this first part, we create the console to initialize it.


## Console    :computer:
The console is a command line interpreter that permits management of the backend of HolbertonBnB. It can be used to handle and manipulate all classes utilized by the application.


### Using the console
The HolbertonBnB console can be run both interactively and non-interactively. To run the console in non-interactive mode, pipe any command(s) into an execution of the file console.py at the command line.


```
 echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 

```
To use console in interactive mode, run the file ```console.py``` by itself:
```
./console.py
```
while the console running in interactive mode display a prompt for input:
```
./console.py
(hbnb) 
```
To quit the console enter the comand ```quit``` or input an EOF (End Of File)signal ```ctrl+D```

```
./console.py
(hbnb) quit
```

```
./console.py
(hbnb) EOF
```

## Testing :straight_ruler:
Unittest for the AirBnB Cloe nproject are defined in the ```test``` folder. To run the entire test suite simultaneously, execute the following comand:
```
python3 unittest -m discover tests
```
## Authors

- [@Dancolm95](https://github.com/Dancolm95)

