## Unity自定义Inspector面板


### 一、创建自定义类

```C#
using UnityEngine;

public class Player:MonoBehaviour{
    public int userId;
    public int userAge;
    public string userName;
    public float hp;
    public float atk;
}

```

### 二、创建自定义界面类

```PlayerEditor.cs```需要放在```./Assets/Editor/```文件夹下

```C#
using UnityEngine;
using UnityEditor;

//  继承Editor类，并关联自己的脚本
[CustomEditor(typeof(Player))]
public class PlayerEditor : Editor
{
    //  写法一
    SerializedProperty userId;
    SerializedProperty userAge;
    SerializedProperty userName;
    SerializedProperty hp;
    SerializedProperty atk;
    string[] excludes;

    //  写法二
    Player user;
    bool showFolder;

    //  初始化属性
    private void OnEnable()
    {

        //  写法一
        userId = serializedObject.FindProperty("userId");
        userAge = serializedObject.FindProperty("userAge");
        userName = serializedObject.FindProperty("userName");
        hp = serializedObject.FindProperty("hp");
        atk = serializedObject.FindProperty("atk");
        excludes = new string[] { "m_Script","userId","userName","userAge","hp","atk"};

        user = target as Player;

    }

    //  绘制自定义面板
    public override void OnInspectorGUI()
    {
        //  写法一调用方法
        //serializedObject.Update();
        //  忽略属性显示
        //DrawPropertiesExcluding(serializedObject, excludes);

        //  设置整个界面是以垂直方向来布局
        EditorGUILayout.BeginVertical();

        EditorGUILayout.Space(5);
        EditorGUILayout.LabelField("玩家基础信息");
        EditorGUILayout.Space();
        EditorGUI.indentLevel++;
        user.userName = EditorGUILayout.TextField("名字", user.userName);
        user.userId = EditorGUILayout.IntField("用户ID",user.userId);
        user.userAge = EditorGUILayout.IntSlider("年龄", user.userAge,1,100);

        if (user.userAge > 18)
        {
            EditorGUILayout.HelpBox("成年了",MessageType.Info);
            GUI.color = Color.green;
        }
        else if (user.userAge > 12)
        {
            EditorGUILayout.HelpBox("有点年轻啊", MessageType.Warning);

            GUI.color = Color.blue;
        }
        else {
            EditorGUILayout.HelpBox("未成年", MessageType.Error);

            GUI.color = Color.red;
        }

        Rect ageRect = GUILayoutUtility.GetRect(10, 10);
        EditorGUI.ProgressBar(ageRect, user.userAge / 100.0f, "测试进度条");

        EditorGUI.indentLevel--;

        GUI.color = Color.white;
        EditorGUILayout.Space();

        showFolder = EditorGUILayout.Foldout(showFolder,"展开详情");
        EditorGUI.BeginDisabledGroup(EditorApplication.isPlayingOrWillChangePlaymode);
        if (showFolder) {
            EditorGUI.indentLevel++;
            user.hp = EditorGUILayout.FloatField("血量", user.hp);
            user.atk = EditorGUILayout.FloatField("攻击力", user.atk);
            EditorGUI.indentLevel--;
        }


        //  整个界面垂直方向布局结束
        EditorGUILayout.EndVertical();

        //  写法一调用方法
        //if (serializedObject.ApplyModifiedProperties()) {

        //}
    }
}
```

### 三、EditorWindow

