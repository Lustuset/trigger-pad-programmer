import tkinter
import tkinter.messagebox
import logging
from typing import Any

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__name__)

        self.title("TriggerPad Programmer")

        self.menu_bar = tkinter.Menu(self)
        self.config(menu=self.menu_bar)

        self.file_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self._file_menu_new)
        self.file_menu.add_command(label="Open", command=self._file_menu_open)
        self.file_menu.add_command(label="Save", command=self._file_menu_save)
        self.file_menu.add_command(label="Save as", command=self._file_menu_save_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self._file_menu_exit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Undo", command=self._edit_menu_undo)
        self.edit_menu.add_command(label="Redo", command=self._edit_menu_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self._edit_menu_cut)
        self.edit_menu.add_command(label="Copy", command=self._edit_menu_copy)
        self.edit_menu.add_command(label="Paste", command=self._edit_menu_paste)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        self.program_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.program_menu.add_command(label="Test", command=self._program_menu_compile)
        self.program_menu.add_command(label="Upload", command=self._program_menu_upload)
        self.menu_bar.add_cascade(label="Program", menu=self.program_menu)

        self.debug_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.debug_menu.add_command(label="Connect", command=self._debug_menu_connect)
        self.debug_menu.add_command(label="Log", command=self._debug_menu_log)
        self.debug_menu.add_command(label="Console", command=self._debug_menu_console)
        self.menu_bar.add_cascade(label="Debug", menu=self.debug_menu)

        self.help_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Documentation", command=self._help_menu_documentation)
        self.help_menu.add_command(label="About", command=self._help_menu_about)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        self.report_callback_exception = self._report_callback_exception
    
    def mainloop(self, n: int = 0):
        self.logger.debug("Application started")
        return super().mainloop(n)

    def _file_menu_new(self) -> None:
        self.logger.debug("Clicked on 'File > New'")
        raise NotImplementedError()

    def _file_menu_open(self) -> None:
        self.logger.debug("Clicked on 'File > Open'")
        raise NotImplementedError()
    
    def _file_menu_save(self) -> None:
        self.logger.debug("Clicked on 'File > Save'")
        raise NotImplementedError()
    
    def _file_menu_save_as(self) -> None:
        self.logger.debug("Clicked on 'File > Save as'")
        raise NotImplementedError()
    
    def _file_menu_exit(self) -> None:
        self.logger.debug("Clicked on 'File > Exit'")
        self.exit()
    
    def _edit_menu_undo(self) -> None:
        self.logger.debug("Clicked on 'Edit > Undo'")
        raise NotImplementedError()
    
    def _edit_menu_redo(self) -> None:
        self.logger.debug("Clicked on 'Edit > Redo'")
        raise NotImplementedError()
    
    def _edit_menu_cut(self) -> None:
        self.logger.debug("Clicked on 'Edit > Cut'")
        raise NotImplementedError()
    
    def _edit_menu_copy(self) -> None:
        self.logger.debug("Clicked on 'Edit > Copy'")
        raise NotImplementedError()
    
    def _edit_menu_paste(self) -> None:
        self.logger.debug("Clicked on 'Edit > Paste'")
        raise NotImplementedError()
    
    def _program_menu_compile(self) -> None:
        self.logger.debug("Clicked on 'Program > Test'")
        raise NotImplementedError()
    
    def _program_menu_upload(self) -> None:
        self.logger.debug("Clicked on 'Program > Upload'")
        raise NotImplementedError()
    
    def _debug_menu_connect(self) -> None:
        self.logger.debug("Clicked on 'Debug > Connect'")
        raise NotImplementedError()
    
    def _debug_menu_log(self) -> None:
        self.logger.debug("Clicked on 'Debug > Log'")
        raise NotImplementedError()
    
    def _debug_menu_console(self) -> None:
        self.logger.debug("Clicked on 'Debug > Console'")
        raise NotImplementedError()
    
    def _help_menu_documentation(self) -> None:
        self.logger.debug("Clicked on 'Help > Documentation'")
        raise NotImplementedError()
    
    def _help_menu_about(self) -> None:
        self.logger.debug("Clicked on 'Help > About'")
        raise NotImplementedError("Test")
    
    def _report_callback_exception(self, exc: Any, val: Any, tb: Any):
        self.logger.error("An error occurred", exc_info=(exc, val, tb))

        if isinstance(val, NotImplementedError) and str(val) == "":
            tkinter.messagebox.showerror("Error", "This feature is not implemented") # type: ignore
        elif str(val) == "":
            tkinter.messagebox.showerror("Error", "An unknown error occurred") # type: ignore
        else:
            tkinter.messagebox.showerror("Error", str(val)) # type: ignore
    
    def exit(self) -> None:
        self.logger.debug("Exiting application")
        self.quit()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    App().mainloop()