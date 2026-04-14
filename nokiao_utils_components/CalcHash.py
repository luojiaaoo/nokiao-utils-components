# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentSingleType = typing.Union[str, int, float, Component, None]
ComponentType = typing.Union[
    ComponentSingleType,
    typing.Sequence[ComponentSingleType],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class CalcHash(Component):
    """A CalcHash component.


Keyword arguments:

- id (string; optional):
    组件ID.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- md5Value (string; optional):
    MD5输出.

- sha256Value (string; optional):
    SHA256输出.

- sha384Value (string; optional):
    SHA384输出.

- sha512Value (string; optional):
    SHA512输出.

- value (string; optional):
    输入.

- withTimeSuffix (boolean; optional):
    是否添加时间后缀（对value+时间戳计算hash，用于验证时间有效性，防止重放攻击）."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'nokiao_utils_components'
    _type = 'CalcHash'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        value: typing.Optional[str] = None,
        withTimeSuffix: typing.Optional[bool] = None,
        md5Value: typing.Optional[str] = None,
        sha256Value: typing.Optional[str] = None,
        sha384Value: typing.Optional[str] = None,
        sha512Value: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'md5Value', 'sha256Value', 'sha384Value', 'sha512Value', 'value', 'withTimeSuffix']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'md5Value', 'sha256Value', 'sha384Value', 'sha512Value', 'value', 'withTimeSuffix']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(CalcHash, self).__init__(**args)

setattr(CalcHash, "__init__", _explicitize_args(CalcHash.__init__))
