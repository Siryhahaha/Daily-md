import datetime
import os
import winshell

def create_daily_file(folder):

    mouth_folder = folder + "\\" + datetime.datetime.now().strftime("%Y%m")

    # 生成带 .md 扩展名的文件名
    filename = datetime.datetime.now().strftime("%y%m%d") + ".md"
    filepath = os.path.join(mouth_folder, filename)

    # 创建目标文件夹（如果不存在）
    os.makedirs(mouth_folder, exist_ok=True)

    # 仅当文件不存在时创建
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            f.write(f"## {datetime.datetime.now().strftime('%Y-%m-%d')}\n\n### 目标\n\n\n\n### 记录\n\n\n\n### 感悟")
        print(f"{datetime.datetime.now().strftime('%Y-%m-%d')}日志已创建：{filepath}")
    else:
        print(f"今日日志已存在，跳过创建：{filepath}")

    return filepath

def create_new_lnk(target, name):
    shortcut_path = os.path.join(winshell.desktop(), f"{name}.lnk")
    try:
        os.remove(shortcut_path)
    except:
        pass
    shortcut = winshell.shortcut(winshell.desktop() + f"\\{name}.lnk")
    shortcut.path = target
    shortcut.write()

if __name__ == "__main__":
    # 目标文件夹设为绝对路径
    # target_folder = "/home/your_username/daily_notes"  # Linux/Mac
    target_folder = r"D:\MY OWM FILES\CULUCULU"                 # Windows
    path = create_daily_file(target_folder)
    create_new_lnk(path,"今日日志")