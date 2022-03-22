import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from PIL import Image
import random


def cube(x=0, y=0, z=0, size=10):  # fonction de création de cube, coordonnées de base (0, 0, 0) et taille de base (10)
    sq_x = np.array([x, x, x + size, x + size, x, x, x + size, x + size])
    sq_y = np.array([y, y + size, y + size, y, y, y + size, y + size, y])
    sq_z = np.array([z, z, z, z, z + size, z + size, z + size, z + size])
    sq_w = np.array([1, 1, 1, 1, 1, 1, 1, 1])
    cube = np.array([sq_x, sq_y, sq_z, sq_w])
    return cube


def get_points(figure):  # permet de recuperer les coordonées des angles d'un cube
    points = []
    for i in range(len(figure[0])):
        points.append([figure[0][i], figure[1][i], figure[2][i]])
    return points


def aggrandissement_reduc(figure, val):  # fonction de modification de taille d'un cube
    sq_tx = np.array([val, 0, 0, 0])
    sq_ty = np.array([0, val, 0, 0])
    sq_tz = np.array([0, 0, val, 0])
    sq_tw = np.array([0, 0, 0, 1])
    array_ar = np.array([sq_tx, sq_ty, sq_tz, sq_tw])
    result = np.matmul(array_ar, figure)
    return result


def translation3D(figure, tx, ty, tz):  # translation d'un objet 3d
    sq_tx = np.array([1, 0, 0, tx])
    sq_ty = np.array([0, 1, 0, ty])
    sq_tz = np.array([0, 0, 1, tz])
    sq_tw = np.array([0, 0, 0, 1])
    array_t = np.array([sq_tx, sq_ty, sq_tz, sq_tw])  # matrice de deplacement
    result = np.matmul(array_t, figure)  # multiplication de la matrice de l'objet et de la matrice de rotation
    return result


def rotation3D_x(figure, teta, deplacement_y=0, deplacement_z=0):  # rotation d'un objet 3d sur l'axe x
    xr = np.array([1, 0, 0, 0])
    yr = np.array([0, np.cos(teta), -np.sin(teta), 0])
    zr = np.array([0, np.sin(teta), np.cos(teta), 0])
    wr = np.array([0, 0, 0, 1])

    matrix_rotation = np.array([xr, yr, zr, wr])

    figure = translation3D(figure, 0, -deplacement_y, -deplacement_z)
    figure = np.matmul(matrix_rotation, figure)
    figure = translation3D(figure, 0, deplacement_y, deplacement_z)

    return figure


def c_rotation3D_x(figure, teta, deplacement_y=0,
                   deplacement_z=0):  # fonction permettant de réinitialiser la rotation d'un cube sur l'axe x
    xr = np.array([1, 0, 0, 0])
    yr = np.array([0, np.cos(teta), np.sin(teta), 0])
    zr = np.array([0, -np.sin(teta), np.cos(teta), 0])
    wr = np.array([0, 0, 0, 1])

    matrix_rotation = np.array([xr, yr, zr, wr])

    figure = translation3D(figure, 0, -deplacement_y, -deplacement_z)
    figure = np.matmul(matrix_rotation, figure)
    figure = translation3D(figure, 0, deplacement_y, deplacement_z)

    return figure


def rotation3D_y(figure, teta, deplacement_x=0, deplacement_z=0):  # rotation d'un objet 3d sur l'axe y
    xr = np.array([np.cos(teta), 0, np.sin(teta), 0])
    yr = np.array([0, 1, 0, 0])
    zr = np.array([-np.sin(teta), 0, np.cos(teta), 0])
    wr = np.array([0, 0, 0, 1])

    matrix_rotation = np.array([xr, yr, zr, wr])

    figure = translation3D(figure, -deplacement_x, 0, -deplacement_z)
    figure = np.matmul(matrix_rotation, figure)
    figure = translation3D(figure, deplacement_x, 0, deplacement_z)

    return figure


