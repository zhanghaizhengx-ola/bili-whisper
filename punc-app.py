
from punc import PunctuationExecutor


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--text",
        default = None,
        type = str,
    )
    parser.add_argument(
        "--infer_model_path",
        default = 'pun_models',
        type = str,
    )
    args = parser.parse_args()

    pun_executor = PunctuationExecutor(model_dir=args.infer_model_path, use_gpu=False)
    result = pun_executor(args.text)
    print(result)
