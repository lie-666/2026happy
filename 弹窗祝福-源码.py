import tkinter as tk
import random
import threading
import time

# 全局变量：跟踪打开的弹窗数量
open_windows_count = 0
open_windows_lock = threading.Lock()

def on_window_close(window):
    global open_windows_count
    try:
        window.destroy()
    finally:
        with open_windows_lock:
            open_windows_count -= 1
            if open_windows_count <= 0:
                root.quit()

MACARON_COLORS = [
    '#FFB7C5',  # 樱花粉
    '#FFDAC1',  # 奶油橙
    '#E2F0CB',  # 薄荷绿
    '#B5EAD7',  # 浅水绿
    '#C7CEEA',  # 淡紫色
    '#FF9AA2',  # 珊瑚粉
    '#FFB7B2',  # 浅珊瑚
    '#FFDAC1',  # 杏色
    '#E2F0D9',  # 淡绿色
    '#B5EAD7',  # 青绿色
    '#C7CEEA',  # 淡蓝色
    '#F8B7D3',  # 粉红色
    '#D5A6BD',  # 紫粉色
    '#9FD8CB',  # 蓝绿色
    '#B19CD9',  # 淡紫色
]

BLESSINGS = [
    "新年快乐",
    "万事如意",
    "恭喜发财",
    "大吉大利",
    "福气满满",
    "心想事成",
    "步步高升",
    "阖家欢乐",
    "幸福安康",
    "财运亨通",
    "财源广进",
    "笑口常开",
    "好运连连",
    "吉祥如意",
    "福星高照",
    "身体健康",
    "事业有成",
    "一帆风顺",
    "家庭和睦",
    "幸福美满",
    "五福临门",
    "六六大顺",
    "岁岁平安",
    "年年有余",
    "金玉满堂",
    "花开富贵",
    "喜气洋洋",
    "万事顺心",
    "福如东海",
    "寿比南山",
    "春风得意",
    "前程似锦",
    "瑞气盈门",
    "喜气临门",
    "龙年吉祥",
    "大展宏图",
    "福禄双全",
    "喜气洋洋",
    "飞黄腾达",
    "鹏程万里",
    "万事顺遂",
    "福满乾坤",
    "喜从天降",
    "龙凤呈祥",
    "财源滚滚",
    "好运不断",
    "开心快乐",
    "心旷神怡",
    "笑逐颜开",
    "顺风顺水",
    "顺心顺意",
    "幸福安康",
    "乐享天伦",
    "福寿康宁",
    "安居乐业",
    "蒸蒸日上",
    "红红火火",
    "团团圆圆",
    "美美满满",
    "平平安安",
    "健健康康",
    "快快乐乐",
    "幸幸福福",
    "日进斗金",
    "生意兴隆",
    "财源茂盛",
    "八面来财",
    "四季发财",
    "福气东来",
    "紫气东来",
    "吉星高照",
    "洪福齐天",
]


def create_popup(index):
    """创建一个弹窗"""
    popup = tk.Toplevel()
    popup.title(f"新年祝福")

    bg_color = random.choice(MACARON_COLORS)
    popup.configure(bg=bg_color)

    width = 320
    height = 120
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    x = random.randint(0, max(0, screen_width - width))
    y = random.randint(0, max(0, screen_height - height))
    popup.geometry(f"{width}x{height}+{x}+{y}")

    title_label = tk.Label(
        popup,
        text="祝你在新的一年：",
        font=("Microsoft YaHei", 10, "bold"),
        bg=bg_color,
        fg="#333333",
        anchor="w"
    )
    title_label.place(x=10, y=5)

    blessing_label = tk.Label(
        popup,
        text=random.choice(BLESSINGS),
        font=("Microsoft YaHei", 24, "bold"),
        bg=bg_color,
        fg="BLACK",
        wraplength=width - 40
    )
    blessing_label.pack(expand=True, fill=tk.BOTH, padx=20, pady=(30, 20))

    popup.attributes('-topmost', True)

    def close_window():
        on_window_close(popup)
    
    popup.protocol("WM_DELETE_WINDOW", close_window)
    popup.after(5000, close_window)  # 5秒后自动关闭

    return popup


def start_popups():
    """启动弹窗序列"""
    def create_popups_thread():
        global open_windows_count
        for i in range(300):
            with open_windows_lock:
                open_windows_count += 1
            root.after(0, lambda idx=i: create_popup(idx))
            # 等待0.005秒
            time.sleep(0.005)

    thread = threading.Thread(target=create_popups_thread)
    thread.daemon = True
    thread.start()


root = tk.Tk()
root.title("新年祝福弹窗")
root.withdraw()  

root.after(100, start_popups) 

root.mainloop()