def c_rotation3D_y(figure, teta, deplacement_x=0,
                   deplacement_z=0):  # fonction permettant de réinitialiser la rotation d'un cube sur l'axe y
    xr = np.array([np.cos(teta), 0, -np.sin(teta), 0])
    yr = np.array([0, 1, 0, 0])
    zr = np.array([np.sin(teta), 0, np.cos(teta), 0])
    wr = np.array([0, 0, 0, 1])

    matrix_rotation = np.array([xr, yr, zr, wr])

    figure = translation3D(figure, -deplacement_x, 0, -deplacement_z)
    figure = np.matmul(matrix_rotation, figure)
    figure = translation3D(figure, deplacement_x, 0, deplacement_z)

    return figure


def rotation3D_z(figure, teta, deplacement_x=0, deplacement_y=0):  # rotation d'un objet 3d sur l'axe z
    xr = np.array([np.cos(teta), -np.sin(teta), 0, 0])
    yr = np.array([np.sin(teta), np.cos(teta), 0, 0])
    zr = np.array([0, 0, 1, 0])
    wr = np.array([0, 0, 0, 1])

    matrix_rotation = np.array([xr, yr, zr, wr])

    figure = translation3D(figure, -deplacement_x, -deplacement_y, 0)
    figure = np.matmul(matrix_rotation, figure)
    figure = translation3D(figure, deplacement_x, deplacement_y, 0)

    return figure


def c_rotation3D_z(figure, teta, deplacement_x=0,
                   deplacement_y=0):  # fonction permettant de réinitialiser la rotation d'un cube sur l'axe z
    xr = np.array([np.cos(teta), np.sin(teta), 0, 0])
    yr = np.array([-np.sin(teta), np.cos(teta), 0, 0])
    zr = np.array([0, 0, 1, 0])
    wr = np.array([0, 0, 0, 1])

    matrix_rotation = np.array([xr, yr, zr, wr])

    figure = translation3D(figure, -deplacement_x, -deplacement_y, 0)
    figure = np.matmul(matrix_rotation, figure)
    figure = translation3D(figure, deplacement_x, deplacement_y, 0)

    return figure


def rotation3D(figure, teta_x=0, teta_y=0, teta_z=0, deplacement_x=0, deplacement_y=0,
               deplacement_z=0):  # fonction regroupant les 3 rotation d'axes possible
    xr = np.array([1, 0, 0, 0])
    yr = np.array([0, np.cos(teta_x), -np.sin(teta_x), 0])
    zr = np.array([0, np.sin(teta_x), np.cos(teta_x), 0])
    wr = np.array([0, 0, 0, 1])

    matrix_rotation_x = np.array([xr, yr, zr, wr])

    xr = np.array([np.cos(teta_y), 0, np.sin(teta_y), 0])
    yr = np.array([0, 1, 0, 0])
    zr = np.array([-np.sin(teta_y), 0, np.cos(teta_y), 0])
    wr = np.array([0, 0, 0, 1])

    matrix_rotation_y = np.array([xr, yr, zr, wr])

    xr = np.array([np.cos(teta_z), -np.sin(teta_z), 0, 0])
    yr = np.array([np.sin(teta_z), np.cos(teta_z), 0, 0])
    zr = np.array([0, 0, 1, 0])
    wr = np.array([0, 0, 0, 1])

    matrix_rotation_z = np.array([xr, yr, zr, wr])

    figure = translation3D(figure, -deplacement_x, -deplacement_y, -deplacement_z)
    figure = np.matmul(matrix_rotation_x, figure)
    figure = np.matmul(matrix_rotation_y, figure)
    figure = np.matmul(matrix_rotation_z, figure)
    figure = translation3D(figure, deplacement_x, deplacement_y, deplacement_z)

    return figure