```C#
using UnityEditor;
using UnityEngine;

[ExecuteInEditMode]
public class Screenshot : EditorWindow
{

    int resWidth = Screen.width * 4;
    int resHeight = Screen.height * 4;

    public Camera myCamera;
    int scale = 1;

    string path = "";
    bool showPreview = true;
    RenderTexture renderTexture;

    bool isTransparent = false;

    // Add menu item named "My Window" to the Window menu
    [MenuItem("Tools/Saad Khawaja/Instant High-Res Screenshot")]
    public static void ShowWindow()
    {
        //Show existing window instance. If one doesn't exist, make one.
        EditorWindow editorWindow = EditorWindow.GetWindow(typeof(Screenshot));
        editorWindow.autoRepaintOnSceneChange = true;
        editorWindow.Show();
        editorWindow.titleContent = new GUIContent("Screenshot");
    }

    float lastTime;

    void OnGUI()
    {
        EditorGUILayout.LabelField("Resolution", EditorStyles.boldLabel);
        resWidth = EditorGUILayout.IntField("Width", resWidth);
        resHeight = EditorGUILayout.IntField("Height", resHeight);

        EditorGUILayout.Space();

        scale = EditorGUILayout.IntSlider("Scale", scale, 1, 15);

        //显示帮助信息
        EditorGUILayout.HelpBox("The default mode of screenshot is crop - so choose a proper width and height. The scale is a factor " +
            "to multiply or enlarge the renders without loosing quality.", MessageType.None);

        EditorGUILayout.Space();

        GUILayout.Label("Save Path", EditorStyles.boldLabel);

        EditorGUILayout.BeginHorizontal();
        EditorGUILayout.TextField(path, GUILayout.ExpandWidth(false));
        if (GUILayout.Button("Browse", GUILayout.ExpandWidth(false)))
            path = EditorUtility.SaveFolderPanel("Path to Save Images", path, Application.dataPath);

        EditorGUILayout.EndHorizontal();

        EditorGUILayout.HelpBox("Choose the folder in which to save the screenshots ", MessageType.None);
        EditorGUILayout.Space();

        GUILayout.Label("Select Camera", EditorStyles.boldLabel);

        myCamera = EditorGUILayout.ObjectField(myCamera, typeof(Camera), true, null) as Camera;

        if (myCamera == null)
        {
            myCamera = Camera.main;
        }

        isTransparent = EditorGUILayout.Toggle("Transparent Background", isTransparent);

        EditorGUILayout.HelpBox("Choose the camera of which to capture the render. You can make the background transparent using the transparency option.", MessageType.None);

        EditorGUILayout.Space();
        EditorGUILayout.BeginVertical();
        EditorGUILayout.LabelField("Default Options", EditorStyles.boldLabel);

        if (GUILayout.Button("Set To Screen Size"))
        {
            resHeight = (int)Handles.GetMainGameViewSize().y;
            resWidth = (int)Handles.GetMainGameViewSize().x;

        }

        if (GUILayout.Button("Default Size"))
        {
            resHeight = 1440;
            resWidth = 2560;
            scale = 1;
        }

        EditorGUILayout.EndVertical();

        EditorGUILayout.Space();
        EditorGUILayout.LabelField("Screenshot will be taken at " + resWidth * scale + " x " + resHeight * scale + " px", EditorStyles.boldLabel);

        if (GUILayout.Button("Take Screenshot", GUILayout.MinHeight(60)))
        {
            if (path == "")
            {
                path = EditorUtility.SaveFolderPanel("Path to Save Images", path, Application.dataPath);
                Debug.Log("Path Set");
                TakeHiResShot();
            }
            else
            {
                TakeHiResShot();
            }
        }

        EditorGUILayout.Space();
        EditorGUILayout.BeginHorizontal();

        if (GUILayout.Button("Open Last Screenshot", GUILayout.MaxWidth(160), GUILayout.MinHeight(40)))
        {
            if (lastScreenshot != "")
            {
                Application.OpenURL("file://" + lastScreenshot);
                Debug.Log("Opening File " + lastScreenshot);
            }
        }

        if (GUILayout.Button("Open Folder", GUILayout.MaxWidth(100), GUILayout.MinHeight(40)))
        {

            Application.OpenURL("file://" + path);
        }

        if (GUILayout.Button("More Assets", GUILayout.MaxWidth(100), GUILayout.MinHeight(40)))
        {
            Application.OpenURL("https://www.assetstore.unity3d.com/en/#!/publisher/5951");
        }

        EditorGUILayout.EndHorizontal();

        if (takeHiResShot)
        {
            int resWidthN = resWidth * scale;
            int resHeightN = resHeight * scale;
            RenderTexture rt = new RenderTexture(resWidthN, resHeightN, 24);
            myCamera.targetTexture = rt;

            TextureFormat tFormat;
            if (isTransparent)
                tFormat = TextureFormat.ARGB32;
            else
                tFormat = TextureFormat.RGB24;

            Texture2D screenShot = new Texture2D(resWidthN, resHeightN, tFormat, false);
            myCamera.Render();
            RenderTexture.active = rt;
            screenShot.ReadPixels(new Rect(0, 0, resWidthN, resHeightN), 0, 0);
            myCamera.targetTexture = null;
            RenderTexture.active = null;
            byte[] bytes = screenShot.EncodeToPNG();
            string filename = ScreenShotName(resWidthN, resHeightN);

            System.IO.File.WriteAllBytes(filename, bytes);
            Debug.Log(string.Format("Took screenshot to: {0}", filename));
            Application.OpenURL(filename);
            takeHiResShot = false;
        }

        EditorGUILayout.HelpBox("In case of any error, make sure you have Unity Pro as the plugin requires Unity Pro to work.", MessageType.Info);
    }

    private bool takeHiResShot = false;
    public string lastScreenshot = "";


    public string ScreenShotName(int width, int height)
    {

        string strPath = "";

        strPath = string.Format("{0}/screen_{1}x{2}_{3}.png",
                             path,
                             width, height,
                                       System.DateTime.Now.ToString("yyyy-MM-dd_HH-mm-ss"));
        lastScreenshot = strPath;

        return strPath;
    }

    public void TakeHiResShot()
    {
        Debug.Log("Taking Screenshot");
        takeHiResShot = true;
    }
}


```