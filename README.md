# bugvoyage

## WTF?

You know what is `hypothesis` python library is, right? Basically it generates whole lot of tests that can be used to fuzz your code for subtle bugs. So, this repo is my humble attempt to mine some CPython bugs by fuzzing.

## Installation
```bash
pip install -r requirements.txt
```
## Run
```python
py.test tests/ -n num_of_workers
```
Cross your fingers and wait for some fail.

## Current status
Current test set is rather minimalistic, dull and straight forward as hell. Need more corner case checks and more tests basically.