def counter_rotation3D(figure, teta_x=0, teta_y=0, teta_z=0, deplacement_x=0, deplacement_y=0,
                       deplacement_z=0):  # fonction permettant de réinitialiser la rotation d'un cube sur n'importe quel axe
    xr = np.array([1, 0, 0, 0])
    yr = np.array([0, np.cos(teta_x), np.sin(teta_x), 0])
    zr = np.array([0, -np.sin(teta_x), np.cos(teta_x), 0])
    wr = np.array([0, 0, 0, 1])

    matrix_rotation_x = np.array([xr, yr, zr, wr])

    xr = np.array([np.cos(teta_y), 0, -np.sin(teta_y), 0])
    yr = np.array([0, 1, 0, 0])
    zr = np.array([np.sin(teta_y), 0, np.cos(teta_y), 0])
    wr = np.array([0, 0, 0, 1])

    matrix_rotation_y = np.array([xr, yr, zr, wr])

    xr = np.array([np.cos(teta_z), np.sin(teta_z), 0, 0])
    yr = np.array([-np.sin(teta_z), np.cos(teta_z), 0, 0])
    zr = np.array([0, 0, 1, 0])
    wr = np.array([0, 0, 0, 1])

    matrix_rotation_z = np.array([xr, yr, zr, wr])

    figure = translation3D(figure, -deplacement_x, -deplacement_y, -deplacement_z)
    figure = np.matmul(matrix_rotation_x, figure)
    figure = np.matmul(matrix_rotation_y, figure)
    figure = np.matmul(matrix_rotation_z, figure)
    figure = translation3D(figure, deplacement_x, deplacement_y, deplacement_z)

    return figure


def init_plt():  # permet d'initaliser la fenetre de matplotlib et de colorier les faces des cubes
    global fig  # import de variables dans la fonction
    global ax
    global nbimg
    global figures
    global angle

    nbimg += 1  # variable comptant le nombre d'images créées
    print(nbimg)

    fig = plt.figure(figsize=(12, 12))  # parametres de la zone de dessin matplotlib
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    ax.set_zlim(-20, 20)
    ax.view_init(elev=25, azim=angle)
    angle += 2.5
    plt.axis('off')  # parametres de la zone de dessin matplotlib

    for k in range(27):  # coloriage des faces des cubes
        points = get_points(figures[k])
        edges = [[points[0], points[1], points[2], points[3]]]
        face = Poly3DCollection(edges, linewidths=1, edgecolors='black')
        face.set_facecolor(dic_color[k]["bottom"])
        ax.add_collection3d(face)

        edges = [[points[4], points[5], points[6], points[7]]]
        face = Poly3DCollection(edges, linewidths=1, edgecolors='black')
        face.set_facecolor(dic_color[k]["top"])
        ax.add_collection3d(face)

        edges = [[points[0], points[3], points[7], points[4]]]
        face = Poly3DCollection(edges, linewidths=1, edgecolors='black')
        face.set_facecolor(dic_color[k]["left"])
        ax.add_collection3d(face)

        edges = [[points[1], points[2], points[6], points[5]]]
        face = Poly3DCollection(edges, linewidths=1, edgecolors='black')
        face.set_facecolor(dic_color[k]["right"])
        ax.add_collection3d(face)

        edges = [[points[3], points[2], points[6], points[7]]]
        face = Poly3DCollection(edges, linewidths=1, edgecolors='black')
        face.set_facecolor(dic_color[k]["face"])
        ax.add_collection3d(face)

        edges = [[points[0], points[1], points[5], points[4]]]
        face = Poly3DCollection(edges, linewidths=1, edgecolors='black')

        face.set_facecolor(dic_color[k]["back"])

        ax.add_collection3d(face)


def create_cubes():  # création des 9 cubes du  rubiks cube
    list = []  # liste des cubes créées
    for i in [6.0, -5.0, -16.0]:  # position choisis pour que le centre du cube du milieu soit en 0, 0, 0
        for j in [6.0, -5.0, -16.0]:
            for k in [6.0, -5.0, -16.0]:
                list.append(cube(i, j, k, 10))
    return list


def top_face(rubiks_cube):  # obtenir la face du haut du rubiks cube (utilisation des positions)
    low_point_for_cube = {}
    for i in range(9):
        for j in range(27):
            l_lowest_z = rubiks_cube[j][2][0]
            for point in rubiks_cube[j][2]:
                if point <= l_lowest_z:
                    low_point_for_cube[j] = point

    return list(({k: v for k, v in sorted(low_point_for_cube.items(), key=lambda item: item[1])}.keys()))[18:]


