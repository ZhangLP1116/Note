### 配置成系统服务

1.  在`/usr/lib/systemd/system`目录下添加nginx.service,内容如下:

   ```
   vim /usr/lib/systemd/system/nginx.service
   ```

   ```
   [Unit]
   Description=nginx web service
   Documentation=http://nginx.org/en/docs/
   After=network.target
   
   [Service]
   Type=forking
   PIDFile=/usr/local/nginx/logs/nginx.pid
   ExecStartPre=/usr/local/nginx/sbin/nginx -t -c /usr/local/nginx/conf/nginx.conf
   ExecStart=/usr/local/nginx/sbin/nginx
   ExecReload=/usr/local/nginx/sbin/nginx -s reload
   ExecStop=/usr/local/nginx/sbin/nginx -s stop
   PrivateTmp=true
   
   [Install]
   WantedBy=default.target
   ```

   

2. 添加完成后如果权限有问题需要进行权限设置

   ```
   chmod 755 /usr/lib/systemd/system/nginx.service
   ```

3. 使用系统命令来操作Nginx服务

   ```
   启动: systemctl start nginx
   停止: systemctl stop nginx
   重启: systemctl restart nginx
   重新加载配置文件: systemctl reload nginx
   查看nginx状态: systemctl status nginx
   开机启动: systemctl enable nginx
   ```

   

### 配置nginx环境变量

目的：可以使用nginx直接访问到/usr/local/nginx/sbin/nginx，简化命令使用

1. 修改`/etc/profile`文件

   ```
   vim /etc/profile
   在最后一行添加
   export PATH=$PATH:/usr/local/nginx/sbin
   ```

2. 使之立即生效

   ```
   source /etc/profile
   ```

3. 测试

   ```
   nginx -V
   ```

   

