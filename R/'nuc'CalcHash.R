# AUTO GENERATED FILE - DO NOT EDIT

#' @export
'nuc'CalcHash <- function(id=NULL, key=NULL, md5Value=NULL, sha256Value=NULL, sha384Value=NULL, sha512Value=NULL, value=NULL, withTimeSuffix=NULL) {
    
    props <- list(id=id, key=key, md5Value=md5Value, sha256Value=sha256Value, sha384Value=sha384Value, sha512Value=sha512Value, value=value, withTimeSuffix=withTimeSuffix)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'CalcHash',
        namespace = 'nokiao_utils_components',
        propNames = c('id', 'key', 'md5Value', 'sha256Value', 'sha384Value', 'sha512Value', 'value', 'withTimeSuffix'),
        package = 'nokiaoUtilsComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
