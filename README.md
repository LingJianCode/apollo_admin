由于携程apollo权限修改不方便，我又不懂java代码，所以只好直接从数据库入手操作用户权限问题。
#安装
1.先决条件apollo的ApolloConfigDB_pro库和ApolloPortalDB需要在同一个mysql实例上，在views中使用了跨库sql查询
2.python3环境
3.pip install -r requirements.txt 
4.python manage.py runserver 0.0.0.0:8888
#使用
##用户+namespace权限查询和修改直接访问
http://127.0.0.1:8888/permission/display/
##用户所有权限查询和修改
http://127.0.0.1:8888/apollo/show/,启动apollo是你想查看和修改的用户的登录id
通过勾选和取消勾选来添加和取消权限
