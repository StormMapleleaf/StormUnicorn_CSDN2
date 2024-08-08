### 1. 为自己的Linux系统创建用户：cuihua，并设置登录密码

```
sudo adduser cuihua
```

### 2. 在 /opt/目录下创建一个 my.txt 文件，并修改权限为 666

```
sudo touch /opt/my.txt
sudo chmod 666 /opt/my.txt
```

### 3. 切换用户为 cuihua，并使用vim 进入my.txt文件，在文件写入子串 "翠花，上酸菜！"

```
su - cuihua
vim /opt/my.txt
按 i 进入插入模式，输入，按 Esc 退出插入模式，输入:wq
```

### 4. 使用cat命令查看 my.txt 文件内容

```
cat /opt/my.txt
```

### 5. 继续在 /opt/ 目录下创建一个test目录，并将此目录所有者和所属组设为 cuihua 用户

```
sudo mkdir /opt/test
sudo chown cuihua:cuihua /opt/test
```

### 6. 使用 cuihua用户在 /opt/test/ 目录下创建子目录 tt ，并在tt目录中创建 a.txt、b.txt

```
mkdir /opt/test/tt
touch /opt/test/tt/a.txt /opt/test/tt/b.txt
```

### 7. 将 /etc/sysctl.conf 文件 复制到 /opt/test/tt/ 目录下

```
sudo cp /etc/sysctl.conf /opt/test/tt/
```

### 8. 使用vim 进入 /opt/test/tt/sysctl.conf 将 25和28前的 # 去掉

```
vim /opt/test/tt/sysctl.conf
按 x 删除 # ，按 Esc 退出插入模式，输入 :wq!
```

### 9. 将 /opt/test/tt/ 目录 打包成 tt.tar.gz 压缩包

```
tar -czvf /opt/test/tt.tar.gz -C /opt/test tt
```

### 10. 将 /opt/test/tt/ 目录删除后再解压 tt.tar.gz 压缩包

```
rm -r /opt/test/tt
tar -xzvf /opt/test/tt.tar.gz -C /opt/test
```