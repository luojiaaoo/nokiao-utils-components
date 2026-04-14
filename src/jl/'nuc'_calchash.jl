# AUTO GENERATED FILE - DO NOT EDIT

export 'nuc'_calchash

"""
    'nuc'_calchash(;kwargs...)

A CalcHash component.

Keyword arguments:
- `id` (String; optional): 组件ID
- `key` (String; optional): 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
- `md5Value` (String; optional): MD5输出
- `sha256Value` (String; optional): SHA256输出
- `sha384Value` (String; optional): SHA384输出
- `sha512Value` (String; optional): SHA512输出
- `value` (String; optional): 输入
- `withTimeSuffix` (Bool; optional): 是否添加时间后缀（对value+时间戳计算hash，用于验证时间有效性，防止重放攻击）
"""
function 'nuc'_calchash(; kwargs...)
        available_props = Symbol[:id, :key, :md5Value, :sha256Value, :sha384Value, :sha512Value, :value, :withTimeSuffix]
        wild_props = Symbol[]
        return Component("'nuc'_calchash", "CalcHash", "nokiao_utils_components", available_props, wild_props; kwargs...)
end

