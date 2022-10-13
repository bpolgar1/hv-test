# HV-test

## Assignment

Write code that will perform the following when executed on node 3

1. Retrieve a list of file objects in `/mnt/share1/test` on node 1 and node2 in parallel.
2. Return success if contents match; error if there is a mismatch.

Bonus points:

- Include validation of file metadata
- Include data integrity check of files

## Run script

- Run the following command:

    `python main.py --host_1 "n1" --path_1 "/mnt/share1/test" --host_2 "n2" --path_2 "/mnt/share1/test"`

## Run tests

1. Install dev dependencies:

    `pip install -r requirements-dev.txt`

2. Run tests:

    `pytest`
