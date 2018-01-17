# Mind-Master-assistant-through-tesseract
#Stay Simple, Live young 口-口

python新人，上手5d后完成的第一个项目，留念.

思路:
  -题目识别: pytesseract + 手动预设识别区域 + 多线程
  -答案查找: 上网扒问答平台统计词频.
  -图片获取以及答案选择: Android ADB

配置:
  -mi-5手机,微信6.6.1版
  -tesseract
  -ADB
  -python以及一堆包
运行:
  -自行修改__init__的box参数,要与题目和答案对应.
  -运行__init__
  -题目出现时按enter(不必等待答案).

效果:
  -所需时间:6秒, 50%取决于tesseract的识别效率.
  -正确率:
    -查询类问题:高
    -逻辑类问题:低
