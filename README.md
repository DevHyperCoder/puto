# PUTO: PDF to Booklet converter

Split given PDF document into 4 page groups and convert them to booklet format.
It creates a PDF like shown below:

```

First side (Odd pages): Page 4 and Page 1
    -------------------
    |        |        |
    | Page 4 | Page 1 |
    |        |        |
    -------------------
    
Second side (Even pages): Page 2 and Page 3
    -------------------
    |        |        |
    | Page 2 | Page 3 |
    |        |        |
    -------------------
```

Take the odd numbered page and put it back with the non printing side facing up
and the **lower number** page going into the printer. This probably does not
make sense, I will try to add a graphic when I get the time to do so

## Installation

```sh
git clone https://github.com/DevHyperCoder/puto.git
cd puto
pip install -r requirements.txt
```

> You may consider using a virtualenv  to contain your installation

## Usage

`python main.py <input file> <output file>`

## Dependencies

```
pdf2image==1.16.0
Pillow==9.0.1
```

Please check the README of [pdf2image](https://pypi.org/project/pdf2image/) to
install the necessary dependencies in your system. 

## LICENSE

`puto` is licensed under the GNU GPL 3.0
