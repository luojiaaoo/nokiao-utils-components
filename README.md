# nokiao-utils-components

nokiao-utils-components 是一个 Dash 组件库，提供常用的工具组件用于 Dash 应用开发。

## 安装

```bash
pip install nokiao_utils_components
```

## 组件

### CalcHash

计算字符串的多种哈希值（MD5、SHA256、SHA384、SHA512）。

#### 输入属性

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `value` | string | 否 | 要计算哈希的输入字符串 |
| `withTimeSuffix` | boolean | 否 | 是否添加时间后缀（默认 `false`）。启用后会在输入值后追加当前时间戳，可用于验证时间有效性，防止重放攻击 |

#### 输出属性

| 属性 | 类型 | 说明 |
|------|------|------|
| `md5Value` | string | MD5 哈希值（32位十六进制） |
| `sha256Value` | string | SHA256 哈希值（64位十六进制） |
| `sha384Value` | string | SHA384 哈希值（96位十六进制） |
| `sha512Value` | string | SHA512 哈希值（128位十六进制） |

#### 使用示例

```bash
python usages\calc_hash.py
```