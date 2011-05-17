def ordered_list(src, *args):
    if args:
        src = list([src]) + list(args)
    if isinstance(src, OrderedList):
        return src
    return OrderedList(src)


def ordered_item(src, before=None, after=None):
    if isinstance(src, OrderedListItem):
        src.update(None, before, after)
        return src
    return OrderedListItem(src, before, after)


def merge_lists(list1, list2):
    list1 = map(ordered_item, list1)
    list2 = map(ordered_item, list2)
    result = list1 + list2
    for item1 in result:
        id1 = item1.get_content()
        for item2 in result:
            id2 = item2.get_content()
            if id1 in item2.after:
                item1.before |= set([id2])
            if id1 in item2.before:
                item1.after |= set([id2])
        # We may indicate conflict somehow or throw an error
        # conflict = item1.before & item1.after
        # if conflict:
        #     raise Exception("Can't resolve list items order.")
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
