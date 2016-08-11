
网页版 http://hktkdy.com/2016/08/09/201608/spotify-to-easenet/
# 动机

最近一直在用Spotify在线听歌，Spotify的好处在于能够发现更多好听的歌曲。然而，它的订阅实在是太贵了，因此也就不能够离线下载，而虽然我在用Spotify，但是也没有抛弃网易云音乐，用它来下载歌曲也很不错，网易云音乐的评论区也往往欢乐多多，因此，我就有了这个想法，想要将Spotify的歌单转到网易云音乐歌单。





# 思路

上网google了一番之后，发现确实有很多的中文用户乃至于外国用户在纠结着怎样导出Spotify的歌单甚至是下载整个歌单的歌曲。我首先找到了[Exportify](https://rawgit.com/watsonbox/exportify/master/exportify.html) 这个网站，它是能够通过接入Spotify的API来将Spotify的歌单找到并支持导出为CSV格式的文件。

而我们知道，网易云音乐也是支持导入歌单的，但仅限于酷狗或酷我的歌单，而酷狗的歌单文件是.kgl格式的，因此如果要想将Spotify歌单转到网易云音乐歌单，我们就首先需要将这种CSV格式的文件转成kgl格式的文件。

本来我是想着用JS的，因为最近一段时间都在用JS，但是从操作文件的角度上讲，我觉得Python还是更有优势的。虽然Python已经很久没用了，但是还是想尝试一下。

# 过程

## 1.导出Spotify歌单
使用刚才提到的[Exportify](https://rawgit.com/watsonbox/exportify/master/exportify.html)  导出歌单，在此过程中，需要Spotify的授权。

![](http://7ktu2f.com1.z0.glb.clouddn.com/exportify.jpg)

授权之后经过分析会出现类似上面的界面，这个时候你只需要挑选你想要导出的歌单并导出之即可。

## ~~2.CSV转JSON（这是之前的思路）~~

~~用记事本打开CSV文件(你也可以打开试试)，发现使用Python对它直接处理并不是很方便。因此，想到首先对之转化为JSON格式文件。~~

~~用记事本(或其他文本编辑器均可)打开CSV文件，然后全选其中的内容,把内容复制到[csv2json](http://www.csvjson.com/csv2json)进行转换：~~

![](http://7ktu2f.com1.z0.glb.clouddn.com/csv2json.jpg)

~~转换完成之后如上图所示，这个时候我们看到已经出现了JSON。~~

## 3.Python文件操作

### 3.1 分析KGL 文件

为了分析KGL文件，我从网络上下载了一个酷狗歌单，它的基本结构是：




		<?xml version="1.0" encoding="windows-1252"?>
		<List ListName="默认列表">
		<File>
		<MediaFileType>0</MediaFileType>
		<FileName>邓紫棋 - 泡沫.mp3</FileName>
		<FilePath>.</FilePath>
		<FileSize>4186975</FileSize>
		<Duration>258000</Duration>
		<Hash>36542b20231db1633eea72f7d6b27492</Hash>
		<Lyric>F:\KuGou\Lyric\邓紫棋 - 泡沫-36542b20231db1633eea72f7d6b27492.krc</Lyric>
		<Bitrate>128000</Bitrate>
		<MandatoryBitrate>0</MandatoryBitrate>
	</File>
	<File>
		<MediaFileType>0</MediaFileType>
		<FileName>灌篮高手 - 好想大声说我爱你.mp3</FileName>
		<FilePath>.</FilePath>
		<FileSize>1618124</FileSize>
		<Duration>231000</Duration>
		<Hash>34e31be84ce3d7c0cfad66e28c0b8220</Hash>
		<Lyric>F:\KuGou\Lyric\灌篮高手 - 好想大声说我爱你-34e31be84ce3d7c0cfad66e28c0b8220.krc</Lyric>
		<Bitrate>56000</Bitrate>
		<MandatoryBitrate>128000</MandatoryBitrate>
	</File>
	<File>
		<MediaFileType>0</MediaFileType>
		<FileName>筷子兄弟 - 小苹果.mp3</FileName>
		<FilePath>.</FilePath>
		<FileSize>3382542</FileSize>
		<Duration>211000</Duration>
		<Hash>fcd49446e26461d95433e9eea5c7a790</Hash>
		<Lyric>F:\KuGou\Lyric\筷子兄弟 - 小苹果-fcd49446e26461d95433e9eea5c7a790.krc</Lyric>
		<Bitrate>128000</Bitrate>
		<MandatoryBitrate>128000</MandatoryBitrate>
	</File>
	</List>


经过反复地修改并导入到网易云音乐中进行测试最终发现，一个简化的KGL文件需要是类似这样的：


```
<?xml version="1.0" encoding="windows-1252"?>

<List ListName="默认列表">

<FileName>邓紫棋 - 泡沫.mp3</FileName>

<FileName>筷子兄弟 - 小苹果.mp3</FileName>
```



甚至结尾的</List>也可以去掉了。

### 3.2 Python 编程
Python文件中写入以下代码(我使用的是Python2.7)

~~首先将在第二步中转化出的JSON文本复制粘贴到一个空白的文本文件中，这里取名spotify.txt，新建一个Python文件(在这里我取名spotify.txt)，将spotify.txt与你的新的Python文件置于同一目录之下。~~

### 3.2.1 csv转xml

直接使用[开源代码](http://code.activestate.com/recipes/577423-convert-csv-to-xml/)

转换完成之后会生成一个.xml文件，这个文件是个中转文件，我在程序的最后对这个文件进行了删除操作。

### 3.2.2 xml转kgl

使用正则表达式进行查找，新建一个.kgl文件对它进行写入操作。



这个时候从该目录(在我的电脑上是C:\Python27\Lib)就能够找到你想要的.kgl格式的歌单了，为了方便我们把它放到桌面上。

## 4.导入到网易云音乐

打开并登录到网易云音乐首页，在右上角下拉菜单中选择导入歌单。将刚刚我们转化好的.kgl文件(在此例中为weekly.kgl)按照要求导入到网易云音乐中。顺利地话，就能够在「我的音乐」的歌单列表里看到我们刚刚导入的歌单了。

不过这里需要说明的是，由于网易云音乐的曲库并不齐全，在我的测试中，以「 Discovery Weekly」歌单为例，它是Spotify官方根据你在Spotify上的听歌情况通过算法推荐出的一个含有30首歌曲的歌单，但是在导入到网易云音乐之后，[只有23首了。](http://music.163.com/#/my/m/music/playlist?id=439913085) 



## 实现

此次总共导入了两个歌单，一个是[「Discovery Weekly」](http://music.163.com/#/my/m/music/playlist?id=439913085)一个是[「Liked from radio」](http://music.163.com/#/my/m/music/playlist?id=439868832),总体效果还不错。整个过程总共三步，归纳起来第一步使用在线工具得到csv格式的歌单，第二步使用python一键转换，第三步登录网易云音乐导入歌单，熟练之后，导入到网易云音乐一个歌单可以在一分钟之内完成(代码你都写好了，只需要Run一下就OK)。











 






