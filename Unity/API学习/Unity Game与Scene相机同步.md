主要用到API```SceneView.lastActiveSceneView.camera```


### Game视图与Scene视图相机同步

```C#
Camera.main.transform.SetPositionAndRotation(SceneView.lastActiveSceneView.camera.transform.position, SceneView.lastActiveSceneView.camera.transform.rotation);
```

### Scene视图与Game视图相机同步

```C#
Camera cameraMain = Camera.main;
var sceneView = SceneView.lastActiveSceneView;
if (sceneView != null)
{
    sceneView.cameraSettings.nearClip = cameraMain.nearClipPlane;
    sceneView.cameraSettings.fieldOfView = cameraMain.fieldOfView;
    sceneView.pivot = cameraMain.transform.position +
        cameraMain.transform.forward * sceneView.cameraDistance;
    sceneView.rotation = cameraMain.transform.rotation;
}
```