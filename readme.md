# 洗数据工具

之前不会写python gui，写的简直是丢人。。。非常不建议你们看源码。。。

#### 功能说明

* 上一张/下一张图切换
* 图片放大/缩小
* 判断标注正确与否，自动保存并进入下一张图片
* 可反复修改清洗结果；如果该图像已被清洗过，会显示清洗结果
* 支持跳转，可以多人协作

#### 用法

##### 配置config.proto

* train_list：对应于train.txt，就是那个图片+label的文件
* label_list：对应于label_list.txt，是那个ZJLXXX 对应 violin...那个文件
* right_list：清洗后，认为标注正确的图片list，会自动保存
* wrong_list：清洗后，认为标注不正确的图片list，会自动保存
* pic_rootpaht：数据集图片的根目录

##### python2 gui.py
* 入口在code/gui.py下，进入code/目录，python2 gui.py即可
* 依赖pillow和tkinter，如果没有的话，需要安装一下
* 窗口太小可以拖大一点

##### 多人协作

* 咋说呢，大家的图片list要保持一致
* 然后每个人洗不同的数据段，跳转功能就是干这个用的（注意从0开始）
* 最后大家把right_list和wrong_list合并一下就好了

#### 最后强调几点

* 有bug的话联系我，我会修的
* 如果觉得不好用，就换一种方式把，说实在的我自己也觉得我这玩意写出来不好用
* 不要笑，尤其看源码的时候，不要笑

