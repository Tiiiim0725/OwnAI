# 基础概念

OwnAI基于OpenClaw概念重新构建框架开发，希望可以通过一些技术路径解决OpenClaw在使用过程中大量消耗上下文在工具Prompts上的问题，降低大模型上下文干扰同时减少不必要的上下文token消耗。

## Agent工具

## System工具-abilities工具

base工具分权限管理，部分base工具需要高权限才能使用

### 文件读写类

1、文件查看

2、文件编辑
编辑文件工具对system内部文件夹有黑名单机制，分权限管理。

3、新建文件

4、删除文件

### 终端命令bash

可以用来执行bash终端命令的工具，设置命令黑名单

### 子代理类

创建新的sub-agent，隔离上下文
通过RAG获取满足功能需要的子代理列表
删除指定子代理

### 浏览器工具

连接浏览器搜索网页获取信息

### agent间通讯工具

用于agent间相互通讯调用

### RAG库工具

可以获取需要的skill使用方法、重要信息、Agent功能查询等。

### 状态Markdown管理工具

可以管理状态md文件

### 权限申请工具

用于向用户申请外部文件夹的编辑权限，这个工具需要用户的实际确认，同时将确认记录保存

### 长期记忆创建工具

### skill技能创建工具

### 数据库工具

## skill工具

外置工具不默认作为Prompt发送给大模型，但是依旧根据权限默认给每一个agent注册对应的外置工具，agent需要从RAG工具中获取适合的工具使用方法才能够使用。
每一个skill文件中包含跟这个skill相关的skill说明文档以及skill-python文件
Agent 可以通过RAG获取相关的skill然后知道怎么去调用这些object-skill

## 状态Markdown

状态Markdown是一种临时的rask处理列表，记录当下任务进度，以及需要被派发的任务。
状态Markdown只能由两个内置Agent来编辑，一个是任务审查Agent、另一个是任务列表创建Agent

## Agent实例

Agent分为system-Agent和sub-Agent两个类型，system-Agent是系统内置的Agent
system-Agent
sub-Agent

## RAG向量工具

我们希望使用RAG来处理所有非必须的信息，例如长期记忆、skill工具及使用方法、Agent间功能查询等。
RAG-base模块
用于被调用，可以创建RAG向量数据、查询RAG数据，所有被向量化的文本都应该有一个结构化的格式用来显示文本来源等
RAG向量库-qdrant-docker
RAG调用工具-API
给大模型工具开放的接口函数

## Message系统

Message系统比较类似于飞书，它可以让每一个Agent有自己的收件箱和发送箱，并且使用history_x.md文件存储起来
发信工具
用于唤醒某一个Agent
群聊系统
同一个项目下的sub-Agent可以查看所有的收发信

## 权限管理系统

外部系统安全
Agent框架默认只能对Agent所在的工作空间进行编辑
用户设置外部系统权限
如果用户需要Agent去对外部的某一个项目目录进行编辑，首先需要调用权限申请工具让用户进行手动确认才能获取权限。
系统内部储存权限管理的配置文件

## 长期记忆系统

## sql数据库系统

## UI模块

## Agent设置组件

## 安装包组件

## 开发注意事项

### 测试脚本

所有的测试脚本都应该放在test/目录下

### 任务计划

所有的任务计划都放在task/目录下，按照任务计划进行开发
