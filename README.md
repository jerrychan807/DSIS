# DSIS

Document sensitive information scanner

文件里的敏感信息扫描器

---

# 介绍:

检查客户端程序存储在手机中的SharedPreferences配置文件
对目录下的文件内容(一般是xml)进行检查,看是否包含敏感文件

> 在网上找了一下,好像没找到合适的工具,就自己随便写了个简单的工具
> 后面可能会拓展到别的文件后缀,到时候遇到再说

---

# 使用方法:

```
# 安装依赖模块
pip3 install -r requirements.txt

# Run
python3 dsid.py <your-folder-path>
```

# 效果:



---

# refs:

规则参考:

https://github.com/repoog/GitPrey/blob/master/pattern/info.db
