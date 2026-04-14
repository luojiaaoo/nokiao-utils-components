% Auto-generated: do not edit by hand
\name{'nuc'CalcHash}

\alias{'nuc'CalcHash}

\title{CalcHash component}

\description{

}

\usage{
'nuc'CalcHash(id=NULL, key=NULL, md5Value=NULL, sha256Value=NULL,
sha384Value=NULL, sha512Value=NULL, value=NULL,
withTimeSuffix=NULL)
}

\arguments{
\item{id}{Character. 组件ID}

\item{key}{Character. 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果}

\item{md5Value}{Character. MD5输出}

\item{sha256Value}{Character. SHA256输出}

\item{sha384Value}{Character. SHA384输出}

\item{sha512Value}{Character. SHA512输出}

\item{value}{Character. 输入}

\item{withTimeSuffix}{Logical. 是否添加时间后缀（对value+时间戳计算hash，用于验证时间有效性，防止重放攻击）}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

