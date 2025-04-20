import numpy as np
import cv2

x = np.uint8([250])
y = np.uint8([10])
# z = cv2.add(x, y) # 250 + 10 = 260 => 255

# zのデータ型を指定してみる
z = cv2.add(x, y, dtype=cv2.CV_8U)


print(f'z = {z}')

# --- デバッグ情報: x の内容、データ型、形状を出力 ---
print(f"x: {x}, dtype: {x.dtype}, shape: {x.shape}")

# --- デバッグ情報: y の内容、データ型、形状を出力 ---
print(f"y: {y}, dtype: {y.dtype}, shape: {y.shape}")

# --- デバッグ情報: z のデータ型と形状を出力 ---
print(f"z: dtype: {z.dtype}, shape: {z.shape}")