
##  废弃API

```C#
//  同步加载AssetBundle
//  使用新API AssetBundle.LoadFromFile()
public static AssetBundle CreateFromFile(string path){}

//  从字节数组同步加载
//  使用新API LoadFromMemory
public static AssetBundle CreateFromMemoryImmediate(byte[] binary){}

//  从字节数组异步加载
//  使用新API AssetBundle.LoadFromMemoryAsync()
public static AssetBundleCreateRequest CreateFromMemory(byte[] binary)(){}
```

## 一、AssetBundle静态方法


### 从本地加载AssetBundle
- 同步加载 ```public static AssetBundle LoadFromFile(string path, uint crc, ulong offset){}```
- 异步加载```public static AssetBundleCreateRequest LoadFromFileAsync(string path, uint crc, ulong offset){}```

```C#
//  path            ab包本地路径
//  crc(默认0)      未压缩内容的可选 CRC-32 校验和。如果它不为零，则内容将在加载之前与校验和进行比较，如果不匹配则给出错误。
//  offset(默认0)   字节偏移量，可以指定从何处开始读取AssetBundle
```

使用举例：  
```C#
//  同步加载
public void LoadAB(string abName)
{
    string path = Path.Combine(Application.streamingAssetsPath, abName);
    AssetBundle ab = AssetBundle.LoadFromFile(path);
    GameObject obj = ab.LoadAsset<GameObject>("Cube");
    GameObject.Instantiate(obj);
}


//  异步加载
public IEnumerator AsyncLoadAB(string abName)
{
    yield return new WaitForEndOfFrame();

    string path = Path.Combine(Application.streamingAssetsPath, abName);

    AssetBundleCreateRequest abcReq = AssetBundle.LoadFormFileAsync(path);

    yield return abcReq;

    AssetBundle ab = abcReq.assetBundle;

    AssetBundleRequest abReq = ab.LoadAssetAsync<GameObject>("Cube");

    yield return abReq;

    GameObject obj = abReq.asset as GameObject;
    GameObject.Instantiate(obj);
}
```

### 从字节数组加载(占内存，慎用)
- 同步加载 ```public static AssetBundle LoadFromMemory(byte[] binary, uint crc, ulong offset){}```
- 异步加载```public static AssetBundleCreateRequest LoadFromMemoryAsync(byte[] binary, uint crc, ulong offset){}```

注意：      
```AssetBundle.LoadFromMemory```基本上是无法在手机上用的，因为要多占一份内存，所以大多Unity项目都不进行资源加密。  
可以使用Unity新添加的API ```LoadFromStream```，可以在构建AB包时加密，Read时解密

### 从Stream加载
- 同步加载```public static AssetBundle LoadFromStream(System.IO.Stream stream, uint crc, uint managedReadBufferSize)```
- 异步加载```public static AssetBundleCreateRequest LoadFromSteamAsync(System.IO.Stream, uint crc, uint managedReadBufferSize)```
  
使用举例：  
```C#

public void LoadFromStream(string abName)
{
    string path = Path.Combine(Application.streamingAssetsPath, abName);
    using(FileStream file = new FileStream(path, FileMode.Open, FileAccess.Read))
    {
        AssetBundle ab = AssetBundle.LoadFromStream(file);
        GameObject obj = ab.LoadAsset<GameObject>("Cube");
        GameObject.Instantiate(obj);
    }

}

```

### 卸载所有AssetBundle

```public static void UnloadAllAssetBundles(bool unloadAllObjects)```
```C#
//  unloadAllObjects 是否卸载所有加载的资源，如果为true，会卸载包括正在使用的资源
```

### 获取已加载的AssetBundle

```public static IEnumerable AssetBundle.GetAllLoadedAssetBundles()```

### 压缩 AssetBundle(Unity 2018.3新增API)
```public static AssetBundleRecompressOperation RecompressAssetBundleAsync(string inputPath, string outputPath, BuildCompression method, uint expectedCRC = 0, ThreadPriority priority = ThreadPriority.Low) ```

可以把资源包重新压缩为Uncompression或LZ4格式，这下资源包的格式完全变得可控了，可以应用更多策略处理资源包。

```C#
//  inputPath   要再压缩的AssetBundle路径
//  outpath     要生成并再压缩的AssetBundle路径，可能与inputPath相同
//  method      压缩方法、级别和块大小
//  expectedCRC 作为测试依据的AssetBundle CRC
//  priority    执行压缩的线程优先级
```


## 二、AssetBundle实例方法

### 加载方法

- 同步
```
public Object LoadAsset(string name){}
public Object LoadAsset(string name, Type type){}
public T LoadAsset<T>(string name){}

public Object[] LoadAllAssets(){}
public Object[] LoadAllAssets(Type type){}
public T[] LoadAllAssets<T>(){}
```
- 异步
```
public AssetBundleRequest LoadAssetAsync(string name){}
public AssetBundleRequest LoadAssetAsync(string name, Type type){}
public AssetBundleRequest LoadAssetAsync<T>(string name){}

public AssetBundleRequest LoadAllAssetsAsync(){}
public AssetBundleRequest LoadAllAssetsAsync(Type type){}
public AssetBundleRequest LoadAllAssetsAsync<T>(){}
```

### 卸载方法

```public void Unload(bool unloadAllLoadedObjects)```

### 其他

```C#
//  检测AB包中是否包含某个object
public bool Contains(string name){}
//  获取AB包中所有资产名字(assets/resources/xxx.prefab、assets/resources/yyy.png)
public string[] GetAllAssetNames(){}

public string[] GetAllScenePaths(){}
```