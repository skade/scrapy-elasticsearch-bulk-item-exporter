Description
===========
scrapy-elasticsearch-bulk-item-exporter provides an exporter for Scrapy items that writes [Elasticsearch Bulk](http://www.elasticsearch.org/guide/reference/api/bulk/) format for easy further use with elasticsearch.

Install
=======
   pip install scrapy-elasticsearch-bulk-item-exporter

Usage
-----

   scrapy crawl <spider> -o my.bulk -t elasticsearchbulk

Elasticsearch has an upper limit of bulk document size. 100mb is standard, it can be pushed up to 2GB (not advisable). This splitting can be done using `split(1)`:

   scrapy crawl <spider> -o - -t elasticsearchbulk

Configure settings.py:
----------------------
   FEED_EXPORTERS = {
       'elasticsearchbulk': 'scrapyelasticsearch.ElasticSearchBulkItemExporter'
   }

Changelog
=========
0.1: Initial release

Credit
======

Thanks to [Julien Duponchelle](https://github.com/noplay/), I used his [scrapy-elasticsearch](https://github.com/noplay/scrapy-elasticsearch) for inspriration.

License
=======

Scrapys License: BSD. See LICENSE for details.
