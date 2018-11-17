from django.apps import AppConfig
import h2o

class QuickstartConfig(AppConfig):
    name = 'quickstart'
    verbose_name = 'Quickstart'    
    def ready(self):
        print('ee')
        h2o.init(max_mem_size = "1g")