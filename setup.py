from distutils.core import setup
setup(name='scrapy-elasticsearch-bulk-item-exporter',
      version='0.1',
      license='Apache License, Version 2.0',
      description='An extension of Scrapys JsonLinesItemExporter that exports to elasticsearch bulk format.',
      author='Florian Gilcher',
      author_email='florian.gilcher@asquera.de',
      url='http://github.com/asquera/scrapy-elasticsearch-bulk-item-exporter',
      keywords="scrapy elastic search",
      py_modules=['scrapyelasticsearch'],
      platforms = ['Any'],
      install_requires = ['scrapy'],
      classifiers = [ 'Development Status :: 4 - Beta',
                      'Environment :: No Input/Output (Daemon)',
                      'License :: OSI Approved :: BSD License',
                      'Operating System :: OS Independent',
                      'Programming Language :: Python']
)
