#from base_case import base_case
import base_case

class case_existing_file(base_case.base_case):
    '''File exists.'''

    def test(self, handler):
        return os.path.isfile(handler.full_path)

    def act(self, handler):
        self.handle_file(handler, handler.full_path)

class case_no_file(base_case.base_case):
	def test(self,handler):
		return not os.path.exists(handler.full_path)
	def act(self,handler):
		raise ServerException("'{0}' not found".format(handler.full_path))


class case_always_fail(base_case.base_case):
	def test(self,handler):
		return True
	def act(self,handler):
		raise ServerException("'{0}' unknown object".format(handler.path))

class case_directory_index_file(base_case.base_case):
	def index_path(self,handler):
		return os.path.join(handler.full_path,'index.html')
	def test(self,handler):
		return os.path.isdir(handler.full_path) and \
		os.path.isfile(self.index_path(handler))
	def act(self,handler):
		handler.handle_file(self.index_path(handler))

class case_directory_no_index_file(base_case.base_case):
    '''Serve listing for a directory without an index.html page.'''

    def index_path(self, handler):
        return os.path.join(handler.full_path, 'index.html')

    def test(self, handler):
        return os.path.isdir(handler.full_path) and \
               not os.path.isfile(self.index_path(handler))

    def act(self, handler):
        handler.list_dir(handler.full_path)

class case_cgi_file(base_case.base_case):
	def test(self,handler):
		return os.path.isfile(handler.full_path) and \
		handler.full_path.endwith(".py")

	def act(self,handler):
		handler.run_cgi(handler.full_path)
