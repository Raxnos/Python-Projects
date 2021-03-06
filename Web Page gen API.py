

"""
This program is not the intended one. Will fix according to the intended.

1) Create a document 

2) head
3) body

functions;

-setting title
-setting lists (ol/ul)

"""

"""
<!DOCTYPE html>

<html>

<head>
</head>

<body>

</body>


</html>

"""

		
class Component:

	def __init__(self, tag_name):
		self.tag_name = tag_name
		
	def extract(self):
		pass
		
		
class Title(Component):

	def __init__(self, title_string):
		Component.__init__(self, "title")
		self.title_string = title_string

	def extract(self):
		return "<{}>{}</{}>".format(self.tag_name, 
									self.title_string,
									self.tag_name)
			
class List(Component):

	

	def __init__(self, setting="unordered"):
		list_type = {
			
			"ordered" : "ol",
			"unordered" : "ul"
		}
		self.items = []
		try:
			Component.__init__(self, list_type[setting])
		except KeyError:
			Component.__init__(self, list_type["unordered"])
	
	def add_item(self, item):
		self.items.append(Item(item))
		
	def extract(self):
		ret_string = ""
		for item in self.items:
			ret_string += "<{}>{}</{}>".format(self.tag_name,
							item.extract(),
							self.tag_name)
		return ret_string
			
class Item(Component):
		
	def __init__(self, item):
		Component.__init__(self, "li")
		self.item = item
			
	def extract(self):
		return "<{}>{}</{}>".format(self.tag_name,
									self.item,
									self.tag_name)
			
class Document:
	
	def __init__(self, doc_name="index"):
		self.doc_name = doc_name
		self.head = [] #must contain Component objects
		self.body = [] #must contain Component objects
		self.object_stack = []
		
	def add_to_head(self, element):
		self.head.append(element)
		
	def add_to_body(self, element):
		self.body.append(element)
		
	def link_docu(self):
		pass
	
	def create_document(self):
		with open(self.doc_name+".html","w") as doc_file:
			doc_file.write("<!DOCTYPE html>\n<html>\n")
			
			doc_file.write("<head>")
			for component in self.head:
				doc_file.write(component.extract())
			doc_file.write("</head>")
			doc_file.write("<body>")
			for component in self.body:
				doc_file.write(component.extract())
			doc_file.write("</body>")
			doc_file.write("</html>\n")
			
		
	
	
