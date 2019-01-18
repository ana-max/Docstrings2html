import argparse
import shutil
from contextlib import suppress
from parser_filenames import Parser
from building_html.html_builder import Builder


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('names_of_files', nargs='+',
                        help='Enter the files names'
                             'or directories names '
                             'what you want to '
                             'get all docstrings')
    return parser.parse_args()


def main():
    args = parse_arguments()
    parser = Parser(args.names_of_files)
    with suppress(FileNotFoundError):
        shutil.rmtree('documentation')
    structure = parser.get_directories_structure()
    builder = Builder(structure)
    builder.build_html()


if __name__ == '__main__':
    main()
