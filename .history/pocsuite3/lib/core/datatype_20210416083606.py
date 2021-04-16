from collections import OrderedDict  # 有序字典


class AttribDict(OrderedDict):  # 扩展有序字典
    """
    AttrDict extends OrderedDict to provide attribute-style access. # 提供属性式访问
    Items starting with __ or _OrderedDict__ can't be accessed as attributes. # OrderedDict 不支持对对__开头或者_OrderedDict__开头的属性进行访问
    """
    __exclude_keys__ = set()

    def __getattr__(self, name):
        if (name.startswith('__') or name.startswith('_OrderedDict__')
                or name in self.__exclude_keys__):
            return super(AttribDict, self).__getattribute__(name)
        else:
            try:
                return self[name]
            except KeyError:
                raise AttributeError(name)

    def __setattr__(self, name, value):
        if (name.startswith('__') or name.startswith('_OrderedDict__')
                or name in self.__exclude_keys__):
            return super(AttribDict, self).__setattr__(name, value)
        self[name] = value

    def __delattr__(self, name):
        if (name.startswith('__') or name.startswith('_OrderedDict__')
                or name in self.__exclude_keys__):
            return super(AttribDict, self).__delattr__(name)
        del self[name]
