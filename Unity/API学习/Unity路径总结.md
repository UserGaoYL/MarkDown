### 1、Application.temporaryCachePath

临时数据缓存目录

```C#
//  Windows:    C:/Users/xxx/AppData/Local/Temp/ProjectCompanyName/ProjectName
//  Android:    /storage/emulated/0/Android/data/com.test.path/cache
```

### 2、Application.persistentDataPath

持久化数据存储目录的路径，可以在此路径下存储一些持久化的数据文件

```C#
//  Windows:    C:/Users/Host-435/AppData/LocalLow/ProjectCompanyName/ProjectName 
//  Android:    /storage/emulated/0/Android/data/com.test.path/files 
```

### 3、Application.streamingAssetsPath

流数据的缓存目录

```C#
//  Windows:    ./ProjectName/Assets/StreamingAssets 
//  Android:    jar:file:///data/app/com.test.path-Kef7E5fdZvX_R9yfrSd1ZQ==/base.apk!/assets

//  windows相当于 Application.dataPath + "/StreamingAssets"
//  android相当于 "jar:file://" + Application.dataPath + "!/assets"
```

加载路径下资源，使用```UnityWebRequest```

```C#
IEnumerator LoadImage(string imgName)
{
    string url = Path.Combine(Application.streamingAssetsPath, imgName);
    UnityWebRequest req = UnityWebRequest.Get(url);

    yield return req.SendWebRequest();

    byte[] imgData;
    Texture2D texture = new Texture2D(2,2);
    imgData = req.downloadHandler.data; 
    texture.LoadImage(imgData);

    Vector2 pivot = new Vector2(0.5f, 0.5f);
    Sprite sprite = Sprite.Create(texture, new Rect(0.0f, 0.0f, texture.width, texture.height), pivot, 100.0f);

    Image img = GetComponent<Image>();
    img.sprite = sprite;
}
```

### 4、Application.dataPath

项目文件夹所在路径

```C#
//  Windows:     ./ProjectName/Assets 
//  Android:    /data/app/com.test.path-Kef7E5fdZvX_R9yfrSd1ZQ==/base.apk 
```