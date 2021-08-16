
### 一、基类Collider
```C#
//  碰撞器
public class Collider : Component
{
    //  碰撞器脚本是否开启
    public bool enabled { get; set; }

    //  刚体组件
    public Rigidbody attachedRigidbody { get; }

    //  是否开启触发器
    public bool isTrigger { get; set; }

    //  碰撞器默认参数（官方提示不懂不要修改它）
    public float contactOffset { get; set; }

    //  获取距离指定坐标最近的碰撞点
    public Vector3 ClosestPoint(Vector3 position);

    //  碰撞器包围盒
    public Bounds bounds { get; }

    //  共享材质，修改它会影响到原始材质，所以要注意使用方式，避免误修改本地的材质球属性，并且会影响到所有使用该材质的对象
    [NativeMethod("Material")]
    public PhysicMaterial sharedMaterial { get; set; }

    //  每次调用都会生成一个新的Clone材质,修改它不影响原始材质
    public PhysicMaterial material
    {
        [NativeMethod("GetClonedMaterial")] get;
        [NativeMethod("SetMaterial")] set;
    }

    //  射线检测，是否与碰撞器相交
    private RaycastHit Raycast(Ray ray, float maxDistance, ref bool hasHit);

    //  射线检测，返回碰撞信息
    public bool Raycast(Ray ray, out RaycastHit hitInfo, float maxDistance)
    {
        bool hasHit = false;
        hitInfo = Raycast(ray, maxDistance, ref hasHit);
        return hasHit;
    }

    [NativeName("ClosestPointOnBounds")]
    private void Internal_ClosestPointOnBounds(Vector3 point, ref Vector3 outPos, ref float distance);

    //  获取距离指定坐标最近的碰撞盒上的坐标
    public Vector3 ClosestPointOnBounds(Vector3 position)
    {
        float dist = 0f;
        Vector3 outpos = Vector3.zero;
        Internal_ClosestPointOnBounds(position, ref outpos, ref dist);
        return outpos;
    }
}
```

### 二、BoxCollider

```C#
//  盒状碰撞器
public class BoxCollider : Collider
{
    //  Box中心点
    public Vector3 center { get; set; }

    //  Box大小
    public Vector3 size { get; set; }

    //  已废弃接口，获取和设置Box大小(一半大小)
    [Obsolete("Use BoxCollider.size instead.")]
    public Vector3 extents { get { return size * 0.5F; }  set { size = value * 2.0F; } }
}
```

### 三、SphereCollider

```C#
//  球状碰撞器
public class SphereCollider : Collider
{
    //  球体中心点
    public Vector3 center { get; set; }

    //  球体半径
    public float radius { get; set; }
}
```

### 四、CapsuleCollider

```C#
//  胶囊碰撞器
public class CapsuleCollider : Collider
{
    //  胶囊中心点
    public Vector3 center { get; set; }

    //  胶囊半径
    public float radius { get; set; }

    //  胶囊高度(默认等于胶囊半径的两倍，此时表示球体)
    public float height { get; set; }

    //  胶囊高度扩展方向(默认Y-Axis)
    //  X-Axis
    //  Y-Axis
    //  Z-Axis
    public int direction { get; set; }

    //  内部方法（在UnityEditor.ColliderUtil里有使用）
    internal Vector2 GetGlobalExtents();
    internal Matrix4x4 CalculateTransform();
}
```

```C#
namespace UnityEditor
{
    internal class ColliderUtil
    {
        static Vector3 GetCapsuleExtents(CapsuleCollider cc)
        {
            return cc.GetGlobalExtents();
        }

        static Matrix4x4 CalculateCapsuleTransform(CapsuleCollider cc)
        {
            return cc.CalculateTransform();
        }
    }
}
```

### 五、MeshCollider

```C#
//  网格碰撞器
public class MeshCollider : Collider
{
    //  网格
    public Mesh sharedMesh { get; set; }

    //  是否是凸网格（IsTrigger属性只有在convex未true时才生效）
    public bool convex { get; set; }

    //  已废弃，返回false
    public bool inflateMesh
    {
        get { return false; } set {}
    }

    //  网格碰撞器配置选项
    public MeshColliderCookingOptions cookingOptions { get; set; }

    //  已废弃
    public float skinWidth { get { return 0f; } set {} }

    //  已废弃
    public bool smoothSphereCollisions { get { return true; } set {} }
}
```

