"""An Itemexporter for scrapy that writes elasticsearch bulk format"""

from scrapy.contrib.exporter import BaseItemExporter
from scrapy.contrib.exporter import JsonLinesItemExporter

class ElasticSearchBulkItemExporter(JsonLinesItemExporter):
    def export_item(self, item):
    	requestdict = { "index": { "type": item.__class__.__name__ } }
    	self.file.write(self.encoder.encode(requestdict) + '\n')
    	super(ElasticSearchBulkItemExporter, self).export_item(item)
