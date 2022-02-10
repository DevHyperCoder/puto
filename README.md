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

# LICENSE

`puto` is licensed under the GNU GPL 3.0
