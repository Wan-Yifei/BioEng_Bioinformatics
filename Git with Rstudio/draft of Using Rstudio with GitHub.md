# "如何在Rstudio中运用Git进行版本控制"
### Author: "Yifei Wan"
### Date: "March 28 2018"

**Warning**`:以下内容基于笔者本人使用的Win10操作系统编写。`

## 前言
R语言是进行生物信息学数据分析工作的主要计算机语言之一（加上"**之一**"免得被Python缠住脖子），大量的生物信息学包基于R被开发,比如著名的DESeq2。生物信息学工作者（干“干活”的）乃至实验室的一线研究员（干“湿活”的）都或多或少的会与R接触。编程这种事情嘛，总是免不了时不时要修改下代码什么的。但是如果我某天突然想找回之前被删掉的代码呢应该怎么办呢（行话叫做“滚回，roll back”）？要知道在R中一但保存退出可就没有后悔药可以吃了（和大家使用Excel时完全相同）。这个时候我们就需要请出本文的正神——**版本控制**技术了。

版本控制（version control）是一种记录代码改变过程并加以记录和管理的技术&工程思想，它可以帮我们轻松地归纳整理与可视化出程序“进化”的历史过程，并且在我们提出要求时为我们滚回其中特定的历史阶段。这在多人合作开发的时候尤其有用。版本控制可以避免因为一个人的失误而全局皆损，并且在最短的时间内帮助开发组回到上一步，甚至它还能统计出每个人的工作量。版本控制也可以被当成一个云端数据库用来托管我们繁杂而老旧的项目，这样你就不用担心自己的服务器和工作站上有大量记不起来用途的文件夹了。托管别的东西也可以，比如本文采用的所有图片都托管在GitHub上。如果你想了解更多相关内容可以阅读以下官方文档：
[About Version Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control).

主流的版本控制系统（version control system）有SVN和GitHub等。其中GitHub采用了分布式代码管理的技术，是目前最流行的代码版本控制工具而且是开源和免费的（免费其实该打引号，免费的数据仓库会处于公开状态，任何人都可以访问，但是只有项目参与者可以提交和修改，对于一般的生信项目这不算事。不空开的私人仓库就要付费）。作为菜鸟的笔者接下来将对Github与Rstudio结合的方法进行分享。本着能用图片说明就不要用文字的原则，本文预计含有大量图片，所以请注意流量消耗。

## 在开始前的准备
1. 安装R语言：如果您没有R应该也不会点进本文来……不过还是奉上链接[R language](https://www.r-project.org/)。
2. 安装Rstudio: Rstudio是R最受欢的集成开发环境（IDE）,提供了成熟的可视化编程界面。而且其界面似乎为数据分析进行过专门的优化，使用MATLAB与Spyder（Python的一款开发环境）进行数据分析的读者一定能发现三者窗口布置非常类似……强烈建议使用Rstudio来取代RGui，大幅提高效率。如果您还没有安装请点击然后选择适配操作系统的版本下载：[Rstudio](https://www.rstudio.com/products/RStudio/)。

## 1. Git的安装与配置
接下来我们将会一一步一步地安装和配置Git。只有Git？Hub怎么不见了？其实GitHub分为本地仓库（local repository）与远端仓库（remote repository）两部分，计算机上的代码会先提交到本地再推送到远端。其中本地的管理工具被叫做Git,远端的就是GitHub的网站，统称Github。
### 1.1 GitHub 申请账户
对于远端其实比较简单，登陆[GitHub](https://github.com/)的网站注册一个账号就可以了，这个不多说。
### 1.2 下载和安装Git
点击链接后选择合适的版本下载：[Git download](https://git-scm.com/downloads)。
安装时最好不要修改默认路径，因为Rstudio会很死脑筋地来这个路径搜索Git。
在安装过程中会问你需要使用哪种命令行？其实用`Git Bash only`已经够了，但是因为Win10幺蛾子多（我忍不住说了实话）所以还是选择`CMD + Git Bash(Unix命令行）`的混搭方式：
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/git%20setup.PNG)

其他选项都用默认就可以了。可以让程序自己创建一个快捷方式，将来会方便些。
### 1.3 建立本地的R项目
在运用版本控制的过程中有两种基本的剧本，第一种（剧本A）就是先在本地建立了开发项目进行开发，之后再在远端建立仓库，最后将已经存在的项目推送到远端。这很常见，有的时候在旅途中突然有个点子立马开始码代码，但是没有wifi无法推送，就等到到达之后再建立远端仓库进行提交。但是这种方法会遇到一些问题，所以也是本文讨论重点。第二种剧本（剧本B）略有差异，是先去建立了远端空仓库，然后将仓库与配置了Git的Rstudio连接起来建立项目。换言之，建立项目时远端仓库已经存在而且Rstudio会弹出窗口询问你的远端仓库地址。我们先讨论较为复杂第剧本A：
+ 打开Rstudio在菜单中选择建立新项目：
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/new%20project.PNG)

+ 然后选择`New Directory`:

![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/new%20project2.PNG)

+ 接下来当然是`New Project`：

![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/new%20project3.PNG)

+ 最后设定项目的名称:

![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/new%20project4.PNG)

到此，R本地项目的建立完成。为了接下来的调试，我们可以在此项目下建立一个新的R脚本`test.R`并且写入一句批注：
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/r1.PNG)

### 1.4 建立远端仓库
既然已经有了本地项目了，现在就该着手建立远端仓库了。
首先登陆Github账户，选择`Start a project`,然后出现如下页面：
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/test%20repo%201.PNG)

输入你想要的项目名称和描述（可选），注意在下方有一个打钩的选项询问是否初始化一个`README.md`文件，那其实就是一个自述文件，你可以在其中输入对项目的详细说明面得将来忘记（和你下载游戏补丁时遇到的`读我.txt`是一类东西，不过是使用了Markdown格式，本文原稿也是Markdown格式）。你之后也手动创建这个文件。点击`Create repository`完成创建远端代码仓库。

### 1.5 将远端地址添加到本地
Rstudio和Git还没有智能到我们建立了GitHub远端就自动知道的地步（就算能我也一定让Firewall把他们ban掉，太吓人了），所以我们需要人工的将远端地址添加到远程的记录中。本地的Git的配置有两种方式，一个是使用Rstudio内部的Git菜单和控制台，对应的是CMD命令行。我实在不喜欢CMD的冗长显示（其实是因为我记不住命令），所以选择第二种方式使用`Git bash`，对应的是Unix/Linux命令行。有时遇到异常或错误，`Git bash`会提示你可以尝试的命令，只需要复制粘贴就行，很贴心。用刚才安装时建立的快捷方式打开`Git bash`。
+ 





