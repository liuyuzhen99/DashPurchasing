# 文件目录结构

## Tevon表格相关
- 从tevon导出的表格获取part的VFF\PVS\0-Serie进度并与milestone比对识别traffic light: tevon_test.py (get_milestone_summary)
- 绘制VFF\PVS\0-Serie milestone Summary: cluster_bar_plot.py
    - create_VFF_milestone_sum
    - create_PVS_milestone_sum
    - create_0Serie_milestone_sum

## milestone相关
- 读取milestone信息： milestone_test.py
- 绘制milestone：data_test.py(table.DataTable)

## QPNI-Status Summary
- 寻找sharepoint文件程序：traversal_file_test.py
- 处理excel文件程序： excel_reader_test.py
- 绘制QPNI-Status: cluster_bar_plot.py(create_ml_sum_cluster_barplot)