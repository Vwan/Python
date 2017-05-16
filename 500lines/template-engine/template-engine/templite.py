class Templite(Object):
	def __init__(self,text,*contexts):
		self.context={}
		for context in contexts:
			self.context.update(context)
		self.all_vars=set()
		self.loop_vars=set()

		code = CodeBuilder()
		code.add_line("def render_function(context,do_dots)")
		code.indent()
		vars_code = code.add_section()
		code.add_line("result=[]")
		code.add_line("append_result = result.append")
		code.add_line("extend_result = result.extend")
		code.add_line("to_str = str")
