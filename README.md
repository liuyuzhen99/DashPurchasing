# Dash Purchasing

## Business Background业务背景
in Purchasing department, different colleagues talk with different suppliers to check the parts.
there's questionnaire template (excel) which include many questions for them to fill in.
they store the questionnaire in sharepoint, however the files is too much, it's hard for coordinator to check the status.
So the coordinator and manager need a dashboard for general information of the status.
采购部门中不同的同事管理不同的供应商和零件。
它们用excel模版问卷调研回答问题。
这些excel存储在sharepoint中，但是文件过多导致协调员无法跟踪进度。
所以协调员与经理需要一个仪表盘来展示这些零件的基本进度信息。

## Function功能
upload three files to the app:
1. TEVON excel upload: it defines target ready time for different parts定义零件的可用时间
2. part description upload: it descripe sharepoint folder structure描述sharepoint文件目录结构
3. milestone json upload: it descripe big milestones描述里程碑节点

根据上传文件和预先定义好的sharepoint路径，产生仪表盘展示对应信息.同时支持在仪表盘中输入信息并导出

1. app.py 主函数，展示home和Dashboard链接
2. pages: 页面函数
3. datas：读取数据函数
4. plotlys：处理数据并展示

## Business Process flow diagram
![Business Process Flow Diagram](https://github.com/user-attachments/assets/7e3a6e59-f678-40e0-8fb6-661fbeebf4f3)


## context & scope diagram
![context   Scope Diagram](https://github.com/user-attachments/assets/51bed048-c747-438b-b16a-e973c6adb1fd)


## pages
![homepage](https://github.com/user-attachments/assets/a21265f5-dd5b-4a80-a4d8-26d31245679b)
<img width="1376" alt="Snipaste_2025-06-14_18-35-36" src="https://github.com/user-attachments/assets/d92f74b0-d452-4c3e-bd3e-910d32e4366d" />
<img width="1795" alt="image" src="https://github.com/user-attachments/assets/809e4680-4db7-4e62-8111-de2e803a2a17" />