def mid_cubes_z(rubiks_cube):  # obtenir la ligne de cube du milieu (entre le haut et le bas)
    low_point_for_cube = {}
    for i in range(9):
        for j in range(27):
            l_lowest_z = rubiks_cube[j][2][0]
            for point in rubiks_cube[j][2]:
                if point <= l_lowest_z:
                    low_point_for_cube[j] = point

    return list(({k: v for k, v in sorted(low_point_for_cube.items(), key=lambda item: item[1])}.keys()))[9:18]


def bottom_face(rubiks_cube): #obtenir les 9 cubes du bas du rubiks cube
    low_point_for_cube = {}
    for i in range(9):
        for j in range(27):
            l_lowest_z = rubiks_cube[j][2][0]
            for point in rubiks_cube[j][2]:
                if point <= l_lowest_z:
                    low_point_for_cube[j] = point

    return list(({k: v for k, v in sorted(low_point_for_cube.items(), key=lambda item: item[1])}.keys()))[:9]


def right_face(rubiks_cube): #obtenir les 9 cubes de droite du rubiks cube
    low_point_for_cube = {}
    for i in range(9):
        for j in range(27):
            l_lowest_z = rubiks_cube[j][1][0]
            for point in rubiks_cube[j][1]:
                if point <= l_lowest_z:
                    low_point_for_cube[j] = point

    return list(({k: v for k, v in sorted(low_point_for_cube.items(), key=lambda item: item[1])}.keys()))[18:]


def left_face(rubiks_cube):#obtenir les 9 cubes de gauche du rubiks cube
    low_point_for_cube = {}
    for i in range(9):
        for j in range(27):
            l_lowest_z = rubiks_cube[j][1][0]
            for point in rubiks_cube[j][1]:
                if point <= l_lowest_z:
                    low_point_for_cube[j] = point

    return list(({k: v for k, v in sorted(low_point_for_cube.items(), key=lambda item: item[1])}.keys()))[:9]


def front_face(rubiks_cube):#obtenir les 9 cubes de la face du rubiks cube
    low_point_for_cube = {}
    for i in range(9):
        for j in range(27):
            l_lowest_z = rubiks_cube[j][0][0]
            for point in rubiks_cube[j][0]:
                if point <= l_lowest_z:
                    low_point_for_cube[j] = point

    return list(({k: v for k, v in sorted(low_point_for_cube.items(), key=lambda item: item[1])}.keys()))[18:]


def back_face(rubiks_cube):#obtenir les 9 cubes du dos du rubiks cube
    low_point_for_cube = {}
    for i in range(9):
        for j in range(27):
            l_lowest_z = rubiks_cube[j][0][0]
            for point in rubiks_cube[j][0]:
                if point <= l_lowest_z:
                    low_point_for_cube[j] = point

    return list(({k: v for k, v in sorted(low_point_for_cube.items(), key=lambda item: item[1])}.keys()))[:9]


figures = create_cubes() #liste des cubes composants le rubiks cube

vitesse = 10 #vitesse de rotation des faces


def initialize_colors(rubiks_cube): #permet d'obtenir la couleur à attribuer a chaques faces des cubes
    dic_list = [{"top": "k", "bottom": "k", "right": "k", "left": "k", "face": "k", "back": "k"} for i in range(27)]
    for i in bottom_face(rubiks_cube):
        dic_list[i]["bottom"] = "w"
    for i in top_face(rubiks_cube):
        dic_list[i]["top"] = "y"
    for i in front_face(rubiks_cube):
        dic_list[i]["face"] = "blue"
    for i in back_face(rubiks_cube):
        dic_list[i]["back"] = "green"
    for i in right_face(rubiks_cube):
        dic_list[i]["right"] = "red"
    for i in left_face(rubiks_cube):
        dic_list[i]["left"] = "darkorange"

    return dic_list


