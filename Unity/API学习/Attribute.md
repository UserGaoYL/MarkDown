## Unity常用属性介绍

### 一、AddComponentMenu

```C#
[AddComponentMenu("xxx/yyy")]
public class MyComponent:MonoBehaviour{

}
```

### 二、RequireComponent

```C#
public class MyBaseComponent:MonoBehaviour{

}

[RequireComponent(typeof(MyBaseComponent))]
public class MyComponent:MonoBehaviour{

}
```

### 三、ContextMenu、ContextMenuItem

```C#
public class MyComponent:MonoBehaviour{

    [ContextMenuItem("名字详细信息","MyNameMethod")]
    public string name;

    private void MyNameMethod(){
        Debug.Log("打印名字：" + name);
    }

    [ContextMenu("菜单选项执行方法")]
    private void MyContextMenuMethod(){

    }
}
```

### 四、HelpURL

```C#
[HelpURL("http://www.baidu.com")]
public class MyComponent:MonoBehaviour{

}
```

### 五、Header、ToolTip

```C#
public class MyComponent:MonoBehaviour{
    [Header("设置年龄")]
    public int age;

    [ToolTip("这是名字")]
    public string name;
}
```

### 六、Serializable、SerializeField、HideInInspector、NonSerialized

```C#
[Serializable]
public struct MyStruct
{
    public string name;
    public int age;
}

public class MyComponent:MonoBehaviour{
    [Header("自定义结构体")]
    public MyStruct myStruct;

    [SerializeField]
    private string name;

    [HideInInspector]
    public string country;
}
```

### 七、其他

- ```Space```
- ```Range```
- ```Multiline```
- ```InitializeOnLoad```