import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt

# 读取CTA图像
cta_image = sitk.ReadImage('subject030_0000.mha')

# 设定初始种子点和初始阈值
seed = (239, 196, 586)  # 例如，手动选择的种子点
# initial_threshold_value = 10


seg = sitk.ConfidenceConnected(cta_image, seedList=[seed],
                                   numberOfIterations=2,#越大增长越多
                                   multiplier=2,#越小灰度范围越窄
                                   initialNeighborhoodRadius=2,#越大增长越多
                                   replaceValue=1)

sitk.WriteImage(seg, 'seg.nii.gz')

# # 转换为numpy数组以进行显示
# segmented_array = sitk.GetArrayFromImage(seg)

# # 显示结果
# plt.figure(figsize=(12, 6))
# plt.subplot(1, 2, 1)
# plt.title('Original CTA Image')
# plt.imshow(sitk.GetArrayViewFromImage(cta_image)[100, :, :], cmap='gray')
# plt.subplot(1, 2, 2)
# plt.title('Segmented Aorta')
# plt.imshow(segmented_array[100, :, :], cmap='gray')
# plt.show()