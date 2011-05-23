def list_fragment(src, *args, **kwargs):
    '''
    Just a list fragment.

    Use it if you want to merge this fragment with another list in future.
    Also use ordered_item() to bring some order (you may mix them with regular items).

    Usage:
        list_fragment([1, 2, 3]) -> [1, 2, 3]
        list_fragment(1, 2, 3) -> [1, 2, 3]
        list_fragment([1]) -> [1]
        list_fragment(1) -> [1]

    Set keyword parameter "keep_order" to True (or equal) if you want to save items order while reordering
    (it's True by default so you may disable it).

    Example 1:
        l1 = list_fragment('a', 'b', ordered_item('c', after='d'), keep_order=False)
        l2 = ['d']
        merge_lists(l1, l2) # ['d', 'a', 'b', 'c'] - 'd' was inserted as early as possible

    Example 2:
        l1 = list_fragment('a', 'b', ordered_item('c', after='d'))
        l2 = ['d']
        merge_lists(l1, l2) # ['a', 'b', 'd', 'c'] - 'd' was inserted just before 'c', original order was counted
    '''
    if not isinstance(src, (list, tuple)):
        src = [src]
    else:
        src = list(src)

    if args:
        src += list(args)

    if isinstance(src, ListFragment):
        res = src
    else:
        res = ListFragment(src)

    if kwargs.get('keep_order', True):
        for i, item in enumerate(res):
            if not isinstance(item, OrderedItem):
                item = res[i] = OrderedItem(item)
            if i > 0:
                item.after.add(res[i-1].get_id())

    return res


def ordered_item(src, before=None, after=None):
    if isinstance(src, OrderedItem):
        src.update(None, before, after)
        return src
    return OrderedItem(src, before, after)


def merge_lists(list1, list2):
    list1 = map(ordered_item, list1)
    list2 = map(ordered_item, list2)
    result = list1 + list2

    # Sorting manually, because our relation isn't symmetric nor transitive
    # We should improve sorting method in future
    sorted = []
    while result:
        min = None
        min_pos = None
        for a in result:
            for i, b in enumerate(result):
                # item should take part in some relation and be the lowest one
                if (b < a or a > b) and (b < min or min > b or min is None):
                    min = b
                    min_pos = i
        if min_pos is None:
            sorted += result
            result = None
        else:
            sorted.append(result.pop(min_pos))
    return sorted


class ListFragment(list):
    pass


class OrderedItem(object):
    content = None
    before = None
    after = None

    def __init__(self, content, before=None, after=None):
        super(OrderedItem, self).__init__()
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

    def get_id(self):
        return self.content

    def __repr__(self):
        return self.get_id()

    def __cmp__(self, item):
        if isinstance(item, OrderedItem):
            item = item.get_id()
        if set([item, '*']) & self.before:
            return -1
        elif set([item, '*']) & self.after:
            return 1
        else:
            return 0
