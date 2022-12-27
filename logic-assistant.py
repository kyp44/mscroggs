#! /usr/bin/env python3
"""
Run with -h for a description
"""
import numpy as np
import argparse
import itertools as it
from collections import namedtuple
import pickle
import sys
import os

# PyQt
from PyQt5 import QtWidgets, QtCore

# Work file name
fname = "logic-work.pickle"

# Parse command line arguments
parser = argparse.ArgumentParser(description="GUI program that allows manual solving of general grid or logic puzzles using logic. "
                                 "Upon exiting, the current work is saved to " + fname + ". Delete this file to start over or setup a new grid.")
parser.add_argument("symbols", metavar="SYMBOLS", type=str, nargs="?",
                    default=None, help="CSV of possible symbols in each cell or variable")
parser.add_argument("--vars", "-v", metavar="VARS", type=str, default=None,
                    help="CSV variables that are each assigned one of the symbols for a non-grid puzzle")
parser.add_argument("--size", "-s", metavar="SIZE", type=str, default=None,
                    help="CSV of numbers of rows and columns (in that order) for a grid puzzle")
args = parser.parse_args()

# Work package
Work = namedtuple("Work", ("symbols", "vars", "gsize", "stack"))

if os.path.exists(fname):
    print("Loading from", fname, "and ignoring command line arguments")
    # Load previously saved work
    with open(fname, "rb") as f:
        work = pickle.load(f)
else:
    # Start new work
    try:
        # Check arguments
        if args.symbols is None or (args.vars is None and args.size is None):
            raise ValueError(
                "Must pass symbols and either a set of variables or a grid size")

        # Get symbols
        symbols = tuple(args.symbols.split(","))

        if args.vars is not None:
            # Get variables
            vars = tuple(args.vars.split(","))

            # Determine grid size base on number of variables
            nrc = int(np.ceil(np.sqrt(len(vars))))
            gsize = (nrc, nrc)
        else:
            # Get grid size
            gsize = tuple(map(int, args.size.split(",")))[:2]
            vars = None

        work = Work(symbols, vars, gsize, [])
    except Exception as e:
        print("Argument error:", e)
        exit(1)

# Format cell values
val_cols = int(np.ceil(np.sqrt(len(work.symbols))))

# Value selection dialog


class ValueDialog(QtWidgets.QDialog):
    def __init__(self, parent, vals):
        """
        See class docstring.
        """
        super(ValueDialog, self).__init__(parent)

        # Set values
        self.values = vals

        # Create grid
        grid = QtWidgets.QGridLayout()

        # Add check boxes
        self.cboxes = {}
        (r, c) = (0, 0)
        for i, val in enumerate(work.symbols):
            cbox = QtWidgets.QCheckBox(val)
            cbox.setChecked(val in self.values)
            grid.addWidget(cbox, r, c)
            self.cboxes[val] = cbox
            c += 1
            if (i+1) % val_cols == 0:
                r += 1
                c = 0

        # Vbox layout
        vbox = QtWidgets.QVBoxLayout()

        # Add grid and buttons
        vbox.addLayout(grid)
        all_button = QtWidgets.QPushButton("All")
        all_button.clicked.connect(lambda: self.set_all_vals(True))
        vbox.addWidget(all_button)
        none_button = QtWidgets.QPushButton("None")
        none_button.clicked.connect(lambda: self.set_all_vals(False))
        vbox.addWidget(none_button)
        reset_button = QtWidgets.QPushButton("Reset")
        reset_button.clicked.connect(lambda: self.reset())
        vbox.addWidget(reset_button)
        ok_button = QtWidgets.QPushButton("OK")
        ok_button.clicked.connect(lambda: self.close())
        vbox.addWidget(ok_button)

        # Set layout and title
        self.setLayout(vbox)
        self.setWindowTitle("Set Values")

        # Set modality and show
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()

    def set_all_vals(self, checked):
        for cbox in self.cboxes.values():
            cbox.setChecked(checked)

    def reset(self):
        for val in work.symbols:
            self.cboxes[val].setChecked(val in self.values)

    def closeEvent(self, evt):
        # Rebuild values set based on check boxes
        self.values = set(
            [val for val in work.symbols if self.cboxes[val].isChecked()])

# Cell widget


