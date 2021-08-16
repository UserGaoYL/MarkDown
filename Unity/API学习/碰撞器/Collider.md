# Collider


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