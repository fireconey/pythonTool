'''工具包'''
# 导入包区
import os


class Until():
	#判断参数是否是空
	def space(self,*k):
		for key in k:
			if key=="" or key==None or " " in k:
				return "error:有的参数是空-Until-space"


	# path：直接传入一个路径或文件，如果以斜线开头表示别的路径
	#不是斜线开头表示在当前目录下的路径或文件
	def chkwd(self,path):
		if self.space(path)=="error:有的参数是空-Until-space":
			print("error:有的参数是空(Until-chkwd)")
			return "error:有的参数是空(Until-chkwd)"
		pathsplite=path.split("/")
		cw=os.getcwd()
		if len(pathsplite[0])==0:
			if os.path.exists(path):
				return path
			else:
				print("error:没有此路径-%s-(Until-chkwd()-1)" %path)
				return
		else:
			if os.path.exists(cw+"/"+path):
				return cw+"/"+path
			else:
				print("error:没有此路径-%s-(Until-chkwd()-2)" %(cw+"/"+path))
				return

				


	# 大小写转换
	def toLower(self,case):
		if self.space(case)=="error:有的参数是空-Until-space":
			print("error:有的参数是空-Until-toLower")
			return "error:有的参数是空-Until-toLower"
		return case.lower()

	def toUpper(self,case):
		if self.space(case)=="error:有的参数是空-Until-space":
			print("error:有的参数是空-Until-toUpper")
			return "error:有的参数是空-Until-toUpper"
		return case.upper()


# 文件操作区
	def getcwd(self):
		return os.getcwd()


	def chdir(self,path):
		if self.space(path)=="error:有的参数是空-Until-space":
			print("error:有的参数是空-Until-chdir")
			return "error:有的参数是空-Until-chdir"
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

	#进入下一级子目录
	#path:子目录的名称
	def childir(self,path):
		if self.space(path)=="error:有的参数是空-Until-space":
			print("error:有的参数是空-Until-chdir")
			return "error:有的参数是空-Until-chdir"
		dir=os.getcwd()
		if os.path.exists(dir+"/"+path):
			os.chdir(dir+"/"+path)
			return "OK(Until-childir)"
		else:
			print ("error:没有此路径-%s-(until-childir)"  %(dir+"/"+path))
			return 

	#创建子目录
	#filename：要创建的文件的名称
	#path：文件存放的目录，当没有指定是默认是当前的目录。
	def mkdir(self,filename,path=os.getcwd()):#默认的带惨的只能放在后面
		if self.space(filename)=="error:有的参数是空-Until-space":
			print("error:有的参数是空-Until-mkdir")
			return "error:有的参数是空-Until-mkdir"
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
    #oldname：可以是带路径的名称也可以只是一个名称（默认在当前目录中）
    #newname：只是一个名称所以要
	def rename(self,oldname,newname):
		if self.space(oldname,newname)=="error:有的参数是空-Until-space":
			print("error:有的参数是空-Until-rename")
			return "error:有的参数是空-Until-rename"

		cw=os.getcwd()
		splitoldname=oldname.split("/")
		link=""
		for i in range(0,len(splitoldname)-1):
			link=link+splitoldname[i]+"/"

		if cw ==link:
			if os.path.exists(oldname):
				os.rename(oldname,newname)
			else:
				return "error:Fiale-unexiste(Until-rename1)"
		else:
			#如果没有在这工作目录中则要切换路径后进行查询
			if os.path.exists(oldname):
				#只能是目录对目录，名称对名称，否则在当前目录中创建
				#指定的目录中那个文件删除掉
				os.rename(oldname,link+newname)	
			else:
				return "error:Faile-unexiste(Until-rename2)"
		return "OK(Until-rename)"


	#进行文件的读写
	#filename：文件名称
	def read(self,filename):
		if self.space(filename)=="error:有的参数是空-Until-space":
			print("error:有的参数是空(Until-read)")
			return "error:有的参数是空(Until-read)"

		t=self.chkwd(filename)
		if not t==None:

			with open(t,"r",encoding="utf-8") as r:
				file=r.read()
				return file

	#进行文件的写
	#filename:文件的名称
	#content:要写入的内容
	def write(self,filename,content):
		if self.space(filename)=="error:有的参数是空-Until-space":
			print("error:有的参数是空(Until-read)")
			return "error:有的参数是空(Until-read)"

		t=self.chkwd(filename)
		if not t==None:
			with open(t,"w",encoding="utf-8") as r:
				file=r.write(content)
				return "OK:write(Until-write)"





ty=Until()
print(ty.read("/Users/TH/Desktop/python工具包/test.py"))

print(os.getcwd())
ty.predir()
ty.predir()
ty.predir()
print(os.getcwd())












		