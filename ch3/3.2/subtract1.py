import numpy as np
import cv2

x = np.uint8([10])
y = np.uint8([5])
z = cv2.subtract(x, y) # 10 - 5 = 5
print(f'z = {z}')

# --- デバッグ情報: x の内容、データ型、形状を出力 ---
print(f"x: {x}, dtype: {x.dtype}, shape: {x.shape}")

# --- デバッグ情報: y の内容、データ型、形状を出力 ---
print(f"y: {y}, dtype: {y.dtype}, shape: {y.shape}")

# --- デバッグ情報: z のデータ型と形状を出力 ---
print(f"z: dtype: {z.dtype}, shape: {z.shape}")