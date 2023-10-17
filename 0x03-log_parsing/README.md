# 0x03-log_parsing

Contains a module that reads `stdin` line by line and computes metrics.

Input format:
`<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`

After every 10 lines and/or a keyboard interruption `(CTRL + C)`, the following statistics are printed:

- Total file size: `File size: <total size>`,
where `<total size>` is the sum of all previous `<file size>`.
- Number of lines by status code:
  - possible status code: `200, 301, 400, 401, 403, 404, 405, 500`
  - if a status code doesn’t appear or is not an integer, it is not printed.
  - format: `<status code>: <number>`
  - status codes are printed in ascending order

The `generator.py` module is used to generate and print logs to the `stdout`
that match the input format above that can be used to test `0-stats.py`.

## Example

```Bash
kim@eternity:~/alx-interview/0x03-log_parsing$ ./generator.py | ./0-stats.py
File size: 4589
200: 3
301: 4
400: 1
401: 2
File size: 8536
200: 5
301: 7
400: 3
401: 2
403: 1
405: 1
500: 1
File size: 15001
200: 9
301: 8
400: 4
401: 2
403: 2
404: 1
405: 2
500: 2
^CFile size: 15602
200: 10
301: 8
400: 4
401: 2
403: 3
404: 1
405: 2
500: 2
Traceback (most recent call last):
  File "./generator.py", line 8, in <module>
    sleep(random.random())
KeyboardInterrupt
```

\
**_Happy coding 💻_**
