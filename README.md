# 🎊 新年祝福弹窗程序 (New Year Blessings Popup)

[![版本](https://img.shields.io/badge/版本-v1.0.0-brightgreen)](https://github.com/yourusername/new-year-blessings-popup/releases)
[![许可证](https://img.shields.io/badge/许可证-Apache%202.0-blue)](LICENSE)
[![系统支持](https://img.shields.io/badge/平台-Windows%207+-success)](https://github.com/yourusername/new-year-blessings-popup)
[![大小](https://img.shields.io/badge/文件大小-8MB-lightgrey)]()
[![无需安装](https://img.shields.io/badge/运行方式-绿色免安装-orange)]()

一个已编译为独立可执行文件的新年祝福弹窗程序，无需Python环境即可在Windows系统上直接运行。程序会自动创建大量带有新年祝福的彩色弹窗，营造浓厚的节日氛围。

## 📦 程序信息

### 文件详情
- **文件名**: `新年祝福弹窗.exe`
- **文件大小**: 约8-10MB
- **编译方式**: PyInstaller单文件打包
- **系统要求**: Windows 7/8/10/11 (64位)
- **运行环境**: 完全独立，无需安装Python或任何依赖库

### 安全说明
```
✅ 程序已通过主流杀毒软件扫描
✅ 不包含任何恶意代码或后门
✅ 不收集任何用户信息
✅ 运行后不会残留系统垃圾
✅ 开源代码透明可查
```

## 🚀 一键运行体验

### 下载与运行
1. **下载可执行文件**
   - 从[Release页面](https://github.com/yourusername/new-year-blessings-popup/releases)下载最新版
   - 或直接下载：`新年祝福弹窗.exe`

2. **直接双击运行**
   ```
   📁 下载文件夹
    └── 🎉 新年祝福弹窗.exe   ← 双击此文件
   ```

3. **立即观看效果**
   - 程序启动后，屏幕上将陆续出现300个彩色祝福弹窗
   - 每个弹窗显示5秒后自动关闭
   - 所有弹窗关闭后程序自动退出

### 运行效果预览
```
🖥️ 屏幕将出现如下效果：
1. 首先出现1个主窗口（隐藏状态，仅后台运行）
2. 每隔0.005秒创建一个新祝福弹窗
3. 弹窗随机分布在屏幕各处
4. 每个弹窗使用不同颜色的马卡龙背景
5. 显示随机的新年祝福语
6. 弹窗全部创建完成后，逐个自动关闭
```

## ⚙️ 高级使用方式

### 命令行参数（可选）
```cmd
# 基本用法 - 双击运行或：
新年祝福弹窗.exe

# 查看帮助信息
新年祝福弹窗.exe --help

# 指定弹窗数量（默认300个）
新年祝福弹窗.exe --count 100

# 控制弹窗显示时间（默认5秒）
新年祝福弹窗.exe --duration 3

# 批量创建弹窗的速度（默认0.005秒）
新年祝福弹窗.exe --delay 0.01
```

### 创建桌面快捷方式
1. 右键点击 `新年祝福弹窗.exe`
2. 选择"发送到" → "桌面快捷方式"
3. 重命名快捷方式为"新年祝福"
4. 可右键属性设置图标（使用自带图标资源）

### 添加到开始菜单
```powershell
# 手动添加：
1. 复制exe文件到：C:\ProgramData\Microsoft\Windows\Start Menu\Programs\
2. 或在开始菜单右键选择"更多" → "打开文件位置"
```

## 🎯 应用场景实例

### 场景一：办公室新年惊喜
```
👨‍💼 公司IT部门：
1. 通过内部网络共享exe文件
2. 通知员工在指定时间统一运行
3. 全体员工屏幕同时出现新年祝福
4. 营造集体庆祝氛围
```

### 场景二：家庭聚会娱乐
```
👨‍👩‍👧‍👦 家庭活动：
1. 投影仪连接电脑
2. 全屏运行祝福程序
3. 大屏幕上展示动态祝福效果
4. 作为新年倒计时后的特别节目
```

### 场景三：商场节日装饰
```
🏬 商业场所：
1. 在展示电脑上循环运行
2. 搭配音响播放新年音乐
3. 吸引顾客关注，增加节日气氛
4. 可定制显示公司LOGO或祝福语
```

## 🔧 自定义配置（高级用户）

### 方法一：配置文件定制
创建 `config.ini` 文件与exe同目录：
```ini
[Settings]
window_count = 200
display_duration = 7
creation_delay = 0.003
window_width = 350
window_height = 150

[Appearance]
font_size = 24
title_font_size = 12
always_on_top = true
```

### 方法二：修改源代码重新打包
如需深度定制，需要Python环境重新编译：
```bash
# 1. 克隆源代码
git clone https://github.com/yourusername/new-year-blessings-popup.git

# 2. 修改配置（修改new_year_blessings.py）
# 3. 安装PyInstaller
pip install pyinstaller

# 4. 重新打包
pyinstaller --onefile --windowed --name "新年祝福弹窗" new_year_blessings.py

# 5. 生成新exe在dist文件夹
```

## 📊 性能优化建议

### 对于较旧电脑
```
1. 减少弹窗数量：使用 --count 100 参数
2. 增加创建间隔：使用 --delay 0.02 参数
3. 关闭其他大型程序释放内存
4. 建议在运行前重启explorer.exe
```

### 对于高性能电脑
```
1. 增加弹窗数量：--count 500
2. 加快创建速度：--delay 0.001
3. 延长显示时间：--duration 10
4. 可同时运行多个实例创造叠加效果
```

## ❓ 常见问题解答

### Q1: 运行后弹窗太多卡死了怎么办？
**A**: 等待5-10秒会自动关闭，或按 `Alt+F4` 关闭最上层窗口。建议下次运行时减少弹窗数量。

### Q2: 杀毒软件报告威胁？
**A**: 这是PyInstaller打包程序的误报。可在[Virustotal](https://www.virustotal.com)验证，或添加信任。

### Q3: 如何停止运行中的程序？
**A**: 
1. 按 `Ctrl+Shift+Esc` 打开任务管理器
2. 找到"新年祝福弹窗"进程
3. 右键结束任务

### Q4: 支持macOS或Linux吗？
**A**: 当前exe仅支持Windows。macOS/Linux用户需从源码运行Python脚本。

### Q5: 如何修改祝福语？
**A**: 需要修改源代码重新打包，或等待后续版本支持外部祝福语文件。

## 🆕 更新计划

### 即将推出的功能
- [ ] v1.1: 支持外部祝福语文本文件导入
- [ ] v1.2: 增加背景音乐选项
- [ ] v1.3: 支持自定义颜色主题
- [ ] v1.4: 添加设置图形界面(GUI)
- [ ] v1.5: 支持定时启动功能

## 📝 开源声明

```
项目基于Apache 2.0开源协议发布
源代码仓库：https://github.com/yourusername/new-year-blessings-popup
欢迎提交Issue和Pull Request
```

## 🎁 特别提示

在以下时间运行效果更佳：
- 新年倒计时（12月31日23:59）
- 春节期间拜访亲友时
- 公司年会活动现场
- 任何需要营造节日氛围的场合

---

**祝您使用愉快，新年快乐！🎉**  
如有问题或建议，请访问GitHub仓库提交反馈。
```
