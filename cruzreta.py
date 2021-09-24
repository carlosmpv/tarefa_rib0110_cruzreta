import math

def get_intersection(xp1, yp1, xc1, yc1, xp2, yp2, xc2, yc2):
    mr1 = (yp1 - yc1) / (xp1 -xc1)
    mr2 = (yp2 - yc2) / (xp2 - xc2)

    x = (-(mr2 * xc2) + yc2 + (mr1 * xc1) - yc1) / (mr1 - mr2)
    y = (mr1 * x)  - (mr1 * xc1) + yc1

    return (x, y)


def get_3d_point(xp1, yp1, zp1, xc1, yc1, zc1, xp2, yp2, zp2, xc2, yc2, zc2):
    x1, y1 = get_intersection(xp1, yp1, xc1, yc1, xp2, yp2, xc2, yc2)
    x2, z1 = get_intersection(xp1, zp1, xc1, zc1, xp2, zp2, xc2, zc2)
    z2, y2 = get_intersection(zp1, yp1, zc1, yc1, zp2, yp2, zc2, yc2)

    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    z = (z1 + z2) / 2

    return (x, y, z)


if __name__ == '__main__':
    xc1, xp1, xc2, xp2 = 365.800, 0.000, 131.400, 179.400
    yc1, yp1, yc2, yp2 = 211.000, 133.900, 384.800, 0.000
    zc1, zp1, zc2, zp2 = 107.000, 50.900, 151.800, 17.100

    expected = (158.606, 167.917, 75.664)
    result = get_3d_point(xp1, yp1, zp1, xc1, yc1, zc1, xp2, yp2, zp2, xc2, yc2, zc2)

    assert(abs(result[0] - expected[0]) < 0.001)
    assert(abs(result[1] - expected[1]) < 0.001)
    assert(abs(result[2] - expected[2]) < 0.001)

    xyz_c1 = []
    xyz_p1 = []
    xyz_c2 = []
    xyz_p2 = []

    while len(xyz_c1) != 3:
        print("Insira a posição (x, y, z) da camera 1 separados por espaço e com . no lugar de ,")
        answer = input("(x, y, z): ")

        try:
            xyz_c1 = [float(v) for v in answer.split(" ")]
        except:
            print("Por favor insira valores válidos")
            continue

    while len(xyz_p1) != 3:
        print("Insira a posição (x, y, z) da projeção da camera 1 separados por espaço e com . no lugar de ,")
        answer = input("(x, y, z): ")

        try:
            xyz_p1 = [float(v) for v in answer.split(" ")]
        except:
            print("Por favor insira valores válidos")
            continue
    
    while len(xyz_c2) != 3:
        print("Insira a posição (x, y, z) da camera 2 separados por espaço e com . no lugar de ,")
        answer = input("(x, y, z): ")

        try:
            xyz_c2 = [float(v) for v in answer.split(" ")]
        except:
            print("Por favor insira valores válidos")
            continue

    while len(xyz_p2) != 3:
        print("Insira a posição (x, y, z) da projeção da camera 2 separados por espaço e com . no lugar de ,")
        answer = input("(x, y, z): ")

        try:
            xyz_p2 = [float(v) for v in answer.split(" ")]
        except:
            print("Por favor insira valores válidos")
            continue

    result = get_3d_point(
        xyz_p1[0], xyz_p1[1], xyz_p1[2],
        xyz_c1[0], xyz_c1[1], xyz_c1[2],
        xyz_p2[0], xyz_p2[1], xyz_p2[2],
        xyz_c2[0], xyz_c2[1], xyz_c2[2],
    )
    print("Ponto de intersecão tridimensional: ", result)
    
    

    

    