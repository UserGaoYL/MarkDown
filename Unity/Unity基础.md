# 渲染基础

### 1.渲染管线
![通用渲染管线](./images/渲染管线.png "通用渲染管线")

内置渲染管线 (BuildIn Render Pipeline)

可编程渲染管线**SRP**(Scriptable Render Pipeline)

轻量级渲染管线**LWRP**(Lightweight Render Pipeline) 改名为 **URP**(Universal Render Pipeline)

高清晰渲染管线**HDRP**(HD Render Pipeline)

##### URP
<details>
<summary>内置渲染流程</summary>

![URP](./images/内置渲染流程.png "URP")
</details>



##### 渲染队列
<details>
<summary>渲染队列</summary>

| 渲染队列        | 描述   |  渲染队列值 |
| --------   | --------   | :-----  |
| Background | 这个队列通常被最先渲染. | 1000 |
| Geometry | 不透明物体的渲染队列.大多数物体都应该使用该队列进行渲染,也是Unity Shader中默认的渲染队列. | 2000 |
| AlphaTest |  有透明通道,需要进行Alpha Test的物体的队列,比在Geomerty中更有效.| 2450 |
| Transparent | 该渲染队列在Geometry和AlphaTest队列后被渲染.（不写入深度缓存的Shaders）对象使用该队列.比如玻璃和粒子效果. | 3000 |
| Overlay | 该渲染队列是为覆盖物效果服务的.不论什么最后被渲染的对象使用该队列,比如镜头光晕. | 4000 |

</details>

##### 渲染类型 (标识作用)
<details>
<summary>渲染类型</summary>

Opaque: 用于大多数着色器（法线着色器、自发光着色器、反射着色器以及地形的着色器）.
Transparent:用于半透明着色器（透明着色器、粒子着色器、字体着色器、地形额外通道的着色器）.
TransparentCutout: 蒙皮透明着色器（Transparent Cutout,两个通道的植被着色器）.
Background: 天空盒着色器.
Overlay: GUITexture,镜头光晕,屏幕闪光等效果使用的着色器.
TreeOpaque: 地形引擎中的树皮.
TreeTransparentCutout:  地形引擎中的树叶.
TreeBillboard: 地形引擎中的广告牌树.
GrassBillboard: 地形引擎何中的广告牌草.
</details>

##### 混合模式
<details>
<summary>25种混合合效果</summary>

![混合模式](./images/25种混合模式.jpg "混合模式")
![原始图](./原始图.jpg "原始图")

</details>

<details>
<summary>混合参数</summary>

| 参数        | 描述   |
| --------   | :-----  |
| One      | 因子：1  |
| Zero        |   因子：0   |
| SrcColor        |    源颜色值    |
| SrcAlpha        |    源颜色的Alpha值    |
| DstColor        |    目标颜色值    |
| DstAlpha        |    目标颜色的Alpha值    |
| OneMinusSrcColor        |    1-源颜色值    |
| OneMinusSrcAlpha        |    1-源颜色的Alpha值    |
| OneMinusDstColor        |    1-目标颜色值    |
| OneMinusDstAlpha        |    1-目标颜色的Alpha值    |

</details>

<details>
<summary>常用混合效果</summary>

| 模式 | 开关 |
| ---- | :----|
|正常（Normal）| Blend SrcAlpha OneMinusSrcAlpha |
|柔和相加（Soft Addtive） | Blend OneMinusDstAlpha One |
|正片叠底（Multiply）,即相乘 | Blend DstColor Zero | 
|两倍相乘（2x Multiply）| Blend DstColor SrcColor |
|滤色（Screen）| Blend OneMinusDstColor One |

</details>

<details>
<summary>影响渲染顺序的因素</summary>

1.深度
2.渲染队列
3.应用阶段绘制提交顺序(比如UI) 这里和动态合并批次有一定关系

</details>

### 2.相机
<details>
<summary>主要参数</summary>

| 参数 | 描述 |
| ---- | :---- |
| Clear Flags | 清除标记 |
| Background | 背景 |
| Culling Mask | 需要渲染的Layer |
| Projection | 投影方式 |
| Clipping Planes | 剪裁平面(远/近) |
| Viewport Rect	| 视口的大小 |
| Depth | 相机绘制顺序 |

</details>

注意:RenderTexture一定要注意合理的尺寸.避免不必要的开销.


### 3.Shader基础

#### 1).基础语法
Unity **ShaderLab**支持使用GLSL、HLSL和CG三种语言编写shader.
**CG** （C for Graphics ）是 NVIDIA 公司开发的语言.从名字上来看的出它是 C 语言的亲戚,现实是它保留了 C 语言的大部分语义.NVIDIA官方已经宣布自CG3.1版本后,不再维护和发展Cg语言.
**HLSL**（High Level Shader Language） 的简称,由微软和NVIDIA共同开发的语言.语法跟 CG 非常的相似.
**GLSL** （OpenGL Shading Language） 的简称,OPENGL 组件开发的,语法也是基于 C 语言的.




