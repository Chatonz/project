from PIL import Image
import os
# 指定要裁剪的 GIF 文件路径
gif_file_path = 'input.gif'
root_dir = 'images'
resize_dir = 'images1'
for subfolder in os.listdir(root_dir):
    print(subfolder)
    path1 = os.path.join(root_dir,subfolder)
    path11 = os.path.join(resize_dir,subfolder)
    for subfolder1 in os.listdir(path1):
        path2 = os.path.join(path1,subfolder1)
        path22 = os.path.join(path11,subfolder1)
        for subfolder2 in os.listdir(path2):
            path3 = os.path.join(path2,subfolder2)
            path33 = os.path.join(path22,subfolder2)
            for subfolder3 in os.listdir(path3):
                GIF_path = os.path.join(path3,subfolder3)
                save_path = os.path.join(path33,subfolder3)
                with Image.open(GIF_path) as gif:
                    crop_box = (60, 65, 900, 900)  # 你可以根据需要调整这些值

                    # 对 GIF 图像进行裁剪
                    cropped_gif = gif.crop(crop_box)


                    # 保存裁剪后的 GIF 文件
                    cropped_gif.save(save_path)

                    print(f"裁剪后的 GIF 已保存为 {save_path}")

