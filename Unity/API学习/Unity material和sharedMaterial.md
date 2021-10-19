Unity 通过修改材质相对应shader的一些属性，来调整模型表现形式。通常是获取模型的MeshRender组件，然后获取它的Material属性  

这里有两个方法获取材质：  

**material** 

**sharedMaterial**


### 1、sharedMaterial
The shared material of this object.
Modifying sharedMaterial will change the appearance of all objects using this material,  
 and change material settings that are stored in the project too.
It is not recommended to modify materials returned by sharedMaterial.   
If you want to modify the material of a renderer use material instead

字面意思，共享材质。修改了这个材质，所有使用相同材质的模型，都将发生变化，并且还会修改本地材质。  
所以使用相同材质，有不同变化需求的，不要在这里使用共享材质来修改材质属性


### 2、material
Returns the first instantiated Material assigned
to the renderer.
Modifying material will change the material for this object only.
If the material is used by any other renderers, this will clone the shared material and start using it from now on.

第一个实例化后的材质，直接用代码说明

```C#

//  A B同时使用材质C

//  使用材质MatC
MeshRender mrA;
//  使用材质MatC
MeshRender mrB;


//  测试
Material sharedA = mrA.sharedMaterial;
Material sharedB = mrB.sharedMaterial;


//  sharedA == sharedB    true
//  这里共享材质是相同的都是材质C，修改任意的sharedA或者sharedB都会修改本地的材质C，他们公用一份内存

Material matA = mrA.material;
Material matB = mrB.material;
//  matA == matB    false
//  这里的材质是材质C的两个实例化，各自修改matA、matB，或者直接修改MatC都不会相互影响，他们是相互独立的


//  第一个材质实例化之后，再次调用获取共享材质方法
sharedA = mrA.sharedMaterial;
sharedB = mrB.sharedMaterial;

//  sharedA == sharedB  false
//  这里的共享材质已经变成了各自实例化后的材质，所以是不一样的

```


### 注意
所以在使用材质修改材质属性时，要留意自己的改动是否会影响到其他对象的属性，是否会改动本地材质