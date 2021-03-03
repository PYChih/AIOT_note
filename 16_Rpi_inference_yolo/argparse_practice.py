import os
import argparse
import imghdr
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-name", type=str)
    parser.add_argument("-ID", type=str)
    args = parser.parse_args()
    input_id = args.ID
    name = args.name
    print("ID: {}, name : {}".format(input_id, name))
