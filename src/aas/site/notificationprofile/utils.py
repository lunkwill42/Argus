class AttrGetter:
    def __init__(self, attr_name: str):
        self.attr_name = attr_name

    def __call__(self, obj):
        return getattr(obj, self.attr_name)

    @property
    def query(self):
        return self.attr_name


class NestedAttrGetter(AttrGetter):
    def __init__(self, attr_name: str):
        super().__init__(attr_name)
        self._attr_names = attr_name.split(".")
        self._attr_query = "__".join(self._attr_names)

    def __call__(self, obj):
        obj_attr = obj
        for attr_name in self._attr_names:
            obj_attr = getattr(obj_attr, attr_name)
        return obj_attr

    @property
    def query(self):
        return self._attr_query
