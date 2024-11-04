# Credits: https://github.com/PRich57/windows-cursor-hiding-utility

import ctypes
from ctypes import wintypes

# Constants
OCR_NORMAL = 32512
SPI_SETCURSORS = 0x0057
SPIF_UPDATEINIFILE = 0x01
SPIF_SENDCHANGE = 0x02


class WindowsAPI:
    def __init__(self):
        print('Locating user32.dll from WindowsAPI ... ', end='')
        self.user32 = ctypes.windll.user32
        print('OK' if self.user32 else 'ERROR')

        self.user32.GetCursorPos.argtypes = [ctypes.POINTER(wintypes.POINT)]
        self.user32.SetSystemCursor.argtypes = [ctypes.c_void_p, ctypes.c_uint]
        self.user32.SetSystemCursor.restype = ctypes.c_bool
        self.user32.CopyIcon.argtypes = [ctypes.c_void_p]
        self.user32.CopyIcon.restype = ctypes.c_void_p
        self.user32.LoadCursorW.argtypes = [ctypes.c_void_p, ctypes.c_int]
        self.user32.LoadCursorW.restype = ctypes.c_void_p
        self.user32.SystemParametersInfoW.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint]
        self.user32.SystemParametersInfoW.restype = ctypes.c_bool

        self.original_cursor = None
        self.is_cursor_hidden: bool = False

    def switch_cursor_visibility(self) -> None:
        if self.is_cursor_hidden:
            self.show_cursor()
        else:
            self.hide_cursor()

    def hide_cursor(self) -> None:
        """
        Hide the cursor by replacing it with an invisible one.
        """
        invisible_cursor = self.__create_invisible_cursor()
        self.original_cursor = self.user32.CopyIcon(
            self.user32.LoadCursorW(None, OCR_NORMAL)
        )
        self.user32.SetSystemCursor(invisible_cursor, OCR_NORMAL)

        self.is_cursor_hidden = True
    
    def show_cursor(self) -> None:
        """
        Restore the original cursor.
        """
        if not self.original_cursor:
            self.original_cursor = self.user32.CopyIcon(
                self.user32.LoadCursorW(None, OCR_NORMAL)
            )

        if self.user32.SetSystemCursor(self.original_cursor, OCR_NORMAL):
            # Force a cursor update across all monitors
            self.user32.SystemParametersInfoW(SPI_SETCURSORS, 0, None, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)
        
        self.is_cursor_hidden = False
    
    def __create_invisible_cursor(self) -> ctypes.c_void_p:
        """
        Create an invisible cursor.

        Returns:
            A handle to the created invisible cursor.
        """
        and_mask = (ctypes.c_ubyte * 4)(0xFF, 0xFF, 0xFF, 0xFF)
        xor_mask = (ctypes.c_ubyte * 4)(0, 0, 0, 0)
        return self.user32.CreateCursor(None, 0, 0, 1, 1, and_mask, xor_mask)
