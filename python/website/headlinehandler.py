from xml.sax.handler import ContentHandler
from xml.sax import parse

class HeadlineHandler(ContentHandler):

	in_headlines = False

	def __init__(self, headlines):
		ContentHandler.__init__(self)
		self.headlines = headlines
		self.data = []

	def startElement(self, name, attrs):
		if name == 'h1':
			self.in_headlines = True

	def endElement(self, name):
		if name == 'h1':
			text = ''.join(self.data)
			self.data = []
			self.headlines.append(text)
			self.in_headlines = False

	def characters(self, string):
		if self.in_headlines:
			self.data.append(string)
			
headlines = []
parse('website.xml', HeadlineHandler(headlines))

print 'The following <h1> elements were found:'
for h in headlines:
	print h