##### 1.基础语法       
<details>
<summary>着色器语法结构</summary>

![着色器语法结构](./images/最简单的shader.png "着色器语法结构")
</details>
##### 2.最简单的shader 

<details>
<summary>着色器流程</summary>

![rendering-pipeline](./images/rendering-pipeline.jpg "着色器流程")
</details>


##### 3光照
<details>
<summary>四大光照模型</summary>

1.Lambert模型(漫反射)
2.Phong模型(镜面反射)
3.Blinn-Phong光照模型(修正镜面光)
4.Rendering Equation(全局光照模型）

![光照示例正面](./images/光照示例正面.jpg "光照示例正面")
![光照示例背面](./images/光照示例背面.jpg "光照示例背面")
![光照示例下面](./images/光照示例下面.jpg "光照示例下面")

</details>

<details>
<summary>兰伯特与半兰伯特</summary>

**Lambert光照模型**
![漫反射模型](./images/漫反射模型.png "漫反射模型")
Lambert是理想的漫反射模型,他表现的材质较为均匀,不能反映粗糙度带来的变化.
兰伯特定律：反射光线的强度与表面光线和光源方向之间的夹角的余弦成正比.
Cdiffuse = (Clight·Mdiffuse)max(0, n·I)
其中n代表的是表面法线,I是由光线与表面的交点指向光源的单位矢量,Mdiffuse是材质的漫发射颜色,Clight是光源的颜色


**HalfLambert光照模型**
该光照模型是由Valve公司开发《半条命》时提出的,是一种用于低光照区域照亮物体的技术.
由前面的兰伯特公式我们知道一旦入射光向量与材质表面的角度大于90度,那么得到的漫反射颜色就会全部变为黑色,没有任何明暗变化效果！
Half Lambert 是在 Lambert 模型的基础上,做了微调,也就是将光源方向与法线方向的点乘结果,从原来[-1, 1],映射为 [0, 1],这样原来背光面,也会有明暗效果.

Half Lambert 光照模型公式: 最终颜色 = 直射光颜色 * 漫反射颜色 * (dot(光源方向, 法线方向) * 0.5 + 0.5)
</details>



#### 2).常用函数
[函数图形](http://graphtoy.com/)
[函数手册](http://developer.download.nvidia.com/cg/index_stdlib.html)
<details>
<summary>几个常用的函数</summary>

| 函数 | 描述 |
| ---- | :----|
| radians(x) | 函数将角度值转换为弧度值 |
| round | 四舍五入 |
| floor | 向下取整 |
| ceil | 向上取整, ceil(float(1.3)) ,其返回值为 2.0 |
| saturate | 如果 x 小于 0,返回 0；如果 x 大于 1,返回1；否则,返回 x |
| sign(x) | 如果 x 大于 0,返回 1；如果 x 小于 0,返回-1；否则返回 0.|
| dot | 返回 A 和 B 的点积 (dot product)  |
| frac | 返回参数X的小数部分 |
| clip | 当参数小于0时,丢弃当前片元 |
</details>


### 4.常见效果实现
##### 技能CD
1.绘制图片
2.挖洞
3.随着时间线性 角度线性变化

<details>
<summary>Atan2</summary>

[Atan2](https://zh.wikipedia.org/wiki/Atan2)
</details>

<details>
<summary>时间函数</summary>

//t是自该场景加载开始所经过的时间，4个分量分别是 (t/20, t, t*2, t*3)
_Time   float4  time (t/20, t, t*2, t*3),   
//t 是时间的正弦值，4个分量分别是 (t/8, t/4, t/2, t)
_SinTime    float4  Sine of time: (t/8, t/4, t/2, t).
//t 是时间的余弦值，4个分量分别是 (t/8, t/4, t/2, t)
_CosTime    float4  Cosine of time: (t/8, t/4, t/2, t).
//dt 是时间增量，4个分量的值分别是(dt, 1/dt, smoothDt, 1/smoothDt)
nity_DeltaTime  float4  Delta time: (dt, 1/dt, smoothDt, 1/smoothDt).
</details>

### 5.连连看
**ASE** Amplify Shader Editor


### 6.后处理
##### Bloom
##### Depth Of Feild
##### Color Grading
##### Fog


### 7.学习网站
1.[Unity用户手册](https://docs.unity3d.com/Manual/index.html)
2.[Unity论坛](https://forum.unity.com/)
3.[AssetStore](https://assetstore.unity.com/)
4.[UnityGithub](https://github.com/Unity-Technologies)
5.[reddit](https://www.reddit.com/r/Unity3D/)
6.[CatLike](https://catlikecoding.com/)
7.[UWA](https://blog.uwa4d.com/)
8.[元素](https://www.element3ds.com/)
9.[知乎](https://www.zhihu.com/)
10.[浅墨](https://www.zhihu.com/people/mao-xing-yun)
11.[MOMO](https://www.xuanyusong.com/)





