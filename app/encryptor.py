#============ HEADER =================================================
"""
Document: encryptor.py
Function: Module for the encryption processes.
Author: PURA, Joshua Elijah L.
Date Created: November 5, 2025
Date Updated: November 5, 2025
Version: 0.0.1
"""
from itertools import zip_longest

#======================================================================

#============== LIBRARIES =============================================
import numpy as np
import hashlib
import secrets
#======================================================================

#============== CLASS =================================================
class Encryptor:
    def __init__(self, data, encryption_arr):
        """
        Function: __init__
        Description: This private function gets triggered once
                     the Encryptor class is instantiated.
        Parameters:
            data (str): This is the data to be encrypted
            encryption_arr (list): This is a Numpy Array of
                                    encryption key.
        Returns:
            None
        Raises:
            none
        """
        self.data = data
        self.encryption_arr = encryption_arr
        self.max_bit = 256
        self.cubeMax = 16
        self.repetitions_key = self.__keyGenerator__(encryption_arr[1])
        self.process_key = self.__keyGenerator__(encryption_arr[2])
        self.f = []
        self.b = []
        self.u = []
        self.d = []
        self.r = []
        self.l = []
        self.window = 192
        self.fmax = 32
        self.bmax = 64
        self.umax = 96
        self.dmax = 128
        self.rmax = 160
        self.lmax = 192
        self.process = [["lc", "rc", "uc", "dc"],
                        ["fc", "l", "r", "u"],
                        ["d", "f"],
                        []]


#================ PRE-ENCRYPTION ======================================
    def __cubeFill__ (self, data):
        """
        Function: __cubeFill__
        Description: This private function is for simply filling
                     all the faces of the cube with data.
        Parameters:
            data (str): This is the data to be encrypted
        Returns:
            None
        Raises:
            none
        """

        # It iterates all from 0 to 192, jumping 2 every loop
        for i in range(0, self.window, 2):
            # This checks if the length of the data is long enough
            # If the data is not long enough for 192 character
            # It will just append 0 to it
            if i < len(data):
                data_pair = data[i:i + 2]
                if len(data_pair) == 1:
                    data_pair = ''.join(data_pair + '0')
            else:
                data_pair = "00"

            # This checks which face should be filled
            if i < self.fmax:
                self.f = np.append(self.f, data_pair)
            elif i < self.bmax:
                self.b = np.append(self.b, data_pair)
            elif i < self.umax:
                self.u = np.append(self.u, data_pair)
            elif i < self.dmax:
                self.d = np.append(self.d, data_pair)
            elif i < self.rmax:
                self.r = np.append(self.r, data_pair)
            elif i < self.lmax:
                self.l = np.append(self.l, data_pair)

        self.__cubeFinalizer__()



    def __cubeFinalizer__ (self):
        f = np.array(self.f[:9]).reshape(3, 3)
        b = np.array(self.b[:9]).reshape(3, 3)
        u = np.array(self.u[:9]).reshape(3, 3)
        d = np.array(self.d[:9]).reshape(3, 3)
        r = np.array(self.r[:9]).reshape(3, 3)
        l = np.array(self.l[:9]).reshape(3, 3)
        print(f)
        print(b)
        print(u)
        print(d)
        print(r)
        print(l)

    def encrypt(self):
        self.__cubeFill__(self.data)



    def __keyGenerator__(self, key):
        """
        Function: __keyGenerator__
        Description: This private function converts the integer key into
                     a binary key which will be used for the encryption
                     later.
        Parameters:
            key (int)
        Returns:
            binary_key (str): This function returns a stream of
                              binary numbers to be used in the
                              encryption process.
        Raises:
            none
        """
        binary_key = ""
        str_key = str(key)
        i = 0
        while len(binary_key) < self.max_bit:
            binary_key += bin(int(str_key[i]))[2:]
            i = (i + 1) % len(str_key)
        binary_key = binary_key[:self.max_bit]
        return binary_key



#================ ENCRYPTION PROCESSES=================================
    """
        The partial_data array contains all the 6 faces of the cube. Assume the following:
        F - Front of the cube
        B - Back of the cube
        U - Top of the cube
        D - Bottom of the cube
        R - Right of the cube
        L - Left of the cube

        The data to be encrypted will be stored in the following format:
        partial_data = [
            [
              [F1, F2, F3],
              [ F4, F5, F6],
              [ F7, F8, F9],
            ], 
            [
              [B1, B2, B3],
              [B4, B5, B6],
              [B7, B8, B9]]
            ], 
            [
              [U1, U2, U3],
              [U4, U5, U6],
              [U7, U8, U9]
            ], 
            [
              [D1, D2, D3],
              [D4, D5, D6],
              [D7, D8, D9]
            ], 
            [ 
              [R1, R2, R3],
              [R4, R5, R6],
              [R7, R8, R9]
            ], [
              [L1, L2, L3],
              [L4, L5, L6],
              [L7, L8, L9]
            ]
        ]
    """
    def __f__ (self, rep):
        """
        Function: __f__
        Description: This private function contains algorithm to rotate the
                     front face of the cube.
        Parameters:
            rep (int): The number of repetitions of the rotation.
        Returns:
            None.
        Raises:
            none
        """
        for i in range(rep):
            # rotate f face
            f_new = np.rot90(self.f, k=-1)

            # Update affected column when f face is rotated
            u_new = np.array([self.u[0], self.u[1], self.l[:, 2]])
            r_new = np.array([
                [self.u[2][0], self.r[0][1], self.r[2][2]],
                [self.u[2][1], self.r[1][1], self.r[1][2]],
                [self.u[2][2], self.r[2][1], self.r[2][2]]
            ])
            d_new = np.array([self.r[:, 0], self.d[1], self.d[2]])
            l_new = np.array([
                [self.l[0][0], self.l[0][1], self.d[0][0]],
                [self.l[1][0], self.l[1][1], self.d[0][1]],
                [self.l[2][0], self.l[2][1], self.d[0][2]]
            ])

            # Save the changes on the class arrays
            self.f = np.array(f_new)
            self.d = np.array(d_new)
            self.u = np.array(u_new)
            self.r = np.array(r_new)
            self.l = np.array(l_new)

            print(f"This is ${i} rotation")
            print(f_new)
            print(u_new)
            print(r_new)
            print(d_new)
            print(l_new)

    def fMove(self, rep):
        self.__f__(rep)






#======================================================================


# Front face
F = np.array([
    ["F1", "F2", "F3"],
    ["F4", "F5", "F6"],
    ["F7", "F8", "F9"]
])

# Back face
B = np.array([
    ["B1", "B2", "B3"],
    ["B4", "B5", "B6"],
    ["B7", "B8", "B9"]
])

# Up face
U = np.array([
    ["U1", "U2", "U3"],
    ["U4", "U5", "U6"],
    ["U7", "U8", "U9"]
])

# Down face
D = np.array([
    ["D1", "D2", "D3"],
    ["D4", "D5", "D6"],
    ["D7", "D8", "D9"]
])

# Right face
R = np.array([
    ["R1", "R2", "R3"],
    ["R4", "R5", "R6"],
    ["R7", "R8", "R9"]
])

# Left face
L = np.array([
    ["L1", "L2", "L3"],
    ["L4", "L5", "L6"],
    ["L7", "L8", "L9"]
])

enkrip = Encryptor("asd", [1,2,3])
enkrip.f = F
enkrip.b = B
enkrip.u = U
enkrip.d = D
enkrip.r = R
enkrip.l = L

enkrip.fMove()