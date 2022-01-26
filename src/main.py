
import argparse
from xml.dom import minidom

        
     
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", help="specify the train path")
    parser.add_argument("--test", help="specify the test path")
    parser.add_argument("--output", help="specify the output path")
    args = parser.parse_args()

    # print(args.train, args.output)

    # dev_set = xml.dom.minidom.parse(args.train)
    dev_set = minidom.parse(args.train)

    sent = dev_set.getElementsByTagName('sentence')

    print(sent)
    
    # print(dev_set.nodeName, dev_set.firstChild.tagName)
    # with open(args.train,'r') as file:
    #     data = file.read()

    #     print(data)


if __name__ == "__main__":
    main()

