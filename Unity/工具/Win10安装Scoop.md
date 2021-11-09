
### 一、Scoop安装

1. 打开PowerShell，在 PowerShell 中输入下面内容，保证允许本地脚本的执行：

```set-executionpolicy remotesigned -scope currentuser```

选择"Y"

2. 然后执行下面的命令安装 Scoop：

```iex (new-object net.webclient).downloadstring('https://get.scoop.sh')```

3. 静待脚本执行完成，安装成功后，让我们尝试一下：

```scoop help```

### 二、Scoop使用

基础语法 ```scoop + 动作 + 对象```

常用的几个基础动作

|命令|说明|
|:-:|:-:|
|search|搜索软件名|
|install|安装软件|
|update|更新软件|
|status|查看软件状态|
|uninstall|卸载软件|
|info|查看软件详情|
|home|打开软件主页|



### 三、修改默认软件安装路径

```$env:SCOOP='D:\Scoop'```
#### 先添加用户级别的环境变量 SCOOP
```[environment]::setEnvironmentVariable('SCOOP',$env:SCOOP,'User')```

#### 下载安装

#### 然后下载安装 Scoop （如果使用默认安装路径则直接运行下面的命令）
```iex (new-object net.webclient).downloadstring('https://get.scoop.sh')```

#### 或者使用下面的命令安装：
```iwr -useb get.scoop.sh | iex```

```$env:SCOOP_GLOBAL='D:\GlobalScoopApps'```

```[environment]::setEnvironmentVariable('SCOOP_GLOBAL',$env:SCOOP_GLOBAL,'Machine')```

---

[详细使用参考](https://sspai.com/post/52496)  

[修改安装路径](https://www.thisfaner.com/p/scoop/)