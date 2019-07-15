import cv2
import random

def random_light_color(img):
    B, G, R = cv2.split(img)

    b_rand = random.randint(-50, 50)
    if b_rand == 0:
        pass
    elif b_rand > 0:
        lim = 255 - b_rand
        B[B > lim] = 255
        B[B <= lim] = (b_rand + B[B <= lim]).astype(img.dtype)
    elif b_rand < 0:
        lim = 0 - b_rand
        B[B < lim] = 0
        B[B >= lim] = (b_rand + B[B >= lim]).astype(img.dtype)

    g_rand = random.randint(-50, 50)
    if g_rand == 0:
        pass
    elif g_rand > 0:
        lim = 255 - g_rand
        G[G > lim] = 255
        G[G <= lim] = (g_rand + G[G <= lim]).astype(img.dtype)
    elif g_rand < 0:
        lim = 0 - g_rand
        G[G < lim] = 0
        G[G >= lim] = (g_rand + G[G >= lim]).astype(img.dtype)

    r_rand = random.randint(-50, 50)
    if r_rand == 0:
        pass
    elif r_rand > 0:
        lim = 255 - r_rand
        R[R > lim] = 255
        R[R <= lim] = (r_rand + R[R <= lim]).astype(img.dtype)
    elif r_rand < 0:
        lim = 0 - r_rand
        R[R < lim] = 0
        R[R >= lim] = (r_rand + R[R >= lim]).astype(img.dtype)

    img_merge = cv2.merge((B, G, R))
    return img_merge

#传入文件路径
def img(path):
    img = cv2.imread(path)
    img_crop = img[0:300, 0:400]
    M = cv2.getRotationMatrix2D((img.shape[1] / 2, img.shape[0] / 2), 45, 1)
    img_rotate = cv2.warpAffine(img_crop, M, (img.shape[1], img.shape[0]))
    img_random_color = random_light_color(img_rotate)

    cv2.imshow("img", img_random_color)
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()

if __name__ == "__main__":
    img('horse.jpg')