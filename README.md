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

## 历史版本
- V1.0版与视频中这位UP主设计的差不多是一样的，用起来也没问题，只是个别引脚需要设置上拉电阻；
- V1.1版本在V1.0的基础上增加了一个无源蜂鸣器，这样它就可以演奏美妙的音乐了；
- V1.2版本将原来负责右按键和上按键的43、44号引脚改为了2、3号引脚，因为在电池接口附近有43、44引脚的扩展口，不占用它们可以更好的利用为数不多的引脚，同时增加了一个SD卡槽，这样我们就可以读取SD卡里的文件了，能做的事情就更多了；
- V1.3版本将无源蜂鸣器和SD卡槽移到了背面，方便在母座与T-Display-S3之间放置一个合适的锂电池，当然，如果不用母座直接焊接T-Display-S3到板子上也是可以的，还提供了一个电池电源线的出入口，可以通过这个小洞将电池电源线引到背面，适合做3D外壳时将电池设计在背面仓的情况，同时还增加了一个外置天线座，T-Display-S3支持外置天线，不过这个在信号比较好的地方可有可无，也可以选择不焊接这个元器件。

PCB Gerber中仅有V1.2与V1.3版本，因为前两个版本我觉得没有必要上传，大家可以根据自己的喜好选择性的焊接元器件。  
在此感谢一下[嘉立创](https://lceda.cn/)每月2次的免费打板，给初学PCB板设计的我有一个实现自己想法的机会~！我的PCB板子就是使用嘉立创EDA Pro设计的：) 

## 引脚图
显示屏的引脚图可以参考[Lilygo T-Display-S3](https://github.com/Xinyuan-LilyGO/T-Display-S3)的图片，这里不做介绍。

JoyCon按键部分：
| 按键    | 引脚   |
| :-------| :---- |
| start   | 0     |
| select  | 14    |
| up      | 3     |
| down    | 18    |
| left    | 2     |
| right   | 17    |
| a       | 21    |
| b       | 16    |

无源蜂鸣器部分，引脚为1

SD卡部分：
| 按键    | 引脚   |
| :-------| :---- |
| sck     | 12    |
| mosi    | 11    |
| moso    | 13    |
| cs      | 10    |

## 元器件说明
- R1~R7为0603的10K贴片电阻
- R8为0805的180Ω贴片电阻
- C1为0805的100nF贴片电容
- D1为SOD-123的1N4148开关二极管
- Q1为SOD-23的S8550三极管
- BUZZER为MLT-7525贴片无源蜂鸣器
- 按键为6 * 6 * 5的四脚贴片按键
- SD卡槽这个不知道怎么描述了，明显的特征就是后边两个洞，里边有个小弹簧的:)
- 外置天线座根据图中的样子选就可以，尺寸应该都是一样的

## 参考资料
除了JoyCon按键参考了视频UP主的设计之外，无源蜂鸣器参考了MLT-7525规格书中的设计，SD卡参考了[微雪官网的设计](https://www.waveshare.net/w/upload/8/83/Micro-SD-Storage-Board-Schematic.pdf)。  
在这里要给微雪电子点个赞，他们设计的开发板都可以在官网找到对应的原理图，对刚入门的小白来说很有参考价值。

测试用例是基于github上的一个micropython固件，为了方便大家就上传了一份到framework文件夹里，欢迎到他的仓库下载最新版本：https://github.com/russhughes/s3lcd  
当然，如果使用C/C++开发也是没问题的~！
