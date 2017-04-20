from setuptools import setup, find_packages
print (find_packages())

setup(
    name         = 'ideoneSearcher',
    version      = '1.0',
    packages     = find_packages(),
#    package_data = {'ideone': ['scrapy.cfg', 'settings.conf']},
    data_files   = [('config', ['ideone/scrapy.cfg', 'ideone/settings.conf'])],
    entry_points = {'scrapy': ['settings = IdeoneSearcher.settings']},
    scripts      = ['ideone/scrone']
)
