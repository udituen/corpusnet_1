
from lxml import etree 
from xml.sax.saxutils import escape



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