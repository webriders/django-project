def ol(src, *args):
    if args:
        src = list([src]) + list(args)
    if isinstance(src, OrderedList):
        return src
    return OrderedList(src)


def li(src, before=None, after=None):
    if isinstance(src, OrderedListItem):
        src.update(None, before, after)
        return src
    return OrderedListItem(src, before, after)


def merge(l1, l2):
    l1 = map(li, l1)
    l2 = map(li, l2)
    result = l1 + l2
    for i1 in result:
        s1 = i1.get_content()
        for i2 in result:
            s2 = i2.get_content()
            if s1 in i2.after:
                i1.before |= set([s2])
            if s1 in i2.before:
                i1.after |= set([s2])
        conflict = i1.before & i1.after
        if conflict:
            pass # we may indicate conflict somehow or throw an error
    result.sort()
    return result


class OrderedList(list):
    pass


class OrderedListItem(object):
    content = None
    before = None
    after = None

    def __init__(self, content, before=None, after=None):
        super(OrderedListItem, self).__init__()
        self.before = set()
        self.after = set()
        self.update(content, before, after)

    def update(self, content=None, before=None, after=None):
        if content:
            self.content = content
        if before:
            if isinstance(before, basestring):
                before = [before]
            self.before = set(before)
        if after:
            if isinstance(after, basestring):
                after = [after]
            self.after = set(after)

    def get_content(self):
        return self.content

    def __repr__(self):
        return self.get_content()

    def __cmp__(self, item):
        if isinstance(item, OrderedListItem):
            item = item.get_content()
        if set([item, '*']) & self.before:
            return -1
        elif set([item, '*']) & self.after:
            return 1
        else:
            return 0
