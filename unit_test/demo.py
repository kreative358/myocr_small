import os
from unit_test import UnitTest

# %% Set up paths 
myocr_small_module = "../myocr_small"
verbose = 2
test_data = "./data/myocr_smallUnitTestPackage.pickle"
image_data_dir = "../examples"

# %% Initialize UnitTest
unit_test = UnitTest(myocr_small_module, 
                     test_data,
                     image_data_dir
                     )
# %% Run UnitTest at verbosity level 2
unit_test.do_test(verbose = 2)