# "如何在Rstudio中运用Git进行版本控制"
### Author: "Yifei Wan"
### Date: "March 28 2018"

`Warning:以下内容基于笔者本人使用的Win10操作系统编写。`

## 前言
R语言是进行生物信息学数据分析工作的主要计算机语言之一（加上"**之一**"免得被Python缠住脖子），大量的生物信息学包是基于R开发,比如著名的DESeq2。生物信息学工作者（干“干活”的）与实验室的一线研究员（干“湿活”的）都或多或少的会与R接触。编程这种事情嘛，总是免不了时不时要修改下代码什么的。但是如果我某天突然想找回之前被删掉的代码呢应该怎么办呢（行话叫做“滚回，roll back”）？要知道在R中一但保存退出可就没有后悔药可以吃了（和大家使用Excel时完全相同）。这个时候我们就需要请出本文的正神——**版本控制**技术了。

版本控制（version control）是一种记录代码改变过程并加以记录和管理的技术&工程思想，它可以帮我们轻松地归纳整理与可视化出程序“进化”的历史过程，并且在我们提出要求时为我们滚回其中特定的历史阶段。这在多人合作开发的时候尤其有用。版本控制可以避免因为一个人的失误而全局皆损，并且在最短的时间内帮助开发组回到上一步，甚至它还能统计出每个人的工作量。版本控制也可以被当成一个云端数据库用来托管我们繁杂而老旧的项目，这样你就不用担心自己的服务器和工作站上有大量记不起来用途的文件夹了。托管别的东西也可以，比如本文采用的所有图片都托管在GitHub上。如果你想了解更多相关内容可以阅读以下官方文档：
[About Version Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control).

主流的版本控制系统（version control system）有SVN和GitHub等。其中GitHub采用了分布式代码管理的技术，是目前最流行的代码版本控制工具而且是开源和免费的（免费该打引号，免费的数据仓库会处于公开状态，任何人都可以访问，但是只有项目参与者可以提交和修改，对于一般的生信项目这不算事。不空开的私人仓库就要付费）。作为菜鸟的笔者接下来将分享连接Github与Rstudio的方法。本着能用图片说明就不要用文字的原则，本文预计含有大量图片，所以请注意流量消耗。

## 在开始前的准备
1. 安装R语言：如果您没有R应该也不会点进本文来……不过还是奉上链接[R language](https://www.r-project.org/)。
2. 安装Rstudio: Rstudio是R最受欢的集成开发环境（IDE）,提供了成熟的可视化编程界面。而且其界面似乎为数据分析进行过专门的优化，使用MATLAB与Spyder（Python的一款开发环境）进行数据分析的读者一定能发现三者窗口布置非常类似……强烈建议使用Rstudio来取代RGui，大幅提高效率。如果您还没有安装请点击链接然后选择适配操作系统的版本下载：[Rstudio](https://www.rstudio.com/products/RStudio/)。

## 1. Git的安装与配置
接下来我们将会一一步一步地安装和配置Git。只有Git呢？Hub怎么不见了？其实GitHub分为本地仓库（local repository）与远端仓库（remote repository）两部分，计算机上的代码会先提交到本地再推送到远端。其中本地的管理工具被叫做Git,远端的就是GitHub的网站，统称Github。
### 1.1 GitHub 申请账户
对于远端其实比较简单，登陆[GitHub](https://github.com/)的网站注册一个账号就可以了，这个不多说。
### 1.2 下载和安装Git
点击链接后选择合适的版本下载：[Git download](https://git-scm.com/downloads)。
安装时最好不要修改默认路径，因为Rstudio会很死脑筋地来这个路径搜索Git。
在安装过程中会问你需要使用哪种命令行？其实用`Git Bash only`已经够了，但是因为Win10幺蛾子多（我忍不住说了实话）所以还是选择`CMD + Git Bash(Unix命令行）`的混搭方式：
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/git%20setup.PNG)

其他选项都用默认就可以了。可以让程序自己创建一个快捷方式，将来会方便些。
### 1.3 建立本地的R项目
在运用版本控制的过程中有两种基本的剧本，第一种（剧本A）就是先在本地建立了项目进行开发，之后再在远端建立仓库，最后将已经存在的项目推送到远端。这很常见，有的时候在旅途中突然有个点子立马开始码代码，但是没有wifi无法推送，就等到到达之后再建立远端仓库进行提交。但是这种方法会遇到一些问题，所以将是本文讨论重点。第二种剧本（剧本B）略有差异，是先建立了远端空仓库，然后将远端仓库与Rstudio连接起来建立项目。换言之，建立项目时远端仓库已经存在。而且Rstudio会弹出窗口询问你的远端仓库地址。Rstudio会把远端的仓库（如果不是空仓库还会包括内容）克隆到了本地（执行这一操作的命令就是`clone`）。我们先讨论较为复杂的剧本A：
+ 打开Rstudio在菜单中选择建立新项目：
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/new%20project.PNG)

+ 然后选择`New Directory`:

![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/new%20project2.PNG)

+ 接下来当然是`New Project`：

![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/new%20project3.PNG)

+ 最后设定项目的名称，记得把建立本地仓库的复选框打上勾:

![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/new%20project4.PNG)

+ 点击菜单栏`Tools` -> `Version Control` -> `Project Setup`，然后在弹出窗口中选择`Git/svn`。最后将下拉菜单设置为`Git`再点击`Yes`就好。Rstudio会自动重启，不用担心：

![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/Git_SVN.PNG)

此时如果你在Rstudio右上角的窗口中发现多了一个`Git`选项，这就说明你设置成功了：
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/Git%20panel.PNG)

到此，R本地项目的建立完成。为了接下来的调试，我们可以在此项目下建立一个新的R脚本`test.R`并且写入一句批注：
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/r1.PNG)


