'''''''''''
main file for carrying out task
--- convert xml to acceptable format in ism xml -- lexelt
--- add lemma and pos to semcor.senses file
--- edit train_one.bash script.. rewrite memory size
--- run the training process
to execute
python3 src/main.py --train data/train.csv --test data/test.csv --output output/test.csv
Reference code adopted from .... github account
'''''''''''
from lxml import etree 
from xml.sax.saxutils import escape
import argparse
# import xml.dom.minidom
from xml.dom import minidom

# create class for converting xml files to ims file

class Create_lexelt_:
    # define constructor
    def __init__(self, lemma, pos):
        self.item = lemma
        self.pos = pos
        self.instance = []
        self.old_instance = set()

    def exists(self, instance_id):
        return instance_id in self.old_instance
    
    def add_instance(self,this_instance):
        self.instance.append(this_instance)
        self.old_instance.add(this_instance.id)
        
    def __repr__(self):
        return self.item+' '+self.pos+' '+str(len(self.instance))
    
    def __iter__(self):
        for ins in self.instance:
            yield ins

    def create_xml_node(self):
        node = etree.Element('lexelt')
        node.set('item',self.item)
        node.set('pos',self.pos)
        for instance in self.instance:
            node.append(instance.create_xml_node())
        return node
    

class Create_instance:
    # initialize constructor
    def __init__(self):
        self.id = ''
        # self.docsrc = ''
        self.tokens = []
        self.index_head = []
        self.key = ''
   
    def create_xml_node(self):
        node = etree.Element('instance')
        node.set('id', self.id)
        # node.set('docsrc', self.docsrc)
        
        this_string = '<context>'
        start_head = min(self.index_head)
        end_head = max(self.index_head) + 1
        for num_token, token in enumerate(self.tokens):
            if num_token == start_head:
                this_string+=' <head>'+escape(token)
            elif num_token == end_head:
                this_string+='</head> '+escape(token)
            else:
                this_string+=' '+escape(token)
        this_string+='</context>'
        context_node = etree.fromstring(this_string)
        node.append(context_node)
        return node
        
     
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", help="specify the train path")
    # parser.add_argument("--test", help="specify the test path")
    parser.add_argument("--output", help="specify the output path")
    args = parser.parse_args()

    # print(args.train, args.output)

    # dev_set = xml.dom.minidom.parse(args.train)
    dev_set = minidom.parse(args.train)

    sent = dev_set.getElementsByTagName('sentence')

    print(sent[0].firstChild.data)
    
    # print(dev_set.nodeName, dev_set.firstChild.tagName)
    # with open(args.train,'r') as file:
    #     data = file.read()

    #     print(data)


if __name__ == "__main__":
    main()