```C#
[Flags]
public enum MeshColliderCookingOptions
{
    None,
    [Obsolete("No longer used because the problem this was trying to solve is gone since Unity 2018.3", true)] InflateConvexMesh = 1 << 0,
    CookForFasterSimulation = 1 << 1,
    EnableMeshCleaning = 1 << 2,
    WeldColocatedVertices = 1 << 3,
    UseFastMidphase = 1 << 4
}
```

### 六、CharacterController

```C#
//  角色控制碰撞器
public class CharacterController : Collider
{
    //  是否可以超某个方向移动
    public bool SimpleMove(Vector3 speed);

    //  移动
    public CollisionFlags Move(Vector3 motion);

    //  移动速度（只读）
    public Vector3 velocity { get; }

    //  是否在地面上
    public bool isGrounded {[NativeName("IsGrounded")] get; }

    //  碰撞Flag
    public CollisionFlags collisionFlags { get; }

    //  半径,此值本质上是碰撞体的宽度。
    public float radius { get; set; }

    //  高度
    public float height { get; set; }

    //  中心点
    public Vector3 center { get; set; }

    //  将碰撞体限制为爬坡的斜率不超过指示值（以度为单位）。
    public float slopeLimit { get; set; }

    //  仅当角色比指示值更接近地面时，角色才会升高一个台阶。
    //  该值不应该大于角色控制器的高度，否则会产生错误。
    public float stepOffset { get; set; }

    //  两个碰撞体可以穿透彼此且穿透深度最多为皮肤宽度 (Skin Width)。
    //  较大的皮肤宽度可减少抖动。
    //  较小的皮肤宽度可能导致角色卡住。
    //  合理设置是将此值设为半径的 10%
    public float skinWidth { get; set; }

    //  如果角色试图移动到指示值以下，根本移动不了。
    //  此设置可以用来减少抖动。在大多数情况下，此值应保留为 0
    public float minMoveDistance { get; set; }

    //  是否发生碰撞
    public bool detectCollisions { get; set; }

    //  是否可以重叠
    public bool enableOverlapRecovery { get; set; }
}
```

```C#
// CollisionFlags is a bitmask returned by CharacterController.Move.
public enum CollisionFlags
{
    // CollisionFlags is a bitmask returned by CharacterController.Move.
    None = 0,

    // CollisionFlags is a bitmask returned by CharacterController.Move.
    Sides = 1,

    // CollisionFlags is a bitmask returned by CharacterController.Move.
    Above = 2,

    // CollisionFlags is a bitmask returned by CharacterController.Move.
    Below = 4,

    //*undocumented
    CollidedSides = 1,
    //*undocumented
    CollidedAbove = 2,
    //*undocumented
    CollidedBelow = 4
}
```

### 七、TerrainCollider

```C#
//  地形碰撞器
public class TerrainCollider : Collider
{
    //  地形数据
    public extern TerrainData terrainData { get; set; }

    //  射线检测
    extern private RaycastHit Raycast(Ray ray, float maxDistance, bool hitHoles, ref bool hasHit);

    //  地形射线检测
    internal bool Raycast(Ray ray, out RaycastHit hitInfo, float maxDistance, bool hitHoles)
    {
        bool hasHit = false;
        hitInfo = Raycast(ray, maxDistance, hitHoles, ref hasHit);
        return hasHit;
    }
}
```

### 八、WheelCollider

```C#
//  车轮碰撞器
public class WheelCollider : Collider
{
    public extern Vector3 center {get; set; }
    public extern float radius {get; set; }
    public extern float suspensionDistance {get; set; }
    public extern JointSpring suspensionSpring {get; set; }
    public extern bool suspensionExpansionLimited {get; set; }
    public extern float forceAppPointDistance {get; set; }
    public extern float mass {get; set; }
    public extern float wheelDampingRate {get; set; }
    public extern WheelFrictionCurve forwardFriction {get; set; }
    public extern WheelFrictionCurve sidewaysFriction {get; set; }
    public extern float motorTorque {get; set; }
    public extern float brakeTorque {get; set; }
    public extern float steerAngle {get; set; }
    public extern bool isGrounded {[NativeName("IsGrounded")] get; }
    public extern float rpm { get; }
    public extern float sprungMass { get; }

    public extern void ConfigureVehicleSubsteps(float speedThreshold, int stepsBelowThreshold, int stepsAboveThreshold);

    public extern void GetWorldPose(out Vector3 pos, out Quaternion quat);
    public extern bool GetGroundHit(out WheelHit hit);
}
```