### 1.4 建立远端仓库
既然已经有了本地项目了，现在就该着手建立远端仓库了。
首先登陆Github账户，选择`Start a project`,然后出现如下页面：
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/test%20repo%201.PNG)

输入你想要的项目名称和描述（可选），注意在下方有一个打钩的选项询问是否初始化一个`README.md`文件，那其实就是一个自述文件，你可以在其中输入对项目的详细说明免得将来忘记（和你下载游戏补丁时遇到的`读我.txt`是一类东西，不过是使用了Markdown格式，本文原稿也是Markdown格式）。你之后也可以手动创建这个文件。点击`Create repository`完成创建远端代码仓库。

### 1.5 将远端地址添加到本地
Rstudio和Git还没有智能到我们建立了GitHub远端就自动知道的地步（就算能我也一定让Firewall把他们ban掉，太吓人了），所以我们需要人工的将远端地址添加到本地的记录中。本地的Git的配置有两种方式，一个是使用Rstudio内部的Git菜单和控制台，对应的是CMD命令行。我实在不喜欢CMD的冗长显示（其实是因为我记不住命令），所以选择第二种方式使用`Git bash`，对应的是Unix/Linux命令行。有时遇到异常或错误`Git bash`会提示你可以尝试的命令，只需要复制粘贴就行，很贴心。用刚才安装时建立的快捷方式打开`Git bash`。
+ 首先先切换到项目所在目录，输入命令cd与目录地址：
```
cd 'f:/R workspace/test'
```
用单引号引起路径是告诉控制台路径是一个整体，不然会被误认为是多个独立的参数而报错（因为我的路径包含了一个空格）。单引号或双引号都是可以的。需要指出因为是Unix的命令行所以使用了正斜杠`/`，如果你是直接从Windows中复制的路径请记得把反斜杠`\`换掉。
成功后会显示如下：
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/change%20folder.PNG)

在用户名后会出现工作目录的路径并且有一个蓝色的`(master)`，这其实是提示你当前的文件夹内是你程序的主干（暗示在将来的发展中可能会有其他分支）。同时这也告知你Git已经成功初始化了此项目的配置文件开始跟踪这个项目（Git：放心，我盯着了）。如果没有这个`(master)`出现，说明上面的建立项目的过程可能有误，请重来，或手工输入初始化命令：
```
git init
```
+ 使用如下命令查看当前链接的远端仓库：
```
git remote -v
```
此时返回的应该是空白才对，因为我们还没有连接远程仓库：
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/check%20remote1.PNG)

+ 打开GitHub上的远端仓库，可以看到一个绿色按钮`clone or download`，点击并复制弹出窗口中的远端地址：
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/repo%20clone.PNG)

+ 在控制台中输入添加远端地址的命令，记得将你的地址粘贴在命令后。在Unix中复制是`Ctrl + insert`，粘贴是`shift + insert`：
```
git remote add origin https://github.com/WanYifei/test.git ## 地址换成您自己的
```
然后再次检查当前的链接设置，确认是否添加远端成功：
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/add%20remote.PNG)

可以看到返回的结果中有fetch（接收）与push（推送）两个地址。当本地从远端下载数据使用前者，向远端发送数据使用后者，但是其实两个地址是相同的。

### 1.6 将远端数据拉取到本地 
现在远端已经添加成功，我们需要对本地和远端进行同步，首先应该把远端数据拉到本地来。还记得上文提到的`README.md`文件吗，此文件当就前只存在于远端，而本地没有。所以使用pull（拉取）命令将整个远端拷贝到本地进行合并（merge）。程序只会选出在远、本两端存在差异的文件进行传输，所以在文件很多的时候也不会耗费太多时间：
```
git pull origin master
```

但是有时候会**发生错误**，因为Git无法判断本地与远端的数据是否存在历史联系。此时添加如下参数进行拉取和合并：
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/git%20pull%20unrelated.PNG)

因为这会对数据进行覆盖，所以被要求编写一个备注说明情况方便将来检查。这里会自动进入一个Vim文本编辑器内部。Vim可以被视为是Unix/Linux的Word，它有命令模式、输入模式、底线命令模式三种状态。不多说，直接开始操作：

+ 当前Vim处于命令模式下：

![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/vim1.PNG)

+ 按下字母`i`进入输入模式，屏幕底端会出现<insert>或<插入>（专门调出中文操作系统让大家看）：

![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/vim2.PNG)

+ 现在就可以像编辑txt一样修改上方黄字为所需备注，然后Esc返回命令模式。按下冒号`:`进入底线命令模式，输入'wq'回车（意为保存与退出）：

![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/vim3.PNG)

+ 控制台反馈显示`README.md`被成功拉取合并到本地：

![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/merge.PNG)

此时如果打开项目的工作目录会发现`README.md`已经赫然在列。

### 1.7 将工作目录内的文件提交本地仓库

简要介绍下Git在本地的三层结构：
1. 工作目录；
2. 暂存区；
3. 本地代码仓库。

工作目录就是正在进行开发的R程序所在的文件夹。工作目录中的文件在被加入(add）暂存区前被称为“未暂存”（not staged）。暂存区顾名思义是暂时保存代码等待进一步处理或批注的区域，是Git区别于其他版本控制程序的一个特点，有缓冲作用。处于其中的文件被称为暂存的（staged）。暂存数据可以进一步被提交（commit）到本地代码仓库。我们将通过如下步骤来将工作目录中新创建的`test.R`文件提交到本地仓库：
+ 在Rstudio的git窗口中将需要提交到暂存区的文件打钩，文件状态栏（status）出现`A`表示添加（add）成功：
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/stage.PNG)

+ 点击git窗口中的`Commit`按钮进入提交窗口，此时需要在commit message栏中输入提交备注，虽然不写也行，但是推荐在实际工作中认真填写，对于管理项目帮助很大。填完后点击`Commit`完成提交：
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/commit.PNG)
如果提交成功，git窗口中对应的文件条目应该会消失。此时`test.R`就已经处于本地代码库了（committed）。**注意**：提交的其实是文件的一个快照副本而非文件本身，所以工作目录中的对应文件不会消失。

### 1.9 推送本地数据到远端
此时git窗口的向上的箭头按钮"push"已经亮起，说明可以使用，但是为了排除可能的故障我们会用命令行而非图形界面完成推送。与pull相对的push命令可以将本地仓库中的文件发送到远端，程序会自动比较两地文件版本的差异并且加以记录：
```
git push
```
Git在开始推送之前会询问Github用户名与邮箱，因为Github远端在接收本地数据时会记录提交人的身份，邮箱地址被当作ID使用:

![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/push%201st%20username.PNG)

当然密码也是少不了的：

![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/require%20password.PNG)

这么简单就完了？当然不是，推送失败了：
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/git%20push%20fatal.PNG)

究其原因还是程序无法判断本地和远端的历史先后，不知道以谁作为上级分支。所以需要手动为其添加设定，告知程序两者其实是同一个东西，合并就好。应当使用的设置命令已经被bash贴心地给出在反馈中，直接复制粘贴。会有一个窗口弹出来询问你的Github密码：
```
git push --set--upstream origin master
```
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/push%20password.PNG)

此时显示提交成功！
到GitHub的页面上再去确认一下，可以看到`test.R`已经存在于远端了！我们已经成功完成了A剧本下的Git + Rstudio配置！之后不喜欢命令行的同学就可以完全依靠Rstudio中git窗口下的按钮进行简单快速的操作了。
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/push%20success1.PNG)

## 2. 项目文件修改与安全设置
本章节进一步介绍文件的推送和Git的一些全局设置，方便大家使用Git和理解Git的工作方式。为了能够使执行更加清晰，这里继续使用命令行而非图形界面进行操作。
### 2.1 文件修改后的提交
既然是开发中的项目那么频繁的修改就很难避免，在修改后就会需要再次提交与推送。让我们修改一下工作目录中的`test.R`看看会发生什么。在`test.R`中随便敲几个字保存。回到`Git bash`，使用status命令查看本地git监视下的文件状态变化：
```
git status
```
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/git%20status.PNG)


反馈信息中第一行红色的部分显示`test.R`遭到修改（modified），其上方的白字指出修改后没有添加到暂存区（not staged）。如果回到Rstudio中也可以看见`Status`中`test.R`前显示了一个大写的M。

![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/rmodif.PNG)

用上文的方法或命令`add`添加修改后的文件,再次检查状态：
```
git add test.R
```
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/R%20status%202.PNG)

此时反馈变为绿色并告知已经做好提交准备。

然后输入commit命令将其提交到本地库，在参数`-m`后输入文件名与备注，备注多于一个单词需要使用引号：
```
git commit -m test.R 'test password' ## test password是随手写的备注
```
之后的推送过程就会与上文介绍的相同，完成后可以在网页上看到文件与备注都发生了改变

![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/push%20success2.PNG)

### 2.2 开启安全设置
在多次提交文件的过程中，git反复要求用户提供账号密码，这就尴尬了。难道每次提交都要输入账号密码吗？当然不是，我们可以将账号、邮箱、密码都保存在本地，git会自动的调用他们。在本例子中笔者将用户名与邮箱设置为全局变量（Git bash默认推荐的设置方法）。当然也可以设置为局部的，大家可以另行谷歌。

+ 设置全局用户名：

```
git config --global user.name "XXX" ## XXX请换为您的用户名
```
+ 设置邮箱:
```
git config --global user.email "XXX" ## XXX
```
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/set%20username%20and%20email.PNG)

+ 设置完成后需要检查一下全局设置清单，确认是否保存成功：
```
git config --global --list
```
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/check%20username.PNG)

如上图，用户名和邮箱出现在列表中说明设置成功。

+ 设置密码：
密码的设置与用户名不同（毕竟最重要嘛）。有多种方式可以保存或缓冲密码。对于最新的windows版本Git，官方推荐使用credential.helper下的manager进行密码管理。密码会被作为秘钥保存在windows系统的秘钥管理系统而非普通地保存在文本中：
```
git config --global credential.helper manager
````
在下次提交时输入密码后密码就会被记录保存，之后就不再需要反复输入了。
+ 设置好之后再次检查一些全局列表确认密码管理已经打开：
![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/check%20password.PNG)

