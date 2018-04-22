'''工具包'''
# 导入包区
import os




class Until():
	#判断参数是否是空
	def space(self,*k):
		for key in k:
			if key=="" or key==None or " " in k:
				return "有的参数是空-Until-space"
				


	# 大小写转换
	def toLower(self,case):
		if self.space(case)=="有的参数是空-Until-space":
			print("有的参数是空-Until-toLower")
			return "有的参数是空-Until-toLower"
		return case.lower()

	def toUpper(self,case):
		if self.space(case)=="有的参数是空-Until-space":
			print("有的参数是空-Until-toUpper")
			return "有的参数是空-Until-toUpper"
		return case.upper()


# 文件操作区
	def getcwd(self):
		return os.getcwd()


	def chdir(self,path):
		if self.space(path)=="有的参数是空-Until-space":
			print("有的参数是空-Until-chdir")
			return "有的参数是空-Until-chdir"
		os.chdir(path)
		return "OK(Until-chdir)"

	#进入上一级父目录
	def predir(self):
		dir=os.getcwd()
		dirlist=dir.split("/")
		le=len(dirlist)
		newpath=""
		if le>=2:
			for i in range(0,le-1):#由于括号后面的是不能取到的，所以不是le-2
				newpath=newpath+"/"+dirlist[i]
				if i==le-2:
					os.chdir(newpath)
		return "OK(Until-predir)"

	#进入子目录
	def childir(self,path):
		if self.space(path)=="有的参数是空-Until-space":
			print("有的参数是空-Until-chdir")
			return "有的参数是空-Until-chdir"
		dir=os.getcwd()
		os.chdir(dir+"/"+path)
		return "OK(Until-childir)"

	#创建子目录
	def mkdir(self,filename,path=os.getcwd()):#默认的带惨的只能放在后面
		if self.space(filename)=="有的参数是空-Until-space":
			print("有的参数是空-Until-mkdir")
			return "有的参数是空-Until-mkdir"
		t=os.path.exists(path+"/"+filename)
		if not t:
			olddir=os.getcwd()
			os.chdir(path)
			os.mkdir(filename)
			os.chdir(olddir)
			return "OK(Until-mkdir)"
		else:
			return "Fail-existed(Until-mkdir)"

    # 重新命名
	def rename(self,oldname,newname):
		if self.space(oldname,newname)=="有的参数是空-Until-space":
			print("有的参数是空-Until-rename")
			return "有的参数是空-Until-rename"

		cw=os.getcwd()
		splitoldname=oldname.split("/")
		link=""
		for i in range(0,len(splitoldname)-1):
			link=link+splitoldname[i]+"/"

		if cw ==link:
			if os.path.exists(oldname):
				os.rename(oldname,newname)
			else:
				return "Fiale-unexiste(Until-rename1)"
		else:
			#如果没有在这工作目录中则要切换路径后进行查询
			if os.path.exists(oldname):
				#只能是目录对目录，名称对名称，否则在当前目录中创建
				#指定的目录中那个文件删除掉
				os.rename(oldname,link+newname)	
			else:
				return "Faile-unexiste(Until-rename2)"
		return "OK(Until-rename)"


ty=Until()
print(ty.rename("/Users/TH/Desktop/python工具包/h10","hu"))












		