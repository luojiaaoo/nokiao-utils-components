import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import { md5 } from '@noble/hashes/legacy.js';
import { sha256, sha384, sha512 } from '@noble/hashes/sha2.js';
import { bytesToHex } from '@noble/hashes/utils.js';

const CalcHash = (props) => {
    const {
        value,
        withTimeSuffix = false,
        setProps,
    } = props;

    useEffect(() => {
        if (value == null || value.length === 0) {
            setProps({ md5Value: null, sha256Value: null, sha384Value: null, sha512Value: null });
            return;
        }

        const timeSuffix = withTimeSuffix ? Date.now().toString() : '';
        const valueWithTime = value + timeSuffix;
        const showTimeSuffix = withTimeSuffix ? `:${timeSuffix}` : '';
        const data = new TextEncoder().encode(valueWithTime);

        const md5Hash = md5.create();
        md5Hash.update(data);
        const md5Value = bytesToHex(md5Hash.digest());
        setProps({ md5Value: `${md5Value}${showTimeSuffix}` });

        const sha256Hash = sha256.create();
        sha256Hash.update(data);
        const sha256Value = bytesToHex(sha256Hash.digest());
        setProps({ sha256Value: `${sha256Value}${showTimeSuffix}` });

        const sha384Hash = sha384.create();
        sha384Hash.update(data);
        const sha384Value = bytesToHex(sha384Hash.digest());
        setProps({ sha384Value: `${sha384Value}${showTimeSuffix}` });

        const sha512Hash = sha512.create();
        sha512Hash.update(data);
        const sha512Value = bytesToHex(sha512Hash.digest());
        setProps({ sha512Value: `${sha512Value}${showTimeSuffix}` });

    }, [value, withTimeSuffix]);

    return <></>;
}

CalcHash.propTypes = {
    /**
     * 组件ID
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 输入
     */
    value: PropTypes.string,

    /**
     * 是否添加时间后缀（对value+时间戳计算hash，用于验证时间有效性，防止重放攻击）
     */
    withTimeSuffix: PropTypes.bool,

    /**
     * MD5输出
     */
    md5Value: PropTypes.string,

    /**
     * SHA256输出
     */
    sha256Value: PropTypes.string,

    /**
     * SHA384输出
     */
    sha384Value: PropTypes.string,

    /**
     * SHA512输出
     */
    sha512Value: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default CalcHash;
