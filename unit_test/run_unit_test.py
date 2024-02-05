
import argparse
from unit_test import UnitTest 

# %%
def main(args):

    unit_test = UnitTest(args.myocr_small, args.test_data, args.image_data_dir, args.verbose)
    unit_test.do_test(args.verbose)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to run myocr_small unit tet.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--myocr_small", help="Directory of myocr_small to test.")
    parser.add_argument("-t", "--test_data", default="./data/myocr_smallUnitTestPackage.pickle", help="Path to test data.")
    parser.add_argument("-d", "--image_data_dir", default="../examples", help="Path to directory that contains myocr_small example images.")
    parser.add_argument("-v", "--verbose", default=0, type = int, help="Verbosity level of report.")
    args = parser.parse_args()
    main(args)
