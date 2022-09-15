import model
import yaml
from pprint import pprint


def main():
    print("Hello World!")


if __name__ == '__main__':
    with open("config.yml", 'r') as f:
        config = yaml.safe_load(f)
    pprint(config)
    main()
