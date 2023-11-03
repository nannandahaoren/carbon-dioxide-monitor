from lxml import etree




html = etree.HTML('tail.html')
parser = etree.HTMLParser(encoding = 'utf-8')
tree = etree.parse('tail.html',parser=parser)
