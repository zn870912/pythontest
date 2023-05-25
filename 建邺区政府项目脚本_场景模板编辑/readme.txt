1.安装python环境
	略
2.安装依赖库
	pip install -i "https://pypi.douban.com/simple" -r requirements.txt
3.导出场景模板数据
	select id from mp_cscene_cscene where type=1 and deleted=0;
	并将数据导出至本地，文件名改为“bc_data.csv”，并替换原文件
4.执行程序
	运行run.py