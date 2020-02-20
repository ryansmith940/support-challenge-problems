# Problem 1

main.py is not working.  Here is the error:

```bash
$ python3 main.py
Updating table
Traceback (most recent call last):
  File "main.py", line 287, in <module>
    main()
  File "main.py", line 7, in main
    update_table()
  File "main.py", line 268, in update_table
    updated_firstname = row[1].capitalize()
AttributeError: 'NoneType' object has no attribute 'capitalize'
```

## Questions

1) What is the program doing?
1) Why is it not working?
1) What is a possible solution?
1) Are there any other posible solutions?
