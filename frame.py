"""A frame is a rectangular part of the image where Elements
can be placed with given horizontal (left, center, right) and
vertical (top, middle, bottom) alignment.
"""
from elements import Element


class Stack(Element):
    """A Stack is a vertical stack of elements.
    sharing the same horizontal space (width),
    where each can have its own horizontal alignment.

    Elements are stacked with a spacing corresponding to
    their vmargin property. This vertical margin is one-sided:
    it is the margin between the property's element and the
    previous element in the stack.
    (E.g. In the case of a top-valigned stack, this is the
    margin between the 
    """
    def __init__(self, width=None, elements=[]):
        assert isinstance(width, int)
        self.width = width
        if elements:
            valignments = set([e.valign for e in elements])
            # cannot stack together elements with different valignment
            assert len(valignments) == 1
        self._stack = elements

    def __len__(self):
        return len(self._stack)

    def __getitem__(self, i):
        return self._stack[i]


class Frame(Element):
    """A frame is a collection of 3 stacks: top, middle, and bottom.
    """
    def __init__(self, width=None, height=None, elements=[]):
        assert all([isinstance(e, Element) for e in elements])
        self.top = Stack(width=width,
                         elements=[e for e in elements
                                   if e.valign == 'top'])
        self.bottom = Stack(width=width,
                            elements=[e for e in elements
                                      if e.valign == 'bottom'])
        self.middle = Stack(width=width,
                            elements=[e for e in elements
                                      if e.valign == 'middle'])
