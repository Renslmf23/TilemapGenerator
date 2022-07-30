import cv2
import numpy as np


def CreateTilemapTemplate():

    # Load the default downscaled mask. The mask should have a 4x4 grid
    m_mask_name = "mask_temp.png"

    m_mask = cv2.imread(m_mask_name)
    empty_image = np.zeros(m_mask.shape, dtype=np.uint8)

    m_mask = cv2.cvtColor(m_mask, cv2.COLOR_BGR2GRAY)
    _, m_dst = cv2.threshold(m_mask, 0, 255, cv2.THRESH_BINARY_INV)

    # Go trough the grid
    for cube_count_x in range(0, m_dst.shape[0], 4):
        for cube_count_y in range(0, m_dst.shape[1], 4):
            for x in range(0, 4):
                x_coord = x + cube_count_x
                col_is_white = True
                for y in range(0, 4):
                    if y == 1 or y == 2:
                        if x == 1 or x == 2:
                            col_is_white = False
                            continue
                    y_coord = y + cube_count_y
                    # If the mask is black, make the pixel red, else make the pixel green
                    if m_dst[x_coord, y_coord] < 127:
                        empty_image[x_coord, y_coord] = np.array([0, 0, 255], dtype=np.uint8)
                    else:
                        col_is_white = False
                        empty_image[x_coord, y_coord] = np.array([0, 255, 0], dtype=np.uint8)
                # If an edge is completely red, mark the corners as emtpy
                if col_is_white:
                    empty_image[x_coord, cube_count_y] = np.array([0, 0, 0], dtype=np.uint8)
                    empty_image[x_coord, cube_count_y + 3] = np.array([0, 0, 0], dtype=np.uint8)
            # Also check for vertical edges
            for y in range(0, 4):
                y_coord = y + cube_count_y
                row_is_white = True
                for x in range(0, 4):
                    if y == 1 or y == 2:
                        if x == 1 or x == 2:
                            row_is_white = False
                            continue
                    x_coord = x + cube_count_x
                    if m_dst[x_coord, y_coord] > 127:
                        row_is_white = False
                # If an edge is completely red, mark the corners as emtpy
                if row_is_white:
                    empty_image[cube_count_x, y_coord] = np.array([0, 0, 0], dtype=np.uint8)
                    empty_image[cube_count_x + 3, y_coord] = np.array([0, 0, 0], dtype=np.uint8)
    # Save the image
    cv2.imwrite("mask_template.png", empty_image)


if __name__ == "__main__":
    CreateTilemapTemplate()
