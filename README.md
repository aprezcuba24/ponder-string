# ponder-string
This project is only for testing. It has two parts, the client side and the server side.

## Server

To run the server you need to run the following command.

```
python server/main.py
```

To see the `help` you can use this command.

```
python server/main.py
```

The output is

```
usage: main.py [-h] [--verbose | --no-verbose]

options:
  -h, --help               show this help message and exit
  --verbose, --no-verbose  Show more logs. (default: False)
```

## Client

To run the client you need to use the following command.

```
python client/main.py
```

To see the `help` you can use this command.

```
python client/main.py
```

The output is

```
usage: main.py [-h] [-n NUMBER] [-f FILENAME] [-r FILENAME_RESPOND] [--verbose | --no-verbose]

options:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        Numbers of strings.
  -f FILENAME, --file FILENAME
                        Name of the file.
  -r FILENAME_RESPOND, --file-respond FILENAME_RESPOND
                        Name of the file.
  --verbose, --no-verbose
                        Show more logs. (default: False)
```
