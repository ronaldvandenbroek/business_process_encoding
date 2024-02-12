import os
import pprint

from pandas import DataFrame
from encode.utils import read_log, enc_selector
import argparse


def read_args():
    args = argparse.ArgumentParser()
    args.add_argument("--dataset", type=str, default="scenario1_1000_attribute_0.05.xes")
    args.add_argument("--encoding", type=str, default="onehot")
    args.add_argument("--vector_size", type=int, default=8)
    args.add_argument("--aggregation", type=str, default="average")
    args.add_argument("--embed_from", type=str, default="nodes")
    args.add_argument("--edge_operator", type=str, default="average")

    return args.parse_args()


def run(config):
    log = read_log(config["dataset"])

    encoder = enc_selector(config["encoding"])
    encoding = encoder(config, log)

    #print(encoding)

    save_encoding(config, encoding)


def save_encoding(config, encoding:DataFrame):
    results_folder = f'results/{config["encoding"]}/'
    os.makedirs(results_folder, exist_ok=True)
    
    file_name = config["dataset"].split('/')[-1][:-4]
    output_file_path = os.path.join(results_folder, f'{file_name}.csv')

    # If there are potentially more settings these can be added to the file name
    # output_file_path = os.path.join(results_folder, f'{config["encoding"]}_{file_name}.txt')

    encoding.to_csv(output_file_path, index=False)
    print(f'Encoding output saved to: {output_file_path}')


if __name__ == "__main__":
    config = read_args()
    config = vars(config)

    print("\n\nConfig:")
    pprint.pprint(config)

    print("Running...")
    run(config)
