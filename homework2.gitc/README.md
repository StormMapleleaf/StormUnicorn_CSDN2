# 江汉大学暑期训练营作业仓库

## 个人信息
|姓名|学号|班级|联系方式|
|---|---|---|---|
|代齐祥|222226201139|计科221|这是秘密|
## 使用说明
### 目录结构
```
.
|--- README.md
|--- homework date
|---|--- question.md #里面放置作业题目
|---|--- answer  # 作业答案
```
### 使用方式
```bash
# 1. clone本仓库
git clone git@gitcode.net:jhun/homework2.git
# 2. 从 master 创建自己的分支
git checkout -b <your-name> #拼音
# 3. 在该文件的README.md中添加自己的信息
# 4. 每天的作业会发布在master分支，对应当天日期的文件夹中 question || question.md
# 5 拉取最新的master分支，merge到自己的分支中
git checkout master
git pull
git checkout <your-name>
git merge master
# 5. 在自己的分支中创建一个文件夹，命名为answer，将自己的答案放在其中
# 6. 提交自己的答案
git add .
git commit -m "your commit message"
git push  
# 首次推送到远程仓库需要加上 -u 参数 
git push -u origin <your-name>
```

### 注意事项
1. 请不要在master分支上提交代码
2. 切换分支之前需要提交当前分支的修改内容
3. 请不要修改其他人的答案，git会看到记录的
4. 请勿上传大文件，如有需要请在.gitignore中添加

