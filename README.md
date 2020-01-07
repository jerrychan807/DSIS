# DSIS

Document Sensitive Information Scanner

文件里的敏感信息扫描器

---

# 介绍:

扫描一个目录下的所有文件,看文件内是否含有敏感信息。


目前我是用来,检查客户端程序存储在手机中的SharedPreferences配置文件夹(里面文件一般是xml),看是否包含敏感信息

> 在网上找了一下,好像没找到合适的工具,又懒得一个个文件看,就自己随便写了个简单的工具
> 
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

![](https://github.com/jerrychan807/DSIS/blob/master/img/use_result.png)


---

# Todo:

- 支持更多文件后缀
- 规则增强 

---

# refs:

规则参考:

- https://github.com/repoog/GitPrey/blob/master/pattern/info.db
- https://github.com/kootenpv/gittyleaks/blob/e6eba9cb5d8a1cb0ddef1f95c359e0cd47fd90d0/gittyleaks/gittyleaks.py#L96
