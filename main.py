import pprint
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

    # encoder = enc_selector(config["encoding"])
    encodings = [
        # "count2vec",
        # "onehot",
        # "alignment",
        # "logskeleton",
        # "tokenreplay",
        # "doc2vec",
        # "hash2vec",
        # "tfidf",
        # "word2vec",
        # "boostne",
        # "deepwalk",
        # "diff2vec",
        # "glee",
        # "grarep",
        # "hope",
        # "laplacianeigenmaps",
        "netmf",
        "nmfadmm",
        "node2vec",
        "nodesketch",
        "role2vec",
        "walklets",
    ]
    for encoding in encodings:
        encoder = enc_selector(encoding)
        res = encoder(config, log)
        res.to_csv(f"results/{encoding}.csv", index=False)


if __name__ == "__main__":
    config = read_args()
    config = vars(config)

    print("\n\nConfig:")
    pprint.pprint(config)

    print("Running...")
    run(config)