def rotate_face(figures, j): #faire pivoter la face du rubiks cube
    global vitesse
    figures[j] = rotation3D_x(figures[j], np.pi / vitesse, 0, 0)
    return figures


def rotate_back(figures, j): #faire pivoter le dos du rubiks cube
    figures[j] = rotation3D_x(figures[j], np.pi / vitesse, 0, 0)
    return figures


def rotate_right(figures, j): #faire pivoter la droite du rubiks cube
    figures[j] = rotation3D_y(figures[j], np.pi / vitesse, 0, 0)
    return figures


def rotate_left(figures, j): #faire pivoter la gauche du rubiks cube
    figures[j] = rotation3D_y(figures[j], np.pi / vitesse, 0, 0)
    return figures


def rotate_head(figures, j): #faire pivoter le haut du rubiks cube
    figures[j] = rotation3D_z(figures[j], np.pi / vitesse, 0, 0)
    return figures


def rotate_under(figures, j): #faire pivoter le bas du rubiks cube
    figures[j] = rotation3D_z(figures[j], np.pi / vitesse, 0, 0)
    return figures


def rotate_and_spin_top(top): #permet de faire pivoter tout le rubiks cube de 45° puis de le faire pivoter en continue et tourner sa face du haut
    rubiks_cube = figures[:]
    for i in range(27):
        rubiks_cube[i] = rotation3D_z(rubiks_cube[i], 45 * np.pi / 180, 0, 0)
        rubiks_cube[i] = rotation3D_y(rubiks_cube[i], 45 * np.pi / 180, 0, 0)

    for i in range(10):
        for i in range(27):
            figures[i] = rotation3D_z(figures[i], 4.5 * np.pi / 180, 0, 0)
        init_plt()
        plt.savefig(f'{nbimg}.png')
        plt.close()

    for i in range(10):
        for i in range(27):
            figures[i] = rotation3D_y(figures[i], 4.5 * np.pi / 180, 0, 0)
        init_plt()
        plt.savefig(f'{nbimg}.png')
        plt.close()

    for i in range(27):
        figures[i] = rubiks_cube[i]

    for i in range(35):
        for i in top:
            figures[i] = rotation3D_z(figures[i], 7.2 * np.pi / 180)
            figures[i] = rotation3D_x(figures[i], 7.2 * np.pi / 180)
        init_plt()
        plt.savefig(f'{nbimg}.png')
        plt.close()

    for i in range(27):
        figures[i] = rubiks_cube[i]
    init_plt()
    plt.savefig(f'{nbimg}.png')
    plt.close()


def rotate_and_spin_bot(top): #permet de faire pivoter tout le rubiks cube de 45° puis de le faire pivoter en continue et tourner sa face du bas
    rubiks_cube = figures[:]
    for i in range(27):
        rubiks_cube[i] = rotation3D_z(rubiks_cube[i], 45 * np.pi / 180)
        rubiks_cube[i] = rotation3D_y(rubiks_cube[i], 45 * np.pi / 180)
        rubiks_cube[i] = rotation3D_x(rubiks_cube[i], 45 * np.pi / 180)

    for i in range(10):
        for i in range(27):
            figures[i] = rotation3D_x(figures[i], 4.5 * np.pi / 180, 0, 0)
        init_plt()
        plt.savefig(f'{nbimg}.png')
        plt.close()

    """for i in range(27):
        figures[i] = rubiks_cube[i]"""

    for i in range(50):
        for j in top:
            figures[j] = c_rotation3D_x(figures[j], 45 * np.pi / 180)
            figures[j] = c_rotation3D_y(figures[j], 45 * np.pi / 180)
            figures[j] = c_rotation3D_z(figures[j], 45 * np.pi / 180)

            figures[j] = rotation3D_z(figures[j], 7.2 * np.pi / 180)

            figures[j] = rotation3D_z(figures[j], 45 * np.pi / 180)
            figures[j] = rotation3D_y(figures[j], 45 * np.pi / 180)
            figures[j] = rotation3D_x(figures[j], 45 * np.pi / 180)
        init_plt()
        plt.savefig(f'{nbimg}.png')
        plt.close()

    for i in range(10):
        for i in range(27):
            figures[i] = c_rotation3D_x(figures[i], 4.5 * np.pi / 180)
            figures[i] = c_rotation3D_y(figures[i], 4.5 * np.pi / 180)
            figures[i] = c_rotation3D_z(figures[i], 4.5 * np.pi / 180)
        init_plt()
        plt.savefig(f'{nbimg}.png')
        plt.close()


