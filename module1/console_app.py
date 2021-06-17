import argparse


def init_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('message', type=str, help='Message to print')
    parser.add_argument('-r', '--repeats', type=int,
                        default=3, help='Number of print times')
    return parser


def print_times(message, repeats):
    for i in range(repeats):
        print(f'{i+1}: {message}')


# Plik może zostać zaimportowany do innego, ale jeśli zostanie uruchomiony z konsoli, to wywoła instrukcje poniżej
if __name__ == '__main__':
    parser = init_parser()
    args = parser.parse_args()
    print_times(args.message, args.repeats)
