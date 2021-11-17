class Command:

    def set_context(self, context):
        self.ctx = context

    def with_context(self, context):
        self.set_context(context)
        return self

    def set_arguments(self, arguments):
        self.args = arguments

    def with_arguments(self, arguments):
        self.set_arguments(arguments)
        return self

    def execute(self):
        pass

    def prefixed(self, name):
        return f'{self._prefix}_{name}'