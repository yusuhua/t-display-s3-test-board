# t-display-s3-test-board
这是一块为[Lilygo T-Display-S3](https://github.com/Xinyuan-LilyGO/T-Display-S3)设计的扩展板，主要功能有：
- JoyCon按键
- 无源蜂鸣器
- SD卡读写（SPI方式）

<p align="center">
  <img src="https://github.com/yusuhua/t-display-s3-test-board/blob/main/image/gamer.jpg" alt="Gamer display photo"/>
</p>

灵感来源于YouTube上的一个视频，网址：https://www.youtube.com/watch?v=SuTJA3sIOp8&t=2s  
国内用户可以在Bilibili上看到，网址：https://www.bilibili.com/video/BV1zG411j7dF/?spm_id_from=333.337.search-card.all.click ，我就是看到这个视频：)  
当时手中刚好已经买了一块T-Display-S3，对视频中展示的扩展板特别感兴趣，于是就想自己学着设计一块。

# 历史版本
V1.0版与视频中这位UP主设计的差不多是一样的，用起来也没问题，只是个别引脚需要设置上拉电阻；  
V1.1版本在V1.0的基础上增加了一个无源蜂鸣器，这样它就可以演奏美妙的音乐了；  
V1.2版本将原来负责右按键和上按键的43、44号引脚改为了2、3号引脚，因为在电池接口附近有43、44引脚的扩展口，不占用它们可以更好的利用为数不多的引脚；  
V1.3版本又添加了一个SD卡槽，这样我们就可以读取SD卡里的文件了，能做的事情就更多了。
