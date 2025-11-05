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
        self.repetitions_key = self.__keyGenerator__(encryption_arr[1])
        self.process_key = self.__keyGenerator__(encryption_arr[2])


#================ PRE-ENCRYPTION ======================================
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
    



#======================================================================

enkrip = Encryptor("abc", [12312412, 523511, 89324709275])

print(f" Repetition Key: ${enkrip.repetitions_key}")
print(f" Process Key: ${enkrip.process_key}")
