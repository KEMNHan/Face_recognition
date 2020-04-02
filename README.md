
安装模块 [opencv-python]，[freetype]，[PyYAML]。
python -m pip install opencv-python freetype-py PyYAML
下载SDK2.2
将 `lib` 中的所有动态库拷贝到 `lib` 目录中对应的平台目录下。
在 [profile.yml](profile.yml) 中配置 `APP ID` 和 `SDK KEY`。
python demo.py 
按下 `Esc` 或 `q` 或 `Q` 来退出程序、

按下 e 或 E 添加人脸   #demo.py 102行 filename为添加的人脸文件
按下 d 或 D 删除人脸   #demo,py 103行 ID为需要删除的人脸

demo.py 第99为数据库文件 

