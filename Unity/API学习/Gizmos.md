## Gizmos工具类

**Gizmos辅助接口，有助于查看和调试一些效果，```MonoBehaviour```脚本主要调用以下两个方法**  


- ```MonoBehaviour.OnDrawGizmos()```    每帧调用
- ```MonoBehaviour.OnDrawGizmosSelected()```    只有对象被选中时调用
---
### 零、静态变量

- ```Color color``` Gizmos绘制使用的颜色
- ```Matrix4x4 matrix``` 用于渲染所有Gizmos的矩阵
- ```Texture exposure``` 用于LightProbe曝光纹理校正
- ```float probeSize``` 用于LightProbe缩放

---
### 一、绘制线段 DrawLine

```C#
// from:起始点
// to:终点
Gizmos.DrawLine(Vector3 from, Vector3 to);
```
---
### 二、绘制射线 DrawRay


```C#
//  r:射线结构体
Gizmos.DrawRay(Ray r)
{
    //  从射线起点开始
    //  起点+射线方向(单位向量)
    DrawLine(r.origin, r.origin + r.direction);
}

//  from:起点
//  direction:射线方向
Gizmos.DrawRay(Vector3 from,Vector3 direction)
{
    DrawLine(from, from + direction);
}
```
---
### 三、绘制立方体 DrawCube

```C#
//  center:立方体中心点
//  size:立方体大小
Gizmos.DrawCube(Vector3 center, Vector3 size);

//  绘制立方体线框
Gizmos.DrawWireCube(Vector3 center, Vector3 size);
```
---
### 四、绘制球体 DrawSphere

```C#
//  center:球体中心点
//  radius:球体半径
Gizmos.DrawSphere(Vector3 center, float radius);

//  绘制球体线框
Gizmos.DrawWireSphere(Vector3 center, float radius);
```
---
### 五、绘制视锥体 DrawFrustum

```C#
//  center:中心点
//  fov:视野区域(它的大小影响整个视角一周的范围)
//  maxRange:视野最远距离
//  minRange:视野最近距离
//  aspect:视野宽度(它的大小只影响视野左右范围)
Gizmos.DrawFrustum(Vector3 center,float fov,float maxRange,float minRange,float aspect);
```
---
### 六、绘制图标 DrawIcon

```C#
//  center:坐标
//  name:资源名字(必须放在Gizmos文件夹下，名字是文件名全称)
//  allowScaling:允许缩放，默认为true
//  tint:颜色值，默认白色Color(255,255,255,255)
Gizmos.DrawIcon(Vector3 center, string name,bool allowScaling,Color tint);
```
---
### 七、绘制GUI纹理 DrawGUITexture

```C#
//  screenRect:绘制区域
//  texture:纹理
//  mat:材质默认为null
//  leftBorder、rightBorder、topBorder、bottomBorder:从区域各边界插入
Gizmos.DrawGUITexture(Rect screenRect,Texture texture);
Gizmos.DrawGUITexture(Rect screenRect,Texture texture,Material mat);
Gizmos.DrawGUITexture(Rect screenRect,Texture texture,int leftBorder,int rightBorder,int topBorder,int bottomBorder);
Gizmos.DrawGUITexture(Rect screenRect,Texture texture,int leftBorder,int rightBorder,int topBorder,int bottomBorder,Material mat);
```
---
### 八、绘制网格 DrawMesh

```C#
//  position:默认为Vector3.zero
//  rotation:默认为Quaternion.identity
//  scale:默认为Vector3.one
//  submeshIndex:默认为-1
Gizmos.DrawMesh(Mesh mesh);
Gizmos.DrawMesh(Mesh mesh,Vector3 position);
Gizmos.DrawMesh(Mesh mesh,Vector3 position,Quaternion rotation);
Gizmos.DrawMesh(Mesh mesh,Vector3 position,Quaternion rotation,Vector3 scale);
Gizmos.DrawMesh(Mesh mesh,int submeshIndex);
Gizmos.DrawMesh(Mesh mesh,int submeshIndex,Vector3 position);
Gizmos.DrawMesh(Mesh mesh,int submeshIndex,Vector3 position,Quaternion rotation);

Gizmos.DrawWireMesh(Mesh mesh);
Gizmos.DrawWireMesh(Mesh mesh,Vector3 position);
Gizmos.DrawWireMesh(Mesh mesh,Vector3 position,Quaternion rotation);
Gizmos.DrawWireMesh(Mesh mesh,Vector3 position,Quaternion rotation,Vector3 scale);
Gizmos.DrawWireMesh(Mesh mesh,int submeshIndex);
Gizmos.DrawWireMesh(Mesh mesh,int submeshIndex,Vector3 position);
Gizmos.DrawWireMesh(Mesh mesh,int submeshIndex,Vector3 position,Quaternion rotation);
```