def apparition(): #animation de diparition du cube
    bottom = bottom_face(figures)
    top = top_face(figures)
    mid = mid_cubes_z(figures)
    for j in range(40):
        deplacement = 5
        for i in top:
            figures[i] = translation3D(figures[i], 0, 0, deplacement)
            deplacement += 1
        deplacement = 5
        for i in bottom:
            figures[i] = translation3D(figures[i], 0, 0, deplacement)
            deplacement += 1
        deplacement = 5
        for i in mid:
            figures[i] = translation3D(figures[i], 0, 0, deplacement)
            deplacement += 1

        init_plt()
        plt.savefig(f'{nbimg}.png')
        plt.close()


def disparition():
    for i in range(30):
        for i in range(27):
            figures[i] = aggrandissement_reduc(figures[i], 0.75)
        init_plt()
        plt.savefig(f'{nbimg}.png')
        plt.close()


dic_color = initialize_colors(figures)

collection_faces = []

angle = 30
nbimg = -1
oldresult = -1
cote = -1

for i in range(20): # 20 rotations aléatoire du cube
    # draw
    # mouvements
    while cote == oldresult:
        cote = random.randint(0, 5) # selection d'une face aléatoirement
    oldresult = cote # éviter de tourner deux fois la meme face
    if cote == 0:
        print('face')
        for j in range(int(vitesse / 2)):
            init_plt()
            for k in front_face(figures):
                figures = rotate_face(figures, k)

            plt.savefig(f'{nbimg}.png')
            plt.close()
    elif cote == 1:
        print('right')
        for j in range(int(vitesse / 2)):
            init_plt()
            e = right_face(figures)
            for k in e:
                figures = rotate_right(figures, k)

            plt.savefig(f'{nbimg}.png')
            plt.close()
    elif cote == 2:
        print('left')
        for j in range(int(vitesse / 2)):
            init_plt()
            for k in left_face(figures):
                figures = rotate_left(figures, k)

            plt.savefig(f'{nbimg}.png')
            plt.close()
    elif cote == 3:
        print('head')
        for j in range(int(vitesse / 2)):
            init_plt()
            for k in top_face(figures):
                figures = rotate_head(figures, k)

            plt.savefig(f'{nbimg}.png')
            plt.close()
    elif cote == 4:
        print('under')
        for j in range(int(vitesse / 2)):
            init_plt()
            for k in bottom_face(figures):
                figures = rotate_under(figures, k)

            plt.savefig(f'{nbimg}.png')
            plt.close()
    elif cote == 5:
        print('back')
        for j in range(int(vitesse / 2)):
            init_plt()
            for k in back_face(figures):
                figures = rotate_back(figures, k)

            plt.savefig(f'{nbimg}.png')
            plt.close()

bot = bottom_face(figures)
top = top_face(figures)

rotate_and_spin_top(top)

rotate_and_spin_bot(bot)

apparition() # animation d'apparition du cube (chute depuis le haut)

r_nbimg = nbimg

images = [] # liste des images utilisés dans le gif

for n in reversed(range(nbimg)): # inversion de l'animation (pour faire croire une résolution de rubiks cube)
    images.append(Image.open(f'{n}.png'))

figures = create_cubes()

disparition() # animation de disparition (reduction de la taille du rubiks cube)

for n in range(r_nbimg + 1, nbimg):
    images.append(Image.open(f'{n}.png'))

images[0].save('cube.gif', save_all=True, append_images=images[1:], duration=10, loop=0) # création du gif
