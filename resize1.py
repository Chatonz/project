from PIL import Image
import os

def crop_gif(gif_path, save_path, crop_box):
    with Image.open(gif_path) as gif:
        frames = []

        # 遍历所有帧并裁剪
        for frame in range(gif.n_frames):
            gif.seek(frame)
            frame_image = gif.crop(crop_box)
            frames.append(frame_image)

        # 保存裁剪后的 GIF 文件
        frames[0].save(
            save_path,
            save_all=True,
            append_images=frames[1:],
            duration=gif.info['duration'],
            loop=gif.info.get('loop', 0)
        )
        print(f"裁剪后的 GIF 已保存为 {save_path}")

# 指定根目录和保存目录
root_dir = 'images'
resize_dir = 'images1'

# 遍历根目录下的所有子文件夹
for subfolder in os.listdir(root_dir):
    path1 = os.path.join(root_dir, subfolder)
    path11 = os.path.join(resize_dir, subfolder)
    os.makedirs(path11, exist_ok=True)  # 创建目标文件夹

    # 遍历子文件夹下的所有子文件夹
    for subfolder1 in os.listdir(path1):
        path2 = os.path.join(path1, subfolder1)
        path22 = os.path.join(path11, subfolder1)
        os.makedirs(path22, exist_ok=True)  # 创建目标文件夹

        # 遍历子文件夹下的所有子文件夹
        for subfolder2 in os.listdir(path2):
            path3 = os.path.join(path2, subfolder2)
            path33 = os.path.join(path22, subfolder2)
            os.makedirs(path33, exist_ok=True)  # 创建目标文件夹

            # 遍历子文件夹下的所有 GIF 文件
            for filename in os.listdir(path3):
                if filename.endswith('.gif'):
                    GIF_path = os.path.join(path3, filename)
                    save_path = os.path.join(path33, filename)

                    # 裁剪并保存 GIF 文件
                    crop_box = (60, 65, 900, 900)  # 根据需要调整裁剪框
                    crop_gif(GIF_path, save_path, crop_box)
