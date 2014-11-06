import ckanext.mapsearch.model.ogc as mapSearchModel
import ConfigParser
import os
import uuid

class TestMapSearchModel(object):

    #setup_class executes (auto once) before anything in this class
    @classmethod
    def setup_class(self):
        print ("")
        # get config options
        config = ConfigParser.RawConfigParser({
            'ckan_web_map_service_url': '',
        })
        config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'tests_config.cfg'))

        self.serviceUrl = config.get('tests', 'ckan_web_map_service_url')
        self.oHandleWMS = mapSearchModel.HandleWMS(self.serviceUrl)

        if not self.serviceUrl:
            raise Exception('You must provide WebMapServer URL to the tests '
                            ' configuration file')

    #teardown_class executes (auto once) after anything in this class
    @classmethod
    def teardown_class(self):
        print ("")
        self.oHandleWMS = None
        self.serviceUrl = None
        del self.oHandleWMS
        del self.serviceUrl

    #setup executes before each method in this class
    def setup(self):
        print ("")
        print ("TestUM:setup() before each test method")

    #setup executes after each method in this class
    def teardown(self):
        print ("")
        print ("TestUM:teardown() after each test method")

    #test map_search model get_layer_info method's response (data)
    def test_GetLayerInfo(self):
        print 'test_GetLayerInfo(): Running actual test code ..........................'

	def is_array(var):
	    return isinstance(var, (list, tuple))

        params = {"id":str(uuid.uuid4())}

        try:
	    result = self.oHandleWMS.get_layer_info(params)

            assert 'srs' in result
            assert 'layer' in result
            assert 'bbox' in result
            assert 'tile_format' in result

	    assert is_array(result['bbox'])
            assert isinstance(result['srs'], (unicode, str, basestring))
            assert isinstance(result['tile_format'], (unicode, str, basestring))
    	except:
    	    print "Data returned is not correct or one or more of important fields are missing"
    	    assert False
