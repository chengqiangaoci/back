启动:git init
git add . 
git commit -m ""
git status

详细查看修改内容：git diff "文件名"

可以看到该文件相关的commit记录 git log -- filename

查看某次提交中的某个文件变化 git show id filename



可以显示该文件每次提交的diff git log -p filename

详细查看提交历史：git log 
git log --pretty==oneline

回溯某次：git reset --hard "六位数"

查询历史命令：git reflog

删除文件：git rm "文件名"

添加远程库:git remote add origin ""
git push -u origin master
删除远程库 git remote rm origin

克隆：git clone ""

查看分支git branch
创建分支git branch <name>
切换分支 git checkout <name>
创建并切换 git checkout -b <name>
合并某分支到当前分支 git merge <name>
删除分支 git branch -d <name>
删除没有被合并过的分支 git branch -D <name>

储存当前工作 git stash
回到之前储存的工作 git stash pop


查看远程库信息(第二个是详细查看)  git remote / git remote -v

抓取分支:在远程克隆其他github时候一定要记得在己方添加对方的SSH key
同时只能查看到本地的master分支，因此如果要在dev分支上开发
就必须创建远程origin的dev分支到本地：git checkout -b dev origin/dev
然后在本地git add   git commit后，再将dev分支push到远程 git push origin dev
