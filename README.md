# ArcaneStyleTransfer
双城之战风格迁移

# 写在前面
导师课程需要，让我写个有关GAN的项目指导书。由于本人对英雄联盟的热爱(初一玩到研一只打到了铂金5)，将闲来自己跑着玩的双城之战风格迁移数据集用来给学生们作为课程项目。在此也开源给大家使用。

## 数据链接地址
链接：[https://pan.baidu.com/s/1_YojivcNNEIo4-FJXpeopg](https://pan.baidu.com/s/1_YojivcNNEIo4-FJXpeopg) 

提取码：iimp 

介绍：
本数据集是由FFHQ数据集迁移制作而来的，迁移图像是ArcaneGAN跑出来的。里面有10000张成对图片。因此使用有监督GAN(Pix2Pix、Pix2PixHD等)和无监督GAN(CycleGAN、U-GAT-IT等)模型都可以跑。

![在这里插入图片描述](https://img-blog.csdnimg.cn/f4ee86baeb354aefa7b61fc63a2c6d55.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAaWlpaWlpaW1w,size_20,color_FFFFFF,t_70,g_se,x_16)

## 如何自己制作

代码：[https://github.com/hahahappyboy/ArcaneStyleTransfer](https://github.com/hahahappyboy/ArcaneStyleTransfer)

主要参考了：[https://www.bilibili.com/read/cv14584686](https://www.bilibili.com/read/cv14584686)

**如何用？**

下载ArcaneGANv0.4.jit模型(也放在上面那个网盘)，把要迁移的图片放在datasets文件夹下，运行transfer.py文件即可，结果保存在result文件夹下面。

![在这里插入图片描述](https://img-blog.csdnimg.cn/7dfc80dafd474856aedb9f35a41071bb.png)

# 写在后面
很喜欢LOL千珏的一句话

![在这里插入图片描述](https://img-blog.csdnimg.cn/b35fe3eccfc549c6afbec74a199dd201.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAaWlpaWlpaW1w,size_20,color_FFFFFF,t_70,g_se,x_16)

