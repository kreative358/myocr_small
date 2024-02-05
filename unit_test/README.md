# Unit Test

##Description
This module contains unit test for myocr_small.

## Usage
This module can be used as a typical python module. One python wrapper script and on ipython notebook are provided.

### Python script (*recommneded*)
The script can be called with (assuming calling from `myocr_small/`);
```
python ./unit_test/run_unit_test.py --myocr_small ./myocr_small --verbose 2 --test ./unit_test/myocr_smallUnitTestPackage.pickle --data_dir ./examples 
```

#### Script arguments
 * myocr_small: [Required] myocr_small package to test. This should point to a directory where `__init__.py` of myocr_small is located.
 * verbose (-v): [Optional] Verbosity level to report test results (The default is 0)
    * 0: Report only the final result
    * 1: Same as 0 and also results of each tested module.
    * 2: Same as 1 and also results of each test of each module.
    * 3: Same as 2 and also the calculated and the expected outputs of each test.
    * 4 or higher: Same as 3 and also the inputs of each test. (This will produce a lot of text on console).
 * test_data (-t): [Optional] Path to test package to use (The default is `./unit_test/data/myocr_smallUnitTestPackage.pickle`).
 * data_dir (-d): [Optional] Path to myocr_small example images directory. (The default is `./examples/`
 
### Ipython notebook
Please see `demo.ipynb` for documentation.