class CellWidget(QtWidgets.QFrame):
    clicked = QtCore.pyqtSignal(tuple)

    def __init__(self, var, r, c):
        # Initalize to all values
        self.values = set(work.symbols)
        self.var = var
        self.pos = (r, c)

        # Setup from super and set values
        super(CellWidget, self).__init__()

        # Add widget
        hbox = QtWidgets.QHBoxLayout()
        if var is not None:
            vlab = QtWidgets.QLabel(var + " =")
            font = vlab.font()
            font.setPointSize(16)
            vlab.setFont(font)
            hbox.addWidget(vlab)
        self.vals_label = QtWidgets.QLabel()
        hbox.addWidget(self.vals_label)
        self.setLayout(hbox)

        # Get default font size
        self.fsize = self.vals_label.font().pointSize()
        self.set_values(self.values)

        # Set size
        self.setFrameShape(QtWidgets.QFrame.Panel)
        self.vals_label.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

    def cell_str(self):
        os = ""
        i = 1
        for val in work.symbols:
            if val in self.values:
                os += val
                if i % val_cols == 0 and i < len(self.values):
                    os += "\n"
                i += 1
        return os

    def set_values(self, vals):
        self.values = vals
        self.vals_label.setText(self.cell_str())
        font = self.vals_label.font()
        if len(self.values) == 1:
            font.setPointSize(28)
        else:
            font.setPointSize(self.fsize)
        self.vals_label.setFont(font)

    def mousePressEvent(self, evt):
        self.clicked.emit(self.pos)

# Main dialog


class MainDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainDialog, self).__init__()

        # Set title
        self.setWindowTitle("Logic Assistant")

        # Center on the screen for default position
        self.move(100, 100)

        # Main vbox
        vbox = QtWidgets.QVBoxLayout()

        # State hbox
        hbox = QtWidgets.QHBoxLayout()
        hbox.setAlignment(QtCore.Qt.AlignLeft)

        # State contols
        self.ss_count_label = QtWidgets.QLabel()
        self.update_ss_count()
        push_button = QtWidgets.QPushButton("Push")
        push_button.clicked.connect(self.push_state)
        pop_button = QtWidgets.QPushButton("Pop")
        pop_button.clicked.connect(self.pop_state)

        # Add state controls
        hbox.addWidget(push_button)
        hbox.addWidget(pop_button)
        hbox.addWidget(QtWidgets.QLabel("State stack:"))
        hbox.addWidget(self.ss_count_label)
        vbox.addLayout(hbox)

        # Create grid
        grid = QtWidgets.QGridLayout()
        grid.setSpacing(0)

        # Create cells
        self.cells = {}
        if work.vars is None:
            # Make the grid
            for r, c in it.product(range(work.gsize[0]), range(work.gsize[1])):
                cell = CellWidget(None, r, c)
                cell.clicked.connect(self.cell_clicked)
                self.cells[cell.pos] = cell
                grid.addWidget(cell, r, c)
        else:
            # Make grid based on variables
            r, c = 0, 0
            for v in work.vars:
                cell = CellWidget(v, r, c)
                cell.clicked.connect(self.cell_clicked)
                self.cells[cell.pos] = cell
                grid.addWidget(cell, r, c)
                c += 1
                if c > work.gsize[1] - 1:
                    c = 0
                    r += 1

        # Now make the cells a uniform size
        sizes = [cell.sizeHint() for cell in self.cells.values()]
        if work.vars is None:
            # Make all cells square
            w = max([max(s.width(), s.height()) for s in sizes])
            size = (w, w)
        else:
            w = max(map(lambda s: s.width(), sizes))
            h = max(map(lambda s: s.height(), sizes))
            size = (w, h)
        for cell in self.cells.values():
            cell.setFixedSize(*size)

        # NOTE: There is some super annoying issue where resizing the cells smaller than some
        # maximum value causes the QGridLayout not to update. I was unable to figure out how
        # to resolve this.

        # Add grid to layout
        vbox.addLayout(grid)

        # Need to a generic widget to wrap layout
        mw = QtWidgets.QWidget(self)
        mw.setLayout(vbox)
        self.setCentralWidget(mw)

        # Disable resizing
        self.setFixedSize(self.sizeHint())

        # If we have a saved state then pop it (otherwise there is no effect)
        self.pop_state()

        # Display the window
        self.show()

    def cell_clicked(self, pos):
        vd = ValueDialog(self, self.cells[pos].values)
        vd.exec_()
        self.cells[pos].set_values(vd.values)

    def update_ss_count(self):
        self.ss_count_label.setText(str(len(work.stack)))

    def push_state(self):
        # Build state
        state = {pos: cell.values for pos, cell in self.cells.items()}
        work.stack.append(state)
        self.update_ss_count()

    def pop_state(self):
        if len(work.stack) < 1:
            return

        state = work.stack.pop()
        for pos, vals in state.items():
            self.cells[pos].set_values(vals)
        self.update_ss_count()


# Create or use existing GUI application
app = QtWidgets.QApplication(sys.argv)

# Launch the main dialog
md = MainDialog()
app.exec_()

# Push current state then save
md.push_state()
with open(fname, "wb") as f:
    pickle.dump(work, f)
