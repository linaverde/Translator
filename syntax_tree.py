from anytree import NodeMixin, RenderTree

class MyNodeClass(NodeMixin):  # Add Node feature

    def __init__(self, term, deep, pi_stack_number, right_number, parent=None, children=None):
        super(MyNodeClass, self).__init__()
        self.term = term

        self.deep = deep
        self.pi_stack_number = pi_stack_number
        self.right_number = right_number
        self.parent = parent
        if children:
            self.children = children