`credential.helper = manager`显示已经成功启动密码管理。

### 3. 剧本B条件下的配置
剧本B是较为简单的情况，有了上文剧本A的操作经验可以很快完成设置。
首先建立远端仓库。然后再打开Rstudio建立项目。
+ 这次请选择第三项`Version control`：

![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/new%20project2.PNG)

+  然后选择Git：

！[img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/clone/new%20project%20local.PNG)

+ 最后将远端的地址粘贴到对话框中，项目名会自动出现，点击`Create project`将远端克隆到本地：

![img](https://raw.githubusercontent.com/Wan-Yifei/BioEng_Bioinformatics/master/Git%20with%20Rstudio/clone/new%20project%20local%20git.PNG)

此刻基本的配置就已经完成，可以自由进行pull或Push等操作了！可以根据使用需要决定是否进行安全设置。是不是比剧本A简单多了？所以如果可以请选择以这种方式建立项目。

## 尾声
上面絮絮叨叨了这么多，初步的介绍了Git与Rstudio结合进行版本控制的方法，希望能给您带来些许的收获。生物信息学作为一个交叉学科涉及面极其广阔，需要掌握大量的知识和技能，而计算机科学理论与计算机工程技巧毫无疑问是其中重要一环。笔者作为初出茅庐的新人也在不断学习当中。希望能有更多机会与大家交流，共同进步。如果您对此文有什么意见或建议欢迎留言或发送邮件交流。

最后再次感谢阅读！也欢迎您访问BioEng查阅更多生命科学相关文章。





